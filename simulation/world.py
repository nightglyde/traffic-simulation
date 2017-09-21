from util import *

from obstacle import Obstacle
from car import Car
from controller import CarController

SCALE_CHANGE = 1.25

class World(Obstacle):
    def __init__(self, screen, width, height):
        self.screen = screen

        self.width  = width
        self.height = height

        self.hull = [Vector(0, 0),
                     Vector(self.width, 0),
                     Vector(self.width, self.height),
                     Vector(0, self.height)]

        self.obstacles = []
        self.grass     = []

        self.cars        = []
        self.controllers = []
        self.num_cars = 0

        self.paused = False

        # pan and zoom
        self.scale = min(SCREEN_WIDTH  / self.width  * 0.9,
                         SCREEN_HEIGHT / self.height * 0.9)

        self.scale_min = min(SCREEN_WIDTH  / self.width * 0.4,
                             SCREEN_HEIGHT / self.width * 0.5)

        self.scale_max = max(SCREEN_WIDTH  / CAR_LENGTH * 0.5,
                             SCREEN_HEIGHT / CAR_LENGTH * 0.5)

        self.offset = Vector((SCREEN_WIDTH  / self.scale - self.width)  / 2,
                             (SCREEN_HEIGHT / self.scale - self.height) / 2)

        self.starting_position = None
        self.starting_offset   = None

        self.panning = False
        self.selected_car = None

    def checkObject(self, world_object):
        for point in world_object.hull:
            if not self.checkInside(point):
                return False

        for obstacle in self.obstacles:
            if obstacle.checkCollision(world_object):
                return False

        for grass in self.grass:
            if grass.checkCollision(world_object):
                return False

        return True

    def generateRandomPosition(self):
        x = random.random() * self.width
        y = random.random() * self.height
        return Vector(x, y)

    def addGrass(self, points):
        grass = Obstacle(self, "grass", LIGHT_GREEN, points, False)
        self.grass.append(grass)

    def addObstacle(self, name, colour, points):
        obstacle = Obstacle(self, name, colour, points)
        self.obstacles.append(obstacle)

    def addCar(self, name, colour, time):
        self.num_cars += 1

        # create car
        while True:
            pos   = self.generateRandomPosition()
            angle = Angle(random.random()*2*math.pi)

            car = Car(self, name, colour, pos, angle, time)
            if self.checkObject(car):

                for other_car in self.cars:
                    if car.checkCollision(other_car):
                        break
                else:
                    self.cars.append(car)
                    break

        # create car controller
        controller = CarController(self, name, colour)
        self.controllers.append(controller)

    def pause(self, time):
        self.paused = not self.paused
        if self.paused:
            for car in self.cars:
                car.pause(time)

            for controller in self.controllers:
                controller.pause(time)

        else:
            for car in self.cars:
                car.unpause(time)

            for controller in self.controllers:
                controller.unpause(time)

    def firstUpdate(self, time):
        for i in range(self.num_cars):
            position, angle = self.cars[i].update(time)
            self.controllers[i].firstUpdate(position, angle, time)

    def update(self, time):
        if self.panning:
            self.updatePan(Vector(*pygame.mouse.get_pos()))

        if self.paused:
            return

        for i in range(self.num_cars):
            position, angle = self.cars[i].update(time)
            self.controllers[i].update(position, angle, time)

        if self.selected_car:
            if self.selected_car.stopped:
                self.selected_car = None
            else:
                self.followCar(self.selected_car)

        for i in range(self.num_cars):
            controller_i = self.controllers[i]

            for j in range(i+1, self.num_cars):
                controller_j = self.controllers[j]

                if controller_i.checkCollision(controller_j):
                    controller_i.stop(controller_j)
                    controller_j.stop(controller_i)
                    self.cars[i].stop()
                    self.cars[j].stop()

            for obstacle in self.obstacles:
                if controller_i.checkCollision(obstacle):
                    controller_i.stop(obstacle)
                    self.cars[i].stop()

        for i in range(self.num_cars):
            engine, steering, braking = self.controllers[i].control()
            self.cars[i].control(engine, steering, braking)

    def scaleDistance(self, distance):
        return round(distance * self.scale)

    def getScreenPosition(self, true_position):
        return (true_position + self.offset) * self.scale

    def getDrawable(self, point):
        point = self.getScreenPosition(point)
        return [round(point.x), round(point.y)]

    def getTruePosition(self, screen_position):
        return screen_position/self.scale - self.offset

    def zoomIn(self, mouse_position):
        if self.selected_car != None:
            mouse_position = SCREEN_CENTRE

        true_mouse_position = self.getTruePosition(mouse_position)
        if not self.checkInside(true_mouse_position):
            return

        new_scale = min(self.scale * SCALE_CHANGE, self.scale_max)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def zoomOut(self, mouse_position):
        if self.selected_car != None:
            mouse_position = SCREEN_CENTRE

        true_mouse_position = self.getTruePosition(mouse_position)
        if not self.checkInside(true_mouse_position):
            return

        new_scale = max(self.scale / SCALE_CHANGE, self.scale_min)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def followCar(self, car):
        screen_centre = self.getTruePosition(SCREEN_CENTRE)
        self.offset  += screen_centre - car.position

    def startPan(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        if not self.checkInside(true_mouse_position):
            self.panning = False

        for car in self.cars:
            if car.checkInside(true_mouse_position):
                self.selected_car = car
                self.panning = False
                return

        self.selected_car = None

        self.starting_position = mouse_position
        self.starting_offset   = self.offset
        self.panning = True

    def updatePan(self, mouse_position):
        if not self.panning:
            return

        diff = (mouse_position - self.starting_position) / self.scale
        self.offset = self.starting_offset + diff

    def stopPan(self):
        self.panning = False

    def draw(self):
        for grass in self.grass:
            grass.draw()

        box = [self.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.screen, BLACK, box, 1)

        for obstacle in self.obstacles:
            obstacle.draw()

        for controller in self.controllers:
            controller.draw()

        for car in self.cars:
            car.drawWheelPaths()

        for car in self.cars:
            if car is self.selected_car:
                car.draw(True)
            else:
                car.draw()


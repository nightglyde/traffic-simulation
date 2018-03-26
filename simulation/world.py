from util import *

from obstacle import Obstacle
from car import Car
from controller import CarController

from generate_world import roads_list

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
        self.centre = Vector(self.width/2, self.height/2)

        self.obstacles = []
        self.grass     = []

        self.starting_positions = []
        self.waypoint_options   = []

        self.cars        = []
        self.controllers = []
        self.num_cars = 0

        # pan and zoom
        self.scale = min(SCREEN_WIDTH  / self.width  * 0.9,
                         SCREEN_HEIGHT / self.height * 0.9)

        self.scale_min = min(SCREEN_WIDTH  / self.width * 0.5,
                             SCREEN_HEIGHT / self.width * 0.5)

        self.scale_max = min(SCREEN_WIDTH  / CAR_LENGTH * 0.5,
                             SCREEN_HEIGHT / CAR_LENGTH * 0.5)

        self.offset = Vector((SCREEN_WIDTH  / self.scale - self.width)  / 2,
                             (SCREEN_HEIGHT / self.scale - self.height) / 2)

        self.pan_position = None
        self.pan_offset   = None

        self.panning = False
        self.selected_car = None

        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

    def checkWaypoint(self, waypoint):
        if not self.checkInside(waypoint.position):
            return False
        if waypoint.checkBorder(self):
            return False
        for obstacle in self.obstacles:
            if waypoint.checkCollision(obstacle):
                return False
        for grass in self.grass:
            if waypoint.checkCollision(grass):
                return False
        return True

    def checkCar(self, car):
        for point in car.hull:
            if not self.checkInside(point):
                return False
        for obstacle in self.obstacles:
            if obstacle.checkCollision(car):
                return False
        for grass in self.grass:
            if grass.checkCollision(car):
                return False
        return True

    def generateRandomPosition(self):
        x = random.random() * self.width
        y = random.random() * self.height
        return Vector(x, y)

    def addGrass(self, points):
        grass = Obstacle(self, "grass", LIGHT_GREEN, points)
        self.grass.append(grass)

    def addObstacle(self, name, colour, points):
        obstacle = Obstacle(self, name, colour, points)
        self.obstacles.append(obstacle)

    def addStartingPosition(self, point):
        self.starting_positions.append(point)

    def addWaypointOption(self, point):
        self.waypoint_options.append(point)

    def getWaypointOptions(self, waypoints):
        waypoint = waypoints[-1]

        good_options = []
        for pos in self.waypoint_options:
            if pos is waypoint.position:
                continue

            vec = pos - waypoint.position
            if vec.mag() > 10:
                continue

            diff = angleBetween(vec, getVector(waypoint.angle))
            if diff > math.pi/3:
                continue

            good_options.append(pos)

        return good_options

    def addCar(self, name, colour, time):
        # create car
        while True:
            road = random.choice(roads_list)
            road_vec = road.end - road.start

            pos = road.start + road_vec * random.random()
            angle = getAngle(road_vec)

            car = Car(self, name, colour, pos, angle, time)
            if self.checkCar(car):

                for other_car in self.cars:
                    if car.checkCollision(other_car):
                        break

                else:
                    controller = CarController(car, road)
                    self.controllers.append(controller)

                    self.cars.append(car)
                    self.num_cars += 1
                    return

    def alt_addCar(self, name, colour, time):
        # create car
        while True:
            #pos = random.choice(self.starting_positions)

            pos   = self.generateRandomPosition()
            angle = getAngle(pos - self.centre)

            #for option in waypoint_options:
            #    vec = option - pos
            #    if vec.mag() > 10:
            #        continue

            #    angle = getAngle(vec)
            #    break

            car = Car(self, name, colour, pos, angle, time)
            if self.checkCar(car):

                for other_car in self.cars:
                    if car.checkCollision(other_car):
                        break
                else:
                    controller = CarController(car, road)
                    self.controllers.append(controller)

                    self.cars.append(car)
                    self.num_cars += 1
                    return

    def update(self, time):
        for car in self.cars:
            car.update(time)

        crash = False
        for i in range(self.num_cars):
            car_i = self.cars[i]

            for j in range(i+1, self.num_cars):
                car_j = self.cars[j]

                if car_i.checkCollision(car_j):
                    car_i.stop(car_j)
                    self.controllers[i].clearWaypoints()
                    if not car_i.stopped:
                        crash = True

                    car_j.stop(car_i)
                    self.controllers[j].clearWaypoints()
                    if not car_j.stopped:
                        crash = True

            for obstacle in self.obstacles:
                if car_i.checkCollision(obstacle):
                    car_i.stop(obstacle)
                    self.controllers[i].clearWaypoints()
                    if not car_i.stopped:
                        crash = True

        for grass in self.grass:
            for car in self.cars:
                if grass.checkCollision(car):
                    grass.colour = DARK_GREEN
                    break
            else:
                grass.colour = LIGHT_GREEN

        for controller in self.controllers:
            if crash:
                controller.clearFuture()
                controller.clearWaypoints()
            controller.update()

    def sendMessages(self):
        messages = {SEND_TO_ALL: []}
        for controller in self.controllers:
            messages[controller.name] = []

        # send messages
        for controller in self.controllers:
            source = controller.name
            for message in controller.sendMessages():
                address, message_type, content = message
                messages[address].append((source, message_type, content))

        # receive messages
        for controller in self.controllers:
            address = controller.name
            controller.receiveMessages(messages[SEND_TO_ALL], messages[address])

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
            true_mouse_position = self.selected_car.centre
        else:
            true_mouse_position = self.getTruePosition(mouse_position)
            if not self.checkInside(true_mouse_position):
                return

        new_scale = min(self.scale * SCALE_CHANGE, self.scale_max)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def zoomOut(self, mouse_position):
        if self.selected_car != None:
            mouse_position = SCREEN_CENTRE
            true_mouse_position = self.selected_car.centre
        else:
            true_mouse_position = self.getTruePosition(mouse_position)
            if not self.checkInside(true_mouse_position):
                return

        new_scale = max(self.scale / SCALE_CHANGE, self.scale_min)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def followCar(self, car):
        screen_centre = self.getTruePosition(SCREEN_CENTRE)
        self.offset  += screen_centre - car.centre

    def startPan(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        if not self.checkInside(true_mouse_position):
            self.panning = False
            return

        for car in self.cars:
            if car.checkInside(true_mouse_position):
                self.selected_car = car
                print("Selected car:", car.name)
                self.panning = False
                return

        self.selected_car = None

        self.pan_position = mouse_position
        self.pan_offset   = self.offset
        self.panning = True

    def updatePan(self, mouse_position):
        if not self.panning:
            return

        diff = (mouse_position - self.pan_position) / self.scale
        self.offset = self.pan_offset + diff

    def stopPan(self):
        self.panning = False

    def draw(self):
        if self.panning:
            self.updatePan(Vector(*pygame.mouse.get_pos()))

        if self.selected_car:
            if self.selected_car.stopped:
                self.selected_car = None
            else:
                self.followCar(self.selected_car)

        for grass in self.grass:
            grass.draw()

        box = [self.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.screen, BLACK, box, 1)

        for obstacle in self.obstacles:
            obstacle.draw(True)

        for controller in self.controllers:
            controller.drawWaypoints()

        for controller in self.controllers:
            controller.drawPath()

        for car in self.cars:
            car.draw(car is self.selected_car)
            #car.drawExtra()

        for road in roads_list:
            thingy = road.end - road.start
            if thingy.mag() == 0.0:
                pygame.draw.circle(self.screen, RED,
                                   self.getDrawable(road.end), 5, 1)
                continue

            start = self.getDrawable(road.start)
            end   = self.getDrawable(road.end)
            pygame.draw.line(self.screen, BLACK, start, end, 1)

            #forward = (road.end - road.start).norm()
            #left    = forward.left90() * 0.5

            #left_corner  = self.getDrawable(road.end - forward + left)
            #right_corner = self.getDrawable(road.end - forward - left)

            #triangle = [end, left_corner, right_corner]

            #pygame.draw.polygon(self.screen, WHITE, triangle)
            #pygame.draw.polygon(self.screen, BLACK, triangle, 1)


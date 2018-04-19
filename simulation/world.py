from util import *

from obstacle import Obstacle
from car import Car
from controller import CarController

from generate_world import roads_list, ramp_roads

from give_way_rules import checkGiveWay

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
        #self.num_cars = 0

        self.car_generator = nextColour(self.cars)

        self.ramp_cooldown = 0
        #self.ramp_cooldown = [0 for road in ramp_roads]

        self.ghosts       = []
        self.crashed_cars = 0

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

        self.panning      = False
        self.selected_car = None

        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

        # temporary
        #self.printables = []
        self.give_way_rules = []

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

    def alt_addCar(self, name, colour, time):
        # create car
        while True:
            #while True:
            #    road = random.choice(roads_list)
            #    road_vec = road.end - road.start
            #    road_length = road_vec.mag()
            #    if road_length > 3:
            #        break

            #dist_along_road = 1 + random.random() * (road_length-2)

            #pos = road.start + road_vec * (dist_along_road/road_length)

            road = random.choice(roads_list)
            road_vec = road.end - road.start

            pos   = road.start + road_vec * random.random()
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
                    #self.num_cars += 1
                    return

    def addCar(self, time):
        colour, name = next(self.car_generator)

        road  = random.choice(ramp_roads)#ramp_roads[road_num]
        pos   = road.start
        angle = getAngle(road.end - road.start)

        car = Car(self, name, colour, pos, angle, time)
        car.speed = MAX_SPEED

        self.controllers.append(CarController(car, road))
        self.cars.append(car)
        self.ramp_cooldown = time + CAR_ADDING_INTERVAL
        #self.ramp_cooldown[road_num] = time + CAR_ADDING_INTERVAL

    def alt_update(self, time):

        if not self.cars:
            # add a bunch of cars

            angle = Vector(random.randint(-1, 1), random.randint(-1, 1))

            presets = [
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                Vector(random.randint(1, 5)*20, random.randint(1, 5)*20),
                #Vector(random.randint(0, 100), random.randint(0, 100)),
            ]

            #presets = [
                #(Vector(50, 50), Vector(0, -1)),
                #(Vector(60, 50), Vector(0, -1)),


            #    (Vector(80, 60), Vector(1, 0)),
            #    (Vector(90, 60), Vector(1, 0)),
            #]

            for pos in presets:
                colour, name = next(self.car_generator)

                #pos += SCREEN_CENTRE

                car = Car(self, name, colour, pos, angle, time)
                self.cars.append(car)

        num_cars = len(self.cars)

        self.printables.clear()

        for car_i in self.cars:
            for car_j in self.cars:
                if car_i == car_j:
                    continue

                give_way, intersect = checkGiveWay(car_i, car_j)

                if give_way:
                    print(car_i.name, "gives way to", car_j.name)
                    self.printables.append((car_i, car_j))
                #else:
                #    print(car_j.name, "gives way to", car_i.name)

                #self.printables.append((car_i, car_j, intersect))

    def update(self, time):
        for car in self.cars:
            car.update(time)

        num_cars = len(self.cars)

        #crash = False
        for i in range(num_cars):
            car_i = self.cars[i]

            for j in range(i+1, num_cars):
                car_j = self.cars[j]

                dist = (car_i.position - car_j.position).mag()
                if dist < 10 and car_i.checkCollision(car_j):
                        self.controllers[i].clearWaypoints()
                        #if not car_i.stopped:
                        #    crash = True
                        car_i.stop(car_j)

                        self.controllers[j].clearWaypoints()
                        #if not car_j.stopped:
                        #    crash = True
                        car_j.stop(car_i)

            #for obstacle in self.obstacles:
            #    if car_i.checkCollision(obstacle):

            #       self.controllers[i].clearWaypoints()
                    #if not car_i.stopped:
                    #    crash = True
            #       car_i.stop(obstacle)

        i = 0
        while i < len(self.controllers):
            car = self.cars[i]
            if car.stopped:
                self.cars.pop(i)
                self.controllers.pop(i)
            else:
                i += 1

        for controller in self.controllers:
            #if crash:
            #    controller.clearFuture()
            #    controller.clearWaypoints()
            controller.update()

        #for grass in self.grass:
        #    for car in self.cars:
        #        if grass.checkCollision(car):
        #            grass.colour = DARK_GREEN
        #            break
        #    else:
        #        grass.colour = LIGHT_GREEN

        self.sendMessages()

        self.give_way_rules.clear()
        for controller_i in self.controllers:
            for controller_j in self.controllers:
                if controller_i == controller_j:
                    continue
                if controller_i.checkGiveWay(controller_j.name):
                    self.give_way_rules.append((controller_i,
                                                controller_j))

        if len(self.cars) < MAX_CARS:

            #valid_ramps = []
            #for i, cooldown in enumerate(self.ramp_cooldown):
            #    if time >= cooldown:
            #        valid_ramps.append(i)

            #if valid_ramps:
            #    random.shuffle(valid_ramps)

            #    for i in range(min(len(valid_ramps), MAX_CARS - len(self.cars))):
            #        self.addCar(time, valid_ramps[i])

            if time >= self.ramp_cooldown:
                self.addCar(time)

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
            #grass.drawOutline()

        box = [self.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.screen, BLACK, box, 1)

        for ghost in self.ghosts:
            #ghost.drawPath()
            ghost.draw()

        for obstacle in self.obstacles:
            obstacle.draw(True)

        for control_a, control_b in self.give_way_rules:
            pos_a = control_a.car.centre
            pos_b = control_b.car.centre

            point_a = self.getDrawable(pos_a)
            point_b = self.getDrawable(pos_b)

            pygame.draw.line(self.screen, control_b.colour,
                             point_a, point_b, 1)

        for controller in self.controllers:
            controller.drawWaypoints()

        #for controller in self.controllers:
        #    controller.drawPath()

        #for car in self.cars:
        #    car.drawPath()

        for car in self.cars:
            car.draw(car is self.selected_car)
            #car.drawExtra()

        #for car in self.cars:
        #    car.drawDesiredPosition()

        #for road in roads_list:
        #    thingy = road.end - road.start
        #    if thingy.mag() == 0.0:
        #        pygame.draw.circle(self.screen, RED,
        #                           self.getDrawable(road.end), 5, 1)
        #        continue

        #    start = self.getDrawable(road.start)
        #    end   = self.getDrawable(road.end)
        #    pygame.draw.line(self.screen, BLACK, start, end, 1)

            #forward = (road.end - road.start).norm()
            #left    = forward.left90() * 0.5

            #left_corner  = self.getDrawable(road.end - forward + left)
            #right_corner = self.getDrawable(road.end - forward - left)

            #triangle = [end, left_corner, right_corner]

            #pygame.draw.polygon(self.screen, WHITE, triangle)
            #pygame.draw.polygon(self.screen, BLACK, triangle, 1)


from util import *

from obstacle import Obstacle
from car import Car
from controller import CarController
from road_network import TrafficLights, IntersectionRoad, EnterIntersection

MAX_GHOSTS = 50

SCALE_CHANGE = 1.25

class World:
    def __init__(self, screen, width, height):
        self.screen = screen

        self.width  = width
        self.height = height

        self.results = []

        #self.hull = [Vector(0, 0),
        #             Vector(self.width, 0),
        #             Vector(self.width, self.height),
        #             Vector(0, self.height)]
        #self.centre = Vector(self.width/2, self.height/2)


        self.all_roads = []
        self.grass     = []

        self.entry_roads = []
        self.recent_cars = []
        self.schedule    = deque()

        self.cars          = []
        self.controllers   = []
        self.car_generator = nextColour(self.cars)

        self.traffic_lights = {}

        self.successful_cars = 0
        self.crashed_cars    = 0
        self.ghosts          = deque()

        # pan and zoom
        self.scale = min(SCREEN_WIDTH  / self.width  * 0.9,
                         SCREEN_HEIGHT / self.height * 0.9)

        self.scale_min = min(SCREEN_WIDTH  / self.width * 0.5,
                             SCREEN_HEIGHT / self.width * 0.5)

        self.scale_max = min(SCREEN_WIDTH  / CAR_LENGTH * 0.5,
                             SCREEN_HEIGHT / CAR_LENGTH * 0.5)

        self.offset = Vector((SCREEN_WIDTH  / self.scale - self.width)  / 2,
                             (SCREEN_HEIGHT / self.scale - self.height) / 2)

        self.default_offset = self.offset
        self.default_scale  = self.scale

        self.pan_position = None
        self.pan_offset   = None

        self.panning      = False
        self.selected_car = None

    def setup(self, roads, intersections, grass,
              entry_roads, valid_routes, schedule):

        self.all_roads     = roads
        self.intersections = intersections

        for points in grass:
            grass_area = Obstacle(self, "grass", LIGHT_GREEN, points)
            self.grass.append(grass_area)

        self.entry_roads  = entry_roads
        for i in range(len(entry_roads)):
            self.recent_cars.append(None)

        self.valid_routes = valid_routes
        self.schedule     = schedule

        if CONTROLLER_MODE == TRAFFIC_LIGHTS_MODE:

            for intersection in intersections:
                self.traffic_lights[intersection] = TrafficLights(self,
                                                                  intersection)

            for routes in valid_routes:
                for route in routes:
                    for instruction in route:
                        if isinstance(instruction, EnterIntersection):
                            intersection = instruction.road.intersection
                            controller = self.traffic_lights[intersection]
                            instruction.setController(controller)

    def addCar(self, time, entry_num, route_num):
        #i = random.randint(0, len(self.entry_roads)-1)
        #road       = self.entry_roads[i]
        #recent_car = self.recent_cars[i]

        road  = self.entry_roads[entry_num]
        route = self.valid_routes[entry_num][route_num]
        angle = road.angle

        recent_car = self.recent_cars[entry_num]
        if recent_car != None:
            dist_along = road.getDistanceAlong(recent_car.position)

            if dist_along >= CAR_LENGTH + SAFETY_GAP:
                pos = road.start
            else:
                dist = dist_along - CAR_LENGTH - SAFETY_GAP
                pos = road.start + road.vec * (dist / road.length)

        else:
            pos = road.start

        colour, name = next(self.car_generator)

        car = Car(self, name, colour, pos, angle, time)
        self.cars.append(car)
        self.recent_cars[entry_num] = car

        self.controllers.append(CarController(car, road, route))

    def update(self, time):

        # traffic lights mode only
        for intersection in self.traffic_lights:
            self.traffic_lights[intersection].update(time)

        for car in self.cars:
            car.update(time)

        num_cars = len(self.cars)

        for i in range(num_cars):
            car_i = self.cars[i]

            for j in range(i+1, num_cars):
                car_j = self.cars[j]

                dist = (car_i.position - car_j.position).mag()
                if dist < 10 and car_i.checkCollision(car_j):
                    car_i.crash(car_j)
                    car_j.crash(car_i)

        get_new_focus = False
        i = 0
        while i < len(self.controllers):
            car = self.cars[i]
            if car.stopped:
                self.cars.pop(i)
                self.controllers.pop(i)
                if self.selected_car == car:
                    #self.resetZoom()
                    get_new_focus = True
            else:
                i += 1

        if get_new_focus:
            if self.cars:
                self.selected_car = random.choice(self.cars)
            else:
                self.resetZoom()

        for controller in self.controllers:
            controller.update(time)

        for grass in self.grass:
            for car in self.cars:
                if grass.checkCollision(car):
                    grass.colour = DARK_GREEN
                    break
            else:
                grass.colour = LIGHT_GREEN

        self.sendMessages()

        while self.schedule:
            start_time, entry_num, route_num = self.schedule[0]

            if start_time <= time:
                self.addCar(time, entry_num, route_num)
                self.schedule.popleft()
            else:
                break

        while len(self.ghosts) > MAX_GHOSTS:
            self.ghosts.popleft()

    def sendMessages(self):
        messages = {}#SEND_TO_ALL: []}
        for recv in self.controllers:
            messages[recv.name] = []

        # send messages
        for sender in self.controllers:

            for message in sender.sendMessages():
                address, message_type, context, content = message
                message = (sender.name, address, message_type, context, content)

                if address == SEND_TO_ALL:
                    for recv in self.controllers:
                        if sender == recv:
                            continue
                        messages[recv.name].append(message)

                elif address == LINE_OF_SIGHT:
                    for recv in self.controllers:
                        if sender == recv:
                            continue

                        #if CONTROLLER_MODE == TRAFFIC_LIGHTS_MODE:
                        #    dist = (recv.car.centre - sender.car.centre).mag()
                        #    if dist <= SIGHT_RADIUS:
                        #        messages[recv.name].append(message)
                        #else:
                        messages[recv.name].append(message)

                elif address in messages:
                    messages[address].append(message)

        # receive messages
        for controller in self.controllers:
            controller.receiveMessages(messages[controller.name])

    def scaleDistance(self, distance):
        return round(distance * self.scale)

    def getScreenPosition(self, true_position):
        return (true_position + self.offset) * self.scale

    def getDrawable(self, point):
        point = self.getScreenPosition(point)
        return [round(point.x), round(point.y)]

    def getTruePosition(self, screen_position):
        return screen_position/self.scale - self.offset

    def resetZoom(self):
        self.selected_car = None

        self.scale  = self.default_scale
        self.offset = self.default_offset

    def zoomIn(self, mouse_position):
        if self.selected_car != None:
            mouse_position = SCREEN_CENTRE
            true_mouse_position = self.selected_car.centre
        else:
            true_mouse_position = self.getTruePosition(mouse_position)
            #if not self.checkInside(true_mouse_position):
            #    return

        new_scale = min(self.scale * SCALE_CHANGE, self.scale_max)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def zoomOut(self, mouse_position):
        if self.selected_car != None:
            mouse_position = SCREEN_CENTRE
            true_mouse_position = self.selected_car.centre
        else:
            true_mouse_position = self.getTruePosition(mouse_position)
            #if not self.checkInside(true_mouse_position):
            #    return

        new_scale = max(self.scale / SCALE_CHANGE, self.scale_min)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def followCar(self, car):
        screen_centre = self.getTruePosition(SCREEN_CENTRE)
        self.offset  += screen_centre - car.centre

    def startPan(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        #if not self.checkInside(true_mouse_position):
        #    self.panning = False
        #    return

        for car in self.cars:
            if car.checkInside(true_mouse_position):
                self.selected_car = car
                #print("Selected car:", car.name)
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

    def draw(self, paused):
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

        for road in self.all_roads:
            start = self.getDrawable(road.start)
            end   = self.getDrawable(road.end)

            pygame.draw.line(self.screen, BLACK, start, end, 1)

        if CONTROLLER_MODE == TRAFFIC_LIGHTS_MODE:
            for intersection in self.traffic_lights:
                self.traffic_lights[intersection].draw()

        #box = [self.getDrawable(point) for point in self.hull]
        #pygame.draw.polygon(self.screen, BLACK, box, 1)

        for ghost in self.ghosts:
            #ghost.drawPath()
            ghost.draw(False, paused)

        #for controller in self.controllers:
        #    controller.drawRoute()

        #for controller in self.controllers:
        #    controller.drawPath()

        #for car in self.cars:
        #    car.drawPath()

        for car in self.cars:
            car.draw(car is self.selected_car, paused)
            #car.drawExtra()

        #for car in self.cars:
        #    car.drawDesiredPosition()

        for controller in self.controllers:
            controller.draw()


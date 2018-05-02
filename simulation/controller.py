from util import *

from road_network import IntersectionRoad

PATH_MEMORY = 50

MIN_ROUTE_PIECES = 20

class FollowRoad:
    def __init__(self, road, speed):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

        self.next_road = road.next_road

    def checkLights(self):
        return GREEN_LIGHT

    def getNextRoad(self):
        return self.next_road

class ChangeSpeed:
    def __init__(self, speed, timeout):
        self.speed   = speed
        self.timeout = timeout

class EnterIntersection(FollowRoad):
    def __init__(self, road, speed, controller, turn):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

        self.controller = controller
        self.turn       = turn

        exit = road.getExit(turn)
        self.pair      = (road.input_index, exit)
        self.next_road = road.getPath(exit)[0]

    def checkLights(self):
        return self.controller.lights[self.pair]

class CarController:
    def __init__(self, car):
        self.car  = car

        self.route = car.route

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.path = car.path
        self.path.append(self.car.position)

        self.messages = []
        self.car_status = {}

        self.addInstruction(self.car.road)
        self.generateRoute()

    def addInstruction(self, road):
        if isinstance(road, IntersectionRoad):
            while True:
                turn = random.choice([LEFT, CENTRE, RIGHT])
                if road.getExit(turn) != None:
                    break

            controller = self.world.traffic_controllers[road.intersection]
            instruction = EnterIntersection(road, MAX_SPEED,
                                            controller, turn)
        else:
            instruction = FollowRoad(road, MAX_SPEED)

        self.route.append(instruction)

    def generateRoute(self):
        if not self.route:
            return

        while len(self.route) < MIN_ROUTE_PIECES:
            road = self.route[-1].getNextRoad()
            if road == None:
                return
            self.addInstruction(road)

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        self.generateRoute()

    def followCar(self, dist_apart, speedA):#posA, speedA, roadA):
        #distA = 0
        #for instruction in self.route:
        #    if not isinstance(instruction, ChangeSpeed):
        #        road = instruction.road
        #        if road == roadA:
        #            distA += roadA.getDistanceAlong(posA)
        #            break
        #        distA += road.length
        #else:
        #    return False, None

        #distB = self.car.road.getDistanceAlong(self.car.centre)
        #dist_apart = distA - distB

        #if dist_apart <= 0:
        #    # either they're behind you, or they're already crashed into you
        #    return False, None

        stop_distA = calculateStopDistance(speedA)
        stop_distB = dist_apart + stop_distA - CAR_LENGTH - SAFETY_GAP

        if stop_distB <= 0:
            #print(self.name, stop_distB, "too close", self.car.time / 1000)
            return 0#True, 0

        max_speed = calculateMaxSpeed(stop_distB, self.car.speed)
        return max_speed#True, max_speed

    def checkCarsAhead(self):
        # find people on your route
        distB = self.car.road.getDistanceAlong(self.car.centre)

        distance = 0
        options = []
        for instruction in self.route:
            if not isinstance(instruction, ChangeSpeed):
                road = instruction.road

                for car_name in self.car_status:
                    posA, angleA, speedA, roadA = self.car_status[car_name]

                    if road == roadA:
                        distA = distance + roadA.getDistanceAlong(posA)
                        if distA > distB:
                            options.append((distA, speedA))
                #if options:
                #    break
                distance += road.length

        if not options:#else:
            # there's no one on your route
            return MAX_SPEED

        options.sort()
        distA, speedA = options[0]

        dist_apart = distA - distB

        if dist_apart <= 0:
            # either they're behind you, or they're already crashed into you
            return MAX_SPEED

        return self.followCar(dist_apart, speedA)


    def sendMessages(self):
        if self.car.stopped:
            return []

        status = (self.car.centre, self.car.angle,
                  self.car.speed,  self.car.road)
        self.messages.append((LINE_OF_SIGHT, CURRENT_DETAILS, status))
        return self.messages

    def receiveMessages(self, messages):
        if self.car.stopped:
            return

        self.messages.clear()

        #car_status = {}

        self.car_status.clear()

        next_speed = MAX_SPEED
        for message in messages:
            source, destination, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                #position, angle, speed, road = content

                self.car_status[source] = content

                #following, speed_choice = self.checkFollowing(
                #    position, speed, road)
                #if following:
                #    next_speed = min(next_speed, speed_choice)

        next_speed = min(MAX_SPEED, self.checkCarsAhead())

        if next_speed < MAX_SPEED:
            self.car.limitSpeed(next_speed, 1000)

            #self.route.appendleft(ChangeSpeed(next_speed, 1000))

    def drawRoute(self):
        screen = self.world.screen
        colour = self.colour
        for instruction in self.route:
            if isinstance(instruction, ChangeSpeed):
                continue
            road = instruction.road
            waypoint = instruction.waypoint
            a = self.world.getDrawable(road.start)
            b = self.world.getDrawable(road.end)
            w = self.world.getDrawable(waypoint)
            pygame.draw.line(screen,   LIGHTER[colour], a, b, 3)
            pygame.draw.circle(screen, DARKER[colour],  w, 3, 2)


from util import *

from road_network import IntersectionRoad, TerminalRoad

PATH_MEMORY = 50

MIN_ROUTE_PIECES = 20

class FollowRoad:
    def __init__(self, road, speed):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

    def getNextRoad(self):
        return self.road.next_road

class ChangeSpeed:
    def __init__(self, speed, timeout):
        self.speed   = speed
        self.timeout = timeout

class EnterIntersection:
    def __init__(self, road, speed, controller, exit):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

        self.controller = controller
        self.entrance   = road.input_index
        self.exit       = exit

        self.path = road.getPath(exit)

    def checkLights(self):
        return self.controller.lights[(self.entrance, self.exit)]

    def getNextRoad(self):
        return self.path[0]

class ExitWorld:
    def __init__(self, road, speed):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

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

        self.addInstruction(self.car.road)
        self.generateRoute()

    def addInstruction(self, road):
        if isinstance(road, IntersectionRoad):
            exit = random.choice(road.getPathOptions())
            controller = self.world.traffic_controllers[road.intersection]
            instruction = EnterIntersection(road, MAX_SPEED,
                                            controller, exit)

        elif isinstance(road, TerminalRoad):
            instruction = ExitWorld(road, MAX_SPEED)

        else:
            instruction = FollowRoad(road, MAX_SPEED)

        self.route.append(instruction)

    def generateRoute(self):
        if not self.route:
            return

        while len(self.route) < MIN_ROUTE_PIECES:
            instruction = self.route[-1]
            if isinstance(instruction, ExitWorld):
                return
            road = instruction.getNextRoad()
            self.addInstruction(road)

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        self.generateRoute()

    def checkFollowing(self, posA, speedA, roadA):
        distA = 0
        for instruction in self.route:
            if not isinstance(instruction, ChangeSpeed):
                road = instruction.road
                if road == roadA:
                    distA += roadA.getDistanceAlong(posA)
                    break
                distA += road.length
        else:
            return False, None

        distB = self.car.road.getDistanceAlong(self.car.centre)
        dist_apart = distA - distB

        if dist_apart <= 0:
            # either they're behind you, or they're already crashed into you
            return False, None

        safety_gap = CAR_LENGTH + 2
        stop_distA = calculateStopDistance(speedA)
        stop_distB = dist_apart + stop_distA - safety_gap

        if stop_distB <= 0:
            #print(self.name, stop_distB, "too close", self.car.time / 1000)
            return True, 0

        max_speed = calculateMaxSpeed(stop_distB, self.car.speed)
        return True, max_speed

    def sendMessages(self):
        if self.car.stopped:
            return []

        status = (self.car.centre, self.car.angle,
                  self.car.speed,  self.car.road)
        self.messages.append((SEND_TO_ALL, CURRENT_DETAILS, status))
        return self.messages

    def receiveMessages(self, public, private):
        if self.car.stopped:
            return

        self.messages.clear()

        next_speed = MAX_SPEED
        for message in public:
            source, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                position, angle, speed, road = content

                following, speed_choice = self.checkFollowing(
                    position, speed, road)
                if following:
                    next_speed = min(next_speed, speed_choice)

        if next_speed < MAX_SPEED:
            self.route.appendleft(ChangeSpeed(next_speed, 1000))

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


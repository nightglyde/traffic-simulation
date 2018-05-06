from util import *

from road_network import IntersectionRoad

PATH_MEMORY = 50

MIN_ROUTE_PIECES = 20

LOOK_AHEAD_DIST = 3
AVOID_CIRCLES   = False

class FollowRoad:
    def __init__(self, road, speed):
        self.road     = road
        self.waypoint = road.end
        self.speed    = speed

        self.turn = road.next_turn

        self.next_road = road.next_road

    def checkLights(self):
        return GREEN_LIGHT

    def getNextRoad(self):
        return self.next_road

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
    def __init__(self, car, road):
        self.car  = car
        self.road = road
        self.time = car.time

        self.route         = deque()
        self.speed_limit   = -1
        self.speed_timeout = -1

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.path = car.path
        self.path.append(self.car.position)

        self.messages = []
        self.car_status = {}

        self.addInstruction(self.road)
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

    def limitSpeed(self, speed, timeout):
        self.speed_limit   = speed
        self.speed_timeout = self.time + timeout

    def getNextTurn(self):
        for instruction in self.route:
            turn = instruction.turn
            if turn != None:
                return turn

        return CENTRE

    def crossingSpeed(self, instruction, dist_left):
        if instruction.checkLights() == GREEN_LIGHT:
            return MAX_SPEED

        speed = self.car.speed
        max_speed = calculateMaxSpeed(dist_left, speed)
        if speed < max_speed:
            # you can't stop in time, so keep going and hope for the best
            return MAX_SPEED

        return max_speed

    def updateRoute(self):
        # find latest instruction
        while self.route:
            instruction = self.route[0]
            road = instruction.road

            road_vec = road.end - road.start
            road_len = road_vec.mag()

            self_vec  = self.car.centre - road.start
            self_dist = dotProduct(self_vec, road.vec) / road.length

            if self_dist >= road_len:
                self.route.popleft()
                continue
            break

        # check if car has reached the end of its route
        if not self.route:
            return False

        # save the current road
        self.road = road
        self.next_turn = self.getNextTurn()

        # find desired speed
        dist_left = road_len - self_dist - CAR_LENGTH/2
        speed     = self.crossingSpeed(instruction, dist_left)
        if self.time < self.speed_timeout:
            desired_speed = min(speed, self.speed_limit)
        else:
            desired_speed = speed

        # find desired position
        look_ahead = self_dist + LOOK_AHEAD_DIST
        for instruction in self.route:
            road = instruction.road

            road_vec = road.end - road.start
            road_len = road_vec.mag()

            if look_ahead <= road_len:
                desired_position = road.start + road_vec * (look_ahead/road_len)
                break

            look_ahead -= road_len

        else:
            desired_position = road.end

        # find desired angle
        desired_angle = getAngle(desired_position - self.car.position)

        if AVOID_CIRCLES:
            angle = self.car.angle
            pos   = self.car.position

            angle_difference = desired_angle - angle
            if angle_difference < ANGLE_0:
                centre   = getTurningCircle(LEFT, pos, angle, TURN_RADIUS)
                distance = (desired_position - centre).mag()
                if distance < TURN_RADIUS:
                    desired_angle = angle + ANGLE_90
            elif angle_difference > ANGLE_0:
                centre   = getTurningCircle(RIGHT, pos, angle, TURN_RADIUS)
                distance = (desired_position - centre).mag()
                if distance < TURN_RADIUS:
                    desired_angle = angle - ANGLE_90

        return desired_speed, desired_position, desired_angle, self.next_turn

    def update(self, time):
        if self.car.stopped:
            return

        self.time = time

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        self.generateRoute()

        self.car.control(self.updateRoute())

    def followCar(self, dist_apart, speedA):

        stop_distA = calculateStopDistance(speedA)
        stop_distB = dist_apart + stop_distA - CAR_LENGTH - SAFETY_GAP

        if stop_distB <= 0:
            return 0

        max_speed = calculateMaxSpeed(stop_distB, self.car.speed)
        return max_speed

    def checkCarsAhead(self):
        # find people on your route
        distB = self.road.getDistanceAlong(self.car.centre)

        intersection_count = 0
        is_intersection = False

        distance = 0
        options = []
        options2 = []
        for instruction in self.route:

            if isinstance(instruction, EnterIntersection):
                intersection_count += 1
                is_intersection = True

            else:
                if intersection_count > 1:
                    break
                is_intersection = False

            road = instruction.road

            for car_name in self.car_status:
                posA, angleA, speedA, roadA, turnA = self.car_status[car_name]

                if road == roadA:

                    distA = distance + roadA.getDistanceAlong(posA)
                    if distA > distB:
                        options.append((distA, speedA))

                        if is_intersection:
                            if intersection_count == 1:
                                if turnA == instruction.turn:
                                    options2.append((distA, speedA))
                            elif intersection_count == 2:
                                options2.append((distA, speedA))
                        else:
                            if intersection_count == 1:
                                options2.append((distA, speedA))

            distance += road.length

        if not options:
            # there's no one on your route
            return MAX_SPEED

        options.sort()
        distA, speedA = options[0]

        dist_apart = distA - distB

        #if dist_apart <= 0:
        #    # either they're behind you, or they're already crashed into you
        #    return MAX_SPEED

        return self.followCar(dist_apart, speedA)


    def sendMessages(self):
        if self.car.stopped:
            return []

        status = (self.car.centre, self.car.angle, self.car.speed,
                  self.road, self.next_turn)
        self.messages.append((LINE_OF_SIGHT, CURRENT_DETAILS, status))
        return self.messages

    def receiveMessages(self, messages):
        if self.car.stopped:
            return

        self.messages.clear()

        self.car_status.clear()

        next_speed = MAX_SPEED
        for message in messages:
            source, destination, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                self.car_status[source] = content

        next_speed = self.checkCarsAhead()
        if next_speed < MAX_SPEED:
            self.limitSpeed(next_speed, 1000)

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


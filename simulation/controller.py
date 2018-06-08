from util import *

from road_network import IntersectionRoad, FollowRoad, EnterIntersection, VirtualTrafficLights

PATH_MEMORY = 10#50

MIN_ROUTE_PIECES = 20

LOOK_AHEAD_DIST = 3
AVOID_CIRCLES   = False

DURING_INTERSECTION = 0
DURING_TURN         = 1
AFTER_TURN          = 2

class CarController:
    def __init__(self, car, road, route):
        self.car  = car

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour
        self.time   = car.time

        self.route              = deque()
        self.traffic_controller = None
        self.setupRoute(route)

        self.road       = route[0].road
        self.dist_along = road.getDistanceAlong(self.car.centre)

        self.path = car.path
        self.path.append(self.car.position)

        self.knowledge = {}

        self.following_speed = MAX_SPEED
        self.blocked         = False

    def setupRoute(self, route):
        if CONTROLLER_MODE == VIRTUAL_TRAFFIC_LIGHTS_MODE:
            controller = VirtualTrafficLights(self)

            for instruction in route:
                if isinstance(instruction, EnterIntersection):
                    instruction = instruction.copy()
                    instruction.setController(controller)
                self.route.append(instruction)

            self.traffic_controller = controller

        else:
            self.route = deque(route)
            self.traffic_controller = None

    def followCar(self, dist_apart, speedA):

        stop_distA = getStopDistance(speedA)
        stop_distB = dist_apart + stop_distA - CAR_LENGTH - SAFETY_GAP

        if stop_distB <= 0:
            #print("TOO CLOSE", self.name, dist_apart)
            return 0

        max_speed = getSpeedToStop(stop_distB, self.car.speed)
        return max_speed

    def checkCarsAhead(self):
        # find people on your route
        cars_ahead   = []
        cars_turning = []

        distB = self.dist_along

        cars_left = set(self.knowledge.keys())
        distance  = 0

        exit_distance = None

        # this might get rid of the stopping in the middle of the intersection
        # problem. however, also consider that when the car is blocked, it
        # should be able to safely move forward until it reaches the intersection
        if isinstance(self.road, IntersectionRoad):#not self.road.danger:
            turn_status = DURING_INTERSECTION
        else:
            turn_status = None

        for instruction in self.route:
            road = instruction.road

            if turn_status == DURING_INTERSECTION:
                if isinstance(instruction, FollowRoad):
                    turn_status = DURING_TURN
            elif turn_status == DURING_TURN:
                if not instruction.danger:
                    turn_status = AFTER_TURN
                    exit_distance = distance
            elif turn_status == AFTER_TURN:
                if instruction.danger:
                    break

            cars_done = set()
            for car_name in cars_left:
                speedA, roadA, distA, turnA = self.knowledge[car_name]

                if road == roadA:
                    cars_done.add(car_name)
                    distA += distance
                    if distA > distB:
                        cars_ahead.append((distA, speedA, car_name))

                        if turn_status == DURING_INTERSECTION:
                            if turnA == instruction.turn:
                                cars_turning.append((distA, speedA, car_name))
                        elif turn_status == DURING_TURN:
                            cars_turning.append((distA, speedA, car_name))
                        elif turn_status == AFTER_TURN:
                            cars_turning.append((distA, speedA, car_name))

            cars_left -= cars_done
            distance  += road.length

            #last_road = road

            if not cars_left:
                break

            if cars_ahead and turn_status == None:
                break

        if not cars_ahead:
            self.following_speed = MAX_SPEED
            self.blocked = False
            return

        cars_ahead.sort()
        distA, speedA, car_name = cars_ahead[0]
        self.following_speed = self.followCar(distA - self.dist_along, speedA)

        if (not cars_turning) or (exit_distance == None):
            self.blocked = False
            return

        if False:#if CONTROLLER_MODE == TRAFFIC_LIGHTS_MODE:
            cars_turning.sort()
            distA, speedA, car_name = cars_turning[-1]
            stop_distA = distA + getStopDistance(speedA)

            safe_space = stop_distA - exit_distance - CAR_LENGTH/2

        else:
            safe_space = distance - exit_distance - CAR_LENGTH/2

        #cars_turning.sort()
        #distA, speedA, car_name = cars_turning[-1]
        #stop_distA = distA + getStopDistance(speedA)

        #safe_space = stop_distA - exit_distance - CAR_LENGTH/2

        if safe_space <= 0:
            self.blocked = False
            return

        cars_fit = safe_space / (CAR_LENGTH + SAFETY_GAP)

        self.blocked = cars_fit < len(cars_turning)

    def followCar(self, dist_apart, speedA):

        stop_distA = getStopDistance(speedA)
        stop_distB = dist_apart + stop_distA - CAR_LENGTH - SAFETY_GAP

        if stop_distB <= 0:
            #print("TOO CLOSE", self.name, dist_apart)
            return 0

        max_speed = getSpeedToStop(stop_distB, self.car.speed)
        return max_speed

    def getDesiredSpeed(self):
        if not self.blocked and self.route[0].checkLights() == GREEN_LIGHT:
            desired_speed = MAX_SPEED

        else:
            dist_left = self.road.length - self.dist_along
            speed     = self.car.speed
            stop_dist = getStopDistance(speed)

            if dist_left < stop_dist:
                # you can't stop in time, so keep going and hope for the best
                desired_speed = MAX_SPEED
            else:
                desired_speed = getSpeedToStop(dist_left - CAR_LENGTH/2, speed)

        return min(desired_speed, self.following_speed)

    def getDesiredPosition(self):
        look_ahead = self.dist_along + LOOK_AHEAD_DIST
        for instruction in self.route:
            road = instruction.road
            road_len = road.length

            if look_ahead <= road_len:
                desired_position = road.start + road.vec * (look_ahead/road_len)
                break

            look_ahead -= road_len

        else:
            desired_position = road.end

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

        return desired_position, desired_angle

    def getTurningSignal(self):
        for instruction in self.route:
            turn = instruction.turn
            if turn != None:
                return turn

        return CENTRE

    def update(self, time):
        if self.car.stopped:
            return

        self.time = time

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        # update route
        while self.route:
            instruction = self.route[0]
            road = instruction.road

            dist_along = road.getDistanceAlong(self.car.centre)
            if dist_along >= road.length:
                self.route.popleft()
                continue
            break

        # check if car has reached the end of its route
        if not self.route:
            self.car.stop()
            return

        # save the current road
        self.road       = road
        self.dist_along = dist_along

        # check if the road ahead is blocked, and
        # check if you are closely following a car
        self.checkCarsAhead()

        # update traffic controller
        if self.traffic_controller != None:
            self.traffic_controller.update(time, instruction)

        # generate control signal
        desired_speed                   = self.getDesiredSpeed()
        desired_position, desired_angle = self.getDesiredPosition()
        self.next_turn                  = self.getTurningSignal()

        self.car.control(desired_speed, desired_position,
                         desired_angle, self.next_turn)

    def sendMessages(self):
        messages = []
        if self.car.stopped:
            return messages

        content = (self.car.speed, self.road, self.dist_along, self.next_turn)
        messages.append((LINE_OF_SIGHT, VISIBLE_DETAILS, None, content))

        if self.traffic_controller != None:
            messages += self.traffic_controller.sendMessages()

        return messages

    def receiveMessages(self, messages):
        if self.car.stopped:
            return

        self.knowledge.clear()

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if message_type == VISIBLE_DETAILS:
                self.knowledge[source] = content

        if self.traffic_controller != None:
            self.traffic_controller.receiveMessages(messages)

    def drawRoute(self):
        screen = self.world.screen
        colour = self.colour
        for instruction in self.route:
            road = instruction.road
            a = self.world.getDrawable(road.start)
            b = self.world.getDrawable(road.end)
            pygame.draw.line(screen,   LIGHTER[colour], a, b, 3)
            #pygame.draw.circle(screen, DARKER[colour],  w, 3, 2)

    def draw(self):
        if self.traffic_controller != None:
            self.traffic_controller.draw()


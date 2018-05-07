from util import *

from road_network import IntersectionRoad, FollowRoad, EnterIntersection

PATH_MEMORY = 10#50

MIN_ROUTE_PIECES = 20

LOOK_AHEAD_DIST = 3
AVOID_CIRCLES   = False

BEFORE_INTERSECTION = 0
DURING_INTERSECTION = 1
DURING_TURN         = 2
AFTER_TURN          = 3

class CarController:
    def __init__(self, car, road, route):
        self.car  = car

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour
        self.time   = car.time

        self.route      = deque(route)
        self.road       = route[0].road
        self.dist_along = road.getDistanceAlong(self.car.centre)

        self.path = car.path
        self.path.append(self.car.position)

        self.knowledge = {}

    def addInstruction(self, road):
        if isinstance(road, IntersectionRoad):
            while True:
                turn = random.choice([LEFT, CENTRE, RIGHT])
                if road.getExit(turn) != None:
                    break

            controller = self.world.traffic_controllers[road.intersection]
            instruction = EnterIntersection(road, turn)
            instruction.setController(controller)
            self.route.append(instruction)
        else:
            instruction = FollowRoad(road)
            self.route.append(instruction)

    def generateRoute(self):
        if not self.route:
            return

        while len(self.route) < MIN_ROUTE_PIECES:
            road = self.route[-1].getNextRoad()
            if road == None:
                return
            self.addInstruction(road)

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

        entrance_distance = None
        exit_distance     = None

        turn_status = BEFORE_INTERSECTION
        for instruction in self.route:

            if turn_status == BEFORE_INTERSECTION:
                if isinstance(instruction, EnterIntersection):
                    turn_status = DURING_INTERSECTION
            elif turn_status == DURING_INTERSECTION:
                if isinstance(instruction, FollowRoad):
                    turn_status = DURING_TURN
                    entrance_distance = distance
            elif turn_status == DURING_TURN:
                if not instruction.danger:
                    turn_status = AFTER_TURN
                    exit_distance = distance
            elif turn_status == AFTER_TURN:
                if instruction.danger:
                    break

            road = instruction.road
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

            if not cars_left:
                break

        if not cars_ahead:
            return MAX_SPEED

        cars_ahead.sort()

        distA, speedA, car_name = cars_ahead[0]
        following_speed = self.followCar(distA - self.dist_along, speedA)

        if (not cars_turning) or (exit_distance == None):
            return following_speed

        cars_turning.sort()

        distA, speedA, car_name = cars_turning[-1]
        distA += getStopDistance(speedA)
        safe_space = distA - exit_distance - CAR_LENGTH/2
        # for some reason this gets different values for different turns...

        cars_fit = safe_space / (CAR_LENGTH + SAFETY_GAP)

        if cars_fit < 0:
            return following_speed

        #else:
        #    print("#"+self.name, car_name, len(cars_turning), cars_fit, safe_space, self.time / 1000)

        if cars_fit >= len(cars_turning):
            return following_speed

        dist_left = entrance_distance - self.dist_along - CAR_LENGTH/2
        turn_speed = getSpeedToStop(dist_left, self.car.speed)
        return min(following_speed, turn_speed)

    def getDesiredSpeed(self):
        if self.route[0].checkLights() == GREEN_LIGHT:
            desired_speed = MAX_SPEED

        else:
            dist_left     = self.road.length - self.dist_along - CAR_LENGTH/2
            speed         = self.car.speed
            speed_to_stop = getSpeedToStop(dist_left, speed)
            if speed < speed_to_stop:
                # you can't stop in time, so keep going and hope for the best
                desired_speed = MAX_SPEED
            else:
                desired_speed = speed_to_stop

        return min(desired_speed, self.checkCarsAhead())

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

        self.generateRoute()

        # update route
        while self.route:
            instruction = self.route[0]
            road = instruction.road

            dist_along = road.getDistanceAlong(self.car.centre)
            if dist_along >= road.length:
                self.route.popleft()
                continue

            # save the current road
            self.road       = road
            self.dist_along = dist_along
            break

        # check if car has reached the end of its route
        if not self.route:
            self.car.stop()
            return

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

        status = (self.car.speed, self.road, self.dist_along, self.next_turn)
        messages.append((LINE_OF_SIGHT, CURRENT_DETAILS, status))

        return messages

    def receiveMessages(self, messages):
        if self.car.stopped:
            return

        self.knowledge.clear()

        next_speed = MAX_SPEED
        for message in messages:
            source, destination, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                self.knowledge[source] = content

    def drawRoute(self):
        screen = self.world.screen
        colour = self.colour
        for instruction in self.route:
            road = instruction.road
            a = self.world.getDrawable(road.start)
            b = self.world.getDrawable(road.end)
            pygame.draw.line(screen,   LIGHTER[colour], a, b, 3)
            #pygame.draw.circle(screen, DARKER[colour],  w, 3, 2)


from util import *

from road_network import IntersectionRoad, FollowRoad, EnterIntersection, VirtualTrafficLights, MyTrafficController

#PATH_MEMORY = 10#50

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

        self.route = deque()
        self.stops = deque()
        self.roads = set()
        self.traffic_controller = None
        self.setupRoute(route)

        self.road       = route[0].road
        self.dist_along = road.getDistanceAlong(self.car.centre)

        #self.path = car.path
        #self.path.append(self.car.position)

        self.knowledge     = {}
        self.road_register = {}
        self.stop_register = {}

        self.following_speed = MAX_SPEED
        #self.blocked         = False
        self.spaces_left     = ROAD_CLEAR

        self.next_turn = None # Needed???

    def setupRoute(self, route):
        if self.world.strategy == TRAFFIC_LIGHTS_MODE:
            for instruction in route:

                if isinstance(instruction, EnterIntersection):
                    self.stops.append(instruction.road)

                self.route.append(instruction)
                self.roads.add(instruction.road)

            self.traffic_controller = None

        else:
            if self.world.strategy == VIRTUAL_TRAFFIC_LIGHTS_MODE:
                controller = VirtualTrafficLights(self)
            elif self.world.strategy == MY_TRAFFIC_CONTROLLER_MODE:
                controller = MyTrafficController(self)

            for instruction in route:
                if isinstance(instruction, EnterIntersection):
                    instruction = instruction.copy()
                    instruction.setController(controller)

                    self.stops.append(instruction.road)

                self.route.append(instruction)
                self.roads.add(instruction.road)

            self.traffic_controller = controller

    def checkBlocked(self):
        self.spaces_left = ROAD_CLEAR

        if not isinstance(self.road, IntersectionRoad):
            return

        if len(self.stops) < 2:
            return

        curr_stop = self.stops[0]
        next_stop = self.stops[1]

        queue_capacity = next_stop.length / MIN_DIST_APART

        if next_stop in self.stop_register:
            queue_length = len(self.stop_register[next_stop])
        else:
            queue_length = 0

        if curr_stop in self.stop_register:

            distB = self.dist_along

            for car_name in self.stop_register[curr_stop]:
                speedA, roadA, distA, turnA, stopA = self.knowledge[car_name]

                if distA > distB and turnA == self.next_turn:
                    queue_length += 1

        if queue_length == 0:
            return

        self.spaces_left = max(0, queue_capacity - queue_length)

    def alt_checkBlocked(self):
        distB = self.dist_along

        if not isinstance(self.road, IntersectionRoad):
            #self.blocked = False
            self.spaces_left = ROAD_CLEAR
            return

        dist_left = self.road.length - distB
        if dist_left > VTL_THRESHOLD:
            #self.blocked = False
            self.spaces_left = ROAD_CLEAR
            return

        cars_turning  = []
        exit_distance = None

        turn_status = DURING_INTERSECTION

        distance = 0
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

            if road in self.road_register:
                for car_name in self.road_register[road]:
                    speedA, roadA, distA, turnA, stopA = self.knowledge[car_name]

                #for car_name, speedA, distA, turnA in self.knowledge[road]:
                    distA += distance

                    if turn_status == DURING_INTERSECTION:
                        if distA > distB and turnA == instruction.turn:
                            cars_turning.append((distA, speedA, car_name))
                    else:
                        cars_turning.append((distA, speedA, car_name))

            distance += road.length

        if (not cars_turning) or (exit_distance == None):
            #self.blocked = False
            self.spaces_left = ROAD_CLEAR
            return

        if False:#if self.world.strategy == TRAFFIC_LIGHTS_MODE:
            cars_turning.sort()
            distA, speedA, car_name = cars_turning[-1]
            stop_distA = distA + getStopDistance(speedA)

            safe_space = stop_distA - exit_distance - CAR_LENGTH/2

        else:
            safe_space = distance - exit_distance - CAR_LENGTH/2

        if safe_space <= 0:
            print("APPLEDIRT")
            #self.blocked = False
            self.spaces_left = ROAD_CLEAR
            return

        cars_fit = safe_space / MIN_DIST_APART
        #self.blocked = cars_fit < len(cars_turning)

        self.spaces_left = max(0, cars_fit - len(cars_turning) + 1)

        #print(self.name, cars_fit < len(cars_turning), cars_fit, len(cars_turning), self.spaces_left)

    def checkCarsAhead(self):
        distB = self.dist_along

        distance   = 0
        cars_ahead = []

        dist_thresh = distB + getStopDistance(self.car.speed) + MIN_DIST_APART

        for instruction in self.route:
            road = instruction.road

            if road in self.road_register:
                for car_name in self.road_register[road]:
                    speedA, roadA, distA, turnA, stopA = self.knowledge[car_name]

            #if road in self.knowledge:
            #    for car_name, speedA, distA, turnA in self.knowledge[road]:

                    distA += distance

                    if distA > distB:
                        cars_ahead.append((distA, speedA, car_name))

                if cars_ahead:
                    break

            distance += road.length
            if distance > dist_thresh: # follow distance
                break

        if not cars_ahead:
            self.following_speed = MAX_SPEED
            return

        cars_ahead.sort()
        distA, speedA, car_name = cars_ahead[0]
        self.following_speed = getFollowSpeed(distA - self.dist_along,
                                              self.car.speed, speedA)

    def getDesiredSpeed(self):
        if self.spaces_left >= 1 and self.route[0].checkLights() == GREEN_LIGHT:
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

        #self.path.append(self.car.position)
        #if len(self.path) > PATH_MEMORY:
        #    self.path.popleft()

        # update route
        while self.route:
            instruction = self.route[0]
            road = instruction.road

            dist_along = road.getDistanceAlong(self.car.centre)
            if dist_along >= road.length:
                self.route.popleft()
                self.roads.remove(road)

                if self.stops and road == self.stops[0]:
                    self.stops.popleft()

                continue
            break

        # check if car has reached the end of its route
        if not self.route:
            self.car.stop()
            return

        # was moved from below
        self.next_turn = self.getTurningSignal()

        # save the current road
        self.road       = road
        self.dist_along = dist_along

        self.checkBlocked()   # check if the road ahead is blocked
        self.checkCarsAhead() # check if you are closely following a car

        # update traffic controller
        if self.traffic_controller != None:
            self.traffic_controller.update(time, instruction)

        # generate control signal
        desired_speed                   = self.getDesiredSpeed()
        desired_position, desired_angle = self.getDesiredPosition()

        self.car.control(desired_speed, desired_position,
                         desired_angle, self.next_turn,
                         self.road)

    def sendMessages(self):
        messages = []
        if self.car.stopped:
            return messages

        if self.stops:
            next_stop = self.stops[0]
        else:
            next_stop = None

        content = (self.car.speed, self.road, self.dist_along, self.next_turn, next_stop)
        messages.append((LINE_OF_SIGHT, VISIBLE_DETAILS, None, content))

        if self.traffic_controller != None:
            messages += self.traffic_controller.sendMessages()

        return messages

    def receiveMessages(self, messages):
        if self.car.stopped:
            return

        self.knowledge.clear()
        self.road_register.clear()
        self.stop_register.clear()

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if message_type == VISIBLE_DETAILS:
                #self.knowledge[source] = content

                speed, road, dist_along, next_turn, next_stop = content

                #if not road in self.roads:
                #    continue

                self.knowledge[source] = content

                if next_stop in self.stop_register:
                    self.stop_register[next_stop].append(source)
                else:
                    self.stop_register[next_stop] = [source]

                if road in self.roads:
                    if road in self.road_register:
                        self.road_register[road].append(source)
                    else:
                        self.road_register[road] = [source]

                #new_content = (source, speed, dist_along, next_turn)

                #if road in self.knowledge:
                #    self.knowledge[road].append(new_content)
                #else:
                #    self.knowledge[road] = [new_content]


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

        #if self.spaces_left < ROAD_CLEAR:
        #    pos = self.world.getDrawable(self.car.centre)

        #    font = pygame.font.SysFont('Helvetica', 12, bold=True)
        #    text = font.render(str(round(self.spaces_left, 2)), False, BLACK)
        #    rect = text.get_rect(center=pos)
        #    self.world.screen.blit(text, rect)


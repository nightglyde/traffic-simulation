from util import *

from obstacle import Obstacle
from waypoint import Waypoint, FuturePoint
from generate_world import TerminalRoad

MAX_WAYPOINTS = 10
MAX_FUTURE    = 10
FUTURE_SPEED  = 100#20#10#20#6

FUTURE_INTERVAL = TIME_STEP * 6

PATH_MEMORY = 50

MIN_ROUTE_PIECES = 20

SENSE_GIVE_WAY_THRESHOLD = 30

class CarController(Obstacle):
    def __init__(self, car):
        self.car  = car

        self.route = car.route

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.sim_car = self.car.copy()
        self.future  = deque()

        self.path = car.path
        self.path.append(self.car.position)

        self.messages       = []
        self.car_status     = {}
        self.give_way_rules = {}

        self.give_way_announcements = {}

        self.generateRoute()

    def clearFuture(self):
        self.future.clear()
        self.sim_car = self.car.copy()

    def simulateFuture(self):
        while self.future and self.future[0].end_time < self.car.time:
            if (self.future[0].position - self.car.position).mag() > 2:
                self.clearFuture()
                break
            self.future.popleft()

        if len(self.future) >= MAX_FUTURE:
            return

        car = self.sim_car
        for i in range(FUTURE_SPEED):
            if car.time % FUTURE_INTERVAL == 0:
                if len(self.future) >= MAX_FUTURE:
                    return

                if self.future:
                    start_time = self.future[-1].end_time
                    start_hull = self.future[-1].end_hull
                else:
                    start_time = self.car.time
                    start_hull = self.car.hull
                self.future.append(FuturePoint(car, start_time, start_hull))

            car.update(car.time + TIME_STEP)

    def addInstruction(self, instruction):
        self.route.append(instruction)
        self.sim_car.route.append(instruction)

    def generateRoute(self):
        while len(self.route) < MIN_ROUTE_PIECES:
            if not self.route:
                road = self.car.road
            else:
                road = self.route[-1].getNextRoad()

            # this is an arbitrary value that happens to work with
            # getting the car to stop in time for the intersection
            dist = 15
            if isinstance(road, TerminalRoad):
                if road.length > dist:
                    distance = road.length - dist

                    waypoint = road.start + road.vec * (distance / road.length)

                    # if we're able to get the cars to judge speeds and distances
                    # properly, we won't need this bit
                    self.addInstruction(FollowRoad(road, waypoint, MAX_SPEED))

                exit = random.choice(road.getPathOptions())
                self.addInstruction(TrafficLight(road, exit))

            else:
                self.addInstruction(FollowRoad(road, road.end, MAX_SPEED))

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        self.generateRoute()

        #self.simulateFuture()

    def checkFollowing(self, car_name):
        car_pos, car_angle, car_speed, car_road = self.car_status[car_name]

        my_speed = self.car.speed

        if my_speed <= car_speed:
            # you're not going to crash into them
            return False, None

        my_distance = self.car.road.getDistanceAlong(self.car.position)

        their_distance = 0
        for instruction in self.route:
            if not isinstance(instruction, ChangeSpeed):
                road = instruction.road

                if road == car_road:
                    their_distance += car_road.getDistanceAlong(car_pos)
                    break

                their_distance += road.length

        else:
            return False, None

        # turn this into a general form, so that for any object (stationary
        # or moving), we can maintain a safe distance from that object,
        # regardless of whether that object, speeds up, slows down, remains
        # at the same speed, or is completely stationary. if the object is
        # is stationary, we need to choose a cautious speed of approach, such
        # that we will be able to slow down in time to stop in time to get to
        # the safe distance. if the object is moving, we need to be prepared
        # for them to slow down. to handle this, we could pick a speed slower
        # than theirs, or scale the "safe distance" by how fast we are going

        # could try to approximate the acceleration of the other car, by looking
        # at their change in speed over time. however, i'd prefer to be able
        # to do this using speed alone

        # what if they're getting slower?
        # what if you want to go more forwards so that you're closer to
        # the next car?

        distance_apart = their_distance - my_distance - CAR_LENGTH - 1#safety gap

        if distance_apart <= 0:
            # either they're behind you, or they're already crashed into you
            return False, None

        my_speed = self.car.speed

        deceleration = min(BRAKING_CONSTANT, CAR_WEIGHT) / CAR_MASS
        braking_time = (my_speed - car_speed) / deceleration

        time_until_crash = distance_apart / (my_speed - car_speed)

        return True, time_until_crash - braking_time

    def checkGiveWay(self, car_name):
        car_pos, car_angle, car_speed, car_road = self.car_status[car_name]

        ab = getVector(self.car.angle)
        xy = getVector(car_angle)
        ax = car_pos - self.car.centre

        ax_dist = ax.mag()

        if ax_dist > SENSE_GIVE_WAY_THRESHOLD:
            # car is too far away to bother
            return False

        ab_cross_xy = crossProduct(ab, xy)

        turn = sign(ab_cross_xy)
        if turn == CENTRE:
            # parallel

            if dotProduct(ab, xy) <= 0:
                # facing opposite directions
                return self.name > car_name

            ax_dot_xy = dotProduct(ax, xy)
            if ax_dot_xy > 0:
                # car 1 is behind car 2
                return True
            if ax_dot_xy < 0:
                # car 1 is in front of car 2
                return False

            ax_cross_ab = crossProduct(ax, ab)
            if ax_cross_ab < 0:
                # car 1 is to the left of car 2
                return True
            if ax_cross_ab > 0:
                # car 1 is to the right of car 2
                return False

            # car 1 is on top of car 2
            return self.name > car_name

        ax_cross_ab = crossProduct(ax, ab)
        ax_cross_xy = crossProduct(ax, xy)

        ab_rel_dist = ax_cross_xy / ab_cross_xy
        xy_rel_dist = ax_cross_ab / ab_cross_xy

        if ab_rel_dist > xy_rel_dist:
            return True

        if ab_rel_dist < xy_rel_dist:
            return False

        return turn == RIGHT

        #intersect = self_position + ab * ab_rel_dist

    def checkFuture(self, their_name, their_futures, giving_way_to):
        for my_future in self.future:
            for their_future in their_futures:
                if my_future.checkCollision(their_future):
                    return True
        return False

    def sendMessages(self):
        if self.car.stopped:
            return []

        status = (self.car.centre, self.car.angle,
                  self.car.speed,  self.car.road)
        self.messages.append((SEND_TO_ALL, CURRENT_DETAILS, status))
        #self.messages.append((SEND_TO_ALL, FUTURE_DETAILS, self.future.copy()))
        return self.messages

    def receiveMessages(self, public, private):
        if self.car.stopped:
            return

        self.messages.clear()

        giving_way_to = set()
        match_speed_of = set()
        #given_way_by  = set()

        for message in public:
            source, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                position, angle, speed, road = content
                self.car_status[source]      = (position, angle, speed, road)

                #if source in self.give_way_announcements:
                #    give_way, timeout = self.give_way_announcements[source]

                #    if self.car.time >= timeout:
                #        del self.give_way_announcements[source]
                #        self.give_way_rules[source] = self.checkGiveWay(source)#[0]

                #else:

                self.give_way_rules[source] = self.checkGiveWay(source)

                if self.give_way_rules[source]:

                    following, time_left = self.checkFollowing(source)
                    if following:
                        print(self.name, "following", source, time_left)

                        if time_left < 1:
                            match_speed_of.add(source)

                #if source in given_way_by:
                #    self.give_way_rules[source] = False
                #else:
                #    self.give_way_rules[source] = self.checkGiveWay(source)[0]

            elif message_type == FUTURE_DETAILS:
                if source in self.give_way_rules:
                    if self.give_way_rules[source]:
                        if self.checkFuture(source, content, giving_way_to):
                            print(self.name, "is giving way to", source,
                                  "at time", self.car.time / 1000)
                            giving_way_to.add(source)

                        #elif self.checkFollowing(source):
                        #    print(self.time, "should match speed of", source,
                        #          "at time", self.car.time / 1000)
                        #    match_speed_of.add(source)


            elif message_type == GIVE_WAY_MESSAGE:
                car_name, timeout = content
                if car_name == self.name:
                    print(source, "is giving way to", car_name,
                          "until time", timeout)
                    self.give_way_rules[source] = False
                    self.give_way_announcements[source] = (False, timeout)

                    # find a way to make this last over several seconds,
                    # so that they don't switch their give ways

        if giving_way_to:
            #self.car.setDesiredSpeed(0, self.car.time + TIME_STEP*20, MAX_SPEED)
            #road, waypoint, desired_speed, time = self.route[0]
            #self.route.appendleft((road, waypoint, 0, 1000))
            self.route.appendleft(ChangeSpeed(0, 1000))
            self.clearFuture()

            #for car_name in giving_way_to:
            #    timeout = self.car.time + 4000
            #    print(self.car.time, timeout)

            #    content = (car_name, timeout)
            #    self.messages.append((SEND_TO_ALL, GIVE_WAY_MESSAGE, content))
            #    self.give_way_announcements[car_name] = (True, timeout)

        elif match_speed_of:
            min_speed = MAX_SPEED
            for car_name in match_speed_of:

                print(self.name, "is matching speed of", car_name,
                      "at time", self.car.time / 1000, self.car.speed)

                position, angle, speed, road = self.car_status[car_name]

                min_speed = min(speed, min_speed)

            print(self.name, self.car.speed, min_speed)

            # temporary: use an underestimate, see if that helps
            min_speed *= 0.75

            #road, waypoint, desired_speed, time = self.route[0]
            #self.route.appendleft((road, waypoint, min_speed, 1000))
            self.route.appendleft(ChangeSpeed(min_speed, 1000))
            self.clearFuture()

    def drawWaypoints(self):
        #if self.waypoints:
        #    self.waypoints[0].draw()

        #screen = self.world.screen
        #colour = self.colour
        #for road, waypoint, speed, time in self.route:
        #    a = self.world.getDrawable(road.start)
        #    b = self.world.getDrawable(road.end)
        #    w = self.world.getDrawable(waypoint)
        #    pygame.draw.line(screen, LIGHTER[colour], a, b, 3)
        #    pygame.draw.circle(screen, DARKER[colour], w, 3, 2)

        for future_point in self.future:
            future_point.draw()

        #for car in self.world.cars:
        #    if car != self.car:
        #        intersect = self.world.getDrawable(checkGiveWay(self.car, car))
        #        pygame.draw.circle(screen, DARKER[colour], intersect, 3, 2)


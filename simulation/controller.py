from util import *

from obstacle import Obstacle
from waypoint import Waypoint, FuturePoint

MAX_WAYPOINTS = 10
MAX_FUTURE    = 10
FUTURE_SPEED  = 20#10#20#6

FUTURE_INTERVAL = TIME_STEP * 6

PATH_MEMORY = 50

MIN_ROUTE_PIECES = 20

SENSE_GIVE_WAY_THRESHOLD = 30

class CarController(Obstacle):
    def __init__(self, car, road):
        self.car  = car
        #self.road = road

        self.route = car.route#deque()
        self.next_road = road
        #car.control(self.route)

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.sim_car = self.car.copy()
        self.future  = deque()

        self.waypoints     = deque()
        self.score         = 0
        self.waypoint_time = self.car.time
        #self.generateWaypoints()

        self.path = car.path
        self.path.append(self.car.position)

        self.messages       = []
        self.car_status     = {}
        self.give_way_rules = {}

        #self.slow_time = -1
        #self.keep_time = -1

    def clearFuture(self):
        self.future.clear()
        self.sim_car = self.car.copy()

    def clearWaypoints(self):
        self.waypoints.clear()
        self.waypoint_time = self.car.time
        self.clearFuture()

    def addWaypoint(self, waypoint):
        self.waypoints.append(waypoint)
        self.sim_waypoints.append(waypoint)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1].position
        else:
            prev = self.car.position

        while True:
            pos      = self.world.generateRandomPosition()
            angle    = getAngle(pos - prev)
            waypoint = Waypoint(self, pos, angle)

            if self.world.checkWaypoint(waypoint):
                self.addWaypoint(waypoint)
                return

    def alt_addRandomWaypoint(self):
        if self.waypoints:
            waypoints = self.waypoints
            prev      = waypoints[0].position
        else:
            waypoints = [self.car]
            prev      = self.car.angle

        options = self.world.getWaypointOptions(waypoints)
        if not options:
            options = self.world.waypoint_options

        pos   = random.choice(options)
        angle = getAngle(pos - prev)
        waypoint = Waypoint(self, pos, angle)
        self.addWaypoint(waypoint)

    def generateWaypoints(self):
        while len(self.waypoints) < MAX_WAYPOINTS:
            self.addRandomWaypoint()

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

            #for obstacle in self.world.obstacles:
            #    if obstacle.checkCollision(car):

            #        self.route.appendleft((self.road,
            #            self.car.time + TIME_STEP * 10, 0))

            #        self.clearFuture()
            #        return

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        #while self.waypoints:
        #    waypoint = self.waypoints[0]

        #    if waypoint.checkInside(self.car.centre):
        #        self.waypoints.popleft()
        #        self.score += 1
        #        self.waypoint_time = self.car.time
        #    else:
        #        break

        #    self.generateWaypoints()

        # generate route
        while len(self.route) < MIN_ROUTE_PIECES:

            # randomised route now, path finding later
            road = random.choice(self.next_road.next_roads)
            self.next_road = road

            start    = road.start
            end      = road.end
            road_vec = end - start

            mag = road_vec.mag()
            for i in range(1, int(mag), 5):
                pos = start + road_vec * (i / mag)

                instruction = (road, pos, MAX_SPEED, None)

                self.route.append(instruction)
                self.sim_car.route.append(instruction)

            instruction = (road, end, MAX_SPEED, None)
            self.route.append(instruction)
            self.sim_car.route.append(instruction)

        #self.road = self.route[0][0]

        self.simulateFuture()

    def checkGiveWay(self, car_name):
        car_pos, car_angle, car_speed = self.car_status[car_name]

        ab = getVector(self.car.angle)
        xy = getVector(car_angle)
        ax = car_pos - self.car.position

        if ax.mag() > SENSE_GIVE_WAY_THRESHOLD:
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

        if turn == RIGHT:
            return True

        return False

        #intersect = self_position + ab * ab_rel_dist

    def checkFutures(self, their_name, their_futures, giving_way_to):
        for my_future in self.future:
            for their_future in their_futures:

                if my_future.checkCollision(their_future):

                    #if self.checkGiveWay(their_name):
                    print(self.name, "is giving way to", their_name,
                          "at time", self.car.time / 1000)
                    #giving_way_to.append((their_name, my_future.start_time))
                    giving_way_to.add(their_name)

                    return


        #my_iter    = iter(self.future)
        #their_iter = iter(content)

        #try:
        #    my_future    = next(my_iter)
        #    their_future = next(their_iter)
        #except StopIteration:
        #    continue

        #while True:
        #    try:
        #        if my_future.checkCollision(their_future):
        #            if checkGiveWay(my_future, their_future):
        #                print(self.name, "is giving way to", source,
        #                      "at time", self.car.time / 1000)
        #                giving_way_to.append(source)
        #            break

        #        if my_future.start_time <= their_future.start_time:
        #            my_future = next(my_iter)
        #        else:
        #            their_future = next(their_iter)

        #    except StopIteration:
        #        break

        #i_points = len(self.future)
        #j_points = len(content)

        #i = 0
        #j = 0

        #my_future = self.future[i]
        #their_future = content[j]

        #while i < i_points and j < j_points:

    def sendMessages(self):
        if self.car.stopped:
            return []

        status = (self.car.position, self.car.angle, self.car.speed)
        self.messages.append((SEND_TO_ALL, CURRENT_DETAILS, status))
        self.messages.append((SEND_TO_ALL, FUTURE_DETAILS, self.future.copy()))
        return self.messages

    def receiveMessages(self, public, private):
        if self.car.stopped:
            return

        self.messages.clear()

        giving_way_to = set()
        given_way_by  = set()

        for message in public:
            source, message_type, content = message

            if source == self.name:
                continue

            elif message_type == CURRENT_DETAILS:
                position, angle, speed  = content
                self.car_status[source] = (position, angle, speed)

                if source in given_way_by:
                    self.give_way_rules[source] = False
                else:
                    self.give_way_rules[source] = self.checkGiveWay(source)

            elif message_type == FUTURE_DETAILS:
                if source in self.give_way_rules:
                    if self.give_way_rules[source]:
                        self.checkFutures(source, content, giving_way_to)

            elif message_type == GIVE_WAY_MESSAGE:
                if content == self.name:
                    self.give_way_rules[source] = False
                    given_way_by.add(source)

                    # find a way to make this last over several seconds,
                    # so that they don't switch their give ways

        if giving_way_to:
            self.car.setDesiredSpeed(0, self.car.time + TIME_STEP*20, MAX_SPEED)
            road, waypoint, desired_speed, time = self.route[0]
            self.route.appendleft((road, waypoint, 0,
                                   self.car.time + TIME_STEP*20))


            #last_road = self.sim_car.route[0][0]

            #stop_at_next = False
            #for i in range(len(self.route)):
            #    road, waypoint, desired_speed, time = self.route[i]

                #if road == last_road:
                #    stop_at_next = True

                #elif stop_at_next:
                #    break

                #desired_speed = #max(0.1, desired_speed/2)#-1)
            #    desired_speed = desired_speed/2

            #    self.route[i] = (road, waypoint, desired_speed, time)

            #    if i >= 5:
            #        break

            self.clearFuture()

            for car_name in giving_way_to:
                self.messages.append((SEND_TO_ALL, GIVE_WAY_MESSAGE, car_name))

    def drawWaypoints(self):
        #if self.waypoints:
        #    self.waypoints[0].draw()

        #screen = self.world.screen
        #colour = self.colour
        #for road, waypoint, speed, time in self.route:
        #    a = self.world.getDrawable(road.start)
        #    b = self.world.getDrawable(road.end)
            #w = self.world.getDrawable(waypoint)
        #    pygame.draw.line(screen, LIGHTER[colour], a, b, 3)
            #pygame.draw.circle(screen, DARKER[colour], w, 3, 2)

        for future_point in self.future:
            future_point.draw()

        #for car in self.world.cars:
        #    if car != self.car:
        #        intersect = self.world.getDrawable(checkGiveWay(self.car, car))
        #        pygame.draw.circle(screen, DARKER[colour], intersect, 3, 2)


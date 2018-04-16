from util import *

from obstacle import Obstacle
from waypoint import Waypoint, FuturePoint

MAX_WAYPOINTS = 10
MAX_FUTURE    = 20#10
FUTURE_SPEED  = 6

FUTURE_INTERVAL = TIME_STEP * 3#6

PATH_MEMORY = 50

MAX_SPEED  = 15
SLOW_SPEED = 7.5

MIN_ROUTE_PIECES = 20

def checkGiveWay(self_future, other_future):
    self_position = self_future.position
    self_angle    = self_future.angle

    other_position = other_future.position
    other_angle    = other_future.angle

    ab = getVector(self_angle)
    xy = getVector(other_angle)
    ax = other_position - self_position

    ab_cross_xy = crossProduct(ab, xy)

    turn = sign(ab_cross_xy)
    if turn == CENTRE:
        # no idea
        # return self_position + (ax/2)
        return self_future.name < other_future.name

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

    #print(self_future.name, ab_rel_dist, xy_rel_dist, turn==RIGHT)

    #intersect = self_position + ab * ab_rel_dist
    #return intersect

class CarController(Obstacle):
    def __init__(self, car, road):
        self.car  = car
        self.road = road

        self.route = deque()
        self.next_road = self.road
        car.control(self.route)

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.sim_car = self.car.copy()
        self.future  = deque()

        self.waypoints     = deque()
        self.score         = 0
        self.waypoint_time = self.car.time
        #self.generateWaypoints()

        self.path = deque()
        self.path.append(self.car.position)

        self.messages   = []
        self.car_status = {}

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
        while self.future and self.future[0].time < self.car.time:
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
                    prev_hull = self.future[-1].orig_hull
                else:
                    prev_hull = self.car.hull

                self.future.append(FuturePoint(car, prev_hull))

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

        self.road = self.route[0][0]

        self.simulateFuture()

    def sendMessages(self):
        if self.car.stopped:
            return []

        self.messages.append((SEND_TO_ALL, CURRENT_DETAILS,
                              (self.car.position, self.car.angle)))
        self.messages.append((SEND_TO_ALL, FUTURE_DETAILS, self.future.copy()))
        return self.messages

    def receiveMessages(self, public, private):
        if self.car.stopped:
            return

        self.messages.clear()

        for message in public:
            source, message_type, content = message

            if source == self.name:
                continue

            if message_type == CURRENT_DETAILS:
                position, angle = content
                self.car_status[source] = (position, angle, self.car.time)

            elif message_type == FUTURE_DETAILS:
                num = min(len(self.future), len(content))
                for i in range(num):

                    # get the convex hull of self.future[i] and self.future[i+1]
                    # and the convect hull of content[i] and content[i+1]
                    # and then check if those obstacles collide

                    my_future    = self.future[i]
                    their_future = content[i]

                    dist = (their_future.position - my_future.position).mag()
                    if dist < 10 and my_future.checkCollision(their_future):

                            # remove this bit
                            #if dist < 3:
                            #    print("Dist<3", end=" ")
                            #if my_future.checkCollision(their_future):
                            #    print("collis", end=" ")
                            #print(self.name, source, self.car.time/10)

                            if checkGiveWay(my_future, their_future):
                                print(self.name, "is giving way to", source,
                                      "at time", self.car.time / 1000)

                                road, waypoint, speed, time = self.route[0]

                                self.route.appendleft(
                                    (road, waypoint, 0,
                                     self.car.time + TIME_STEP*20)#10)
                                )

                            self.clearFuture()
                            break

    def drawPath(self):
        if len(self.path) > 1:
            path = [self.world.getDrawable(point) for point in self.path]
            pygame.draw.lines(self.world.screen, GREY, False, path, 1)

    def drawWaypoints(self):
        if self.waypoints:
            self.waypoints[0].draw()

        screen = self.world.screen
        colour = self.colour
        for road, waypoint, speed, time in self.route:
            a = self.world.getDrawable(road.start)
            b = self.world.getDrawable(road.end)
            #w = self.world.getDrawable(waypoint)
            pygame.draw.line(screen, colour, a, b, 1)
            #pygame.draw.circle(screen, DARKER[colour], w, 3, 2)

        for future_point in self.future:
            future_point.draw()

        #for car in self.world.cars:
        #    if car != self.car:
        #        intersect = self.world.getDrawable(checkGiveWay(self.car, car))
        #        pygame.draw.circle(screen, DARKER[colour], intersect, 3, 2)


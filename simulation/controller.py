from util import *

from obstacle import Obstacle
from waypoint import Waypoint, FuturePoint

MAX_WAYPOINTS = 10
MAX_FUTURE    = 10

FUTURE_INTERVAL = TIME_STEP * 6

PATH_MEMORY = 50

class CarController(Obstacle):
    def __init__(self, car):
        self.car = car

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.sim_car       = None
        self.future        = deque()
        self.sim_waypoints = deque()

        self.waypoints     = deque()
        self.score         = 0
        self.waypoint_time = self.car.time
        self.generateWaypoints()

        self.path = deque()
        self.path.append(self.car.position)

        self.messages = []

        self.slow_time = -1
        self.keep_time = -1

    def clearFuture(self):
        self.future.clear()
        self.sim_car = None

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

        if self.sim_car is None:
            self.sim_car       = self.car.copy()
            self.sim_waypoints = self.waypoints.copy()

        if len(self.future) >= MAX_FUTURE or not self.sim_waypoints:
            return

        car      = self.sim_car
        waypoint = self.sim_waypoints[0]
        for i in range(3):
            if car.time % FUTURE_INTERVAL == 0:
                if len(self.future) >= MAX_FUTURE:
                    return
                self.future.append(FuturePoint(car))

            if waypoint.checkInside(car.centre):
                self.sim_waypoints.popleft()
                if self.sim_waypoints:
                    waypoint = self.sim_waypoints[0]
                else:
                    return

            slow = car.time <= self.slow_time
            keep = car.time <= self.keep_time
            car.control(waypoint, slow, keep)
            car.update(car.time + TIME_STEP)

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        while self.waypoints:
            waypoint = self.waypoints[0]

            if waypoint.checkInside(self.car.centre):
                self.waypoints.popleft()
                self.score += 1
                self.waypoint_time = self.car.time
            else:
                break

            self.generateWaypoints()

        self.simulateFuture()

        slow = self.car.time <= self.slow_time
        keep = self.car.time <= self.keep_time
        if self.waypoints:
            self.car.control(self.waypoints[0], slow, keep)
        else:
            self.car.control(None, slow, keep)

    def sendMessages(self):
        if self.car.stopped:
            return []

        self.messages.append((SEND_TO_ALL, CURRENT_DETAILS, self.car.position))
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
                pass

            if message_type == FUTURE_DETAILS:
                num = min(len(self.future), len(content))
                for i in range(num):
                    my_future    = self.future[i]
                    their_future = content[i]

                    dist = (their_future.position - my_future.position).mag()
                    if dist < 5:
                        self.clearFuture()
                        future_time = self.car.time + TIME_STEP * 60

                        my_heading    = getVector(my_future.angle)
                        their_heading = getVector(their_future.angle)

                        #cp = crossProduct(my_heading, their_heading)
                        #if cp > 0:
                        if self.name < source:
                            # give way
                            self.slow_time = future_time
                            self.keep_time = future_time
                            print(self.name, "is giving way to", source)

                        break

    def drawPath(self):
        if len(self.path) > 1:
            path = [self.world.getDrawable(point) for point in self.path]
            pygame.draw.lines(self.world.screen, GREY, False, path, 1)

    def drawWaypoints(self):
        if self.waypoints:
            self.waypoints[0].draw()

        for future_point in self.future:
            future_point.draw()


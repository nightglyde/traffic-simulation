from util import *

from obstacle import Obstacle
from waypoint import Waypoint
from car import Car

WAYPOINT_RADIUS    = ROAD_WIDTH / 2
WAYPOINT_THRESHOLD = 0.5

MAX_WAYPOINTS   = 20
TOTAL_WAYPOINTS = 1000

DESIRED_SPEED = 10

PATH_MEMORY = 100

class CarController(Obstacle):
    def __init__(self, car, index):
        self.car   = car
        self.index = index

        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.waypoints     = deque()
        self.score         = 0
        self.waypoint_time = None
        self.limited_mode  = True#False

        self.path = deque()
        self.path.append(self.car.position)

        self.frame_counter = 0

        self.sim_car       = None
        self.sim_waypoints = deque()
        self.future        = deque()

        self.messages = []

        self.slow_time = -1

    def clearWaypoints(self):
        self.waypoints.clear()
        self.waypoint_time = self.car.time
        self.future.clear()

    def addWaypoint(self, waypoint):
        if self.waypoints:
            car = self.waypoints[-1].car
        else:
            car = self.car

        sim_car    = car.copy()
        start_time = sim_car.time

        path = []
        time = start_time

        destination = waypoint.position

        # simulate car driving to next waypoint
        for i in range(1000):
            if i % 20 == 0:
                path.append(sim_car.front)

            if sim_car.withinRadius(destination, WAYPOINT_THRESHOLD):
                break

            slow = sim_car.time <= self.slow_time
            sim_car.control(waypoint, slow)
            time += TIME_STEP
            sim_car.update(time)

        else:
            self.limited_mode = True
            self.limited_addWaypoint(waypoint)
            return True

        path.append(sim_car.front)
        waypoint.update(time-start_time, path, sim_car)
        self.waypoints.append(waypoint)
        return True

    def limited_addWaypoint(self, waypoint):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self.car

        #angle, distance = getPolar(waypoint.position - prev.position)
        #time = distance / DESIRED_SPEED * 1000
        #path = [prev.position, waypoint.position]

        waypoint.update(prev)
        self.waypoints.append(waypoint)
        #waypoint.limited_update(time, path, angle)

        self.sim_waypoints.append(waypoint)

    def addRandomWaypoint(self):
        while True:
            pos      = self.world.generateRandomPosition()
            waypoint = Waypoint(self, pos, WAYPOINT_RADIUS)

            if self.world.checkObject(waypoint):
                if self.limited_mode:
                    self.limited_addWaypoint(waypoint)
                    return
                else:
                    if self.addWaypoint(waypoint):
                        return

    def alt_addRandomWaypoint(self):
        if self.waypoints:
            waypoints = self.waypoints
        else:
            waypoints = [self.car]

        options = self.world.getWaypointOptions(waypoints)
        if not options:
            options = self.world.waypoint_options

        waypoint = Waypoint(self, random.choice(options),
                                  WAYPOINT_RADIUS)
        if self.limited_mode:
            self.limited_addWaypoint(waypoint)
        else:
            self.addWaypoint(waypoint)

    def generateWaypoints(self):
        while len(self.waypoints) < MAX_WAYPOINTS and \
              len(self.waypoints) + self.score < TOTAL_WAYPOINTS:
            self.addRandomWaypoint()

    def simulateFuture(self):
        if self.sim_car is None:
            self.sim_car       = self.car.copy()
            self.sim_waypoints = self.waypoints.copy()

        while self.future and self.future[0][1] < self.car.time:
            self.future.popleft()

        if len(self.future) >= 10:
            return

        if not self.sim_waypoints:
            return

        for i in range(3):
            if self.sim_car.time % (TIME_STEP * 6) == 0:
                self.future.append((self.sim_car.position, self.sim_car.time))

            if self.sim_car.withinRadius(self.sim_waypoints[0].position,
                                         WAYPOINT_THRESHOLD):
                self.sim_waypoints.popleft()
                if not self.sim_waypoints:
                    return

            slow = self.sim_car.time <= self.slow_time
            self.sim_car.control(self.sim_waypoints[0], slow)
            self.sim_car.update(self.sim_car.time + TIME_STEP)

    def update(self):
        if self.car.stopped:
            return

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        if self.waypoint_time is None:
            self.clearWaypoints()
            self.generateWaypoints()

        while self.waypoints:
            waypoint = self.waypoints[0]

            if self.car.withinRadius(waypoint.position, WAYPOINT_THRESHOLD):
                self.waypoints.popleft()
                self.score += 1
                self.waypoint_time = self.car.time

                if self.score == TOTAL_WAYPOINTS:
                    print(self.name, "finished at time",
                          self.waypoint_time / 1000)
            else:
                break

            self.generateWaypoints()

        self.simulateFuture()

        slow = self.car.time <= self.slow_time
        if self.waypoints:
            self.car.control(self.waypoints[0], slow)
        else:
            self.car.control(None, slow)

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

            if source == self.index:
                continue

            if message_type == CURRENT_DETAILS:
                pass

            if message_type == FUTURE_DETAILS:
                other_future = content

                num = min(len(self.future), len(other_future))
                for i in range(num):
                    self_position,  self_time  = self.future[i]
                    other_position, other_time = other_future[i]

                    if self_time != other_time:
                        print("PROBLEM!", self.name, self_time, other_time)
                        #raise RuntimeError

                    if (other_position - self_position).mag() < 6:
                        print("DANGER!", self.index, source)
                        self.future.clear()
                        self.sim_car = None
                        if source < self.index:
                            self.slow_time = self.car.time + TIME_STEP * 60

    def drawPath(self):
        if len(self.path) > 1:
            path = [self.world.getDrawable(point) for point in self.path]
            pygame.draw.lines(self.world.screen, GREY, False, path, 1)

    def drawWaypoints(self):
        #prev = self.world.getDrawable(self.car.position)
        #for waypoint in self.waypoints:
        #    pos = self.world.getDrawable(waypoint.position)
        #    pygame.draw.line(self.world.screen, self.colour, prev, pos, 1)
        #    prev = pos

        #for waypoint in self.waypoints:
        #    waypoint.drawPath()

        if self.waypoints:
            self.waypoints[0].draw()

        rad = self.world.scaleDistance(1)
        for point, time in self.future:
            point = self.world.getDrawable(point)
            pygame.draw.circle(self.world.screen, self.colour, point, rad, 3)


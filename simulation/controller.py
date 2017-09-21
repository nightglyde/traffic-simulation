from util import *

from obstacle import Obstacle
from waypoint import Waypoint

WAYPOINT_RADIUS    = ROAD_WIDTH / 2
WAYPOINT_THRESHOLD = 0.5

WAYPOINT_INTERVAL = TURN_RADIUS * 3

MAX_WAYPOINTS      = 1000
STARTING_WAYPOINTS = 3

DESIRED_SPEED = 10

class CarController(Obstacle):
    def __init__(self, world, name, colour):
        self.world  = world
        self.name   = name
        self.colour = colour

        self.position = None # pixels
        self.angle    = None # radians
        self.speed    = None # pixels per second

        self.projected_position = None # pixels
        self.projected_angle    = None # radians
        self.projected_speed    = None # pixels per second

        self.dt = 0

        self.time          = 0 # miliseconds
        self.start_time    = 0
        self.waypoint_time = 0
        self.pause_time    = 0

        self.stopped = False

        self.hull = []

        self.waypoints = deque()
        self.score     = 0
        self.duration  = 0.0

    def generateHull(self):
        heading = getVector(self.angle)

        car_front = heading          * CAR_LENGTH / 2
        car_left  = heading.left90() * CAR_WIDTH  / 2

        self.hull = [self.position + car_front + car_left,
                     self.position - car_front + car_left,
                     self.position - car_front - car_left,
                     self.position + car_front - car_left]

    def pause(self, time):
        self.pause_time = time

    def unpause(self, time):
        time_paused = time - self.pause_time

        self.time          += time_paused
        self.waypoint_time += time_paused
        self.start_time    += time_paused

    def getTurningCircle(self, direction, position, angle):
        if direction == LEFT:
            centre_vector = getVector(angle - ANGLE_90) * TURN_RADIUS
        else:
            centre_vector = getVector(angle + ANGLE_90) * TURN_RADIUS
        circle_centre = position + centre_vector
        return circle_centre

    def plotTurn(self, a, b):
        destination = b.position

        left_circle = self.getTurningCircle(LEFT, a.position, a.angle)
        left_angle, left_dist = getPolar(destination - left_circle)
        left_car = a.position - left_circle

        right_circle = self.getTurningCircle(RIGHT, a.position, a.angle)
        right_angle, right_dist = getPolar(destination - right_circle)
        right_car = a.position - right_circle

        turn_distances = []

        # plot left turn
        if left_dist >= TURN_RADIUS:
            tan_dist  = math.sqrt(left_dist**2 - TURN_RADIUS**2)
            tan_angle = left_angle - Angle(math.asin(TURN_RADIUS / left_dist))

            left_tan = getVector(tan_angle+ANGLE_90) * TURN_RADIUS

            arc_dist   = leftTurn(left_car, left_tan) * TURN_RADIUS
            total_dist = tan_dist + arc_dist

            arcs = [(left_circle, getAngle(left_car), getAngle(left_tan))]
            tans = [(left_circle + left_tan, destination)]

            turn_distances.append((total_dist, tan_angle, LEFT, arcs, tans))

        else:
            # right turn then left turn
            ratio = right_dist/(2*TURN_RADIUS) - 3*TURN_RADIUS/(2*right_dist)
            angle = right_angle - Angle(math.acos(ratio)) - ANGLE_90
            extra_circle = self.getTurningCircle(LEFT, destination, angle)

            right_extra = extra_circle - right_circle
            extra_right = right_circle - extra_circle
            extra_dest  = destination  - extra_circle

            arc_a = rightTurn(right_car,  right_extra) * TURN_RADIUS
            arc_b = leftTurn(extra_right, extra_dest)  * TURN_RADIUS
            total_dist = arc_a + arc_b

            arcs = [(right_circle, getAngle(right_extra), getAngle(right_car)),
                    (extra_circle, getAngle(extra_right), getAngle(extra_dest))]
            tans = []

            turn_distances.append((total_dist, angle, RIGHT, arcs, tans))

        # plot right turn
        if right_dist >= TURN_RADIUS:
            tan_dist  = math.sqrt(right_dist**2 - TURN_RADIUS**2)
            tan_angle = right_angle + Angle(math.asin(TURN_RADIUS / right_dist))

            right_tan = getVector(tan_angle-ANGLE_90) * TURN_RADIUS

            arc_dist = rightTurn(right_car, right_tan) * TURN_RADIUS
            total_dist = tan_dist + arc_dist

            arcs = [(right_circle, getAngle(right_tan), getAngle(right_car))]
            tans = [(right_circle + right_tan, destination)]

            turn_distances.append((total_dist, tan_angle, RIGHT, arcs, tans))

        else:
            # left turn then right turn
            ratio = left_dist/(2*TURN_RADIUS) - 3*TURN_RADIUS/(2*left_dist)
            angle = left_angle + Angle(math.acos(ratio)) + ANGLE_90
            extra_circle = self.getTurningCircle(RIGHT, destination, angle)

            left_extra = extra_circle - left_circle
            extra_left = left_circle  - extra_circle
            extra_dest = destination  - extra_circle

            arc_a = leftTurn(left_car,    left_extra) * TURN_RADIUS
            arc_b = rightTurn(extra_left, extra_dest) * TURN_RADIUS
            total_dist = arc_a + arc_b

            arcs = [(left_circle,  getAngle(left_car),   getAngle(left_extra)),
                    (extra_circle, getAngle(extra_dest), getAngle(extra_left))]
            tans = []

            turn_distances.append((total_dist, angle, LEFT, arcs, tans))

        turn_distances.sort()
        return turn_distances[0]

    def addWaypoint(self, waypoint):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        distance, angle, turn, arcs, tans = self.plotTurn(prev, waypoint)
        time = distance / DESIRED_SPEED

        waypoint.update(angle, time, turn, arcs, tans)
        self.waypoints.append(waypoint)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        angle_range = ANGLE_30

        count = 0
        while True:
            angle = prev.angle - angle_range + angle_range * 2 * random.random()
            pos   = prev.position + getVector(angle) * WAYPOINT_INTERVAL

            waypoint = Waypoint(self, pos, WAYPOINT_RADIUS)

            if self.world.checkObject(waypoint):
                self.addWaypoint(waypoint)
                break

            count += 1
            if count % 10 == 0:
                angle_range += ANGLE_5

    def firstUpdate(self, position, angle, time):
        self.position = position
        self.angle    = angle
        self.speed    = 0
        self.time     = time

        self.start_time    = time
        self.waypoint_time = time

        # generate initial waypoints
        for i in range(STARTING_WAYPOINTS):
            self.addRandomWaypoint()

        self.generateHull()

    def update(self, position, angle, time):
        self.dt = (time - self.time) / 1000

        if self.stopped:
            return

        position_change = getMagnitude(position - self.position)
        speed = position_change / self.dt

        speed_change = speed - self.speed
        acceleration = speed_change / self.dt

        angle_change     = angle - self.angle
        angular_velocity = angle_change / self.dt

        self.position = position
        self.angle    = angle
        self.speed    = speed
        self.time     = time

        self.projected_speed = self.speed + acceleration * self.dt
        self.projected_angle = self.angle + angular_velocity * self.dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.position + displacement

        self.generateHull()

    def control(self):
        engine_control   = 0
        steering_control = CENTRE
        braking_control  = None

        if self.stopped:
            return engine_control, steering_control, braking_control

        while self.waypoints:
            waypoint    = self.waypoints[0]
            destination = waypoint.position

            angle, distance = getPolar(destination - self.position)
            if distance <= WAYPOINT_THRESHOLD:

                if self.score + len(self.waypoints) < MAX_WAYPOINTS:
                    self.addRandomWaypoint()

                self.waypoints.popleft()

                self.score += 1
                self.duration = (self.time - self.start_time) / 1000

                if self.score == MAX_WAYPOINTS:
                    print(self.name, "finished at time", self.duration)

                duration = (self.time - self.waypoint_time) / 1000
                print("{} {} time_offset: {:.4}".format(
                      self.name, self.score,
                      duration - waypoint.time))
                self.waypoint_time = self.time

                continue

            # adjust angle
            angle, magnitude = getPolar(destination - self.projected_position)
            angle_difference = angle - self.projected_angle
            if angle_difference < ANGLE_0: # left turn

                # test if point is too close
                circle_centre = self.getTurningCircle(LEFT, self.position, self.angle)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < TURN_RADIUS - WAYPOINT_THRESHOLD:
                    steering_control = RIGHT
                else:
                    steering_control = LEFT

            elif angle_difference > ANGLE_0: # right turn

                # test if point is too close
                circle_centre = self.getTurningCircle(RIGHT, self.position, self.angle)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < TURN_RADIUS - WAYPOINT_THRESHOLD:
                    steering_control = LEFT
                else:
                    steering_control = RIGHT

            # adjust speed
            if self.projected_speed > DESIRED_SPEED:
                engine_control -= 1

            elif self.projected_speed < DESIRED_SPEED:
                engine_control  = 1

            braking_control = False
            break

        else:
            # no more waypoints
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control

    def stop(self, other):
        if not self.stopped:
            self.stopped = True
            self.waypoints.clear()
            self.duration = (self.time - self.start_time) / 1000

            print(self.name, "crashed into", other.name,
                  "at time", self.duration)

    def draw(self):
        for waypoint in self.waypoints:
            waypoint.drawPath()

        for waypoint in self.waypoints:
            waypoint.draw()


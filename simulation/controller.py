import math
import random

from collections import deque

from util import *

ESTIMATED_LOWER_LIMIT = -ANGLE_45
ESTIMATED_UPPER_LIMIT = ANGLE_45

SLOW_SPEED = 10 * PIXELS_PER_METRE

WAYPOINT_BIG_GAP   = SCREEN_UNIT * 25 # 250
WAYPOINT_INTERVAL  = SCREEN_UNIT * 17 # 170
WAYPOINT_THRESHOLD = SCREEN_UNIT * 1  # 10

SCREEN_MARGIN = SCREEN_UNIT * 5 # 50

W_MIN_X = SCREEN_MARGIN
W_MIN_Y = SCREEN_MARGIN
W_MAX_X = SCREEN_WIDTH  - SCREEN_MARGIN
W_MAX_Y = SCREEN_HEIGHT - SCREEN_MARGIN

MAX_WAYPOINTS      = 100
STARTING_WAYPOINTS = 3

class CarController:
    def __init__(self, name, colour):
        self.name   = name
        self.colour = colour

        self.position  = None # pixels
        self.car_angle = None # radians
        self.speed     = None # pixels per second

        self.projected_position = None # pixels
        self.projected_angle    = None # radians
        self.projected_speed    = None # pixels per second

        self.time = None # miliseconds

        self.waypoints = deque()
        self.points    = 0

        self.start_time = 0
        self.duration   = 0.0

    def addWaypoint(self, pos, angle):
        self.waypoints.append((pos, angle))

    def addVeryRandomWaypoint(self):
        if self.waypoints:
            prev_pos, prev_angle = self.waypoints[-1]
        else:
            prev_pos   = self.position
            prev_angle = self.car_angle

        x = random.randint(W_MIN_X, W_MAX_X)
        y = random.randint(W_MIN_Y, W_MAX_Y)

        pos   = Vector(x, y)
        angle, magnitude = getPolar(pos - prev_pos)

        self.addWaypoint(pos, angle)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev_pos, prev_angle = self.waypoints[-1]
        else:
            prev_pos   = self.position
            prev_angle = self.car_angle

        angle = prev_angle - ANGLE_30 + ANGLE_60 * random.random()
        displacement = getVector(angle) * WAYPOINT_INTERVAL
        pos = prev_pos + displacement

        count = 0

        while not ((W_MIN_X <= pos.x <= W_MAX_X) and (W_MIN_Y <= pos.y <= W_MAX_Y)):
            if count < 5:
                angle = prev_angle - ANGLE_30 + ANGLE_60 * random.random()
                displacement = getVector(angle) * WAYPOINT_INTERVAL
                pos = prev_pos + displacement
            elif count < 100:
                angle = Angle(random.random()*2*math.pi)
                displacement = getVector(angle) * WAYPOINT_BIG_GAP
                pos = prev_pos + displacement
            else:
                pos = CENTRE_POSITION
                angle, magnitude = getPolar(pos - prev_pos)

            count += 1

        self.addWaypoint(pos, angle)

    def firstUpdate(self, position, car_angle, time):
        self.position     = position
        self.car_angle    = car_angle
        self.speed        = 0
        self.time         = time

        self.start_time = time

        # generate initial waypoints
        for i in range(STARTING_WAYPOINTS):
            self.addRandomWaypoint()

    def update(self, position, car_angle, time):
        dt   = (time - self.time) / 1000

        angle, position_change = getPolar(position - self.position)
        speed = position_change / dt

        speed_change = speed - self.speed
        acceleration = speed_change / dt

        angle_change     = car_angle - self.car_angle
        angular_velocity = angle_change / dt

        self.position  = position
        self.car_angle = car_angle
        self.speed     = speed
        self.time      = time

        self.projected_speed = self.speed     + acceleration * dt
        self.projected_angle = self.car_angle + angular_velocity * dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.position + displacement

    def plotAngle(self, angle):
        radius = SCREEN_AXLE_LENGTH / math.sin(angle.value)

        centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        circle_centre = self.position + centre_vector

        return circle_centre, radius

    def control(self):
        engine_control   = 0
        steering_control = 0
        braking_control  = None

        while self.waypoints:
            destination, w_angle = self.waypoints[0]

            angle, magnitude = getPolar(destination - self.position)
            if magnitude < WAYPOINT_THRESHOLD:

                if self.points + len(self.waypoints) < MAX_WAYPOINTS:
                    self.addRandomWaypoint()

                self.waypoints.popleft()
                self.points += 1
                self.duration = (self.time - self.start_time) / 1000

                if self.points == MAX_WAYPOINTS:
                    print(self.name, self.duration)

                continue

            if self.projected_speed > SLOW_SPEED:
                engine_control -= 1

            elif self.projected_speed < SLOW_SPEED:
                engine_control  = 1

            angle, magnitude = getPolar(destination - self.projected_position)
            angle_difference = self.projected_angle - angle

            if angle_difference > ANGLE_0: # left turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(ESTIMATED_LOWER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = 1

                else:
                    steering_control = -1

            elif angle_difference < ANGLE_0: # right turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(ESTIMATED_UPPER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = -1

                else:
                    steering_control = 1

            braking_control = False
            break

        else:
            # no more waypoints
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control


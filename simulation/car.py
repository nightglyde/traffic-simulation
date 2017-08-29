import math

from util import *

# physics constants
DRAG_CONSTANT    = 0.5
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CAR_LENGTH  = WORLD_UNIT * 10 # 4.5
CAR_WIDTH   = WORLD_UNIT * 4  # 1.8
AXLE_LENGTH = WORLD_UNIT * 6  # 2.7

CENTRE_TO_FRONT  = WORLD_UNIT * 4   # 1.8
CENTRE_TO_REAR   = WORLD_UNIT * 2   # 0.9
CENTRE_TO_GROUND = WORLD_UNIT * 1.5 # 0.675

CAR_MASS   = 1250
CAR_WEIGHT = CAR_MASS * GRAVITY_CONSTANT

STATIC_FRONT_WEIGHT = (CENTRE_TO_FRONT  / AXLE_LENGTH) * CAR_WEIGHT
STATIC_REAR_WEIGHT  = (CENTRE_TO_REAR   / AXLE_LENGTH) * CAR_WEIGHT
HLM                 = (CENTRE_TO_GROUND / AXLE_LENGTH) * CAR_MASS

MAX_ANGLE   = ANGLE_45
LOWER_LIMIT = -MAX_ANGLE
UPPER_LIMIT = MAX_ANGLE

STEERING_RATE_2 = 4
STEERING_RATE_1 = 1

class Car:
    def __init__(self, name, position, car_angle, time):
        self.name = name

        self.position     = position                  # metres
        self.car_angle    = car_angle                 # radians
        self.heading      = getVector(self.car_angle) # unit vector
        self.velocity     = VECTOR_0                  # metres per second
        self.wheel_angle  = ANGLE_0                   # radians
        self.engine_force = MIN_ENGINE_FORCE          # newtons
        self.braking      = False

        self.control_time = time
        self.update_time  = time

    def update(self, time):
        dt               = (time - self.update_time) / 1000
        self.update_time = time

        angle, speed = getPolar(self.velocity)

        # turning corners
        if self.wheel_angle.value != ANGLE_0.value:
            radius    = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            angular_v = speed / radius

            self.car_angle += Angle(angular_v * dt)
            self.heading    = getVector(self.car_angle)

        # driving forwards
        if not self.braking:
            self.velocity = self.heading * speed

            traction           = self.heading  * min(self.engine_force, CAR_WEIGHT)
            drag               = self.velocity * speed * (-DRAG_CONSTANT)
            rolling_resistance = self.velocity         * (-RR_CONSTANT)

            acceleration = (traction + drag + rolling_resistance) / CAR_MASS

        # braking
        elif speed > 0.05:
            self.velocity = self.heading * speed

            brakes             = self.heading  * (-min(BRAKING_CONSTANT, CAR_WEIGHT))
            drag               = self.velocity * speed * (-DRAG_CONSTANT)
            rolling_resistance = self.velocity         * (-RR_CONSTANT)

            acceleration = (brakes + drag + rolling_resistance) / CAR_MASS

        else:
            acceleration  = VECTOR_0
            self.velocity = VECTOR_0

        self.velocity += acceleration  * dt
        self.position += self.velocity * dt

        return self.position, self.car_angle

    def control(self, engine_control, steering_control, braking_control, time):
        dt                = (time - self.control_time) / 1000
        self.control_time = time

        # adjust engine force
        engine_change  = 10000 * dt

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)

        # adjust wheel angle
        large_angle_change = Angle(2*math.pi * dt * STEERING_RATE_2)
        small_angle_change = Angle(2*math.pi * dt * STEERING_RATE_1)

        if steering_control > 0:
            if self.wheel_angle > ANGLE_0:
                self.wheel_angle = min(self.wheel_angle+small_angle_change, UPPER_LIMIT)
            else:
                self.wheel_angle = min(self.wheel_angle+large_angle_change, UPPER_LIMIT)

        elif steering_control < 0:
            if self.wheel_angle < ANGLE_0:
                self.wheel_angle = max(self.wheel_angle-small_angle_change, LOWER_LIMIT)
            else:
                self.wheel_angle = max(self.wheel_angle-large_angle_change, LOWER_LIMIT)

        # toggle brakes
        if braking_control:
            self.braking = True
        else:
            self.braking = False


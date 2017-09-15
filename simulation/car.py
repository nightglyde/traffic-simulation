from util import *

# physics constants
DRAG_CONSTANT    = 0.76090075
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.807

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CENTRE_TO_FRONT  = AXLE_LENGTH / 2
CENTRE_TO_REAR   = AXLE_LENGTH / 2
CENTRE_TO_GROUND = 0.675

CAR_MASS    = 1250
CAR_WEIGHT  = CAR_MASS * GRAVITY_CONSTANT
CAR_INERTIA = (CAR_MASS / 12) * (CAR_LENGTH**2 + CAR_WIDTH**2)

STATIC_FRONT_WEIGHT = (CENTRE_TO_REAR   / AXLE_LENGTH) * CAR_WEIGHT
STATIC_REAR_WEIGHT  = (CENTRE_TO_FRONT  / AXLE_LENGTH) * CAR_WEIGHT
HLM                 = (CENTRE_TO_GROUND / AXLE_LENGTH) * CAR_MASS

MIN_LAT_FORCE = -10000
MAX_LAT_FORCE =  10000

MAX_ANGLE = ANGLE_45

STEERING_RATE = 1

SHOW_WHEELS = True

class Car:
    def __init__(self, name, colour, screen, zoom, position, angle, time):
        self.name   = name
        self.colour = colour
        self.screen = screen
        self.zoom   = zoom

        self.position     = position         # metres
        self.velocity     = VECTOR_0         # metres per second
        self.acceleration = VECTOR_0         # metres per second^2
        self.engine_force = MIN_ENGINE_FORCE # newtons

        self.angle            = angle   # radians
        self.angular_velocity = 0.0     # radians per second
        self.wheel_angle      = ANGLE_0 # radians

        self.braking = False

        self.stopped = False

        self.control_time = time
        self.update_time  = time
        self.pause_time   = 0

    def pause(self, time):
        self.pause_time = time

    def unpause(self, time):
        time_paused = time - self.pause_time

        self.control_time += time_paused
        self.update_time  += time_paused

    def update(self, time):
        if self.stopped:
            return self.position, self.angle

        dt               = (time - self.update_time) / 1000
        self.update_time = time

        v_angle, speed = getPolar(self.velocity)

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            angle, speed = getPolar(self.velocity)

            radius                = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            self.angular_velocity = speed / radius

            self.angle += Angle(self.angular_velocity * dt)

        heading       = getVector(self.angle)
        self.velocity = heading * speed

        force = VECTOR_0

        angle, magnitude = getPolar(self.acceleration)
        a_car = magnitude * math.cos(abs((angle - self.angle).value))

        front_weight = STATIC_FRONT_WEIGHT - HLM * a_car
        rear_weight  = STATIC_REAR_WEIGHT  + HLM * a_car

        if not self.braking:
            # traction force
            force += heading * min(self.engine_force, front_weight)

        elif speed > 0.01:
            # braking force
            force += heading * (-min(BRAKING_CONSTANT, CAR_WEIGHT))

        else:
            self.velocity = VECTOR_0

        # drag / air resistance
        force += self.velocity * speed * (-DRAG_CONSTANT)

        # rolling resistance
        force += self.velocity * (-RR_CONSTANT)

        # convert force to acceleration
        self.acceleration  = force / CAR_MASS
        self.velocity     += self.acceleration  * dt
        self.position     += self.velocity * dt

        return self.position, self.angle

    def control(self, engine_control, steering_control, braking_control, time):
        if self.stopped:
            return

        dt                = (time - self.control_time) / 1000
        self.control_time = time

        # adjust engine force
        engine_change  = 10000 * dt

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change,
                                    MAX_ENGINE_FORCE)
        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change,
                                    MIN_ENGINE_FORCE)

        # adjust wheel angle
        angle_change = Angle(2*math.pi * dt * STEERING_RATE)

        angliness = (self.wheel_angle.value / MAX_ANGLE.value)**2
        if self.wheel_angle < ANGLE_0:
            self.wheel_angle += angle_change * angliness
        else:
            self.wheel_angle -= angle_change * angliness

        if steering_control == RIGHT:
            self.wheel_angle += angle_change
        elif steering_control == LEFT:
            self.wheel_angle -= angle_change

        # toggle brakes
        if braking_control:
            self.braking = True
        else:
            self.braking = False

    def stop(self):
        self.stopped = True

    def draw(self):
        pos = self.position

        forward = getVector(self.angle)
        left    = forward.left90()

        # draw car
        car_front = forward * CAR_LENGTH / 2
        car_left  = left    * CAR_WIDTH  / 2

        chassis = [
            self.zoom.getDrawable(pos + car_front + car_left),
            self.zoom.getDrawable(pos + car_front - car_left),
            self.zoom.getDrawable(pos - car_front - car_left),
            self.zoom.getDrawable(pos - car_front + car_left)
        ]
        if self.stopped:
            pygame.draw.polygon(self.screen, DARKER[self.colour], chassis)
        else:
            pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen, BLACK, chassis, 1)

        # draw arrow
        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [
            self.zoom.getDrawable(pos              + stem_left),
            self.zoom.getDrawable(pos + stem_front + stem_left),
            self.zoom.getDrawable(pos + stem_front + head_left),
            self.zoom.getDrawable(pos + head_front            ),
            self.zoom.getDrawable(pos + stem_front - head_left),
            self.zoom.getDrawable(pos + stem_front - stem_left),
            self.zoom.getDrawable(pos              - stem_left)
        ]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

        if SHOW_WHEELS:
            # draw wheels
            wheel_forward = getVector(self.angle + self.wheel_angle)

            f_wheel_front = wheel_forward          * WHEEL_LENGTH / 2
            f_wheel_left  = wheel_forward.left90() * WHEEL_WIDTH  / 2

            r_wheel_front = forward * WHEEL_LENGTH / 2
            r_wheel_left  = left    * WHEEL_WIDTH  / 2

            axle_front = forward * AXLE_LENGTH / 2
            axle_left  = left    * AXLE_WIDTH  / 2

            # front left wheel
            f_l = pos + axle_front + axle_left
            front_left_wheel = [
                self.zoom.getDrawable(f_l - f_wheel_left + f_wheel_front),
                self.zoom.getDrawable(f_l + f_wheel_left + f_wheel_front),
                self.zoom.getDrawable(f_l + f_wheel_left - f_wheel_front),
                self.zoom.getDrawable(f_l - f_wheel_left - f_wheel_front)
            ]
            pygame.draw.polygon(self.screen, DARK_GREY, front_left_wheel)
            pygame.draw.polygon(self.screen, BLACK,     front_left_wheel, 1)

            # front right wheel
            f_r = pos + axle_front - axle_left
            front_right_wheel = [
                self.zoom.getDrawable(f_r + f_wheel_left + f_wheel_front),
                self.zoom.getDrawable(f_r - f_wheel_left + f_wheel_front),
                self.zoom.getDrawable(f_r - f_wheel_left - f_wheel_front),
                self.zoom.getDrawable(f_r + f_wheel_left - f_wheel_front)
            ]
            pygame.draw.polygon(self.screen, DARK_GREY, front_right_wheel)
            pygame.draw.polygon(self.screen, BLACK,     front_right_wheel, 1)

            # rear left wheel
            r_l = pos - axle_front + axle_left
            rear_left_wheel = [
                self.zoom.getDrawable(r_l - r_wheel_left + r_wheel_front),
                self.zoom.getDrawable(r_l + r_wheel_left + r_wheel_front),
                self.zoom.getDrawable(r_l + r_wheel_left - r_wheel_front),
                self.zoom.getDrawable(r_l - r_wheel_left - r_wheel_front)
            ]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(self.screen, BLACK,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos - axle_front - axle_left
            rear_right_wheel = [
                self.zoom.getDrawable(r_r + r_wheel_left + r_wheel_front),
                self.zoom.getDrawable(r_r - r_wheel_left + r_wheel_front),
                self.zoom.getDrawable(r_r - r_wheel_left - r_wheel_front),
                self.zoom.getDrawable(r_r + r_wheel_left - r_wheel_front)
            ]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(self.screen, BLACK,     rear_right_wheel, 1)


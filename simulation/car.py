from util import *

# physics constants
FRAMES_PER_SECOND = 60
DRAG_CONSTANT    = 0.76090075#01
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.807

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CAR_LENGTH  = WORLD_UNIT * 10 # 4.5
CAR_WIDTH   = WORLD_UNIT * 4  # 1.8
AXLE_LENGTH = WORLD_UNIT * 6  # 2.7

CENTRE_TO_FRONT  = WORLD_UNIT * 3 #4 # 1.8
CENTRE_TO_REAR   = WORLD_UNIT * 3 #2 # 0.9
CENTRE_TO_GROUND = WORLD_UNIT * 1.5 # 0.675

CAR_MASS    = 1250
CAR_WEIGHT  = CAR_MASS * GRAVITY_CONSTANT
CAR_INERTIA = (CAR_MASS / 12) * (CAR_LENGTH**2 + CAR_WIDTH**2)

STATIC_FRONT_WEIGHT = (CENTRE_TO_REAR   / AXLE_LENGTH) * CAR_WEIGHT
STATIC_REAR_WEIGHT  = (CENTRE_TO_FRONT  / AXLE_LENGTH) * CAR_WEIGHT
HLM                 = (CENTRE_TO_GROUND / AXLE_LENGTH) * CAR_MASS

MIN_LAT_FORCE = -10000
MAX_LAT_FORCE =  10000

MAX_ANGLE   = ANGLE_45
LOWER_LIMIT = -MAX_ANGLE
UPPER_LIMIT = MAX_ANGLE

STEERING_RATE = 1

SHOW_WHEELS = True

class Car:
    def __init__(self, name, screen, colour, position, car_angle, time):
        self.name   = name
        self.screen = screen
        self.colour = colour

        self.position     = position         # metres
        self.velocity     = VECTOR_0         # metres per second
        self.acceleration = VECTOR_0         # metres per second^2
        self.engine_force = MIN_ENGINE_FORCE # newtons

        self.car_angle        = car_angle # radians
        self.angular_velocity = 0.0       # radians per second
        self.wheel_angle      = ANGLE_0   # radians

        self.braking = False

        self.control_time = time
        self.update_time  = time

    def update(self, time):
        dt               = (time - self.update_time) / 1000
        self.update_time = time

        v_angle, speed = getPolar(self.velocity)

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            angle, speed = getPolar(self.velocity)

            radius                = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            self.angular_velocity = speed / radius

            self.car_angle += Angle(self.angular_velocity * dt)

        heading        = getVector(self.car_angle)
        self.velocity  = heading * speed

        force = VECTOR_0

        angle, magnitude = getPolar(self.acceleration)
        a_car = magnitude * math.cos(abs((angle - self.car_angle).value))

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

        print(self.engine_force, speed)

        return self.position, self.car_angle

    def control(self, engine_control, steering_control, braking_control, time):
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

    def draw(self):
        pos = self.position * PIXELS_PER_METRE

        forward = getVector(self.car_angle)
        left    = forward.left90()

        # draw car
        car_front = forward * SCREEN_CAR_LENGTH / 2
        car_left  = left    * SCREEN_CAR_WIDTH / 2

        chassis = [(pos + car_front + car_left).coords(),
                   (pos + car_front - car_left).coords(),
                   (pos - car_front - car_left).coords(),
                   (pos - car_front + car_left).coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen, BLACK,       chassis, 1)

        # draw arrow
        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [(pos              + stem_left).coords(),
                 (pos + stem_front + stem_left).coords(),
                 (pos + stem_front + head_left).coords(),
                 (pos + head_front             ).coords(),
                 (pos + stem_front - head_left).coords(),
                 (pos + stem_front - stem_left).coords(),
                 (pos              - stem_left).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

        if SHOW_WHEELS:
            # draw wheels
            wheel_forward = getVector(self.car_angle + self.wheel_angle)

            f_wheel_front = wheel_forward          * SCREEN_WHEEL_LENGTH / 2
            f_wheel_left  = wheel_forward.left90() * SCREEN_WHEEL_WIDTH  / 2

            r_wheel_front = forward * SCREEN_WHEEL_LENGTH / 2
            r_wheel_left  = left    * SCREEN_WHEEL_WIDTH / 2

            axle_front = forward * SCREEN_AXLE_LENGTH / 2
            axle_left  = left    * SCREEN_AXLE_WIDTH / 2

            # front left wheel
            f_l = pos + axle_front + axle_left
            front_left_wheel = [(f_l - f_wheel_left + f_wheel_front).coords(),
                                (f_l + f_wheel_left + f_wheel_front).coords(),
                                (f_l + f_wheel_left - f_wheel_front).coords(),
                                (f_l - f_wheel_left - f_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, front_left_wheel)
            pygame.draw.polygon(self.screen, BLACK,     front_left_wheel, 1)

            # front right wheel
            f_r = pos + axle_front - axle_left
            front_right_wheel = [(f_r + f_wheel_left + f_wheel_front).coords(),
                                 (f_r - f_wheel_left + f_wheel_front).coords(),
                                 (f_r - f_wheel_left - f_wheel_front).coords(),
                                 (f_r + f_wheel_left - f_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, front_right_wheel)
            pygame.draw.polygon(self.screen, BLACK,     front_right_wheel, 1)

            # rear left wheel
            r_l = pos - axle_front + axle_left
            rear_left_wheel = [(r_l - r_wheel_left + r_wheel_front).coords(),
                               (r_l + r_wheel_left + r_wheel_front).coords(),
                               (r_l + r_wheel_left - r_wheel_front).coords(),
                               (r_l - r_wheel_left - r_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(self.screen, BLACK,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos - axle_front - axle_left
            rear_right_wheel = [(r_r + r_wheel_left + r_wheel_front).coords(),
                                (r_r - r_wheel_left + r_wheel_front).coords(),
                                (r_r - r_wheel_left - r_wheel_front).coords(),
                                (r_r + r_wheel_left - r_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(self.screen, BLACK,     rear_right_wheel, 1)

        #if self.wheel_angle.value != 0.0:
        #    radius = AXLE_LENGTH / math.sin(self.wheel_angle.value) * PIXELS_PER_METRE

        #    centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        #    circle_centre = (pos + centre_vector).coords()
        #    radius = abs(round(radius))

        #    if radius < 200:
        #        pygame.draw.circle(self.screen, BLACK, circle_centre, radius, 1)


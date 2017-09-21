from util import *

from obstacle import Obstacle

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
PATH_HISTORY  = 100

SHOW_WHEELS = True

class Car(Obstacle):
    def __init__(self, world, name, colour, position, angle, time):
        self.world  = world
        self.name   = name
        self.colour = colour

        self.position     = position         # metres
        self.velocity     = VECTOR_0         # metres per second
        self.acceleration = VECTOR_0         # metres per second^2
        self.engine_force = MIN_ENGINE_FORCE # newtons

        self.angle       = angle   # radians
        self.wheel_angle = ANGLE_0 # radians

        self.dt = 0 # seconds

        self.time       = time # miliseconds
        self.pause_time = 0

        self.braking = False
        self.stopped = False

        self.generateHull()

        # wheel paths
        self.wheel_paths = [deque() for i in range(4)]

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
        time_paused  = time - self.pause_time
        self.time   += time_paused

    def stop(self):
        self.stopped = True

    def updateWheelPaths(self):
        heading = getVector(self.angle)
        axle_forward = heading          * AXLE_LENGTH / 2
        axle_left    = heading.left90() * AXLE_WIDTH  / 2

        self.wheel_paths[0].append(self.position + axle_forward + axle_left)
        self.wheel_paths[1].append(self.position + axle_forward - axle_left)
        self.wheel_paths[2].append(self.position - axle_forward - axle_left)
        self.wheel_paths[3].append(self.position - axle_forward + axle_left)

        if len(self.wheel_paths[0]) > PATH_HISTORY:
            for path in self.wheel_paths:
                path.popleft()

    def update(self, time):
        self.dt   = (time - self.time) / 1000
        self.time = time

        if self.stopped:
            return self.position, self.angle

        v_angle, speed = getPolar(self.velocity)

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            angle, speed = getPolar(self.velocity)

            radius           = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            angular_velocity = speed / radius

            self.angle += Angle(angular_velocity * self.dt)

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
        self.velocity     += self.acceleration * self.dt
        self.position     += self.velocity     * self.dt

        self.generateHull()
        self.updateWheelPaths()
        return self.position, self.angle

    def control(self, engine_control, steering_control, braking_control):
        if self.stopped:
            return

        # adjust engine force
        engine_change  = 10000 * self.dt

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change,
                                    MAX_ENGINE_FORCE)
        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change,
                                    MIN_ENGINE_FORCE)

        # adjust wheel angle
        angle_change = Angle(2*math.pi * self.dt * STEERING_RATE)

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

    def drawWheelPaths(self):
        for path in self.wheel_paths:
            path = [self.world.getDrawable(point) for point in path]
            width = self.world.scaleDistance(WHEEL_WIDTH)
            pygame.draw.lines(self.world.screen, GREY, False, path, width)

    def draw(self, selected=False):
        if self.stopped:
            colour = DARKER[self.colour]
        else:
            colour = self.colour

        screen = self.world.screen
        pos    = self.position

        forward = getVector(self.angle)
        left    = forward.left90()

        # draw car
        car_front = forward * CAR_LENGTH / 2
        car_left  = left    * CAR_WIDTH  / 2

        chassis = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(screen, colour, chassis)
        pygame.draw.polygon(screen, BLACK,  chassis, 2)

        # draw arrow
        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH / 2
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [
            self.world.getDrawable(pos - head_front + stem_left),
            self.world.getDrawable(pos + stem_front + stem_left),
            self.world.getDrawable(pos + stem_front + head_left),
            self.world.getDrawable(pos + head_front            ),
            self.world.getDrawable(pos + stem_front - head_left),
            self.world.getDrawable(pos + stem_front - stem_left),
            self.world.getDrawable(pos - head_front - stem_left)]

        if selected:
            pygame.draw.polygon(screen, LIGHTER[colour], arrow)
        pygame.draw.polygon(screen, BLACK, arrow, 1)

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
                self.world.getDrawable(f_l - f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_l + f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_l + f_wheel_left - f_wheel_front),
                self.world.getDrawable(f_l - f_wheel_left - f_wheel_front)
            ]
            pygame.draw.polygon(screen, DARK_GREY, front_left_wheel)
            pygame.draw.polygon(screen, BLACK,     front_left_wheel, 1)

            # front right wheel
            f_r = pos + axle_front - axle_left
            front_right_wheel = [
                self.world.getDrawable(f_r + f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_r - f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_r - f_wheel_left - f_wheel_front),
                self.world.getDrawable(f_r + f_wheel_left - f_wheel_front)
            ]
            pygame.draw.polygon(screen, DARK_GREY, front_right_wheel)
            pygame.draw.polygon(screen, BLACK,     front_right_wheel, 1)

            # rear left wheel
            r_l = pos - axle_front + axle_left
            rear_left_wheel = [
                self.world.getDrawable(r_l - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_l - r_wheel_left - r_wheel_front)
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos - axle_front - axle_left
            rear_right_wheel = [
                self.world.getDrawable(r_r + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r - r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_r + r_wheel_left - r_wheel_front)
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_right_wheel, 1)


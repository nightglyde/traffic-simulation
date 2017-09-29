from util import *

from obstacle import Obstacle

# physics constants
DRAG_CONSTANT    = 0.761
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.807

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CAR_MASS   = 1250
CAR_WEIGHT = CAR_MASS * GRAVITY_CONSTANT

SHOW_WHEELS  = True

class Car(Obstacle):
    def __init__(self, world, name, colour, position, angle, time):
        self.world  = world
        self.name   = name
        self.colour = colour

        self.position = position # metres
        self.angle    = angle    # radians
        self.time     = time     # miliseconds

        self.engine_force = MIN_ENGINE_FORCE # newtons
        self.wheel_angle  = ANGLE_0          # radians
        self.velocity     = VECTOR_0         # metres per second
        self.speed        = 0.0              # metres per second

        self.braking = False
        self.reverse = False
        self.stopped = False

        self.generateHull()

        self.speed_time = time
        self.angle_time = time

    def copy(self):
        car = Car(self.world, self.name, self.colour,
                  self.position, self.angle, self.time)

        car.engine_force = self.engine_force
        car.wheel_angle  = self.wheel_angle
        car.velocity     = self.velocity
        car.speed        = self.speed

        car.braking = self.braking
        car.reverse = self.reverse
        car.stopped = self.stopped

        car.speed_time = self.speed_time
        car.angle_time = self.angle_time

        car.generateHull()

        return car

    def generateHull(self):
        heading = getVector(self.angle)

        self.front = self.position + heading * PIVOT_TO_FRONT
        self.rear  = self.position - heading * PIVOT_TO_REAR

        left = heading.left90() * CAR_WIDTH / 2

        self.hull = [self.front - left, self.front + left,
                     self.rear  + left, self.rear  - left]

        self.centre = (self.front + self.rear) / 2

    def stop(self, other):
        if not self.stopped:
            self.stopped = True
            print(self.name, "crashed into", other.name,
                  "at time", self.time / 1000)

    def update(self, time):
        if self.stopped:
            return

        if time <= self.time:
            print("BAD UPDATE")
            return

        dt = (time - self.time) / 1000
        self.time = time

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            radius           = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            angular_velocity = self.speed / radius

            angle_change = Angle(angular_velocity * dt / 2)
            if self.reverse:
                angle_change = -angle_change
            self.angle += angle_change

        heading = getVector(self.angle)
        if self.reverse:
            heading = -heading
        self.velocity = heading * self.speed

        force = VECTOR_0
        if not self.braking:
            # traction force
            force += heading * min(self.engine_force, CAR_WEIGHT)

        elif self.speed > 0.01:
            # braking force
            force += heading * (-min(BRAKING_CONSTANT, CAR_WEIGHT))

        else:
            self.velocity = VECTOR_0
            self.speed    = 0.0

        # drag / air resistance
        force += self.velocity * self.speed * (-DRAG_CONSTANT)

        # rolling resistance
        force += self.velocity * (-RR_CONSTANT)

        # convert force to acceleration
        acceleration   = force / CAR_MASS
        self.velocity += acceleration  * dt
        self.position += self.velocity * dt

        self.speed = getMagnitude(self.velocity)

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            radius           = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            angular_velocity = self.speed / radius

            angle_change = Angle(angular_velocity * dt / 2)
            if self.reverse:
                angle_change = -angle_change
            self.angle += angle_change

        heading = getVector(self.angle)
        if self.reverse:
            heading = -heading
        self.velocity = heading * self.speed

        self.generateHull()

    def controlSpeed(self, new_speed, reverse):
        if self.time <= self.speed_time:
            print("BAD SPEED CONTROL")
            return

        dt = (self.time - self.speed_time) / 1000
        self.speed_time = self.time

        # calculate desired engine force
        speed = getMagnitude(self.velocity)
        acceleration = (new_speed - speed) / dt
        force  = CAR_MASS * acceleration
        force -= speed**2 * (-DRAG_CONSTANT)
        force -= speed    * (-RR_CONSTANT)

        # adjust engine force
        engine_change = 10000 * dt
        if force < self.engine_force:
            self.engine_force = max(self.engine_force-engine_change,
                                    force, MIN_ENGINE_FORCE)
            if force < 0:
                self.braking = True
            else:
                self.braking = False

        elif force > self.engine_force:
            self.engine_force = min(self.engine_force+engine_change,
                                    force, MAX_ENGINE_FORCE)
            self.braking = False

    def controlAngle(self, angle_difference):#new_angle):
        if self.time <= self.angle_time:
            print("BAD ANGLE CONTROL")
            return

        dt = (self.time - self.angle_time) / 1000
        self.angle_time = self.time

        angular_velocity = angle_difference.value / dt
        if angular_velocity == 0.0 or self.speed == 0.0:
            new_wheel_angle = ANGLE_0
        else:
            radius = self.speed / angular_velocity
            ratio  = min(max(-1, PIVOT_TO_AXLE / radius), 1)
            new_wheel_angle = Angle(math.asin(ratio))

        angle_change = Angle(2*math.pi * dt * 0.5)
        if new_wheel_angle < self.wheel_angle:
            self.wheel_angle = max(self.wheel_angle-angle_change,
                                   new_wheel_angle, -MAX_WHEEL_ANGLE)

        elif new_wheel_angle > self.wheel_angle:
            self.wheel_angle = min(self.wheel_angle+angle_change,
                                   new_wheel_angle, MAX_WHEEL_ANGLE)

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
        chassis = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(screen, colour, chassis)
        pygame.draw.polygon(screen, BLACK,  chassis, 2)

        # draw arrow
        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [
            self.world.getDrawable(pos              + stem_left),
            self.world.getDrawable(pos + stem_front + stem_left),
            self.world.getDrawable(pos + stem_front + head_left),
            self.world.getDrawable(pos + head_front            ),
            self.world.getDrawable(pos + stem_front - head_left),
            self.world.getDrawable(pos + stem_front - stem_left),
            self.world.getDrawable(pos              - stem_left)]

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

            axle_front = forward * PIVOT_TO_AXLE
            axle_rear  = forward * (PIVOT_TO_AXLE - AXLE_LENGTH)
            axle_left  = left    * AXLE_WIDTH / 2

            # front left wheel
            f_l = pos + axle_front + axle_left
            front_left_wheel = [
                self.world.getDrawable(f_l - f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_l + f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_l + f_wheel_left - f_wheel_front),
                self.world.getDrawable(f_l - f_wheel_left - f_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, front_left_wheel)
            pygame.draw.polygon(screen, BLACK,     front_left_wheel, 1)

            # front right wheel
            f_r = pos + axle_front - axle_left
            front_right_wheel = [
                self.world.getDrawable(f_r - f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_r + f_wheel_left + f_wheel_front),
                self.world.getDrawable(f_r + f_wheel_left - f_wheel_front),
                self.world.getDrawable(f_r - f_wheel_left - f_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, front_right_wheel)
            pygame.draw.polygon(screen, BLACK,     front_right_wheel, 1)

            # rear left wheel
            r_l = pos + axle_rear + axle_left
            rear_left_wheel = [
                self.world.getDrawable(r_l - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_l - r_wheel_left - r_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos + axle_rear - axle_left
            rear_right_wheel = [
                self.world.getDrawable(r_r - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r + r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_r - r_wheel_left - r_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_right_wheel, 1)

        if abs(self.wheel_angle.value) > ANGLE_1.value / 4:
            radius       = PIVOT_TO_AXLE / abs(math.sin(self.wheel_angle.value))
            radius_inner = radius - CAR_WIDTH/2

            if self.wheel_angle.value < 0:
                circle_centre = getTurningCircle(LEFT, self, radius)
                radius_outer  = getMagnitude(self.hull[1] - circle_centre)

            elif radius > 0:
                circle_centre = getTurningCircle(RIGHT, self, radius)
                radius_outer  = getMagnitude(self.hull[0] - circle_centre)

            rad_out = self.world.scaleDistance(radius_outer)
            rad_in  = self.world.scaleDistance(radius_inner)
            centre  = self.world.getDrawable(circle_centre)

            pygame.draw.circle(screen, GREY, centre, rad_out, 1)
            pygame.draw.circle(screen, GREY, centre, rad_in, 1)

        else:
            front_left  = self.world.getDrawable(self.hull[1] + forward * 20)
            rear_left   = self.world.getDrawable(self.hull[2] - forward * 20)
            front_right = self.world.getDrawable(self.hull[0] + forward * 20)
            rear_right  = self.world.getDrawable(self.hull[3] - forward * 20)

            pygame.draw.line(screen, GREY, rear_left,  front_left,  1)
            pygame.draw.line(screen, GREY, rear_right, front_right, 1)

        #rad    = self.world.scaleDistance(TURN_RADIUS)
        #left_centre  = getTurningCircle(LEFT,  self)
        #right_centre = getTurningCircle(RIGHT, self)
        #l_c = self.world.getDrawable(left_centre)
        #r_c = self.world.getDrawable(right_centre)
        #pygame.draw.circle(screen, GREY, l_c, rad, 1)
        #pygame.draw.circle(screen, GREY, r_c, rad, 1)

        #pos = self.world.getDrawable(pos)
        #f_r = self.world.getDrawable(f_r)
        #f_l = self.world.getDrawable(f_l)
        #pygame.draw.line(screen, GREY, pos, l_c, 1)
        #pygame.draw.line(screen, GREY, pos, r_c, 1)
        #pygame.draw.line(screen, GREY, f_r, l_c, 1)
        #pygame.draw.line(screen, GREY, f_l, r_c, 1)

        #radius_outer = getMagnitude(self.hull[1] - left_centre)
        #radius_inner = TURN_RADIUS - CAR_WIDTH/2

        #rad_out = self.world.scaleDistance(radius_outer)
        #rad_in  = self.world.scaleDistance(radius_inner)

        #pygame.draw.circle(screen, GREY, l_c, rad_out, 1)
        #pygame.draw.circle(screen, GREY, l_c, rad_in,  1)
        #pygame.draw.circle(screen, GREY, r_c, rad_out, 1)
        #pygame.draw.circle(screen, GREY, r_c, rad_in,  1)


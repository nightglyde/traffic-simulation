from util import *

from obstacle import Obstacle

PATH_HISTORY = 100
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
            radius           = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            angular_velocity = self.speed / radius

            angle_change = Angle(angular_velocity * dt)
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

        self.generateHull()

        self.speed = getMagnitude(self.velocity)

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
            ratio  = min(max(-1, AXLE_LENGTH / radius), 1)
            new_wheel_angle = Angle(math.asin(ratio))

        angle_change = Angle(2*math.pi * dt * 2)
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

            axle_front = forward * AXLE_LENGTH
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
            r_l = pos + axle_left
            rear_left_wheel = [
                self.world.getDrawable(r_l - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_l + r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_l - r_wheel_left - r_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos - axle_left
            rear_right_wheel = [
                self.world.getDrawable(r_r - r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r + r_wheel_left + r_wheel_front),
                self.world.getDrawable(r_r + r_wheel_left - r_wheel_front),
                self.world.getDrawable(r_r - r_wheel_left - r_wheel_front),
            ]
            pygame.draw.polygon(screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(screen, BLACK,     rear_right_wheel, 1)

        #radius = self.world.scaleDistance(TURN_RADIUS)
        #left_centre  = self.world.getDrawable(getTurningCircle(LEFT,  self))
        #right_centre = self.world.getDrawable(getTurningCircle(RIGHT, self))
        #pygame.draw.circle(self.world.screen, GREY, left_centre,  radius, 1)
        #pygame.draw.circle(self.world.screen, GREY, right_centre, radius, 1)

        #pos = self.world.getDrawable(pos)
        #f_r = self.world.getDrawable(f_r)
        #f_l = self.world.getDrawable(f_l)
        #pygame.draw.line(self.world.screen, GREY, pos, left_centre,  1)
        #pygame.draw.line(self.world.screen, GREY, pos, right_centre, 1)
        #pygame.draw.line(self.world.screen, GREY, f_r, left_centre,  1)
        #pygame.draw.line(self.world.screen, GREY, f_l, right_centre, 1)


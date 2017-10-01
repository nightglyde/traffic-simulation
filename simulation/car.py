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

DESIRED_SPEED = 10

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

        self.angular_vel = 0.0

        self.generateHull()

        self.speed_time = time
        self.angle_time = time

        self.destination  = None
        self.red_lines    = []

        self.circle_centre  = None
        self.crash_point    = (None, None, None)

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

        if self.wheel_angle.value != 0.0:
            radius = PIVOT_TO_AXLE / abs(math.sin(self.wheel_angle.value))
            if radius > 1000:
                self.circle_centre = None
                return

            if self.wheel_angle < ANGLE_0:
                self.circle_centre = getTurningCircle(LEFT, self, radius)
                self.outer_radius  = (self.hull[1] - self.circle_centre).mag()
            else:
                self.circle_centre = getTurningCircle(RIGHT, self, radius)
                self.outer_radius  = (self.hull[0] - self.circle_centre).mag()
            self.inner_radius = radius - CAR_WIDTH/2
        else:
            self.circle_centre = None

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
            self.angular_vel = self.speed / radius

            angle_change = Angle(self.angular_vel * dt / 2)
            if self.reverse:
                angle_change = -angle_change
            self.angle += angle_change
        else:
            self.angular_vel = 0.0

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

        self.speed = self.velocity.mag()

        # cornering
        if self.wheel_angle.value != ANGLE_0.value:
            radius           = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            self.angular_vel = self.speed / radius

            angle_change = Angle(self.angular_vel * dt / 2)
            if self.reverse:
                angle_change = -angle_change
            self.angle += angle_change
        else:
            self.angular_vel = 0.0

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
        speed = self.velocity.mag()
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

        angle_change = Angle(2*math.pi * dt)
        if new_wheel_angle < self.wheel_angle:
            self.wheel_angle = max(self.wheel_angle-angle_change,
                                   new_wheel_angle, -MAX_WHEEL_ANGLE)

        elif new_wheel_angle > self.wheel_angle:
            self.wheel_angle = min(self.wheel_angle+angle_change,
                                   new_wheel_angle, MAX_WHEEL_ANGLE)

    def alt_controlAngle(self, new_wheel_angle):
        if self.time <= self.angle_time:
            print("BAD ANGLE CONTROL")
            return

        dt = (self.time - self.angle_time) / 1000
        self.angle_time = self.time

        angle_change = Angle(2*math.pi * dt)
        if new_wheel_angle < self.wheel_angle:
            self.wheel_angle = max(self.wheel_angle-angle_change,
                                   new_wheel_angle, -MAX_WHEEL_ANGLE)

        elif new_wheel_angle > self.wheel_angle:
            self.wheel_angle = min(self.wheel_angle+angle_change,
                                   new_wheel_angle, MAX_WHEEL_ANGLE)

    def predictCrash(self, wheel_angle, speed, obstacles):
        least_time = -1
        results    = (None, None, None)

        if wheel_angle.value != ANGLE_0.value:
            car_left = getVector(self.angle).left90() * CAR_WIDTH/2
            car_points = [self.hull[0], self.hull[1],
                          self.hull[2], self.hull[3],
                          self.position - car_left,
                          self.position + car_left,
                          self.front, self.rear,
                          (self.hull[0] + self.hull[3]) / 2,
                          (self.hull[1] + self.hull[2]) / 2]

            radius  = PIVOT_TO_AXLE / abs(math.sin(wheel_angle.value))
            ang_vel = speed / radius

            if wheel_angle < ANGLE_0:
                turn_direction = LEFT
                circle_centre  = getTurningCircle(LEFT, self, radius)
            else:
                turn_direction = RIGHT
                circle_centre  = getTurningCircle(RIGHT, self, radius)

            radius_sorted_points = []
            for point in car_points:
                angle, radius = getPolar(point - circle_centre)
                radius_sorted_points.append((radius, angle, point))
            radius_sorted_points.sort(reverse=True)

            radii      = []
            angles     = []
            speeds     = []
            car_points = []
            for radius, angle, point in radius_sorted_points:
                radii.append(radius)
                angles.append(angle)
                speeds.append(ang_vel * radius)
                car_points.append(point)

            for obstacle in obstacles:
                i, crash_point, time = obstacle.crashCircle(
                    circle_centre, turn_direction, radii, angles, speeds)

                if i is None:
                    continue

                if time < least_time or least_time == -1:
                    least_time = time
                    results    = (car_points[i], crash_point, time)

        else:
            car_points = [self.hull[1], self.hull[0]]
            for obstacle in obstacles:
                car_point, crash_point, time = obstacle.crashLine(
                    car_points, getVector(self.angle), speed)

                if car_point is None:
                    continue

                if time < least_time or least_time == -1:
                    least_time = time
                    results    = (car_point, crash_point, time)

        return results

    def control(self, waypoint):
        self.crash_point = (None, None, None)
        if self.speed > 0.0:

            obstacles = []
            for grass in self.world.grass:
                if grass.withinRadius(self.front, COLLISION_DISTANCE):
                    obstacles.append(grass)

            car_point, crash_point, time = self.predictCrash(
                self.wheel_angle, self.speed, obstacles)

            self.crash_point = (car_point, crash_point, time)

            if not (time is None) and time < 0:
                event = pygame.event.Event(pygame.USEREVENT)
                pygame.event.post(event)

                print(car_point, crash_point, time)

        # look for nearby collisions
        total_vec = VECTOR_0
        self.red_lines = []
        for grass in self.world.grass:
            line, dist, vec = grass.findNearestLine(self.front)
            if line and dist < ROAD_WIDTH/2:
                total_vec += vec
                total_vec = vec
                self.red_lines.append(line)
                self.red_lines.append((line[0], self.front))
                self.red_lines.append((line[1], self.front))
        if self.red_lines:
            destination = self.position + total_vec.norm() * 4
            angle = getAngle(destination - self.position)
            angle_difference = angle - self.angle

            self.controlAngle(angle_difference)
            self.controlSpeed(DESIRED_SPEED, False)

        elif waypoint:
            # adjust wheel angle using destination point
            destination = waypoint.position
            angle, magnitude = getPolar(destination - self.position)
            angle_difference = angle - self.angle

            self.controlAngle(angle_difference)
            self.controlSpeed(DESIRED_SPEED, False)

        else:
            self.controlAngle(ANGLE_0)
            self.controlSpeed(0, False)

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

    def drawExtra(self):
        screen = self.world.screen
        forward = getVector(self.angle)

        for point_1, point_2 in self.red_lines:
            point_1 = self.world.getDrawable(point_1)
            point_2 = self.world.getDrawable(point_2)
            pygame.draw.line(screen, BLACK, point_1, point_2, 1)

        if self.circle_centre:
            centre = self.world.getDrawable(self.circle_centre)

            outer_radius = self.world.scaleDistance(self.outer_radius)
            inner_radius = self.world.scaleDistance(self.inner_radius)

            pygame.draw.circle(screen, GREY, centre, outer_radius, 1)
            pygame.draw.circle(screen, GREY, centre, inner_radius, 1)

            rad = self.world.scaleDistance(0.25)
            car_point, crash_point, time = self.crash_point
            if car_point:
                car_angle, radius = getPolar(car_point - self.circle_centre)
                crash_angle       = getAngle(crash_point - self.circle_centre)

                rect = generateRect(self.circle_centre, radius, self.world)
                if self.wheel_angle < ANGLE_0:
                    angle_1 = car_angle.norm()
                    angle_2 = crash_angle.norm()
                else:
                    angle_1 = crash_angle.norm()
                    angle_2 = car_angle.norm()
                pygame.draw.arc(screen, BLUE, rect, angle_1, angle_2, 1)

                car_point   = self.world.getDrawable(car_point)
                crash_point = self.world.getDrawable(crash_point)
                pygame.draw.circle(screen, BLUE, car_point,   rad, 1)
                pygame.draw.circle(screen, RED,  crash_point, rad, 1)

        else:
            front = forward * COLLISION_DISTANCE

            left        = self.world.getDrawable(self.hull[1])
            front_left  = self.world.getDrawable(self.hull[1] + front)
            right       = self.world.getDrawable(self.hull[0])
            front_right = self.world.getDrawable(self.hull[0] + front)

            pygame.draw.line(screen, GREY, left,  front_left,  1)
            pygame.draw.line(screen, GREY, right, front_right, 1)

            rad = self.world.scaleDistance(0.25)
            car_point, crash_point, time = self.crash_point
            if car_point:
                car_point   = self.world.getDrawable(car_point)
                crash_point = self.world.getDrawable(crash_point)
                pygame.draw.circle(screen, BLUE, car_point,   rad, 1)
                pygame.draw.circle(screen, RED,  crash_point, rad, 1)
                pygame.draw.line(screen,   BLUE, car_point,   crash_point, 1)


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

SLOW_SPEED = 10
MAX_SPEED  = 15

STEERING_RATE = 2*math.pi * 0.5#0.5#2

def calculateMaxSpeed(distance):
    max_force    = -min(BRAKING_CONSTANT, CAR_WEIGHT)
    acceleration = max_force / CAR_MASS
    speed        = math.sqrt(-2 * acceleration * distance)
    return min(speed, MAX_SPEED)

class Car(Obstacle):
    def __init__(self, world, name, colour, position, angle, time):
        self.world  = world
        self.name   = name
        self.colour = colour

        # status
        self.position = position # metres
        self.angle    = angle    # radians
        self.time     = time     # miliseconds
        self.stopped  = False

        # motion
        self.engine_force     = MIN_ENGINE_FORCE # newtons
        self.wheel_angle      = ANGLE_0          # radians
        self.speed            = 0.0              # metres per second
        self.angular_velocity = 0.0              # radians per second

        # control
        self.desired_angle = ANGLE_0
        self.desired_speed = 0.0

        self.generateHull()

        self.destination = None
        self.red_lines   = []
        self.crash       = None

        self.circle_centre = None
        self.bubble        = []

    def copy(self):
        car = Car(self.world, self.name, self.colour,
                  self.position, self.angle, self.time)

        car.stopped          = self.stopped
        car.engine_force     = self.engine_force
        car.wheel_angle      = self.wheel_angle
        car.speed            = self.speed
        car.angular_velocity = self.angular_velocity
        car.desired_angle    = self.desired_angle
        car.desired_speed    = self.desired_speed

        car.generateHull()
        return car

    def generateHull(self):
        forward  = getVector(self.angle)
        left     = forward.left90()
        car_left = left * CAR_WIDTH/2

        self.front  = self.position + forward * PIVOT_TO_FRONT
        self.rear   = self.position - forward * PIVOT_TO_REAR
        self.centre = (self.front + self.rear) / 2

        self.hull = [self.front - car_left, self.front + car_left,
                     self.rear  + car_left, self.rear  - car_left]

    def generateBubble(self):
        forward  = getVector(self.angle)
        left     = forward.left90()
        car_left = left * CAR_WIDTH/2

        bubble_forward = forward * BUBBLE_SIZE
        bubble_left    = left    * BUBBLE_SIZE
        diag_forward   = forward * BUBBLE_DIAG
        diag_left      = left    * BUBBLE_DIAG

        front_left  = self.front    + car_left
        pivot_left  = self.position + car_left
        mid_left    = self.centre   + car_left
        rear_left   = self.rear     + car_left

        front_right = self.front    - car_left
        mid_right   = self.centre   - car_left
        pivot_right = self.position - car_left
        rear_right  = self.rear     - car_left

        #self.bubble = [
        #    self.front, front_left, mid_left,    pivot_left, rear_left,
        #    self.rear,  rear_right, pivot_right, mid_right,  front_right]

        self.bubble = [
            front_right + diag_forward - diag_left,
            front_right + bubble_forward,
            self.front  + bubble_forward,
            front_left  + bubble_forward,
            front_left  + diag_forward + diag_left,
            front_left  + bubble_left,
            mid_left    + bubble_left,
            pivot_left  + bubble_left,
            rear_left   + bubble_left,
            rear_left   - diag_forward + diag_left,
            rear_left   - bubble_forward,
            self.rear   - bubble_forward,
            rear_right  - bubble_forward,
            rear_right  - diag_forward - diag_left,
            rear_right  - bubble_left,
            pivot_right - bubble_left,
            mid_right   - bubble_left,
            front_right - bubble_left,
        ]

        if abs(self.wheel_angle.value) > TINY_ANGLE:
            radius = PIVOT_TO_AXLE / abs(math.sin(self.wheel_angle.value))

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

            self.world.obstacles.append(self)

    def update(self, time):
        if self.stopped:
            return

        if time <= self.time:
            print("BAD UPDATE")
            return

        dt = (time - self.time) / 1000
        self.time = time

        # steering
        ang_diff = (self.desired_angle - self.angle).value
        if ang_diff == 0.0 or self.speed == 0.0:
            desired_wheel_angle = ANGLE_0
        else:

            turn = ang_diff * PIVOT_TO_AXLE * STEERING_RATE / self.speed
            angle_squared = turn + self.wheel_angle.value**2/2

            if angle_squared >= 0.0:
                desired_wheel_angle = Angle(math.sqrt(angle_squared))
            else:
                desired_wheel_angle = Angle(-math.sqrt(abs(angle_squared)))

            #if ang_diff > ANGLE_45.value:
            #    self.desired_speed = min(self.desired_speed, SLOW_SPEED)

        angle_change = Angle(STEERING_RATE * dt)
        if desired_wheel_angle < self.wheel_angle:
            self.wheel_angle = max(self.wheel_angle - angle_change,
                                   desired_wheel_angle, -MAX_WHEEL_ANGLE)
        elif desired_wheel_angle > self.wheel_angle:
            self.wheel_angle = min(self.wheel_angle + angle_change,
                                   desired_wheel_angle, MAX_WHEEL_ANGLE)

        # cornering (part 1)
        if self.wheel_angle.value != ANGLE_0.value:
            radius  = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            ang_vel = self.speed / radius
            self.angle += Angle(ang_vel * dt / 2)

        # speed control
        acceleration   = (self.desired_speed - self.speed) / dt
        desired_force  = CAR_MASS * acceleration
        desired_force += self.speed**2 * DRAG_CONSTANT
        desired_force += self.speed    * RR_CONSTANT

        engine_change = 10000 * dt
        if desired_force < self.engine_force:
            self.engine_force = max(self.engine_force - engine_change,
                                    desired_force, MIN_ENGINE_FORCE)
        elif desired_force > self.engine_force:
            self.engine_force = min(self.engine_force + engine_change,
                                    desired_force, MAX_ENGINE_FORCE)

        # forces acting on car
        if desired_force < 0:
            force = -min(BRAKING_CONSTANT, CAR_WEIGHT) # brakes
        else:
            force = min(self.engine_force, CAR_WEIGHT/2)
        force -= self.speed**2 * DRAG_CONSTANT
        force -= self.speed    * RR_CONSTANT

        # forwards motion of car
        acceleration   = force / CAR_MASS
        self.speed    += acceleration * dt
        self.position += getVector(self.angle) * self.speed * dt

        # cornering (part 2)
        if self.wheel_angle.value != ANGLE_0.value:
            radius  = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            ang_vel = self.speed / radius
            self.angle += Angle(ang_vel * dt / 2)

            self.angular_velocity = abs(ang_vel)
        else:
            self.angular_velocity = 0.0

        self.generateHull()

    def predictCrash(self, obstacles):
        result = None

        if abs(self.wheel_angle.value) > TINY_ANGLE:
            if self.wheel_angle < ANGLE_0:
                turn_direction = LEFT
            else:
                turn_direction = RIGHT

            details = []
            for point in self.bubble:
                for obstacle in obstacles:
                    if obstacle.checkInside(point):
                        break
                else:
                    angle, radius = getPolar(point - self.circle_centre)
                    speed         = self.angular_velocity * radius
                    details.append((radius, angle, speed, point))

            if not details:
                return result
            details.sort(reverse=True)

            for obstacle in obstacles:
                crash = obstacle.crashCircle(self.circle_centre, turn_direction,
                                             details)
                if crash:
                    if result is None or crash < result:
                        result = crash
        else:
            valid_points = []
            for point in self.bubble:
                for obstacle in obstacles:
                    if obstacle.checkInside(point):
                        break
                else:
                    valid_points.append(point)

            if not valid_points:
                return result

            for obstacle in obstacles:
                crash = obstacle.crashLine(valid_points, getVector(self.angle),
                                           self.speed)
                if crash:
                    if result is None or crash < result:
                        result = crash
        return result

    def control(self, waypoint, slow):
        if slow:
            self.desired_speed = SLOW_SPEED
        else:
            self.desired_speed = MAX_SPEED

        self.generateBubble()

        self.crash = None

        if self.speed > 0.0:
            obstacles = []
            for obstacle in self.world.obstacles:
                if obstacle.withinRadius(self.front, COLLISION_DISTANCE):
                    obstacles.append(obstacle)
            for grass in self.world.grass:
                if grass.withinRadius(self.front, COLLISION_DISTANCE):
                    obstacles.append(grass)

            crash = self.predictCrash(obstacles)

            if crash:
                time, car_point, crash_point, line = crash

                if time < ACTION_TIME:
                    self.crash = crash

                    left_sim = self.copy()
                    left_sim.desired_angle = getAngle(line)

                    right_sim = self.copy()
                    right_sim.desired_angle = getAngle(-line)

                    start_time = self.time
                    end_time   = start_time + ACTION_DELAY

                    crash_count = 0

                    left_time = start_time
                    while left_time < end_time:
                        left_time += TIME_STEP
                        left_sim.update(left_time)

                        if not self.world.checkObject(left_sim):
                            crash_count += 1
                            break

                    right_time = start_time
                    while right_time < end_time:
                        right_time += TIME_STEP
                        right_sim.update(right_time)

                        if not self.world.checkObject(right_sim):
                            crash_count += 1
                            break

                    if crash_count == 2:
                        distance = self.speed * time
                        self.desired_speed = min(self.desired_speed,
                                                 calculateMaxSpeed(distance))

                    if left_time > right_time:
                        self.desired_angle = left_sim.desired_angle
                        self.destination   = left_sim.front
                    elif right_time > left_time:
                        self.desired_angle = right_sim.desired_angle
                        self.destination   = right_sim.front
                    elif waypoint:

                        left_dist  = (waypoint.position-left_sim.centre).mag()
                        right_dist = (waypoint.position-right_sim.centre).mag()

                        if left_dist < right_dist:
                            self.desired_angle = left_sim.desired_angle
                            self.destination   = left_sim.front
                        else:
                            self.desired_angle = right_sim.desired_angle
                            self.destination   = right_sim.front
                    else:
                        self.desired_angle = left_sim.desired_angle
                        self.destination   = left_sim.front

        if self.crash:
            return

        elif waypoint:
            self.destination   = waypoint.position
            self.desired_angle = getAngle(self.destination - self.position)

        else:
            self.desired_angle = self.angle
            self.desired_speed = 0
            self.destination   = None

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

        #bubble = [self.world.getDrawable(point) for point in self.bubble]
        #pygame.draw.polygon(screen, LIGHT_GREY, bubble, 1)

        #vec = getVector(self.desired_angle)
        #point = self.world.getDrawable(self.position + vec*4)
        #pos   = self.world.getDrawable(self.position)
        #pygame.draw.line(screen, BLACK, pos, point, 3)

        rad = self.world.scaleDistance(0.25)
        if self.destination:
            dest = self.world.getDrawable(self.destination)
            pygame.draw.circle(screen, BLACK, dest, rad, 1)

        if abs(self.wheel_angle.value) > TINY_ANGLE:
            radius = PIVOT_TO_AXLE / abs(math.sin(self.wheel_angle.value))

            if self.wheel_angle < ANGLE_0:
                self.circle_centre = getTurningCircle(LEFT, self, radius)
                self.outer_radius  = (self.hull[1] - self.circle_centre).mag()
            else:
                self.circle_centre = getTurningCircle(RIGHT, self, radius)
                self.outer_radius  = (self.hull[0] - self.circle_centre).mag()

            self.inner_radius = radius - CAR_WIDTH/2

        else:
            self.circle_centre = None

        if self.circle_centre:
            centre       = self.world.getDrawable(self.circle_centre)
            outer_radius = self.world.scaleDistance(self.outer_radius)
            inner_radius = self.world.scaleDistance(self.inner_radius)

            pygame.draw.circle(screen, GREY, centre, outer_radius, 1)
            pygame.draw.circle(screen, GREY, centre, inner_radius, 1)

            if self.crash:
                time, car_point, crash_point, line = self.crash
                car_angle, radius = getPolar(car_point   - self.circle_centre)
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

            if self.crash:
                time, car_point, crash_point, line = self.crash
                car_point   = self.world.getDrawable(car_point)
                crash_point = self.world.getDrawable(crash_point)
                pygame.draw.circle(screen, BLUE, car_point,   rad, 1)
                pygame.draw.circle(screen, RED,  crash_point, rad, 1)
                pygame.draw.line(screen,   BLUE, car_point,   crash_point, 1)


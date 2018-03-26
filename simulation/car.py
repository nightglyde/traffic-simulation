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

SLOW_SPEED = 7.5
MAX_SPEED  = 15

STEERING_RATE = 2*math.pi * 0.5#2

def calculateMaxSpeed(distance):
    max_force    = -min(BRAKING_CONSTANT, CAR_WEIGHT)
    acceleration = max_force / CAR_MASS
    speed        = math.sqrt(-2 * acceleration * distance)
    return min(speed, MAX_SPEED)

def getNextWheelAngle(desired_car_angle, car_angle, wheel_angle, speed, dt):
    ang_diff = (desired_car_angle - car_angle).value
    if ang_diff == 0.0 or speed == 0.0:
        return wheel_angle
    else:
        turn = abs(ang_diff) * PIVOT_TO_AXLE * STEERING_RATE / speed
        if ang_diff > 0.0:
            ratio = (math.cos(wheel_angle.value) + 1 - turn) / 2
            desired_wheel_angle = Angle(math.acos(max(-1.0, min(ratio, 1.0))))

        else:
            ratio = (math.cos(-wheel_angle.value) + 1 - turn) / 2
            desired_wheel_angle = Angle(-math.acos(max(-1.0, min(ratio, 1.0))))

        #angle_squared = turn + wheel_angle.value**2/2

        #if angle_squared >= 0.0:
        #    desired_wheel_angle = Angle(math.sqrt(angle_squared))
        #else:
        #    desired_wheel_angle = Angle(-math.sqrt(abs(angle_squared)))

    angle_change = Angle(STEERING_RATE * dt)
    if desired_wheel_angle < wheel_angle:
        return max(wheel_angle - angle_change,
                   desired_wheel_angle, -MAX_WHEEL_ANGLE)
    elif desired_wheel_angle > wheel_angle:
        return min(wheel_angle + angle_change,
                   desired_wheel_angle, MAX_WHEEL_ANGLE)
    return wheel_angle

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
        self.route         = deque()
        self.desired_angle = ANGLE_0
        self.desired_speed = 0.0

        self.generateHull()

        self.crash       = None
        self.lines       = []

    def copy(self):
        car = Car(self.world, self.name, self.colour,
                  self.position, self.angle, self.time)

        # status
        car.stopped = self.stopped

        # motion
        car.engine_force     = self.engine_force
        car.wheel_angle      = self.wheel_angle
        car.speed            = self.speed
        car.angular_velocity = self.angular_velocity

        # control
        car.route         = self.route.copy()
        car.desired_angle = self.desired_angle
        car.desired_speed = self.desired_speed

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

        return [
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

    def stop(self, other):
        if not self.stopped:
            self.stopped = True
            print(self.name, "crashed into", other.name,
                  "at time", self.time / 1000)

            self.world.obstacles.append(self)

    def updateRoute(self):
        while self.route:
            waypoint, desired_speed = self.route[0]

            if waypoint.checkInside(self.centre):
                self.route.popleft()
                continue

            destination        = waypoint.position
            self.desired_speed = desired_speed
            self.desired_angle = getAngle(destination - self.position)

            angle_difference = self.desired_angle - self.angle
            if angle_difference < ANGLE_0:
                centre   = getTurningCircle(LEFT, self, TURN_RADIUS)
                distance = (destination - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle + ANGLE_90
            elif angle_difference > ANGLE_0:
                centre   = getTurningCircle(RIGHT, self, TURN_RADIUS)
                distance = (destination - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle - ANGLE_90
            return

        self.desired_speed = 0.0
        self.desired_angle = self.angle

    def update(self, time):
        if self.stopped:
            return

        if time <= self.time:
            print("BAD UPDATE")
            return

        dt = (time - self.time) / 1000
        self.time = time

        if True:
            self.updateRoute()

        self.wheel_angle = getNextWheelAngle(self.desired_angle, self.angle,
                                             self.wheel_angle,   self.speed, dt)

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

    def predictCrash(self, car_points, lines, wheel_angle):
        result = None

        if abs(wheel_angle.value) > TINY_ANGLE:
            radius = PIVOT_TO_AXLE / abs(math.sin(wheel_angle.value))
            if wheel_angle < ANGLE_0:
                circle_centre  = getTurningCircle(LEFT, self, radius)
                turn_direction = LEFT
            else:
                circle_centre  = getTurningCircle(RIGHT, self, radius)
                turn_direction = RIGHT

            details = []
            for point in car_points:
                angle, radius = getPolar(point - circle_centre)
                speed         = self.angular_velocity * radius
                details.append((radius, angle, speed, point))

            details.sort(reverse=True)

            for line in lines:
                crash = crashCircle(line, circle_centre,
                                    turn_direction, details)
                if crash:
                    if result is None or crash < result:
                        result = crash
        else:
            for line in lines:
                crash = crashLine(line, car_points,
                                  getVector(self.angle), self.speed)
                if crash:
                    if result is None or crash < result:
                        result = crash
        return result

    def control(self, route):
        self.route = route

    def old_control(self, waypoint, slow, keep):
        if slow:
            self.desired_speed = SLOW_SPEED
        else:
            self.desired_speed = MAX_SPEED

        self.crash = None
        self.lines = []

        if False: #self.speed > 0.0: # this is the bit we desparately need to replace
            forward = getVector(self.angle)
            for obstacle in self.world.obstacles:
                self.lines += obstacle.linesWithinRadius(self.rear,
                                                         COLLISION_DISTANCE,
                                                         forward)
            for grass in self.world.grass:
                self.lines += grass.linesWithinRadius(self.rear,
                                                      COLLISION_DISTANCE,
                                                      forward)
            car_points = self.generateBubble()
            if car_points:
                crash = self.predictCrash(car_points, self.lines, self.wheel_angle)
            else:
                crash = None

            if crash:
                time, car_point, crash_point, line = crash

                if time < ACTION_TIME:
                    self.crash = crash

                    left_sim = self.copy()
                    left_sim.desired_angle = getAngle(line[1] - line[0])

                    right_sim = self.copy()
                    right_sim.desired_angle = getAngle(line[0] - line[1])

                    start_time = self.time
                    end_time   = start_time + ACTION_DELAY

                    crash_count = 0

                    left_time = start_time
                    while left_time < end_time:
                        left_time += TIME_STEP
                        left_sim.update(left_time)

                        if not self.world.checkCar(left_sim):
                            crash_count += 1
                            break

                    right_time = start_time
                    while right_time < end_time:
                        right_time += TIME_STEP
                        right_sim.update(right_time)

                        if not self.world.checkCar(right_sim):
                            crash_count += 1
                            break

                    #if crash_count == 2:
                    #    distance = self.speed * time
                    #    self.desired_speed = min(self.desired_speed,
                    #                             calculateMaxSpeed(distance))

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
            if keep:
                vec = getVector(self.angle).left90()
                self.destination   = self.position + vec * 4
                self.desired_angle = getAngle(self.destination - self.position)
            else:
                self.destination   = waypoint.position
                self.desired_angle = getAngle(self.destination - self.position)
                angle_difference   = self.desired_angle - self.angle

                if angle_difference < ANGLE_0:
                    centre   = getTurningCircle(LEFT, self, TURN_RADIUS)
                    distance = (self.destination - centre).mag()
                    if distance < TURN_RADIUS:
                        self.desired_angle = self.angle + ANGLE_90

                elif angle_difference > ANGLE_0:
                    centre   = getTurningCircle(RIGHT, self, TURN_RADIUS)
                    distance = (self.destination - centre).mag()
                    if distance < TURN_RADIUS:
                        self.desired_angle = self.angle - ANGLE_90

        else:
            self.desired_angle = self.angle
            self.desired_speed = 0
            self.destination   = None

    def alt_control(self, waypoint, slow):
        if slow:
            self.desired_speed = SLOW_SPEED
        else:
            self.desired_speed = MAX_SPEED

        if waypoint:
            self.destination   = waypoint.position
            self.desired_angle = getAngle(self.destination - self.position)
            angle_difference   = self.desired_angle - self.angle

            if angle_difference < ANGLE_0:
                centre   = getTurningCircle(LEFT, self, TURN_RADIUS)
                distance = (self.destination - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle + ANGLE_90

            elif angle_difference > ANGLE_0:
                centre   = getTurningCircle(RIGHT, self, TURN_RADIUS)
                distance = (self.destination - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle - ANGLE_90
        else:
            self.desired_angle = self.angle
            self.desired_speed = 0
            self.destination   = None

        self.lines = []
        if self.speed > 0.0:
            forward = getVector(self.angle)
            for obstacle in self.world.obstacles:
                self.lines += obstacle.linesWithinRadius(self.rear,
                                                         COLLISION_DISTANCE,
                                                         forward)
            for grass in self.world.grass:
                self.lines += grass.linesWithinRadius(self.rear,
                                                      COLLISION_DISTANCE,
                                                      forward)

            num_lines = len(self.lines)
            for i in range(num_lines-1):
                i_start, i_end = self.lines[i]
                i_vec = i_end - i_start
                for j in range(i+1, num_lines):
                    j_start, j_end = self.lines[j]
                    j_vec = j_end - j_start

                    if crossProduct(i_vec, j_vec) == 0.0:
                        # something
                        pass

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
        if self.stopped:
            return

        screen = self.world.screen
        forward = getVector(self.angle)

        for point_i, point_j in self.lines:
            point_i = self.world.getDrawable(point_i)
            point_j = self.world.getDrawable(point_j)
            pygame.draw.line(screen, self.colour, point_i, point_j, 2)

        if abs(self.wheel_angle.value) > TINY_ANGLE:
            radius = PIVOT_TO_AXLE / abs(math.sin(self.wheel_angle.value))

            if self.wheel_angle < ANGLE_0:
                circle_centre = getTurningCircle(LEFT, self, radius)
                outer_radius  = (self.hull[1] - circle_centre).mag()
            else:
                circle_centre = getTurningCircle(RIGHT, self, radius)
                outer_radius  = (self.hull[0] - circle_centre).mag()

            centre       = self.world.getDrawable(circle_centre)
            outer_radius = self.world.scaleDistance(outer_radius)
            inner_radius = self.world.scaleDistance(radius - CAR_WIDTH/2)

            pygame.draw.circle(screen, GREY, centre, outer_radius, 1)
            pygame.draw.circle(screen, GREY, centre, inner_radius, 1)

            if self.crash:
                time, car_point, crash_point, line = self.crash
                car_angle, radius = getPolar(car_point   - circle_centre)
                crash_angle       = getAngle(crash_point - circle_centre)

                rect = generateRect(circle_centre, radius, self.world)
                if self.wheel_angle < ANGLE_0:
                    angle_1 = car_angle.norm()
                    angle_2 = crash_angle.norm()
                else:
                    angle_1 = crash_angle.norm()
                    angle_2 = car_angle.norm()
                pygame.draw.arc(screen, BLUE, rect, angle_1, angle_2, 1)

                rad = self.world.scaleDistance(0.25)
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

                rad = self.world.scaleDistance(0.25)
                car_point   = self.world.getDrawable(car_point)
                crash_point = self.world.getDrawable(crash_point)
                pygame.draw.circle(screen, BLUE, car_point,   rad, 1)
                pygame.draw.circle(screen, RED,  crash_point, rad, 1)
                pygame.draw.line(screen,   BLUE, car_point,   crash_point, 1)


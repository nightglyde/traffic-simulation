from util import *

from obstacle import Obstacle

from controller import FollowRoad, ChangeSpeed, EnterIntersection

AVOID_CIRCLES = False
SHOW_WHEELS   = True
SHOW_LIGHTS   = True

STEERING_RATE = 2*math.pi * 0.3#0.5#0.1

LOOK_AHEAD_DIST = 3#TURN_RADIUS

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
    def __init__(self, world, name, colour, road, position, angle, time):
        self.world  = world
        self.name   = name
        self.colour = colour

        # status
        self.road     = road
        self.position = position # metres
        self.angle    = angle    # radians
        self.time     = time     # miliseconds
        self.stopped  = False

        # motion
        self.engine_force     = MIN_ENGINE_FORCE # newtons
        self.wheel_angle      = ANGLE_0          # radians
        self.speed            = 0.0              # metres per second

        # control
        self.route            = deque()
        self.desired_position = self.position
        self.desired_angle    = ANGLE_0

        self.desired_speed = 0.0
        self.speed_timeout = -1

        self.generateHull()

        # modified by the controller
        self.path = deque()

    def copy(self):
        car = Car(self.world, self.name, self.colour,
                  self.road, self.position, self.angle, self.time)

        # status
        car.stopped = self.stopped

        # motion
        car.engine_force     = self.engine_force
        car.wheel_angle      = self.wheel_angle
        car.speed            = self.speed

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

    def crash(self, other):
        if not self.stopped:
            self.stopped = True
            print(self.name, "crashed into", other.name,
                  "at time", self.time / 1000,
                  "going speed", self.speed*3.6)

            self.world.crashed_cars += 1
            self.world.ghosts.append(self)

    def stop(self):
        if not self.stopped:
            self.stopped = True
            print(self.name, "finished mission at time", self.time / 1000)
            self.world.successful_cars += 1

    def crossingSpeed(self, instruction, dist_left):
        if instruction.checkLights() == GREEN_LIGHT:
            return MAX_SPEED

        max_speed = calculateMaxSpeed(dist_left, self.speed)
        if self.speed < max_speed:
            # you can't stop in time, so keep going and hope for the best
            return MAX_SPEED

        return max_speed


    def updateRoute(self):
        while self.route:

            instruction = self.route[0]

            if isinstance(instruction, ChangeSpeed):
                self.desired_speed = instruction.speed
                self.speed_timeout = self.time + instruction.timeout

                self.route.popleft()
                continue

            road     = instruction.road
            waypoint = instruction.waypoint

            road_vec = road.end - road.start
            road_len = road_vec.mag()

            self_vec  = self.centre - road.start
            self_dist = dotProduct(self_vec, road.vec) / road.length

            wayp_vec  = waypoint - road.start
            wayp_dist = wayp_vec.mag()

            if self_dist >= wayp_dist:
                self.route.popleft()
                continue

            break

        if not self.route:
            self.stop()

            self.desired_speed    = 0.0
            self.desired_angle    = self.angle
            self.desired_position = self.position
            return

        self.road = road

        if self.time >= self.speed_timeout:
            dist_left = wayp_dist - self_dist - CAR_LENGTH/2
            self.desired_speed = self.crossingSpeed(instruction, dist_left)

        if self_dist + LOOK_AHEAD_DIST <= wayp_dist:
            look_ahead = (self_dist + LOOK_AHEAD_DIST) / wayp_dist
            self.desired_position = road.start + wayp_vec * look_ahead

        else:
            dist_left = LOOK_AHEAD_DIST - (wayp_dist - self_dist)

            for i in range(1, len(self.route)):
                instruction = self.route[i]
                if isinstance(instruction, ChangeSpeed):
                    continue

                next_waypoint = instruction.waypoint

                wayp_vec  = next_waypoint - waypoint
                wayp_dist = wayp_vec.mag()

                if dist_left <= wayp_dist:
                    look_ahead = dist_left / wayp_dist
                    self.desired_position = waypoint + wayp_vec * look_ahead
                    break

                dist_left -= wayp_dist
                waypoint   = next_waypoint

            else:
                self.desired_position = waypoint

        self.desired_angle = getAngle(self.desired_position - self.position)

        if AVOID_CIRCLES:
            angle_difference = self.desired_angle - self.angle
            if angle_difference < ANGLE_0:
                centre   = getTurningCircle(LEFT, self, TURN_RADIUS)
                distance = (self.desired_position - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle + ANGLE_90
            elif angle_difference > ANGLE_0:
                centre   = getTurningCircle(RIGHT, self, TURN_RADIUS)
                distance = (self.desired_position - centre).mag()
                if distance < TURN_RADIUS:
                    self.desired_angle = self.angle - ANGLE_90

    def update(self, time):
        if self.stopped:
            return

        if time <= self.time:
            print("BAD UPDATE")
            return

        dt = (time - self.time) / 1000
        self.time = time

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
        self.speed     = max(0, self.speed + acceleration * dt)
        self.position += getVector(self.angle) * self.speed * dt

        # cornering (part 2)
        if self.wheel_angle.value != ANGLE_0.value:
            radius  = PIVOT_TO_AXLE / math.sin(self.wheel_angle.value)
            ang_vel = self.speed / radius
            self.angle += Angle(ang_vel * dt / 2)

        self.generateHull()

    def getNextTurn(self):
        for instruction in self.route:
            if isinstance(instruction, EnterIntersection):
                return instruction.turn

            if isinstance(instruction, FollowRoad):
                turn = instruction.road.turn

                if turn != None:
                    return turn

        return CENTRE


    def draw(self, selected=False):
        screen = self.world.screen
        pos    = self.position

        forward = getVector(self.angle)
        left    = forward.right90()#left90()
        # TODO: FIX THIS
        # FOR SOME INSANE REASON, LEFT AND RIGHT ARE SWITCHED!!!
        # IT'S LIKE THIS FOR THE WHEELS TOO

        if not self.stopped:
            car_colour   = self.colour
            line_colour  = BLACK
        else:
            car_colour   = LIGHT_GREY
            line_colour  = GREY

        # draw car
        chassis = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(screen, car_colour,  chassis)
        pygame.draw.polygon(screen, line_colour, chassis, 1)

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

        if self.stopped:
            pygame.draw.polygon(screen, self.colour, arrow)
        elif selected:
            pygame.draw.polygon(screen, LIGHTER[self.colour], arrow)

        pygame.draw.polygon(screen, line_colour, arrow, 1)

        # draw lights
        if SHOW_LIGHTS and not self.stopped:
            turn = self.getNextTurn()

            light_front = forward * LIGHT_FRONT
            light_back  = forward * LIGHT_BACK

            light_outer = left * LIGHT_OUTER
            light_mid   = left * LIGHT_MID
            light_inner = left * LIGHT_INNER

            left_headlight = [
                self.world.getDrawable(pos + light_front + light_mid),
                self.world.getDrawable(pos + light_front + light_inner),
                self.world.getDrawable(pos + light_back  + light_inner),
                self.world.getDrawable(pos + light_back  + light_mid),
            ]

            right_headlight = [
                self.world.getDrawable(pos + light_front - light_inner),
                self.world.getDrawable(pos + light_front - light_mid),
                self.world.getDrawable(pos + light_back  - light_mid),
                self.world.getDrawable(pos + light_back  - light_inner),
            ]

            pygame.draw.polygon(screen, LIGHT_YELLOW, left_headlight)
            pygame.draw.polygon(screen, LIGHT_YELLOW, right_headlight)

            left_turning_signal = [
                self.world.getDrawable(pos + light_front + light_outer),
                self.world.getDrawable(pos + light_front + light_mid),
                self.world.getDrawable(pos + light_back  + light_mid),
                self.world.getDrawable(pos + light_back  + light_outer),
            ]

            right_turning_signal = [
                self.world.getDrawable(pos + light_front - light_mid),
                self.world.getDrawable(pos + light_front - light_outer),
                self.world.getDrawable(pos + light_back  - light_outer),
                self.world.getDrawable(pos + light_back  - light_mid),
            ]

            if turn == LEFT and (self.time % 1000) < 500:
                pygame.draw.polygon(screen, AMBER, left_turning_signal)
            else:
                pygame.draw.polygon(screen, GREY, left_turning_signal)

            if turn == RIGHT and (self.time % 1000) < 500:
                pygame.draw.polygon(screen, AMBER, right_turning_signal)
            else:
                pygame.draw.polygon(screen, GREY, right_turning_signal)

            pygame.draw.polygon(screen, BLACK, left_headlight,  1)
            pygame.draw.polygon(screen, BLACK, right_headlight, 1)
            pygame.draw.polygon(screen, BLACK, left_turning_signal,  1)
            pygame.draw.polygon(screen, BLACK, right_turning_signal, 1)

        # draw wheels
        if SHOW_WHEELS and not self.stopped:
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

        else:
            front = forward * COLLISION_DISTANCE

            left        = self.world.getDrawable(self.hull[1])
            front_left  = self.world.getDrawable(self.hull[1] + front)
            right       = self.world.getDrawable(self.hull[0])
            front_right = self.world.getDrawable(self.hull[0] + front)

            pygame.draw.line(screen, GREY, left,  front_left,  1)
            pygame.draw.line(screen, GREY, right, front_right, 1)

    def drawDesiredPosition(self):
        if not self.stopped:
            screen = self.world.screen
            pos    = self.world.getDrawable(self.desired_position)

            radius = max(2, self.world.scaleDistance(0.2))
            pygame.draw.circle(screen, DARKER[self.colour], pos, radius)
            pygame.draw.circle(screen, BLACK,               pos, radius, 1)

    def drawPath(self):
        if len(self.path) > 1:
            path = [self.world.getDrawable(point) for point in self.path]
            pygame.draw.lines(self.world.screen, GREY, False, path, 1)


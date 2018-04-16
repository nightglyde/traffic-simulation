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

AVOID_CIRCLES = False
SHOW_WHEELS   = True

SLOW_SPEED = 7.5
MAX_SPEED  = 15

STEERING_RATE = 2*math.pi * 0.5#0.1

LOOK_AHEAD_DIST = 3#TURN_RADIUS

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
        self.desired_position = self.position

        self.generateHull()

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

    def stop(self, other):
        if not self.stopped:
            self.stopped = True
            print(self.name, "crashed into", other.name,
                  "at time", self.time / 1000)

            #self.world.obstacles.append(self)

            self.world.crashed_cars += 1
            print("Crashed cars:", self.world.crashed_cars)
            self.world.ghosts.append(self)

    def updateRoute(self):
        speed_zero = False
        #while self.route:
        #    road, waypoint, desired_speed, time = self.route[0]
        #    if desired_speed == 0:
        #        if self.time < time:
                    # slam breaks!
                    #self.desired_speed = 0.0
                    #self.desired_angle = getAngle(
                    #    self.desired_position - self.position)
                    #self.desired_angle = self.angle
                    #return
        #            speed_zero = True
        #            break
        #        else:
        #            self.route.popleft()
        #    else:
        #        break

        while self.route:
            road, waypoint, desired_speed, time = self.route[0]

            if desired_speed == 0:
                if self.time < time:
                    speed_zero = True
                else:
                    self.route.popleft()
                    continue

            road_vec = road.end - road.start
            road_len = road_vec.mag()

            self_vec  = self.centre - road.start
            self_dist = dotProduct(self_vec, road_vec) / road_len

            wayp_vec  = waypoint - road.start
            wayp_dist = wayp_vec.mag()

            if self_dist >= wayp_dist:
                self.route.popleft()
                continue

            break

        if not self.route:
            self.desired_speed    = 0.0
            self.desired_angle    = self.angle
            self.desired_position = self.position
            return

        if speed_zero:
            self.desired_speed = 0.0
        else:
            self.desired_speed = desired_speed

        # scale LOOK_AHEAD_DIST by the sharpness of the turn???

        if self_dist + LOOK_AHEAD_DIST <= wayp_dist:
            look_ahead = (self_dist + LOOK_AHEAD_DIST) / wayp_dist
            self.desired_position = road.start + wayp_vec * look_ahead

        else:
            dist_left = LOOK_AHEAD_DIST - (wayp_dist - self_dist)

            for i in range(1, len(self.route)):
                next_waypoint = self.route[i][1]

                wayp_vec  = next_waypoint - waypoint
                wayp_dist = wayp_vec.mag()

                if dist_left <= wayp_dist:
                    look_ahead = dist_left / wayp_dist
                    self.desired_position = waypoint + wayp_vec * look_ahead
                    break

                dist_left    -= wayp_dist
                waypoint = next_waypoint

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

    def control(self, route):
        self.route = route

    def draw(self, selected=False):
        screen = self.world.screen
        pos    = self.position

        forward = getVector(self.angle)
        left    = forward.left90()

        # draw car
        chassis = [self.world.getDrawable(point) for point in self.hull]
        if self.stopped:
            pygame.draw.polygon(screen, LIGHT_GREY, chassis)
            pygame.draw.polygon(screen, GREY,       chassis, 1)
        else:
            pygame.draw.polygon(screen, self.colour, chassis)
            pygame.draw.polygon(screen, BLACK,       chassis, 2)

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
            #pygame.draw.polygon(screen, GREY, arrow, 1)
            pygame.draw.polygon(screen, LIGHTER[self.colour], arrow, 1)

        else:
            if selected:
                pygame.draw.polygon(screen, LIGHTER[self.colour], arrow)
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

            #radius_1 = max(6, self.world.scaleDistance(0.6))
            #pygame.draw.circle(screen, self.colour,          pos, radius_1)
            #pygame.draw.circle(screen, DARKER[self.colour],  pos, radius_1, 1)

            #radius_2 = max(4, self.world.scaleDistance(0.4))
            #pygame.draw.circle(screen, LIGHTER[self.colour], pos, radius_2)
            #pygame.draw.circle(screen, DARKER[self.colour],  pos, radius_2, 1)

            #radius_3 = max(2, self.world.scaleDistance(0.2))
            #pygame.draw.circle(screen, self.colour,          pos, radius_3)
            #pygame.draw.circle(screen, DARKER[self.colour],  pos, radius_3, 1)

            radius_3 = max(2, self.world.scaleDistance(0.2))
            pygame.draw.circle(screen, DARKER[self.colour],  pos, radius_3)
            pygame.draw.circle(screen, BLACK,                pos, radius_3, 1)


from util import *

from obstacle import Obstacle

#from controller import FollowRoad, EnterIntersection

SHOW_WHEELS   = False
SHOW_LIGHTS   = True

STEERING_RATE = 2*math.pi * 0.3#0.3#0.5#0.1

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

        # for results
        self.start_time = time

        # status
        self.position = position # metres
        self.angle    = angle    # radians
        self.time     = time     # miliseconds
        self.stopped  = False
        self.generateHull()

        # motion
        self.engine_force     = MIN_ENGINE_FORCE # newtons
        self.wheel_angle      = ANGLE_0          # radians
        self.speed            = 0.0              # metres per second

        # control
        self.desired_position = self.position
        self.desired_angle    = ANGLE_0
        self.desired_speed    = 0.0

        self.next_turn = CENTRE

        # visualisation
        #self.path = deque() # modified by the controller

        self.random_offset = random.randint(1, 1000)

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
            #print(self.name, "crashed into", other.name,
            #      "at time", self.time / 1000,
            #      "going speed", self.speed*3.6)

            self.world.crashed_cars += 1
            self.world.ghosts.append(self)

    def stop(self):
        if not self.stopped:
            self.stopped = True
            #print(self.name, "finished mission at time", self.time / 1000,
            #      ", position", self.position)
            self.world.successful_cars += 1

            # for results
            duration = self.time - self.start_time
            self.world.results.append(duration)
            print(duration)

    def update(self, time):
        if self.stopped:
            return

        if time <= self.time:
            raise Exception("BAD UPDATE: new time <= current time")

        dt = (time - self.time) / 1000
        self.time = time

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

    def control(self, speed, position, angle, turn):
        self.desired_speed    = speed
        self.desired_position = position
        self.desired_angle    = angle
        self.next_turn        = turn

    def draw(self, selected, paused):
        screen = self.world.screen
        pos    = self.position

        forward = getVector(self.angle)
        left    = forward.right90()#left90()
        # TODO: FIX THIS
        # FOR SOME INSANE REASON, LEFT AND RIGHT ARE SWITCHED!!!
        # IT'S LIKE THIS FOR THE WHEELS TOO

        # car outline
        chassis = [self.world.getDrawable(point) for point in self.hull]

        # arrow outline
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
            self.world.getDrawable(pos              - stem_left),
        ]

        if self.stopped:
            # draw crashed car
            pygame.draw.polygon(screen, LIGHT_GREY,  chassis)
            pygame.draw.polygon(screen, GREY, chassis, 1)
            pygame.draw.polygon(screen, self.colour, arrow)
            pygame.draw.polygon(screen, GREY, arrow, 1)
            return

        # draw active car
        pygame.draw.polygon(screen, self.colour, chassis)
        pygame.draw.polygon(screen, BLACK,       chassis, 1)
        if selected:
            pygame.draw.polygon(screen, LIGHTER[self.colour], arrow)
        pygame.draw.polygon(screen, BLACK, arrow, 1)

        #font = pygame.font.SysFont('Helvetica', 12, bold=True)
        #text = font.render(self.name, False, BLACK)
        #rect = text.get_rect(center=self.world.getDrawable(self.centre))
        #screen.blit(text, rect)

        # draw wheels
        if SHOW_WHEELS and self.world.scale >= 5:
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

        # draw lights
        if SHOW_LIGHTS:

            turning_signal_on = paused or (self.time % 1000) < 500

            if self.next_turn != CENTRE:

                light_front = forward * (PIVOT_TO_CENTRE + 0.5)
                light_mid   = forward * (PIVOT_TO_CENTRE)
                light_back  = forward * (PIVOT_TO_CENTRE - 0.5)

                light_outer = left * (CAR_WIDTH/2 + 1)
                light_inner = left * (CAR_WIDTH/2 + 0.5)

                if self.next_turn == LEFT:
                    left_arrow = [
                        self.world.getDrawable(pos + light_front + light_inner),
                        self.world.getDrawable(pos + light_mid   + light_outer),
                        self.world.getDrawable(pos + light_back  + light_inner),
                    ]
                    pygame.draw.polygon(screen, AMBER, left_arrow)
                    pygame.draw.polygon(screen, BLACK, left_arrow, 1)

                if self.next_turn == RIGHT:
                    right_arrow = [
                        self.world.getDrawable(pos + light_front - light_inner),
                        self.world.getDrawable(pos + light_mid   - light_outer),
                        self.world.getDrawable(pos + light_back  - light_inner),
                    ]
                    pygame.draw.polygon(screen, AMBER, right_arrow)
                    pygame.draw.polygon(screen, BLACK, right_arrow, 1)

            #if self.world.scale >= 15:

            #    light_front = forward * LIGHT_FRONT
            #    light_back  = forward * LIGHT_BACK

            #    light_outer = left * LIGHT_OUTER
            #    light_mid   = left * LIGHT_MID
            #    light_inner = left * LIGHT_INNER

            #    # left headlight
            #    left_headlight = [
            #        self.world.getDrawable(pos + light_front + light_mid),
            #        self.world.getDrawable(pos + light_front + light_inner),
            #        self.world.getDrawable(pos + light_back  + light_inner),
            #        self.world.getDrawable(pos + light_back  + light_mid),
            #    ]

            #    pygame.draw.polygon(screen, LIGHT_YELLOW, left_headlight)
            #    pygame.draw.polygon(screen, BLACK, left_headlight,  1)

            #    # right headlight
            #    right_headlight = [
            #        self.world.getDrawable(pos + light_front - light_inner),
            #        self.world.getDrawable(pos + light_front - light_mid),
            #        self.world.getDrawable(pos + light_back  - light_mid),
            #        self.world.getDrawable(pos + light_back  - light_inner),
            #    ]

            #    pygame.draw.polygon(screen, LIGHT_YELLOW, right_headlight)
            #    pygame.draw.polygon(screen, BLACK, right_headlight, 1)

            #    # left turning signal
            #    left_turning_signal = [
            #        self.world.getDrawable(pos + light_front + light_outer),
            #        self.world.getDrawable(pos + light_front + light_mid),
            #        self.world.getDrawable(pos + light_back  + light_mid),
            #        self.world.getDrawable(pos + light_back  + light_outer),
            #    ]

            #    if self.next_turn == LEFT and turning_signal_on:
            #        pygame.draw.polygon(screen, AMBER, left_turning_signal)
            #    else:
            #        pygame.draw.polygon(screen, GREY, left_turning_signal)
            #    pygame.draw.polygon(screen, BLACK, left_turning_signal,  1)

            #    # right turning signal
            #    right_turning_signal = [
            #        self.world.getDrawable(pos + light_front - light_mid),
            #        self.world.getDrawable(pos + light_front - light_outer),
            #        self.world.getDrawable(pos + light_back  - light_outer),
            #        self.world.getDrawable(pos + light_back  - light_mid),
            #    ]

            #    if self.next_turn == RIGHT and turning_signal_on:
            #        pygame.draw.polygon(screen, AMBER, right_turning_signal)
            #    else:
            #        pygame.draw.polygon(screen, GREY, right_turning_signal)
            #    pygame.draw.polygon(screen, BLACK, right_turning_signal, 1)

        #stop_dist = getStopDistance(self.speed)
        #point = self.world.getDrawable(self.rear + forward * stop_dist)
        #pygame.draw.circle(screen, DARKER[car_colour], point,  3)

        #point = self.world.getDrawable(self.rear + forward * (stop_dist-2))
        #pygame.draw.circle(screen, DARKER[car_colour], point,  3)

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

    #def drawPath(self):
    #    if len(self.path) > 1:
    #        colour = LIGHTER[self.colour]
    #        path = [self.world.getDrawable(point) for point in self.path]
    #        pygame.draw.lines(self.world.screen, colour, False, path, 3)


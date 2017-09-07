from util import *

#TODO - gravitational approach to steering

ESTIMATED_ANGLE  = ANGLE_45
ESTIMATED_RADIUS = SCREEN_UNIT * 6 / math.sin(ESTIMATED_ANGLE.value)# 12 #17 // 2

WAYPOINT_BIG_GAP   = ESTIMATED_RADIUS * 5#SCREEN_UNIT * 36
WAYPOINT_INTERVAL  = ESTIMATED_RADIUS * 4#SCREEN_UNIT * 24
WAYPOINT_THRESHOLD = SCREEN_UNIT * 5

SCREEN_MARGIN = SCREEN_UNIT * 5

W_MIN_X = SCREEN_MARGIN
W_MIN_Y = SCREEN_MARGIN
W_MAX_X = SCREEN_WIDTH  - SCREEN_MARGIN
W_MAX_Y = SCREEN_HEIGHT - SCREEN_MARGIN

SLOW_SPEED = 10 * PIXELS_PER_METRE

MAX_WAYPOINTS      = 100
STARTING_WAYPOINTS = 3

class CarController:
    def __init__(self, name, screen, colour):
        self.name   = name
        self.screen = screen
        self.colour = colour

        self.position  = None # pixels
        self.car_angle = None # radians
        self.speed     = None # pixels per second

        self.projected_position = None # pixels
        self.projected_angle    = None # radians
        self.projected_speed    = None # pixels per second

        self.time = None # miliseconds

        self.waypoints = deque()
        self.points    = 0

        self.start_time = 0
        self.duration   = 0.0

    def addWaypoint(self, pos, angle):
        self.waypoints.append((pos, angle))

    def addVeryRandomWaypoint(self):
        if self.waypoints:
            prev_pos, prev_angle = self.waypoints[-1]
        else:
            prev_pos   = self.position
            prev_angle = self.car_angle

        x = random.randint(W_MIN_X, W_MAX_X)
        y = random.randint(W_MIN_Y, W_MAX_Y)

        pos   = Vector(x, y)
        angle, magnitude = getPolar(pos - prev_pos)

        self.addWaypoint(pos, angle)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev_pos, prev_angle = self.waypoints[-1]
        else:
            prev_pos   = self.position
            prev_angle = self.car_angle

        angle = prev_angle - ANGLE_30 + ANGLE_60 * random.random()
        displacement = getVector(angle) * WAYPOINT_INTERVAL
        pos = prev_pos + displacement

        count = 0

        while not ((W_MIN_X <= pos.x <= W_MAX_X) and (W_MIN_Y <= pos.y <= W_MAX_Y)):
            if count < 5:
                angle = prev_angle - ANGLE_30 + ANGLE_60 * random.random()
                displacement = getVector(angle) * WAYPOINT_INTERVAL
                pos = prev_pos + displacement
            elif count < 100:
                angle = Angle(random.random()*2*math.pi)
                displacement = getVector(angle) * WAYPOINT_BIG_GAP
                pos = prev_pos + displacement
            else:
                pos = CENTRE_POSITION
                angle, magnitude = getPolar(pos - prev_pos)

            count += 1

        self.addWaypoint(pos, angle)

    def firstUpdate(self, position, car_angle, time):
        self.position     = position
        self.car_angle    = car_angle
        self.speed        = 0
        self.time         = time

        self.start_time = time

        # generate initial waypoints
        for i in range(STARTING_WAYPOINTS):
            self.addRandomWaypoint()

    def update(self, position, car_angle, time):
        dt   = (time - self.time) / 1000

        angle, position_change = getPolar(position - self.position)
        speed = position_change / dt

        speed_change = speed - self.speed
        acceleration = speed_change / dt

        angle_change     = car_angle - self.car_angle
        angular_velocity = angle_change / dt

        self.position  = position
        self.car_angle = car_angle
        self.speed     = speed
        self.time      = time

        self.projected_speed = self.speed     + acceleration * dt
        self.projected_angle = self.car_angle + angular_velocity * dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.position + displacement

    def getTurningCircle(self, direction):
        if direction == LEFT:
            centre_vector = getVector(self.car_angle - ANGLE_90) * ESTIMATED_RADIUS
        else:
            centre_vector = getVector(self.car_angle + ANGLE_90) * ESTIMATED_RADIUS
        circle_centre = self.position + centre_vector
        return circle_centre, ESTIMATED_RADIUS

    def control(self):
        engine_control   = 0
        steering_control = CENTRE
        braking_control  = None

        while self.waypoints:
            destination, angle = self.waypoints[0]

            now_angle, now_magnitude = getPolar(destination - self.position)
            if now_magnitude < WAYPOINT_THRESHOLD:

                if self.points + len(self.waypoints) < MAX_WAYPOINTS:
                    self.addRandomWaypoint()

                self.waypoints.popleft()
                self.points += 1
                self.duration = (self.time - self.start_time) / 1000

                if self.points == MAX_WAYPOINTS:
                    print(self.name, self.duration)

                continue

            if self.projected_speed > SLOW_SPEED:
                engine_control -= 1

            elif self.projected_speed < SLOW_SPEED:
                engine_control  = 1

            # seek mouse (temporary)
            #destination = Vector(*pygame.mouse.get_pos())

            angle, magnitude = getPolar(destination - self.projected_position)
            angle_difference = self.projected_angle - angle

            focus_angle = Angle(math.atan(WAYPOINT_THRESHOLD/4/now_magnitude))

            if angle_difference > ANGLE_0: # left turn

                # test if point is too close
                circle_centre, radius = self.getTurningCircle(LEFT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = RIGHT

                elif angle_difference > focus_angle:
                    steering_control = LEFT

            elif angle_difference < ANGLE_0: # right turn

                # test if point is too close
                circle_centre, radius = self.getTurningCircle(RIGHT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = LEFT

                elif angle_difference < -focus_angle:
                    steering_control = RIGHT

            braking_control = False
            break

        else:
            # no more waypoints
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control

    def draw(self):
        colour         = self.colour
        darker_colour  = DARKER[colour]
        lighter_colour = LIGHTER[colour]

        prev = self.position
        for waypoint in self.waypoints:
            pos, angle = waypoint
            pygame.draw.line(self.screen, darker_colour, pos.coords(), prev.coords(), 1)
            prev = pos

        for waypoint in self.waypoints:
            pos, angle = waypoint

            centre = pos.coords()
            pygame.draw.circle(self.screen, colour,         centre, WAYPOINT_OUTER)
            pygame.draw.circle(self.screen, lighter_colour, centre, WAYPOINT_INNER)
            pygame.draw.circle(self.screen, darker_colour,  centre, WAYPOINT_OUTER, 1)
            pygame.draw.circle(self.screen, darker_colour,  centre, WAYPOINT_INNER, 1)

            front = pos + getVector(angle)             * WAYPOINT_INNER
            right = pos + getVector(angle + ANGLE_120) * WAYPOINT_INNER
            left  = pos + getVector(angle - ANGLE_120) * WAYPOINT_INNER

            arrow = [pos.coords(),   right.coords(),
                     front.coords(), left.coords()]
            pygame.draw.polygon(self.screen, colour, arrow)
            pygame.draw.polygon(self.screen, darker_colour, arrow, 1)

        #circle_centre, radius = self.getTurningCircle(LEFT)
        #pygame.draw.circle(self.screen, DARK_GREY, circle_centre.coords(), radius, 1)

        #circle_centre, radius = self.getTurningCircle(RIGHT)
        #pygame.draw.circle(self.screen, DARK_GREY, circle_centre.coords(), radius, 1)

    def drawCar(self):
        pos = self.position

        forward = getVector(self.car_angle)
        left    = forward.left90()

        # draw car
        car_front = forward * SCREEN_CAR_LENGTH / 2
        car_left  = left   * SCREEN_CAR_WIDTH / 2

        chassis = [(pos + car_front + car_left).coords(),
                   (pos + car_front - car_left).coords(),
                   (pos - car_front - car_left).coords(),
                   (pos - car_front + car_left).coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen, BLACK, chassis, 2)

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


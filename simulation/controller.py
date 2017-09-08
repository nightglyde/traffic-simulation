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

class Waypoint:
    def __init__(self, position, angle):
        self.position = position
        self.angle = angle

def ccw(a, b, c):
    return (b.x-a.x) * (c.y-a.y) - (b.y-a.y) * (c.x-a.x)

class CarController:
    def __init__(self, name, screen, colour):
        self.name   = name
        self.screen = screen
        self.colour = colour

        self.position = None # pixels
        self.angle    = None # radians
        self.speed    = None # pixels per second

        self.projected_position = None # pixels
        self.projected_angle    = None # radians
        self.projected_speed    = None # pixels per second

        self.time = None # miliseconds

        self.stopped = False

        self.hull = []

        self.waypoints = deque()
        self.points    = 0

        self.start_time = 0
        self.duration   = 0.0

    def addWaypoint(self, pos, angle):
        self.waypoints.append(Waypoint(pos, angle))

    def addVeryRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        x = random.randint(W_MIN_X, W_MAX_X)
        y = random.randint(W_MIN_Y, W_MAX_Y)
        pos = Vector(x, y)

        angle, magnitude = getPolar(pos - prev.position)

        self.addWaypoint(pos, angle)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        angle = prev.angle - ANGLE_30 + ANGLE_60 * random.random()
        displacement = getVector(prev.angle) * WAYPOINT_INTERVAL
        pos = prev.position + displacement

        count = 0

        while not ((W_MIN_X <= pos.x <= W_MAX_X) and (W_MIN_Y <= pos.y <= W_MAX_Y)):
            if count < 5:
                angle = prev.angle - ANGLE_30 + ANGLE_60 * random.random()
                displacement = getVector(angle) * WAYPOINT_INTERVAL
                pos = prev.position + displacement
            elif count < 100:
                angle = Angle(random.random()*2*math.pi)
                displacement = getVector(angle) * WAYPOINT_BIG_GAP
                pos = prev.position + displacement
            else:
                pos = CENTRE_POSITION
                angle, magnitude = getPolar(pos - prev.position)

            count += 1

        self.addWaypoint(pos, angle)

    def generateHull(self):
        pos = self.position

        forward = getVector(self.angle)
        left    = forward.left90()

        # draw car
        car_front = forward * SCREEN_CAR_LENGTH / 2
        car_left  = left   * SCREEN_CAR_WIDTH / 2

        self.hull = [pos + car_front + car_left,
                     pos - car_front + car_left,
                     pos - car_front - car_left,
                     pos + car_front - car_left]

    def checkCollision(self, other):
        num_points_self  = len(self.hull)
        num_points_other = len(self.hull)

        for i in range(num_points_self):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % num_points_self]

            for point_j in other.hull:
                if ccw(point_i, point_j, point_k) >= 0:
                    break

            else:
                return False

        for i in range(num_points_other):
            point_i = other.hull[i]
            point_k = other.hull[(i+1) % num_points_other]

            for point_j in self.hull:
                if ccw(point_i, point_j, point_k) >= 0:
                    break

            else:
                return False

        return True

    def stop(self):
        if not self.stopped:
            self.stopped = True
            print(self.name, "STOPPED")
            self.waypoints.clear()

    def firstUpdate(self, position, angle, time):
        self.position = position
        self.angle    = angle
        self.speed    = 0
        self.time     = time

        self.start_time = time

        # generate initial waypoints
        for i in range(STARTING_WAYPOINTS):
            self.addRandomWaypoint()

        self.generateHull()

    def update(self, position, angle, time):
        dt   = (time - self.time) / 1000

        angle, position_change = getPolar(position - self.position)
        speed = position_change / dt

        speed_change = speed - self.speed
        acceleration = speed_change / dt

        angle_change     = angle - self.angle
        angular_velocity = angle_change / dt

        self.position = position
        self.angle    = angle
        self.speed    = speed
        self.time     = time

        self.projected_speed = self.speed + acceleration * dt
        self.projected_angle = self.angle + angular_velocity * dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.position + displacement

        self.generateHull()

    def getTurningCircle(self, direction):
        if direction == LEFT:
            centre_vector = getVector(self.angle - ANGLE_90) * ESTIMATED_RADIUS
        else:
            centre_vector = getVector(self.angle + ANGLE_90) * ESTIMATED_RADIUS
        circle_centre = self.position + centre_vector
        return circle_centre, ESTIMATED_RADIUS

    def control(self):
        engine_control   = 0
        steering_control = CENTRE
        braking_control  = None

        if self.stopped:
            return engine_control, steering_control, braking_control

        while self.waypoints:
            waypoint    = self.waypoints[0]
            destination = waypoint.position

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
            pos = waypoint.position
            pygame.draw.line(self.screen, darker_colour, pos.coords(), prev.coords(), 1)
            prev = pos

        for waypoint in self.waypoints:
            pos   = waypoint.position
            angle = waypoint.angle

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
        # draw car
        chassis = [point.coords() for point in self.hull]
        if self.stopped:
            pygame.draw.polygon(self.screen, DARKER[self.colour], chassis)
        else:
            pygame.draw.polygon(self.screen, self.colour, chassis)

        pygame.draw.polygon(self.screen, BLACK, chassis, 2)

        # draw arrow
        forward = getVector(self.angle)
        left    = forward.left90()

        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [(self.position              + stem_left).coords(),
                 (self.position + stem_front + stem_left).coords(),
                 (self.position + stem_front + head_left).coords(),
                 (self.position + head_front            ).coords(),
                 (self.position + stem_front - head_left).coords(),
                 (self.position + stem_front - stem_left).coords(),
                 (self.position              - stem_left).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)


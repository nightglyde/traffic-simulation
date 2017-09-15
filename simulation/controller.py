from util import *

ESTIMATED_ANGLE  = ANGLE_45
ESTIMATED_RADIUS = AXLE_LENGTH / math.sin(ESTIMATED_ANGLE.value)

WAYPOINT_BIG_GAP   = ESTIMATED_RADIUS * 5
WAYPOINT_INTERVAL  = ESTIMATED_RADIUS * 4

DESIRED_SPEED = 10

MAX_WAYPOINTS      = 100
STARTING_WAYPOINTS = 10

class Waypoint:
    def __init__(self, position, angle):
        self.position = position
        self.angle    = angle
        self.time     = None

class CarController:
    def __init__(self, name, colour, screen, zoom):
        self.name   = name
        self.colour = colour
        self.screen = screen
        self.zoom   = zoom

        self.position = None # pixels
        self.angle    = None # radians
        self.speed    = None # pixels per second

        self.projected_position = None # pixels
        self.projected_angle    = None # radians
        self.projected_speed    = None # pixels per second

        self.time       = 0 # miliseconds
        self.start_time = 0
        self.pause_time = 0

        self.stopped = False

        self.hull = []

        self.waypoints = deque()
        self.points    = 0

        self.duration = 0.0

    def pause(self, time):
        self.pause_time = time

    def unpause(self, time):
        time_paused = time - self.pause_time

        self.time       += time_paused
        self.start_time += time_paused

    def addWaypoint(self, pos, angle):
        self.waypoints.append(Waypoint(pos, angle))

    def addVeryRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        pos, angle = generateRandomWorldPosition(prev.position)

        if self.waypoints:
            diff = angle - prev.angle
            prev.angle += diff / 2

        self.addWaypoint(pos, angle)

    def addRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
            angle = prev.angle - ANGLE_30 + ANGLE_60 * random.random()
        else:
            prev = self
            angle = self.angle

        displacement = getVector(angle) * WAYPOINT_INTERVAL
        pos = prev.position + displacement

        while not checkWaypointBoundary(pos):
            angle = Angle(random.random()*2*math.pi)
            displacement = getVector(angle) * WAYPOINT_BIG_GAP
            pos = prev.position + displacement

        if self.waypoints:
            diff = angle - prev.angle
            prev.angle += diff / 2

        self.addWaypoint(pos, angle)

    def generateHull(self):
        pos = self.position

        forward = getVector(self.angle)
        left    = forward.left90()

        car_front = forward * CAR_LENGTH / 2
        car_left  = left    * CAR_WIDTH  / 2

        self.hull = [pos + car_front + car_left,
                     pos - car_front + car_left,
                     pos - car_front - car_left,
                     pos + car_front - car_left]

    def stop(self):
        self.stopped = True
        self.waypoints.clear()

    def checkCollision(self, other):
        num_points_self  = len(self.hull)
        num_points_other = len(self.hull)

        for i in range(num_points_self):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % num_points_self]

            for point_j in other.hull:
                if ccw(point_i, point_j, point_k) <= 0:
                    break
            else:
                return False

        for i in range(num_points_other):
            point_i = other.hull[i]
            point_k = other.hull[(i+1) % num_points_other]

            for point_j in self.hull:
                if ccw(point_i, point_j, point_k) <= 0:
                    break
            else:
                return False

        if not self.stopped:
            print(self.name, "crashed into", other.name)

        elif not other.stopped:
            print(other.name, "crashed into", self.name)

        self.stop()
        other.stop()
        return True

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

    def getTurningCircle(self, direction, position, angle):
        if direction == LEFT:
            centre_vector = getVector(angle - ANGLE_90) * ESTIMATED_RADIUS
        else:
            centre_vector = getVector(angle + ANGLE_90) * ESTIMATED_RADIUS
        circle_centre = position + centre_vector
        return circle_centre

    def control(self):
        engine_control   = 0
        steering_control = CENTRE
        braking_control  = None

        if self.stopped:
            return engine_control, steering_control, braking_control

        while self.waypoints:
            waypoint    = self.waypoints[0]
            destination = waypoint.position
            dest_angle  = waypoint.angle

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

            if self.projected_speed > DESIRED_SPEED:
                engine_control -= 1

            elif self.projected_speed < DESIRED_SPEED:
                engine_control  = 1

            angle, magnitude = getPolar(destination - self.projected_position)
            angle_difference = angle - self.projected_angle
            if angle_difference < ANGLE_0: # left turn

                # test if point is too close
                circle_centre = self.getTurningCircle(LEFT, self.position, self.angle)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < ESTIMATED_RADIUS - WAYPOINT_THRESHOLD:
                    steering_control = RIGHT

                else:
                    steering_control = LEFT

            elif angle_difference > ANGLE_0: # right turn

                # test if point is too close
                circle_centre = self.getTurningCircle(RIGHT, self.position, self.angle)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < ESTIMATED_RADIUS - WAYPOINT_THRESHOLD:
                    steering_control = LEFT

                else:
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

        prev = self.zoom.getDrawable(self.position)
        for waypoint in self.waypoints:
            pos = self.zoom.getDrawable(waypoint.position)
            pygame.draw.line(self.screen, darker_colour, pos, prev, 1)
            prev = pos

        for waypoint in self.waypoints:
            pos   = waypoint.position
            angle = waypoint.angle

            centre = self.zoom.getDrawable(pos)
            inner_radius = self.zoom.scaleDistance(WAYPOINT_INNER)
            outer_radius = self.zoom.scaleDistance(WAYPOINT_OUTER)

            pygame.draw.circle(self.screen, colour,         centre, outer_radius)
            pygame.draw.circle(self.screen, lighter_colour, centre, inner_radius)
            pygame.draw.circle(self.screen, darker_colour,  centre, outer_radius, 1)
            pygame.draw.circle(self.screen, darker_colour,  centre, inner_radius, 1)

            front = pos + getVector(angle)             * WAYPOINT_INNER
            right = pos + getVector(angle + ANGLE_120) * WAYPOINT_INNER
            left  = pos + getVector(angle - ANGLE_120) * WAYPOINT_INNER

            arrow = [centre,
                self.zoom.getDrawable(right),
                self.zoom.getDrawable(front),
                self.zoom.getDrawable(left)
            ]
            pygame.draw.polygon(self.screen, colour, arrow)
            pygame.draw.polygon(self.screen, darker_colour, arrow, 1)

    def drawCar(self):
        # draw car
        chassis = [self.zoom.getDrawable(point) for point in self.hull]
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

        arrow = [
            self.zoom.getDrawable(self.position              + stem_left),
            self.zoom.getDrawable(self.position + stem_front + stem_left),
            self.zoom.getDrawable(self.position + stem_front + head_left),
            self.zoom.getDrawable(self.position + head_front            ),
            self.zoom.getDrawable(self.position + stem_front - head_left),
            self.zoom.getDrawable(self.position + stem_front - stem_left),
            self.zoom.getDrawable(self.position              - stem_left)
        ]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)


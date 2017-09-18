from util import *

DESIRED_SPEED = 10

PATH_HISTORY = 500
GREY_HISTORY = 3

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

        self.dt = 0

        self.time          = 0 # miliseconds
        self.start_time    = 0
        self.waypoint_time = 0
        self.pause_time    = 0

        self.stopped = False

        self.hull = []

        self.waypoints = deque()
        self.points    = 0

        self.duration = 0.0

        self.path       = deque()
        self.greypoints = deque()

    def pause(self, time):
        self.pause_time = time

    def unpause(self, time):
        time_paused = time - self.pause_time

        self.time          += time_paused
        self.waypoint_time += time_paused
        self.start_time    += time_paused

    def getTurningCircle(self, direction, position, angle):
        if direction == LEFT:
            centre_vector = getVector(angle - ANGLE_90) * TURN_RADIUS
        else:
            centre_vector = getVector(angle + ANGLE_90) * TURN_RADIUS
        circle_centre = position + centre_vector
        return circle_centre

    def plotTurn(self, car_pos, car_angle, destination):
        turn_distances = []

        left_circle = self.getTurningCircle(LEFT, car_pos, car_angle)
        left_angle, left_dist = getPolar(destination - left_circle)
        left_car = car_pos - left_circle

        right_circle = self.getTurningCircle(RIGHT, car_pos, car_angle)
        right_angle, right_dist = getPolar(destination - right_circle)
        right_car = car_pos - right_circle

        # plot left turn
        if left_dist >= TURN_RADIUS:
            tan_dist  = math.sqrt(left_dist**2 - TURN_RADIUS**2)
            tan_angle = left_angle - Angle(math.asin(TURN_RADIUS / left_dist))

            left_tan = getVector(tan_angle+ANGLE_90) * TURN_RADIUS

            arc_dist   = leftTurn(left_car, left_tan) * TURN_RADIUS
            total_dist = tan_dist + arc_dist

            arcs = [(left_circle, getAngle(left_car), getAngle(left_tan))]
            tans = [(left_circle + left_tan, destination)]

            turn_distances.append((total_dist, tan_angle, LEFT, arcs, tans))

        else:
            # right turn then left turn
            ratio = right_dist/(2*TURN_RADIUS) - 3*TURN_RADIUS/(2*right_dist)
            angle = right_angle - Angle(math.acos(ratio)) - ANGLE_90
            extra_circle = self.getTurningCircle(LEFT, destination, angle)

            right_extra = extra_circle - right_circle
            extra_right = right_circle - extra_circle
            extra_dest  = destination  - extra_circle

            arc_a = rightTurn(right_car,  right_extra) * TURN_RADIUS
            arc_b = leftTurn(extra_right, extra_dest)  * TURN_RADIUS
            total_dist = arc_a + arc_b

            arcs = [(right_circle, getAngle(right_extra), getAngle(right_car)),
                    (extra_circle, getAngle(extra_right), getAngle(extra_dest))]
            tans = []

            turn_distances.append((total_dist, angle, RIGHT, arcs, tans))

        # plot right turn
        if right_dist >= TURN_RADIUS:
            tan_dist  = math.sqrt(right_dist**2 - TURN_RADIUS**2)
            tan_angle = right_angle + Angle(math.asin(TURN_RADIUS / right_dist))

            right_tan = getVector(tan_angle-ANGLE_90) * TURN_RADIUS

            arc_dist = rightTurn(right_car, right_tan) * TURN_RADIUS
            total_dist = tan_dist + arc_dist

            arcs = [(right_circle, getAngle(right_tan), getAngle(right_car))]
            tans = [(right_circle + right_tan, destination)]

            turn_distances.append((total_dist, tan_angle, RIGHT, arcs, tans))

        else:
            # left turn then right turn
            ratio = left_dist/(2*TURN_RADIUS) - 3*TURN_RADIUS/(2*left_dist)
            angle = left_angle + Angle(math.acos(ratio)) + ANGLE_90
            extra_circle = self.getTurningCircle(RIGHT, destination, angle)

            left_extra = extra_circle - left_circle
            extra_left = left_circle  - extra_circle
            extra_dest = destination  - extra_circle

            arc_a = leftTurn(left_car,    left_extra) * TURN_RADIUS
            arc_b = rightTurn(extra_left, extra_dest) * TURN_RADIUS
            total_dist = arc_a + arc_b

            arcs = [(left_circle,  getAngle(left_car),   getAngle(left_extra)),
                    (extra_circle, getAngle(extra_dest), getAngle(extra_left))]
            tans = []

            turn_distances.append((total_dist, angle, LEFT, arcs, tans))

        turn_distances.sort()
        return turn_distances[0]

    def adjustWaypoints(self):
        prev = self
        for waypoint in self.waypoints:
            distance, angle, turn, arcs, tans = self.plotTurn(prev.position,
                                                              prev.angle,
                                                              waypoint.position)

            time = distance / DESIRED_SPEED
            waypoint.update(angle, time, turn, arcs, tans)

            prev = waypoint

    def addWaypoint(self, pos):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        distance, angle, turn, arcs, tans = self.plotTurn(prev.position,
                                                          prev.angle, pos)

        time = distance / DESIRED_SPEED
        self.waypoints.append(Waypoint(pos, angle, time, turn, arcs, tans))

    def addRandomWaypoint(self):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self

        angle = prev.angle - ANGLE_30 + ANGLE_60 * random.random()
        pos   = prev.position + getVector(angle) * WAYPOINT_INTERVAL

        while not checkWaypointBoundary(pos):
            angle = Angle(random.random()*2*math.pi)
            pos   = prev.position + getVector(angle) * WAYPOINT_BIG_GAP

        self.addWaypoint(pos)

    def firstUpdate(self, position, angle, time):
        self.position = position
        self.angle    = angle
        self.speed    = 0
        self.time     = time

        self.start_time    = time
        self.waypoint_time = time

        # generate initial waypoints
        for i in range(STARTING_WAYPOINTS):
            #self.addRandomWaypoint()
            self.addWaypoint(generateRandomWaypointPosition())

        self.generateHull()
        self.path.append(self.position)

    def update(self, position, angle, time):
        if self.stopped:
            return

        self.dt = (time - self.time) / 1000

        angle, position_change = getPolar(position - self.position)
        speed = position_change / self.dt

        speed_change = speed - self.speed
        acceleration = speed_change / self.dt

        angle_change     = angle - self.angle
        angular_velocity = angle_change / self.dt

        self.position = position
        self.angle    = angle
        self.speed    = speed
        self.time     = time

        self.projected_speed = self.speed + acceleration * self.dt
        self.projected_angle = self.angle + angular_velocity * self.dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.position + displacement

        self.generateHull()
        self.path.append(self.position)

        if len(self.path) > PATH_HISTORY:
            self.path.popleft()

    def control(self):
        engine_control   = 0
        steering_control = CENTRE
        braking_control  = None

        if self.stopped:
            return engine_control, steering_control, braking_control

        while self.waypoints:
            waypoint = self.waypoints[0]

            angle, distance = getPolar(waypoint.position - self.position)
            if distance <= WAYPOINT_THRESHOLD:

                if self.points + len(self.waypoints) < MAX_WAYPOINTS:
                    #self.addRandomWaypoint()
                    self.addWaypoint(generateRandomWaypointPosition())

                self.greypoints.append(waypoint)

                if len(self.greypoints) > GREY_HISTORY:
                    self.greypoints.popleft()

                self.waypoints.popleft()
                self.adjustWaypoints()

                self.points += 1
                self.duration = (self.time - self.start_time) / 1000

                if self.points == MAX_WAYPOINTS:
                    print(self.name, "finished at time", self.duration)

                duration = (self.time - self.waypoint_time) / 1000
                print("{} {} e_time: {:.4}, a_time: {:.4}".format(
                      self.name, self.points,
                      waypoint.time, duration))
                self.waypoint_time = self.time

                continue

            distance, angle, turn, arcs, tans = self.plotTurn(self.position,
                                                              self.angle,
                                                              waypoint.position)

            steering_control = sign(turn)

            if self.projected_speed > DESIRED_SPEED:
                engine_control -= 1

            elif self.projected_speed < DESIRED_SPEED:
                engine_control  = 1

            braking_control = False
            break

        else:
            # no more waypoints
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control

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

    def stop(self, other):
        if not self.stopped:
            self.stopped = True
            self.waypoints.clear()
            self.duration = (self.time - self.start_time) / 1000

            print(self.name, "crashed into", other.name,
                  "at time", self.duration)

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

        return True

    def draw(self):
        colour         = self.colour
        darker_colour  = DARKER[colour]
        lighter_colour = LIGHTER[colour]

        thres_radius = self.zoom.scaleDistance(WAYPOINT_THRESHOLD)
        inner_radius = self.zoom.scaleDistance(WAYPOINT_INNER)
        outer_radius = self.zoom.scaleDistance(WAYPOINT_OUTER)

        path = [self.zoom.getDrawable(point) for point in self.path]
        pygame.draw.lines(self.screen, LIGHT_GREY, False, path, 1)

        for waypoint in self.greypoints:
            for circle_centre, angle_1, angle_2 in waypoint.arcs:
                rect = generateRect(circle_centre, TURN_RADIUS, self.zoom)
                angle_1 = angle_1.norm()
                angle_2 = angle_2.norm()
                pygame.draw.arc(self.screen, GREY,
                                rect, angle_1, angle_2, 1)

            for point_1, point_2 in waypoint.tans:
                point_1 = self.zoom.getDrawable(point_1)
                point_2 = self.zoom.getDrawable(point_2)
                pygame.draw.line(self.screen, GREY,
                                 point_1, point_2, 1)

        for waypoint in self.waypoints:
            for circle_centre, angle_1, angle_2 in waypoint.arcs:
                rect = generateRect(circle_centre, TURN_RADIUS, self.zoom)
                angle_1 = angle_1.norm()
                angle_2 = angle_2.norm()
                pygame.draw.arc(self.screen, darker_colour,
                                rect, angle_1, angle_2, 1)

            for point_1, point_2 in waypoint.tans:
                point_1 = self.zoom.getDrawable(point_1)
                point_2 = self.zoom.getDrawable(point_2)
                pygame.draw.line(self.screen, darker_colour,
                                 point_1, point_2, 1)

        for waypoint in self.greypoints:
            pos   = waypoint.position
            angle = waypoint.angle

            centre = self.zoom.getDrawable(pos)
            pygame.draw.circle(self.screen, DARK_GREY, centre, thres_radius, 1)
            pygame.draw.circle(self.screen, DARK_GREY, centre, outer_radius, 1)

            front = pos + getVector(angle)             * WAYPOINT_INNER
            right = pos + getVector(angle + ANGLE_120) * WAYPOINT_INNER
            left  = pos + getVector(angle - ANGLE_120) * WAYPOINT_INNER

            arrow = [centre,
                self.zoom.getDrawable(right),
                self.zoom.getDrawable(front),
                self.zoom.getDrawable(left)
            ]
            pygame.draw.polygon(self.screen, DARK_GREY, arrow, 1)

        for waypoint in self.waypoints:
            pos   = waypoint.position
            angle = waypoint.angle

            centre = self.zoom.getDrawable(pos)
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


from util import *

from obstacle import Obstacle
from waypoint import Waypoint
from car import Car

WAYPOINT_RADIUS    = ROAD_WIDTH / 2
WAYPOINT_THRESHOLD = 0.5

MAX_WAYPOINTS   = 2
TOTAL_WAYPOINTS = 1000

DESIRED_SPEED = 10

PATH_MEMORY = 300

class CarController(Obstacle):
    def __init__(self, car):
        self.car    = car
        self.world  = car.world
        self.name   = car.name
        self.colour = car.colour

        self.waypoints     = deque()
        self.score         = 0
        self.waypoint_time = None
        self.limited_mode  = False

        self.destination = None
        self.red_lines   = []
        self.options     = []

        self.path = deque()
        self.path.append(self.car.position)

        self.car_side_paths = [deque() for i in range(6)]
        self.updateCarSidePaths()

    def updateCarSidePaths(self):
        car_left = getVector(self.car.angle).left90() * CAR_WIDTH/2

        front_left = self.car.hull[1]
        pivot_left = self.car.position + car_left
        rear_left  = self.car.hull[2]

        front_right = self.car.hull[0]
        pivot_right = self.car.position - car_left
        rear_right  = self.car.hull[3]

        self.car_side_paths[0].append(front_left)
        self.car_side_paths[1].append(pivot_left)
        self.car_side_paths[2].append(rear_left)

        self.car_side_paths[3].append(front_right)
        self.car_side_paths[4].append(pivot_right)
        self.car_side_paths[5].append(rear_right)

        if len(self.car_side_paths[0]) > PATH_MEMORY:
            for path in self.car_side_paths:
                path.popleft()

    def clearWaypoints(self):
        self.waypoints.clear()
        self.waypoint_time = self.car.time

    def addWaypoint(self, waypoint):
        if self.waypoints:
            car = self.waypoints[-1].car
        else:
            car = self.car

        sim_car    = car.copy()
        start_time = sim_car.time

        path = []
        time = start_time

        time_step   = 1000 // FRAMES_PER_SECOND
        destination = waypoint.position

        # simulate car driving to next waypoint
        for i in range(1000):
            if i % 20 == 0:
                path.append(sim_car.position)

            distance = getMagnitude(destination - sim_car.centre)
            if distance <= WAYPOINT_THRESHOLD:
                break

            self.control(sim_car, waypoint)

            time += time_step
            sim_car.update(time)

        else:
            self.limited_mode = True
            self.limited_addWaypoint(waypoint)
            return True

        path.append(sim_car.position)
        waypoint.update(time-start_time, path, sim_car)
        self.waypoints.append(waypoint)
        return True

    def limited_addWaypoint(self, waypoint):
        if self.waypoints:
            prev = self.waypoints[-1]
        else:
            prev = self.car

        angle, distance = getPolar(waypoint.position - prev.position)
        time = distance / DESIRED_SPEED * 1000
        path = [prev.position, waypoint.position]

        self.waypoints.append(waypoint)
        waypoint.limited_update(time, path, angle)

    def addRandomWaypoint(self):
        while True:
            pos      = self.world.generateRandomPosition()
            waypoint = Waypoint(self, pos, WAYPOINT_RADIUS)

            if self.world.checkObject(waypoint):
                if self.limited_mode:
                    self.limited_addWaypoint(waypoint)
                    return
                else:
                    if self.addWaypoint(waypoint):
                        return
                    #else:
                    #    self.clearWaypoints()

    def alt_addRandomWaypoint(self):
        if self.waypoints:
            waypoints = self.waypoints
        else:
            waypoints = [self.car]

        self.options = self.world.getWaypointOptions(waypoints)
        if not self.options:
            self.options = self.world.waypoint_options

        waypoint = Waypoint(self, random.choice(self.options),
                                  WAYPOINT_RADIUS)
        if self.limited_mode:
            self.limited_addWaypoint(waypoint)
        else:
            self.addWaypoint(waypoint)

    def generateWaypoints(self):
        while len(self.waypoints) < MAX_WAYPOINTS and \
              len(self.waypoints) + self.score < TOTAL_WAYPOINTS:
            self.addRandomWaypoint()

    def update(self):
        if self.car.stopped:
            return

        if self.waypoint_time is None:
            self.clearWaypoints()
            self.generateWaypoints()

        while self.waypoints:
            waypoint = self.waypoints[0]

            offset = (self.car.time - self.waypoint_time) - waypoint.time

            distance = getMagnitude(waypoint.position - self.car.centre)
            if distance <= WAYPOINT_THRESHOLD:

                self.waypoints.popleft()
                self.score += 1
                self.waypoint_time = self.car.time

                print("{} {} time offset: {}".format(
                    self.name, self.score, offset))

                if self.score == TOTAL_WAYPOINTS:
                    print(self.name, "finished at time",
                          self.waypoint_time / 1000)

            #elif offset >= 5000: # five seconds over time
            #    print("timed out!", offset)
            #    self.clearWaypoints()

            else:
                break

            self.generateWaypoints()

        self.path.append(self.car.position)
        if len(self.path) > PATH_MEMORY:
            self.path.popleft()

        self.updateCarSidePaths()

        if self.waypoints:
            self.control(self.car, self.waypoints[0])
        else:
            self.control(self.car, None)

    def control(self, car, waypoint):
        # look for nearby collisions
        total_vec = VECTOR_0
        self.red_lines = []
        for grass in self.world.grass:
            line, dist, vec = grass.findNearestLine(car.front)
            if line and dist < ROAD_WIDTH/2:
                total_vec += vec
                total_vec = vec
                self.red_lines.append(line)
                self.red_lines.append((line[0], car.front))
                self.red_lines.append((line[1], car.front))

            #line, dist, vec = grass.findNearestLine(car.position)
            #if line and dist < ROAD_WIDTH/4:
            #    total_vec += vec
            #    total_vec = vec
            #    self.red_lines.append(line)
            #    self.red_lines.append((line[0], car.position))
            #    self.red_lines.append((line[1], car.position))

        if self.red_lines:
            self.destination = car.position + getVector(getAngle(total_vec)) * 4

            angle = getAngle(self.destination - car.position)
            angle_difference = angle - car.angle
            #if angle_difference < ANGLE_0:
            #    car.controlAngle(-MAX_WHEEL_ANGLE)
            #else:
            #    car.controlAngle(MAX_WHEEL_ANGLE)
            car.controlAngle(angle_difference)

            car.controlSpeed(DESIRED_SPEED, False)

        elif waypoint:
            self.destination = waypoint.position

            # adjust wheel angle using destination point
            angle, magnitude = getPolar(self.destination - car.position)
            angle_difference = angle - car.angle

            #if abs(angle_difference.value) < ANGLE_1.value:
            #    car.controlAngle(ANGLE_0)

            #if angle_difference < ANGLE_0: # left turn
                # test if point is too close
                #centre = getTurningCircle(LEFT, car)
                #dist_from_centre = getMagnitude(self.destination - centre)
                #if dist_from_centre < TURN_RADIUS - WAYPOINT_THRESHOLD:
                #    car.controlAngle(ANGLE_90)#MAX_WHEEL_ANGLE)
                #else:
                    #car.controlAngle(-MAX_WHEEL_ANGLE)
                #    car.controlAngle(angle_difference)

            #elif angle_difference > ANGLE_0: # right turn
                # test if point is too close
                #centre = getTurningCircle(RIGHT, car)
                #dist_from_centre = getMagnitude(self.destination - centre)
                #if dist_from_centre < TURN_RADIUS - WAYPOINT_THRESHOLD:
                #    car.controlAngle(-ANGLE_90)#-MAX_WHEEL_ANGLE)
                #else:
                    #car.controlAngle(MAX_WHEEL_ANGLE)
                #    car.controlAngle(angle_difference)

            car.controlAngle(angle_difference)

            car.controlSpeed(DESIRED_SPEED, False)

        else:
            car.controlAngle(ANGLE_0)
            car.controlSpeed(0, False)
            self.destination = car.position

    def drawPath(self):
        #if len(self.path) > 1:
        #    path = [self.world.getDrawable(point) for point in self.path]
        #    pygame.draw.lines(self.world.screen, GREY, False, path, 1)

        colours = [MAGENTA, RED,  YELLOW,
                   GREEN,   CYAN, BLUE]

        if len(self.car_side_paths[0]) > 1:
            for i in range(6):
                colour = colours[i]
                path = self.car_side_paths[i]
                path = [self.world.getDrawable(point) for point in path]
                pygame.draw.lines(self.world.screen, colour, False, path, 1)

    def drawWaypoints(self):
        for waypoint in self.waypoints:
            waypoint.drawPath()

        for waypoint in self.waypoints:
            waypoint.draw()

        for point_1, point_2 in self.red_lines:
            point_1 = self.world.getDrawable(point_1)
            point_2 = self.world.getDrawable(point_2)
            pygame.draw.line(self.world.screen, self.colour, point_1, point_2, 3)

        thres = self.world.scaleDistance(WAYPOINT_THRESHOLD)
        for option in self.options:
            point = self.world.getDrawable(option)
            pygame.draw.circle(self.world.screen, self.colour, point, thres, 1)

        dest = self.world.getDrawable(self.destination)
        pygame.draw.circle(self.world.screen, BLACK, dest, thres, 1)

        #pos = self.world.getDrawable(self.car.position)
        #pygame.draw.line(self.world.screen, self.colour, pos, dest, 1)


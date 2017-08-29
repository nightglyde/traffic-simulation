import math
import pygame
import time
import random

from collections import deque

# define some basic colours in RGB
BLACK      = (  0,   0,   0)
DARK_GREY  = ( 63,  63,  63)
GREY       = (127, 127, 127)
LIGHT_GREY = (191, 191, 191)
WHITE      = (255, 255, 255)
RED        = (255,   0,   0)
YELLOW     = (255, 255,   0)
GREEN      = (  0, 255,   0)
CYAN       = (  0, 255, 255)
BLUE       = (  0,   0, 255)
MAGENTA    = (255,   0, 255)

# physics constants
DRAG_CONSTANT    = 0.5
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

# conversion
SCREEN_UNIT = 10
WORLD_UNIT  = 0.45
PIXELS_PER_METRE = SCREEN_UNIT / WORLD_UNIT

# screen dimensions
SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800

SCREEN_CAR_LENGTH  = SCREEN_UNIT * 10 # 100
SCREEN_CAR_WIDTH   = SCREEN_UNIT * 4  # 40
SCREEN_AXLE_LENGTH = SCREEN_UNIT * 6  # 60
SCREEN_AXLE_WIDTH  = SCREEN_UNIT * 3  # 30

ARROW_LENGTH      = SCREEN_UNIT * 4 # 40
ARROW_WIDTH       = SCREEN_UNIT * 2 # 20
ARROW_STEM_LENGTH = SCREEN_UNIT * 3 # 30
ARROW_STEM_WIDTH  = SCREEN_UNIT * 1 # 10

# world dimensions
WORLD_WIDTH  = SCREEN_WIDTH  / PIXELS_PER_METRE
WORLD_HEIGHT = SCREEN_HEIGHT / PIXELS_PER_METRE

CAR_LENGTH  = WORLD_UNIT * 10 # 4.5
CAR_WIDTH   = WORLD_UNIT * 4  # 1.8
AXLE_LENGTH = WORLD_UNIT * 6  # 2.7

CENTRE_TO_FRONT  = WORLD_UNIT * 4   # 1.8
CENTRE_TO_REAR   = WORLD_UNIT * 2   # 0.9
CENTRE_TO_GROUND = WORLD_UNIT * 1.5 # 0.675

CAR_MASS   = 1250
CAR_WEIGHT = CAR_MASS * GRAVITY_CONSTANT

STATIC_FRONT_WEIGHT = (CENTRE_TO_FRONT  / AXLE_LENGTH) * CAR_WEIGHT
STATIC_REAR_WEIGHT  = (CENTRE_TO_REAR   / AXLE_LENGTH) * CAR_WEIGHT
HLM                 = (CENTRE_TO_GROUND / AXLE_LENGTH) * CAR_MASS

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right90(self):
        return Vector(-self.y, self.x)

    def coords(self):
        return [round(self.x), round(self.y)]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __repr__(self):
        return repr([self.x, self.y])

def getVector(angle):
    return Vector(math.cos(angle.value), math.sin(angle.value))

CENTRE_POSITION = Vector(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
VECTOR_0        = Vector(0, 0)

class Angle:
    def __init__(self, value):

        if value > math.pi:
            value -= math.pi*2

        elif value < -math.pi:
            value += math.pi*2

        self.value = value

    def __add__(self, other):
        return Angle(self.value + other.value)

    def __sub__(self, other):
        return Angle(self.value - other.value)

    def __mul__(self, scalar):
        return Angle(self.value * scalar)

    def __truediv__(self, scalar):
        return Angle(self.value / scalar)

    def __floordiv__(self, scalar):
        return Angle(self.value // scalar)

    def __neg__(self):
        return Angle(-self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return repr(math.degrees(self.value))

def getPolar(vector):
    x = vector.x
    y = vector.y

    magnitude = math.sqrt(x**2 + y**2)

    if x == 0:
        angle = math.pi / 2
    else:
        angle = math.atan(y / x)

    if x < 0:
        angle += math.pi

    return Angle(angle), magnitude

ANGLE_0   = Angle(0)
ANGLE_15  = Angle(math.pi/12)
ANGLE_30  = Angle(math.pi/6)
ANGLE_45  = Angle(math.pi/4)
ANGLE_60  = Angle(math.pi/3)
ANGLE_90  = Angle(math.pi/2)
ANGLE_120 = Angle(math.pi*2/3)

def generateRandomWorldPosition():
    x = random.random() * WORLD_WIDTH
    y = random.random() * WORLD_HEIGHT
    pos = Vector(x, y)
    angle = Angle(random.random()*2*math.pi)
    return pos, angle

MAX_ANGLE   = ANGLE_45
LOWER_LIMIT = -MAX_ANGLE
UPPER_LIMIT = MAX_ANGLE

STEERING_RATE_2 = 4
STEERING_RATE_1 = 1

class Car:
    def __init__(self, name, position, car_angle=ANGLE_0):
        self.name = name

        self.position     = position                  # metres
        self.car_angle    = car_angle                 # radians
        self.heading      = getVector(self.car_angle) # unit vector
        self.velocity     = VECTOR_0                  # metres per second
        self.wheel_angle  = ANGLE_0                   # radians
        self.engine_force = MIN_ENGINE_FORCE          # newtons
        self.braking      = False

        self.control_time = pygame.time.get_ticks()
        self.update_time  = pygame.time.get_ticks()

    def update(self):
        curr_time        = pygame.time.get_ticks()
        dt               = (curr_time - self.update_time) / 1000
        self.update_time = curr_time

        angle, speed = getPolar(self.velocity)

        # turning corners
        if self.wheel_angle.value != ANGLE_0.value:
            radius    = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            angular_v = speed / radius

            self.car_angle += Angle(angular_v * dt)
            self.heading    = getVector(self.car_angle)

        # driving forwards
        if not self.braking:
            self.velocity = self.heading * speed

            traction           = self.heading  * min(self.engine_force, CAR_WEIGHT)
            drag               = self.velocity * speed * (-DRAG_CONSTANT)
            rolling_resistance = self.velocity         * (-RR_CONSTANT)

            acceleration = (traction + drag + rolling_resistance) / CAR_MASS

        # braking
        elif speed > 0.05:
            self.velocity = self.heading * speed

            brakes             = self.heading  * (-min(BRAKING_CONSTANT, CAR_WEIGHT))
            drag               = self.velocity * speed * (-DRAG_CONSTANT)
            rolling_resistance = self.velocity         * (-RR_CONSTANT)

            acceleration = (brakes + drag + rolling_resistance) / CAR_MASS

        else:
            acceleration  = VECTOR_0
            self.velocity = VECTOR_0

        self.velocity += acceleration  * dt
        self.position += self.velocity * dt

        return self.position, self.car_angle

    def control(self, engine_control, steering_control, braking_control):
        curr_time         = pygame.time.get_ticks()
        dt                = (curr_time - self.control_time) / 1000
        self.control_time = curr_time

        # adjust engine force
        engine_change  = 10000 * dt

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)

        # adjust wheel angle
        large_angle_change = Angle(2*math.pi * dt * STEERING_RATE_2)
        small_angle_change = Angle(2*math.pi * dt * STEERING_RATE_1)

        if steering_control > 0:
            if self.wheel_angle > ANGLE_0:
                self.wheel_angle = min(self.wheel_angle+small_angle_change, UPPER_LIMIT)
            else:
                self.wheel_angle = min(self.wheel_angle+large_angle_change, UPPER_LIMIT)

        elif steering_control < 0:
            if self.wheel_angle < ANGLE_0:
                self.wheel_angle = max(self.wheel_angle-small_angle_change, LOWER_LIMIT)
            else:
                self.wheel_angle = max(self.wheel_angle-large_angle_change, LOWER_LIMIT)

        # toggle brakes
        if braking_control:
            self.braking = True
        else:
            self.braking = False

ESTIMATED_LOWER_LIMIT = LOWER_LIMIT
ESTIMATED_UPPER_LIMIT = UPPER_LIMIT
CONTROL_ANGLE         = ANGLE_15

SLOW_SPEED = 10 * PIXELS_PER_METRE

WAYPOINT_INTERVAL  = SCREEN_UNIT * 17 # 100
WAYPOINT_RADIUS    = SCREEN_UNIT * 5  # 50
WAYPOINT_THRESHOLD = SCREEN_UNIT * 1  # 10

W_MIN_X = WAYPOINT_RADIUS
W_MIN_Y = WAYPOINT_RADIUS
W_MAX_X = SCREEN_WIDTH  - WAYPOINT_RADIUS - 1
W_MAX_Y = SCREEN_HEIGHT - WAYPOINT_RADIUS - 1

TOTAL_WAYPOINTS    = 10
STARTING_WAYPOINTS = 3

def generateRandomScreenPosition():
    x = random.randint(W_MIN_X, W_MAX_X)
    y = random.randint(W_MIN_Y, W_MAX_Y)
    a = Angle(random.random()*2*math.pi)
    return Vector(x, y), a

def generateNextPosition(prev_pos, prev_angle):
    angle = prev_angle - ANGLE_15 + ANGLE_30 * random.random()
    displacement = getVector(angle) * WAYPOINT_INTERVAL
    pos = prev_pos + displacement

    while not ((W_MIN_X <= pos.x <= W_MAX_X) and (W_MIN_Y <= pos.y <= W_MAX_Y)):
        angle = Angle(random.random()*2*math.pi)
        displacement = getVector(angle) * WAYPOINT_INTERVAL * 1.5
        pos = prev_pos + displacement

    return pos, angle

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

    def firstUpdate(self, position, car_angle):
        self.position     = position
        self.car_angle    = car_angle
        self.speed        = 0
        self.time         = pygame.time.get_ticks()

        self.start_time = self.time

    def update(self, position, car_angle):
        time = pygame.time.get_ticks()
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

    def plotAngle(self, angle):
        radius = SCREEN_AXLE_LENGTH / math.sin(angle.value)

        centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        circle_centre = self.position + centre_vector

        return circle_centre, radius

    def control(self):
        engine_control   = 0
        steering_control = 0
        braking_control  = None

        while self.waypoints:
            destination, w_angle = self.waypoints[0]

            angle, magnitude = getPolar(destination - self.position)
            if magnitude < WAYPOINT_THRESHOLD:

                if self.points + len(self.waypoints) < TOTAL_WAYPOINTS:
                    pos, w_angle = self.waypoints[-1]
                    self.addWaypoint(*generateNextPosition(pos, w_angle))

                self.waypoints.popleft()
                self.points += 1
                self.duration = (self.time - self.start_time) / 1000
                continue

            if self.projected_speed > SLOW_SPEED:
                engine_control -= 1

            elif self.projected_speed < SLOW_SPEED:
                engine_control  = 1

            angle, magnitude = getPolar(destination - self.projected_position)
            angle_difference = self.projected_angle - angle

            if angle_difference > ANGLE_0: # left turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(ESTIMATED_LOWER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = 1

                else:
                    steering_control = -1

            elif angle_difference < ANGLE_0: # right turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(ESTIMATED_UPPER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = -1

                else:
                    steering_control = 1

            braking_control = False
            break

        else:
            # no more waypoints
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control

    def drawBackground(self):
        prev = self.position
        full_length = True
        for waypoint in self.waypoints:
            pos, angle = waypoint
            pygame.draw.circle(self.screen, self.colour, pos.coords(), WAYPOINT_RADIUS, 2)
            front = pos + getVector(angle)             * WAYPOINT_RADIUS
            right = pos + getVector(angle + ANGLE_120) * WAYPOINT_RADIUS
            left  = pos + getVector(angle - ANGLE_120) * WAYPOINT_RADIUS

            arrow = [pos.coords(),  right.coords(), front.coords(),
                     left.coords(), pos.coords()]
            pygame.draw.polygon(self.screen, self.colour, arrow, 1)

            angle_to_pos,  magnitude = getPolar(pos - prev)
            angle_to_prev, magnitude = getPolar(prev - pos)

            to_prev = pos  + getVector(angle_to_prev) * WAYPOINT_RADIUS

            if full_length:
                to_pos  = prev
            else:
                to_pos  = prev + getVector(angle_to_pos)  * WAYPOINT_RADIUS

            pygame.draw.line(self.screen, self.colour, to_pos.coords(), to_prev.coords(), 1)
            prev = pos
            full_length = False


    def drawCar(self):
        heading  = getVector(self.car_angle)

        # draw car
        forward = heading * SCREEN_CAR_LENGTH / 2
        right   = heading.right90() * SCREEN_CAR_WIDTH / 2

        self.front = self.position + forward
        self.rear  = self.position - forward

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.rear_left   = self.rear  - right
        self.rear_right  = self.rear  + right

        chassis = [self.front_left.coords(), self.front_right.coords(),
                   self.rear_right.coords(), self.rear_left.coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        # draw arrow
        forward = heading
        right   = heading.right90()

        stem_front = forward * ARROW_STEM_LENGTH
        stem_right = right   * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_right = right   * ARROW_WIDTH / 2

        arrow = [(self.position              - stem_right).coords(),
                 (self.position + stem_front - stem_right).coords(),
                 (self.position + stem_front - head_right).coords(),
                 (self.position + head_front             ).coords(),
                 (self.position + stem_front + head_right).coords(),
                 (self.position + stem_front + stem_right).coords(),
                 (self.position              + stem_right).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

INCLUDE_CAPTION = True

CAR_COLOURS = {"RED": RED,  "YEL": YELLOW, "GRN": GREEN,
               "CYA": CYAN, "BLU": BLUE,   "MAG": MAGENTA}
MAX_CARS = 1

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    if INCLUDE_CAPTION:

        # generating fps
        prev_time = pygame.time.get_ticks()
        frames = [0 for f in range(10)]
        f = 0
        fps = 0
        pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

    # create cars
    num_cars = 0
    cars = []
    controllers = []
    for colour_name in CAR_COLOURS:

        pos, angle = generateRandomWorldPosition()
        car = Car(colour_name, pos, angle)
        cars.append(car)

        prev_pos   = pos * PIXELS_PER_METRE
        prev_angle = angle

        controller = CarController(colour_name, screen, CAR_COLOURS[colour_name])
        for i in range(STARTING_WAYPOINTS):
            pos, angle = generateNextPosition(prev_pos, prev_angle)
            controller.addWaypoint(pos, angle)
            prev_pos   = pos
            prev_angle = angle
        controllers.append(controller)

        num_cars += 1
        if num_cars == MAX_CARS:
            break

    # update car models
    updates = []
    for i in range(num_cars):
        position, car_angle = cars[i].update()
        position *= PIXELS_PER_METRE
        updates.append((position, car_angle))

    # send first update to controllers
    for i in range(num_cars):
        controllers[i].firstUpdate(*updates[i])

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the frames per second
        clock.tick(60)

        if INCLUDE_CAPTION:
            # find time between frames
            curr_time = pygame.time.get_ticks()
            dt = (curr_time - prev_time) / 1000
            prev_time = curr_time

            frames[f] = dt
            f += 1
            if f == 10:
                f = 0

            # calculate fps
            total = 0.0
            for frame in frames:
                total += frame
            fps = round(10/total)

            # get car points
            pairs = []
            for controller in controllers:
                pairs.append((-controller.points, controller.duration, controller.name))
            pairs.sort()

            # generate screen caption
            string = "Car Simulator | FPS: {}".format(fps)
            for points, duration, name in pairs:
                string += " | {:3} {:3}".format(name, -points)
            pygame.display.set_caption(string)

        # deal with events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

        # provide controllers with updated information
        updates = []
        for i in range(num_cars):
            position, car_angle = cars[i].update()
            position *= PIXELS_PER_METRE
            updates.append((position, car_angle))

        for i in range(num_cars):
            controllers[i].update(*updates[i])

        # send controller instructions to cars
        controls = []
        for i in range(num_cars):
            engine_control, steering_control, braking_control = controllers[i].control()
            controls.append((engine_control, steering_control, braking_control))

        for i in range(num_cars):
            cars[i].control(*controls[i])

        # draw to screen
        screen.fill(WHITE)

        for controller in controllers:
            controller.drawBackground()

        for controller in controllers:
            controller.drawCar()

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


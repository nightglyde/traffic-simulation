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

# screen dimensions
SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800

SCREEN_CAR_LENGTH  = 100
SCREEN_CAR_WIDTH   = 40
SCREEN_AXLE_LENGTH = 60
SCREEN_AXLE_WIDTH  = 30

ARROW_LENGTH      = 40
ARROW_WIDTH       = 20
ARROW_STEM_LENGTH = 30
ARROW_STEM_WIDTH  = 10

WAYPOINT_RADIUS    = 50
WAYPOINT_THRESHOLD = 5

# world dimensions
PIXELS_PER_METRE = 100 / 4.5

WORLD_WIDTH  = SCREEN_WIDTH  / PIXELS_PER_METRE
WORLD_HEIGHT = SCREEN_HEIGHT / PIXELS_PER_METRE

CAR_LENGTH  = 4.5
CAR_WIDTH   = 1.8
AXLE_LENGTH = 2.7

CENTRE_TO_FRONT   = 1.8
CENTRE_TO_REAR    = 0.9
CENTRE_TO_GROUND  = 0.7

CAR_MASS          = 1250
CAR_WEIGHT        = CAR_MASS * GRAVITY_CONSTANT

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

ANGLE_0  = Angle(0)
ANGLE_15 = Angle(math.pi/12)
ANGLE_30 = Angle(math.pi/6)
ANGLE_45 = Angle(math.pi/4)
ANGLE_60 = Angle(math.pi/3)
ANGLE_90 = Angle(math.pi/2)

MAX_ANGLE     = ANGLE_45
CONTROL_ANGLE = ANGLE_15

LOWER_LIMIT = -MAX_ANGLE
UPPER_LIMIT = MAX_ANGLE
ZERO_ANGLE  = ANGLE_0

STEERING_RATE_2 = 4
STEERING_RATE_1 = 1
SLOW_SPEED    = 10# * PIXELS_PER_METRE

def generateRandomWorldPosition():
    x = random.random() * WORLD_WIDTH
    y = random.random() * WORLD_HEIGHT
    return (x, y)

def generateRandomScreenPosition():
    x = random.randint(WAYPOINT_RADIUS, SCREEN_WIDTH-WAYPOINT_RADIUS-1)
    y = random.randint(WAYPOINT_RADIUS, SCREEN_HEIGHT-WAYPOINT_RADIUS-1)
    return (x, y)

class Car:
    def __init__(self, name, screen, position, car_angle=0, speed=0):
        self.name   = name
        self.screen = screen

        self.position     = Vector(*position)         # metres
        self.speed        = speed                     # metres per second
        self.car_angle    = Angle(car_angle)          # radians
        self.wheel_angle  = ZERO_ANGLE                # radians
        self.heading      = getVector(self.car_angle) # unit vector
        self.engine_force = MIN_ENGINE_FORCE
        self.braking      = False

        self.control_time = pygame.time.get_ticks()
        self.update_time  = pygame.time.get_ticks()

    def update(self):
        curr_time        = pygame.time.get_ticks()
        dt               = (curr_time - self.update_time) / 1000
        self.update_time = curr_time

        # turning corners
        if self.wheel_angle.value != ZERO_ANGLE.value:
            radius    = AXLE_LENGTH / math.sin(self.wheel_angle.value)
            angular_v = self.speed / radius

            self.car_angle += Angle(angular_v * dt)
            self.heading    = getVector(self.car_angle)

        # driving forwards
        velocity = self.heading * self.speed

        if not self.braking:
            traction = self.heading * min(self.engine_force, CAR_WEIGHT)
        elif self.speed > 0:
            traction = self.heading * (-min(BRAKING_CONSTANT, CAR_WEIGHT))
        else:
            traction = Vector(0, 0)

        drag               = velocity * self.speed * (-DRAG_CONSTANT)
        rolling_resistance = velocity              * (-RR_CONSTANT)
        acceleration       = (traction + drag + rolling_resistance) / CAR_MASS

        velocity      += acceleration * dt
        self.position += velocity     * dt

        angle, speed = getPolar(velocity)
        self.speed   = speed

        return self.position, self.car_angle

    def control(self, engine_control, steering_control, braking_control):
        curr_time         = pygame.time.get_ticks()
        dt                = (curr_time - self.control_time) / 1000
        self.control_time = curr_time

        engine_change      = 10000 * dt
        large_angle_change = Angle(2*math.pi * dt * STEERING_RATE_2)
        small_angle_change = Angle(2*math.pi * dt * STEERING_RATE_1)

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)
        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)

        if steering_control > 0:
            if self.wheel_angle > ZERO_ANGLE:
                self.wheel_angle = min(self.wheel_angle+small_angle_change, UPPER_LIMIT)
            else:
                self.wheel_angle = min(self.wheel_angle+large_angle_change, UPPER_LIMIT)
        elif steering_control < 0:
            if self.wheel_angle < ZERO_ANGLE:
                self.wheel_angle = max(self.wheel_angle-small_angle_change, LOWER_LIMIT)
            else:
                self.wheel_angle = max(self.wheel_angle-large_angle_change, LOWER_LIMIT)

        if braking_control:
            self.braking = True
        else:
            self.braking = False

    def plotAngle(self, angle):
        radius = AXLE_LENGTH / math.sin(angle.value)

        centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        circle_centre = self.position + centre_vector

        return circle_centre, radius

    def drawTurningCircle(self):
        if abs(self.wheel_angle.value) > 0.0001:
            circle_centre, radius = self.plotAngle(self.wheel_angle)
            circle_centre = (circle_centre * PIXELS_PER_METRE).coords()
            radius        = abs(round(radius * PIXELS_PER_METRE))
            if radius < 2000:
                pygame.draw.circle(self.screen, GREY, circle_centre, radius, 1)
        else:
            print(self.wheel_angle)

class CarController:
    def __init__(self, name, screen, colour):
        self.name   = name
        self.screen = screen
        self.colour = colour

        # car position and movement
        self.position     = None # metres
        self.car_angle    = None # radians
        self.speed        = None # metres per second
        self.acceleration = None # metres per second per second
        self.time         = None # miliseconds

        self.screen_position = None # pixels

        # control
        self.instructions = deque()

        # this bit is for drawing the path of the car on-screen
        self.path = deque()

    def addInstruction(self, pos):
        self.instructions.append(pos)

    def firstUpdate(self, position, car_angle):
        self.position     = position
        self.car_angle    = car_angle
        self.speed        = 0
        self.acceleration = 0
        self.time         = pygame.time.get_ticks()

        self.screen_position = self.position * PIXELS_PER_METRE

    def update(self, position, car_angle):
        time = pygame.time.get_ticks()
        dt   = (time - self.time) / 1000

        angle, position_change = getPolar(position - self.position)
        speed = position_change / dt

        speed_change = speed - self.speed
        acceleration = speed_change / dt

        angle_change     = car_angle - self.car_angle
        angular_velocity = angle_change / dt

        self.position     = position
        self.car_angle    = car_angle
        self.angular_v    = angular_velocity
        self.speed        = speed
        self.acceleration = acceleration
        self.time         = time

        self.screen_position = self.position * PIXELS_PER_METRE

        self.projected_speed = self.speed     + self.acceleration * dt
        self.projected_angle = self.car_angle + self.angular_v * dt

        average_speed = (self.speed + self.projected_speed) / 2
        displacement  = getVector(self.projected_angle) * average_speed

        self.projected_position = self.screen_position + displacement / PIXELS_PER_METRE

    def plotAngle(self, angle):
        radius = SCREEN_AXLE_LENGTH / math.sin(angle.value)

        centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        circle_centre = self.screen_position + centre_vector

        return circle_centre, radius

    def control(self):
        engine_control   = 0
        steering_control = 0
        braking_control  = None

        while self.instructions:
            destination = Vector(*self.instructions[0])
            angle, magnitude = getPolar(destination - self.projected_position)

            if magnitude < WAYPOINT_THRESHOLD:
                self.instructions.popleft()
                self.addInstruction(generateRandomScreenPosition())
                continue

            if self.projected_speed > SLOW_SPEED:
                engine_control -= 1

            elif self.projected_speed < SLOW_SPEED:
                engine_control  = 1

            angle_difference   = self.projected_angle - angle

            #fine_control_angle = Angle(math.atan(WAYPOINT_THRESHOLD/magnitude))

            if angle_difference > ZERO_ANGLE: # left turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(LOWER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = 1

                else:
                    steering_control = -1

            elif angle_difference < ZERO_ANGLE: # right turn

                # test if point is too close
                circle_centre, radius = self.plotAngle(UPPER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    steering_control = -1

                else:
                    steering_control = 1

            braking_control = False
            break

        else:
            # no instructions to follow
            engine_control   = -1
            steering_control = 0
            braking_control  = True

        return engine_control, steering_control, braking_control

    def drawBackground(self):
        self.path.append(self.screen_position.coords())
        if len(self.path) > 1:

            if len(self.path) > 2000:
                self.path.popleft()

            pygame.draw.lines(self.screen, self.colour, False, self.path, 1)#LIGHT_GREY, False, self.path, 1)

        # draw course
        prev = self.screen_position.coords()
        for instruction in self.instructions:
            pygame.draw.circle(self.screen, self.colour, instruction, WAYPOINT_RADIUS, 5)
            prev = instruction

        #circle_centre, radius = self.plotAngle(LOWER_LIMIT)
        #circle_centre = (circle_centre).coords()
        #radius        = abs(round(radius))
        #if radius < 5000:
        #    pygame.draw.circle(self.screen, DARK_GREY, circle_centre, radius, 1)

        #circle_centre, radius = self.plotAngle(UPPER_LIMIT)
        #circle_centre = (circle_centre).coords()
        #radius        = abs(round(radius))
        #if radius < 5000:
        #    pygame.draw.circle(self.screen, DARK_GREY, circle_centre, radius, 1)

    def drawCar(self):
        heading  = getVector(self.car_angle)

        # draw car
        forward = heading * SCREEN_CAR_LENGTH // 2
        right   = heading.right90() * SCREEN_CAR_WIDTH // 2

        self.front = self.screen_position + forward
        self.rear  = self.screen_position - forward

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
        stem_right = right   * ARROW_STEM_WIDTH // 2
        head_front = forward * ARROW_LENGTH
        head_right = right   * ARROW_WIDTH // 2

        arrow = [(self.screen_position              - stem_right).coords(),
                 (self.screen_position + stem_front - stem_right).coords(),
                 (self.screen_position + stem_front - head_right).coords(),
                 (self.screen_position + head_front             ).coords(),
                 (self.screen_position + stem_front + head_right).coords(),
                 (self.screen_position + stem_front + stem_right).coords(),
                 (self.screen_position              + stem_right).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    fps = 0
    pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

    # create car
    colours = { "Red": RED,  "Yellow": YELLOW,   "Green": GREEN,
               "Cyan": CYAN,   "Blue": BLUE,   "Magenta": MAGENTA}

    #colours = {"Red": RED, "Green": GREEN, "Blue": BLUE}

    #colours = {"Blue": BLUE}

    num_cars = 0
    cars = []
    controllers = []
    for colour_name in colours:
        num_cars += 1

        x, y = generateRandomWorldPosition()
        a = random.random()*math.pi*2
        car = Car(colour_name, screen, (x, y), a)
        cars.append(car)

        controller = CarController(colour_name, screen, colours[colour_name])
        for i in range(1):
            controller.addInstruction(generateRandomScreenPosition())
        controllers.append(controller)

    # update car models
    updates = []
    for i in range(num_cars):
        position, car_angle = cars[i].update()
        updates.append((position, car_angle))

    # send first update to controllers
    for i in range(num_cars):
        controllers[i].firstUpdate(*updates[i])

    # generating fps
    prev_time = pygame.time.get_ticks()
    frames = [0 for i in range(10)]
    f = 0

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the frames per second
        clock.tick(60)

        # find time between frames
        curr_time = pygame.time.get_ticks()
        dt = (curr_time - prev_time) / 1000
        prev_time = curr_time

        frames[f] = dt
        f += 1
        if f == 10:
            f = 0

            total = 0.0
            for frame in frames:
                total += frame

            fps = round(10/total)

            pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

        # deal with events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

        # update car models
        updates = []
        for i in range(num_cars):
            position, car_angle = cars[i].update()
            updates.append((position, car_angle))

        # updated data to controllers
        for i in range(num_cars):
            controllers[i].update(*updates[i])

        # get controller instructions
        controls = []
        for i in range(num_cars):
            engine_control, steering_control, braking_control = controllers[i].control()
            controls.append((engine_control, steering_control, braking_control))

        # send controller instructions to cars
        for i in range(num_cars):
            cars[i].control(*controls[i])

        # draw background
        screen.fill(WHITE)

        for controller in controllers:
            controller.drawBackground()

        # draw cars
        for controller in controllers:
            controller.drawCar()

        # draw turning circles
        #for car in cars:
        #    car.drawTurningCircle()

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


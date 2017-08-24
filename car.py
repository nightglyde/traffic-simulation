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

WIDTH  = 1200
HEIGHT = 800

WAYPOINT_RADIUS    = 30
WAYPOINT_THRESHOLD = 10

CAR_LENGTH  = 100
CAR_WIDTH   = 40
AXLE_LENGTH = 60
AXLE_WIDTH  = 30

ARROW_LENGTH      = 40
ARROW_WIDTH       = 20
ARROW_STEM_LENGTH = 30
ARROW_STEM_WIDTH  = 10

DRAG_CONSTANT    = 0.5
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

PIXELS_PER_METRE = CAR_LENGTH / 4.5

SLOW_SPEED = 10

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

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

    def __neg__(self):
        return Angle(-self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return repr(math.degrees(self.value))

ANGLE_0  = Angle(0)
ANGLE_15 = Angle(math.pi/12)
ANGLE_30 = Angle(math.pi/6)
ANGLE_45 = Angle(math.pi/4)
ANGLE_60 = Angle(math.pi/3)
ANGLE_90 = Angle(math.pi/2)

LOWER_LIMIT = -ANGLE_45
UPPER_LIMIT = ANGLE_45
ZERO_ANGLE  = ANGLE_0

def getVector(angle):
    return Vector(math.cos(angle.value), math.sin(angle.value))

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

class Car:
    def __init__(self, name, screen, colour, position, car_angle=0, speed=0):

        self.name   = name
        self.screen = screen
        self.colour = colour

        self.position     = Vector(*position)
        self.speed        = speed
        self.car_angle    = Angle(car_angle)
        self.wheel_angle  = Angle(0)
        self.heading      = getVector(self.car_angle)
        self.engine_force = MIN_ENGINE_FORCE

        self.braking       = False
        self.radius        = None
        self.circle_centre = None

        # honda civic
        self.mass       = 1250
        self.weight     = self.mass * GRAVITY_CONSTANT
        self.wheel_base = 2.7

        #centre_to_front  = 1.8
        #centre_to_rear   = 0.9
        #centre_to_ground = 0.7

        #self.front_weight_static = (centre_to_front /wheel_base) * self.weight
        #self.rear_weight_static  = (centre_to_rear  /wheel_base) * self.weight
        #self.hLM                 = (centre_to_ground/wheel_base) * self.mass

        self.updateShape()

        # course plotting
        self.instructions = deque()
        self.path_end     = self.front

    def updateShape(self):
        # car shape
        forward = self.heading * CAR_LENGTH // 2
        right = self.heading.right90() * CAR_WIDTH // 2

        self.front = self.position + forward
        self.rear  = self.position - forward

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.rear_left   = self.rear  - right
        self.rear_right  = self.rear  + right

        axle_forward = self.heading * AXLE_LENGTH // 2

        self.front_axle = self.position + axle_forward
        self.rear_axle  = self.position - axle_forward

        self.front_left_wheel  = self.front_axle - right
        self.front_right_wheel = self.front_axle + right
        self.rear_left_wheel   = self.rear_axle  - right
        self.rear_right_wheel  = self.rear_axle  + right

    def addInstruction(self, pos):
        self.instructions.append(pos)
        self.path_end = Vector(*pos)

    def plotAngle(self, angle):
        radius    = self.wheel_base / math.sin(angle.value)
        angular_v = self.speed / radius # radians per second

        radius_adjusted = radius * PIXELS_PER_METRE

        angle_to_centre = self.car_angle + angle + ANGLE_90
        centre_vector   = getVector(angle_to_centre) * radius_adjusted

        if angular_v < 0:
            circle_centre = self.front_left_wheel + centre_vector
        else:
            circle_centre = self.front_right_wheel + centre_vector

        angle, magnitude = getPolar(self.position - circle_centre)

        return angular_v, circle_centre, magnitude

    def control(self, dt):
        angle_change  = Angle(math.pi * dt)
        engine_change = 10000 * dt

        while self.instructions:
            # follow instructions
            destination = Vector(*self.instructions[0])
            angle, magnitude = getPolar(destination - self.position)

            if magnitude < WAYPOINT_THRESHOLD:
                self.instructions.popleft()

                x = random.randint(WAYPOINT_RADIUS, WIDTH-WAYPOINT_RADIUS-1)
                y = random.randint(WAYPOINT_RADIUS, HEIGHT-WAYPOINT_RADIUS-1)
                self.addInstruction((x, y))

                continue

            angle_difference = self.car_angle - angle

            if angle_difference > ZERO_ANGLE: # left turn
                # test if point is too close
                angular_v, circle_centre, radius = self.plotAngle(LOWER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

                elif self.wheel_angle.value >= ZERO_ANGLE.value:
                    self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

                elif abs(angle_difference.value) > ANGLE_15.value:
                    self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

                else:
                    angle, distance_from_circle = getPolar(destination - self.circle_centre)
                    diff = distance_from_circle - abs(self.radius)
                    if diff < 0:
                        self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)
                    elif diff > 0:
                        self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

            elif angle_difference < ZERO_ANGLE: # right turn
                # test if point is too close
                angular_v, circle_centre, radius = self.plotAngle(UPPER_LIMIT)
                angle, distance_from_circle = getPolar(destination - circle_centre)
                if distance_from_circle < abs(radius):
                    self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

                elif self.wheel_angle.value <= ZERO_ANGLE.value:
                    self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

                elif abs(angle_difference.value) > ANGLE_15.value:
                    self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

                else:
                    angle, distance_from_circle = getPolar(destination - self.circle_centre)
                    diff = distance_from_circle - abs(self.radius)
                    if diff < 0:
                        self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)
                    elif diff > 0:
                        self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)

            if self.speed > SLOW_SPEED:
                self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)
            elif self.speed < SLOW_SPEED:
                self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

            self.braking = False
            break

        else:
            # no instructions to follow
            self.path_end = self.front

            if self.wheel_angle > ZERO_ANGLE:
                self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)

            elif self.wheel_angle < ZERO_ANGLE:
                self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

            self.engine_force = MIN_ENGINE_FORCE
            self.braking = True

    def update(self, dt):
        # driving forwards
        velocity = self.heading * self.speed

        if not self.braking:
            traction = self.heading * min(self.engine_force, self.weight)
        elif self.speed > 0:
            traction = self.heading * (-min(BRAKING_CONSTANT, self.weight))
        else:
            traction = Vector(0, 0)

        drag               = velocity * self.speed * (-DRAG_CONSTANT)
        rolling_resistance = velocity              * (-RR_CONSTANT)
        acceleration       = (traction + drag + rolling_resistance) / self.mass

        velocity      += acceleration * dt
        self.position += velocity     * dt * PIXELS_PER_METRE

        angle, speed = getPolar(velocity)
        self.speed   = speed

        # turning corners
        if self.wheel_angle.value == ZERO_ANGLE.value:
            self.radius        = None
            self.circle_centre = None
        else:
            angular_v, circle_centre, radius = self.plotAngle(self.wheel_angle)

            self.car_angle += Angle(angular_v * dt)
            self.heading    = getVector(self.car_angle)

            self.circle_centre = circle_centre
            self.radius        = radius

        # update car shape
        self.updateShape()

    def drawBackground(self):
        # draw course
        prev = self.front.coords()
        for instruction in self.instructions:
            #pygame.draw.line(self.screen,   self.colour, prev, instruction, 1)
            pygame.draw.circle(self.screen, self.colour, instruction, WAYPOINT_RADIUS, 5)
            prev = instruction

    def drawToMouse(self, mouse):
        pygame.draw.line(self.screen, self.colour, self.path_end.coords(), mouse, 1)
        pygame.draw.circle(self.screen, self.colour, mouse, WAYPOINT_RADIUS, 2)

    def drawCar(self):
        # draw car
        chassis = [self.front_left.coords(), self.front_right.coords(),
                   self.rear_right.coords(), self.rear_left.coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        # draw arrow
        forward = self.heading
        right   = self.heading.right90()

        stem_front = forward * ARROW_STEM_LENGTH
        stem_right = right   * ARROW_STEM_WIDTH // 2
        head_front = forward * ARROW_LENGTH
        head_right = right   * ARROW_WIDTH // 2

        arrow = [(self.position              - stem_right).coords(),
                 (self.position + stem_front - stem_right).coords(),
                 (self.position + stem_front - head_right).coords(),
                 (self.position + head_front             ).coords(),
                 (self.position + stem_front + head_right).coords(),
                 (self.position + stem_front + stem_right).coords(),
                 (self.position              + stem_right).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size   = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    fps   = 0
    pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

    # create car
    colours = { "Red": RED,  "Yellow": YELLOW,   "Green": GREEN,
               "Cyan": CYAN,   "Blue": BLUE,   "Magenta": MAGENTA}

    #colours = {"Red": RED, "Green": GREEN, "Blue": BLUE}

    #colours = {"Blue": BLUE}

    cars = []
    for colour_name in colours:
        x = random.randint(CAR_LENGTH, WIDTH-CAR_LENGTH-1)
        y = random.randint(CAR_LENGTH, HEIGHT-CAR_LENGTH-1)
        a = random.random()*math.pi*2
        car = Car(colour_name, screen, colours[colour_name], (x, y), a)

        for i in range(1):
            x = random.randint(WAYPOINT_RADIUS, WIDTH-WAYPOINT_RADIUS-1)
            y = random.randint(WAYPOINT_RADIUS, HEIGHT-WAYPOINT_RADIUS-1)
            car.addInstruction((x, y))

        cars.append(car)

    prev_time = pygame.time.get_ticks()

    frames = [0 for i in range(10)]
    i = 0

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the frames per second
        clock.tick(60)

        # find time between frames
        curr_time = pygame.time.get_ticks()
        dt = (curr_time - prev_time) / 1000
        prev_time = curr_time

        frames[i] = dt
        i += 1
        if i == 10:
            i = 0

        total = 0.0
        for frame in frames:
            total += frame

        fps = round(10/total)

        pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

        # find closest car to mouse
        #mouse = pygame.mouse.get_pos()

        #closest_car = None
        #closest_mag = None
        #for car in cars:
        #    angle, magnitude = getPolar(car.path_end - Vector(*mouse))
        #    if closest_mag == None or closest_mag > magnitude:
        #        closest_car = car
        #        closest_mag = magnitude

        # deal with events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    closest_car.addInstruction(mouse)

        # update cars
        for car in cars:
            car.update(dt)
            car.control(dt)

        # draw background
        screen.fill(WHITE)

        for car in cars:
            car.drawBackground()

        #closest_car.drawToMouse(mouse)

        # draw cars
        for car in cars:
            car.drawCar()

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


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

WIDTH    = 1200
HEIGHT   = 800
WAYPOINT_RADIUS = 20

# actual length and width will be twice this number
CAR_LENGTH = 50
CAR_WIDTH  = 20

ARROW_STEM_LENGTH = 30
ARROW_STEM_WIDTH  = 5
ARROW_HEAD_LENGTH = 10
ARROW_HEAD_WIDTH  = 10

MIN_SPEED = 0
MAX_SPEED = 300

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right90(self):
        return Vector(-self.y, self.x)

    def coords(self):
        return [self.x, self.y]

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

LOWER_LIMIT = Angle(-math.pi/4)
UPPER_LIMIT = Angle(math.pi/4)
ZERO_ANGLE  = Angle(0)

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
    #elif y < 0:
    #    angle += math.pi * 2

    return Angle(angle), magnitude

class Car:
    def __init__(self, screen, colour, position, car_angle=0,
                 speed=MIN_SPEED, wheel_angle=0):

        self.screen = screen
        self.colour = colour

        self.position     = Vector(*position)
        self.speed        = speed
        self.car_angle    = Angle(car_angle)
        self.wheel_angle  = Angle(wheel_angle)
        self.heading      = getVector(self.car_angle)

        self.target       = None
        self.instructions = deque()
        #self.path         = []


        self.time = pygame.time.get_ticks()

    def addInstruction(self, pos):
        instruction = Vector(*pos)
        self.instructions.append(instruction.coords())

    def update(self, target=None):
        # update position and velocity
        time = pygame.time.get_ticks()
        dt = (time - self.time) / 1000
        self.time = time

        self.position += self.heading * self.speed * dt

        self.car_angle += self.wheel_angle * dt
        self.heading    = getVector(self.car_angle)

        angle_change = Angle(math.pi / 2 * dt)
        speed_change = 20 * dt

        if target:
            self.target = target
        else:
            self.target = None

        # follow instructions
        while self.instructions:
            angle, magnitude = getPolar(Vector(*self.instructions[0]) - self.position)

            if magnitude < WAYPOINT_RADIUS:
                self.instructions.popleft()
                continue

            break

        else:
            if not self.target:
                if self.wheel_angle > ZERO_ANGLE:
                    self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)

                elif self.wheel_angle < ZERO_ANGLE:
                    self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

                if self.speed > MIN_SPEED:
                    self.speed = max(self.speed-speed_change, MIN_SPEED)

                return

            angle, magnitude = getPolar(Vector(*self.target) - self.position)

        orbit_angle = Angle(math.atan(WAYPOINT_RADIUS/magnitude))
        angle_difference = self.car_angle - angle

        if abs(angle_difference.value) < orbit_angle.value:
            if self.wheel_angle > ZERO_ANGLE:
                self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)

            elif self.wheel_angle < ZERO_ANGLE:
                self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

            if self.speed < MAX_SPEED:
                self.speed = min(self.speed+speed_change, MAX_SPEED)

        else:
            if angle_difference > orbit_angle:
                self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

            elif angle_difference < -orbit_angle:
                self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

            if self.speed > MIN_SPEED:
                self.speed = max(self.speed-speed_change, MIN_SPEED)

    def draw(self):
        forward = self.heading
        right   = self.heading.right90()

        front = self.position + forward * CAR_LENGTH
        back  = self.position - forward * CAR_LENGTH

        # draw path
        #self.path.append(back.coords())
        #if len(self.path) > 1:
        #    pygame.draw.lines(self.screen, LIGHT_GREY, False, self.path, 1)

        # draw course
        prev = front.coords()
        for instruction in self.instructions:
            pygame.draw.line(self.screen,   self.colour, prev, instruction, 1)
            pygame.draw.circle(self.screen, self.colour, instruction, WAYPOINT_RADIUS, 2)
            prev = instruction

        if self.target:
            pygame.draw.line(self.screen,   self.colour, prev, self.target, 1)
            pygame.draw.circle(self.screen, self.colour, self.target, WAYPOINT_RADIUS, 2)

        # draw car
        front_left  = front - right * CAR_WIDTH
        front_right = front + right * CAR_WIDTH
        back_left   = back  - right * CAR_WIDTH
        back_right  = back  + right * CAR_WIDTH

        chassis = [front_left.coords(), front_right.coords(),
                   back_right.coords(), back_left.coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        # draw arrow
        arrow_base_left  = self.position - right * ARROW_STEM_WIDTH
        arrow_base_right = self.position + right * ARROW_STEM_WIDTH

        arrow_bend_left  = arrow_base_left  + forward * ARROW_STEM_LENGTH
        arrow_bend_right = arrow_base_right + forward * ARROW_STEM_LENGTH

        arrow_point = self.position + forward * (ARROW_STEM_LENGTH + ARROW_HEAD_LENGTH)
        arrow_left  = self.position + forward * ARROW_STEM_LENGTH - right * ARROW_HEAD_WIDTH
        arrow_right = self.position + forward * ARROW_STEM_LENGTH + right * ARROW_HEAD_WIDTH

        arrow = [arrow_base_left.coords(), arrow_bend_left.coords(),
                 arrow_left.coords(), arrow_point.coords(), arrow_right.coords(),
                 arrow_bend_right.coords(), arrow_base_right.coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Here we go!")
    clock = pygame.time.Clock()

    # create car
    colours = [RED, GREEN, BLUE]#[RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    cars = []
    for colour in colours:
        cars.append(Car(screen, colour,
                        (random.randint(0, WIDTH-1),
                         random.randint(0, HEIGHT-1)),
                        random.random()*math.pi*2)
                   )

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the while loop to 10 times per second
        clock.tick(60)

        mouse = pygame.mouse.get_pos()

        closest_car = None
        closest_pos = None
        closest_mag = None
        for car in cars:
            if car.instructions:
                pos = car.instructions[-1]
            else:
                pos = car.position.coords()

            angle, magnitude = getPolar(Vector(*pos) - Vector(*mouse))

            if closest_mag != None:
                if closest_mag > magnitude:
                    closest_car = car
                    closest_pos = pos
                    closest_mag = magnitude

            else:
                closest_car = car
                closest_pos = pos
                closest_mag = magnitude

        for event in pygame.event.get():
            # user did something

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                closest_car.addInstruction(mouse)

        # clear the screen and set the screen background
        screen.fill(WHITE)

        # animate the car
        for car in cars:
            if car is closest_car:
                car.update(mouse)
            else:
                car.update()

        for car in cars:
            car.draw()

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


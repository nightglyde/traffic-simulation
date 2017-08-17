import math
import pygame
import time

from collections import deque

# define some basic colours in RGB
BLACK   = (  0,   0,   0)
GREY    = ( 63,  63,  63)
WHITE   = (255, 255, 255)
RED     = (255,   0,   0)
YELLOW  = (255, 255,   0)
GREEN   = (  0, 255,   0)
CYAN    = (  0, 255, 255)
BLUE    = (  0,   0, 255)
MAGENTA = (255,   0, 255)

WIDTH    = 1200
HEIGHT   = 800
CAR_SIZE = 100
WAYPOINT_RADIUS = 50

MIN_SPEED = 0
MAX_SPEED = 300
MIN_ACCELERATION = -100
MAX_ACCELERATION = 50

TOO_FAST = 50
TOO_SLOW = 20

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
    def __init__(self, screen, colour, position,
                 speed=0, acceleration=0, car_angle=0, wheel_angle=0):

        self.screen = screen
        self.colour = colour

        self.position     = Vector(*position)
        self.speed        = speed
        self.acceleration = acceleration
        self.car_angle    = Angle(car_angle)
        self.wheel_angle  = Angle(wheel_angle)
        self.heading      = getVector(self.car_angle)

        self.instructions = deque()
        self.plan = [self.position.coords()]
        self.path = [self.position.coords()]

        self.target_position = self.position

        self.time = pygame.time.get_ticks()

    def addInstruction(self, pos):
        instruction = Vector(*pos)
        self.instructions.appendleft(instruction)
        self.plan.append(instruction.coords())

    def update(self):
        # update position and velocity
        time = pygame.time.get_ticks()
        dt = (time - self.time) / 1000
        self.time = time

        self.position += self.heading * self.speed * dt
        self.path.append(self.position.coords())

        self.car_angle += self.wheel_angle  * dt
        self.heading    = getVector(self.car_angle)

        self.speed = max(min(self.speed + self.acceleration * dt, MAX_SPEED), MIN_SPEED)

        # follow instructions
        while self.instructions:
            self.target_position = self.instructions[-1]
            angle, magnitude = getPolar(self.target_position - self.position)

            if magnitude < WAYPOINT_RADIUS:
                print("DONE", self.position, self.target_position)
                self.instructions.pop()
                continue

            break

        else:
            self.target_position = Vector(*pygame.mouse.get_pos())
            angle, magnitude = getPolar(self.target_position - self.position)

        orbit_angle = Angle(math.atan(WAYPOINT_RADIUS/magnitude))

        angle_difference = self.car_angle - angle
        angle_change = Angle(math.pi / 2 * dt)

        if abs(angle_difference.value) < orbit_angle.value:
            if self.wheel_angle > ZERO_ANGLE:
                self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)

            elif self.wheel_angle < ZERO_ANGLE:
                self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

            if self.speed < TOO_FAST and self.acceleration < MAX_ACCELERATION:
                self.acceleration = MAX_ACCELERATION

        else:
            if angle_difference > orbit_angle:
                self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

            elif angle_difference < -orbit_angle:
                #self.car_angle += min(angle_change, -angle_difference)
                self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

            if self.speed > TOO_FAST:
                self.acceleration = MIN_ACCELERATION
            elif self.speed < TOO_SLOW:
                self.acceleration = MAX_ACCELERATION
            else:
                self.acceleration = 0

        print(self.wheel_angle, self.speed, self.acceleration)

    def draw(self):
        forward = self.heading * CAR_SIZE / 2
        right   = self.heading.right90() * CAR_SIZE / 5

        chassis_A = self.position + forward - right
        chassis_B = self.position + forward + right
        chassis_C = self.position - forward + right
        chassis_D = self.position - forward - right

        chassis = [chassis_A.coords(), chassis_B.coords(),
                   chassis_C.coords(), chassis_D.coords()]

        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        pygame.draw.lines(self.screen, RED, False, self.path, 1)

        if len(self.plan) > 1:
            pygame.draw.lines(self.screen, GREEN, False, self.plan, 1)

        pygame.draw.circle(self.screen, BLUE, self.target_position.coords(), WAYPOINT_RADIUS, 1)

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Here we go!")
    clock = pygame.time.Clock()

    # create car
    car = Car(screen, BLUE, (WIDTH//2, HEIGHT//2))

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the while loop to 10 times per second
        clock.tick(60)

        for event in pygame.event.get():
            # user did something

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                car.addInstruction(pygame.mouse.get_pos())

        # clear the screen and set the screen background
        screen.fill(WHITE)

        # animate the car
        car.update()
        car.draw() # we start from the 2nd frame, for some reason

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


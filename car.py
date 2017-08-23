import math
import pygame
import time
import random

from collections import deque

# idea: slow down as you get near a point if the next point is angled away from car
# idea: slow down as you get near a point if ther is no next point

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
WAYPOINT_RADIUS = 50

CAR_LENGTH = 100
CAR_WIDTH  = 40

PIXELS_PER_METRE = CAR_LENGTH / 4.5

ARROW_LENGTH = 40
ARROW_WIDTH  = 20
ARROW_STEM_LENGTH = 30
ARROW_STEM_WIDTH  = 10

DRAG_CONSTANT    = 0.5
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

TURNING_SPEED  = 2
STRAIGHT_SPEED = 10

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000


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
    def __init__(self, screen, colour, position, car_angle=0, velocity=(0, 0)):

        self.screen = screen
        self.colour = colour

        self.position     = Vector(*position)
        self.car_angle    = Angle(car_angle)
        self.velocity     = Vector(*velocity)

        self.wheel_angle  = Angle(0)
        self.heading      = getVector(self.car_angle)

        self.engine_force = 0
        self.braking      = False
        self.acceleration = Vector(0, 0)

        # honda civic
        self.mass   = 1250
        self.weight = self.mass * GRAVITY_CONSTANT

        wheel_base       = 2.7
        centre_to_front  = 1.8
        centre_to_rear   = 0.9
        centre_to_ground = 0.7

        self.front_weight_static = (centre_to_front /wheel_base) * self.weight
        self.rear_weight_static  = (centre_to_rear  /wheel_base) * self.weight
        self.hLM                 = (centre_to_ground/wheel_base) * self.mass

        # car shape
        front = self.heading * CAR_LENGTH // 2
        right = self.heading.right90() * CAR_WIDTH // 2

        self.front = self.position + front
        self.back  = self.position - front

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.back_left   = self.back  - right
        self.back_right  = self.back  + right

        # course plotting
        self.instructions = deque()
        self.path_end     = self.front

    def addInstruction(self, pos):
        self.instructions.append(pos)
        self.path_end = Vector(*pos)

    def update(self, dt):
        # update position and velocity

        a_angle, a_magnitude = getPolar(self.acceleration)
        a_car = a_magnitude * math.cos(abs((a_angle - self.car_angle).value))

        front_weight = abs(self.front_weight_static - self.hLM * a_car)
        rear_weight  = abs(self.rear_weight_static  + self.hLM * a_car)

        # friction
        angle, speed = getPolar(self.velocity)
        drag               = self.velocity * speed * (-DRAG_CONSTANT)
        rolling_resistance = self.velocity * (-RR_CONSTANT)

        if not self.braking:
            traction = self.heading * min(self.engine_force, front_weight)
            force    = traction + drag + rolling_resistance

        elif speed > 0:
            braking = getVector(angle) * (-min(BRAKING_CONSTANT, self.weight))
            force   = braking + drag + rolling_resistance

        else:
            force = Vector(0, 0)

        self.acceleration = force / self.mass

        self.velocity += self.acceleration  * dt
        self.position += self.velocity * dt * PIXELS_PER_METRE

        print(self.engine_force, speed, a_magnitude)

        self.car_angle += self.wheel_angle * dt
        self.heading    = getVector(self.car_angle)

        # update car shape
        front = self.heading * CAR_LENGTH // 2
        right = self.heading.right90() * CAR_WIDTH // 2

        self.front = self.position + front
        self.back  = self.position - front

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.back_left   = self.back  - right
        self.back_right  = self.back  + right

        # update course
        angle_change = Angle(math.pi * (dt * 10))
        engine_change = 10000 * dt

        # follow instructions
        while self.instructions:
            angle, magnitude = getPolar(Vector(*self.instructions[0]) - self.position)

            if magnitude < WAYPOINT_RADIUS:
                self.instructions.popleft()
                continue

            angle_difference = self.car_angle - angle

            coarse_angle = Angle(math.atan((WAYPOINT_RADIUS)/magnitude))
            fine_angle   = Angle(math.atan((WAYPOINT_RADIUS/2)/magnitude))

            if abs(angle_difference.value) < fine_angle.value:
                if self.wheel_angle > ZERO_ANGLE:
                    self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)
                elif self.wheel_angle < ZERO_ANGLE:
                    self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

                if speed > STRAIGHT_SPEED:
                    self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)
                elif speed < STRAIGHT_SPEED:
                    self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

                self.braking = False

            else:
                if angle_difference > fine_angle:
                    self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

                elif angle_difference < -fine_angle:
                    self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

                if abs(angle_difference.value) < coarse_angle.value:
                    if speed > TURNING_SPEED:
                        self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)
                    elif speed < TURNING_SPEED:
                        self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

                else:
                    self.braking = True

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

    def drawCourse(self):
        prev = self.front.coords()
        for instruction in self.instructions:
            pygame.draw.line(self.screen,   self.colour, prev, instruction, 1)
            pygame.draw.circle(self.screen, self.colour, instruction, WAYPOINT_RADIUS, 2)
            prev = instruction

    def drawToMouse(self, mouse):
        pygame.draw.line(self.screen, self.colour, self.path_end.coords(), mouse, 1)
        pygame.draw.circle(self.screen, self.colour, mouse, WAYPOINT_RADIUS, 2)

    def drawCar(self):
        # draw car
        chassis = [self.front_left.coords(), self.front_right.coords(),
                   self.back_right.coords(), self.back_left.coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

    def drawArrow(self):
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
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Here we go!")
    clock = pygame.time.Clock()

    # create car
    #colours = [RED, GREEN, BLUE]#[RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    #cars = []
    #for colour in colours:
        #x = random.randint(CAR_LENGTH, WIDTH-CAR_LENGTH-1)
        #y = random.randint(CAR_LENGTH, HEIGHT-CAR_LENGTH-1)
        #a = random.random()*math.pi*2
        #cars.append(Car(screen, colour, (x, y), a))

    cars = [Car(screen, BLUE, (CAR_LENGTH, HEIGHT//2), 0)]

    prev_time = pygame.time.get_ticks()

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the while loop to 10 times per second
        clock.tick(60)

        # find time between frames
        curr_time = pygame.time.get_ticks()
        dt = (curr_time - prev_time) / 1000
        prev_time = curr_time

        # find closest car to mouse
        mouse = pygame.mouse.get_pos()

        closest_car = None
        closest_mag = None
        for car in cars:
            angle, magnitude = getPolar(car.path_end - Vector(*mouse))
            if closest_mag == None or closest_mag > magnitude:
                closest_car = car
                closest_mag = magnitude

        # deal with events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                closest_car.addInstruction(mouse)

        # clear the screen and set the screen background
        screen.fill(WHITE)

        # update cars
        for car in cars:
            car.update(dt)

        # draw courses
        for car in cars:
            car.drawCourse()

        closest_car.drawToMouse(mouse)

        # draw cars
        for car in cars:
            car.drawCar()
            car.drawArrow()

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


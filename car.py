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

CAR_LENGTH   = 100
CAR_WIDTH    = 40
AXLE_LENGTH  = 60
AXLE_WIDTH   = 30

ARROW_LENGTH = 40
ARROW_WIDTH  = 20
ARROW_STEM_LENGTH = 30
ARROW_STEM_WIDTH  = 10

DRAG_CONSTANT    = 0.5
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

PIXELS_PER_METRE = CAR_LENGTH / 4.5

TURNING_SPEED  = 5
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

LOWER_LIMIT = -ANGLE_30
UPPER_LIMIT = ANGLE_30
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
    def __init__(self, screen, colour, position, car_angle=0, speed=0):

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

        # car shape
        front = self.heading * CAR_LENGTH // 2
        right = self.heading.right90() * CAR_WIDTH // 2

        self.front = self.position + front
        self.rear  = self.position - front

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.rear_left   = self.rear  - right
        self.rear_right  = self.rear  + right

        # course plotting
        self.instructions = deque()
        self.path_end     = self.front

    def addInstruction(self, pos):
        self.instructions.append(pos)
        self.path_end = Vector(*pos)

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
            radius = self.wheel_base / math.sin(self.wheel_angle.value)
            angular_v   = self.speed / radius # radians per second

            self.car_angle += Angle(angular_v * dt)
            self.heading    = getVector(self.car_angle)
            self.radius     = radius * PIXELS_PER_METRE

            angle_to_centre = self.car_angle + self.wheel_angle + ANGLE_90
            centre_vector   = getVector(angle_to_centre) * self.radius

            if angular_v < 0:
                self.circle_centre = self.front_left_wheel  + centre_vector
            else:
                self.circle_centre = self.front_right_wheel + centre_vector

        # update car shape
        forward = self.heading * CAR_LENGTH // 2
        right = self.heading.right90() * CAR_WIDTH // 2

        self.front = self.position + forward
        self.rear  = self.position - forward

        self.front_left  = self.front - right
        self.front_right = self.front + right
        self.rear_left   = self.rear  - right
        self.rear_right  = self.rear  + right

        axle_forward = self.heading * AXLE_LENGTH // 2

        front_axle = self.position + axle_forward
        rear_axle  = self.position - axle_forward

        self.front_left_wheel  = front_axle - right
        self.front_right_wheel = front_axle + right
        self.rear_left_wheel   = rear_axle  - right
        self.rear_right_wheel  = rear_axle  + right

        # update course
        angle_change  = Angle(math.pi * dt)
        engine_change = 10000 * dt

        # follow instructions
        while self.instructions:
            destination = Vector(*self.instructions[0])
            angle, magnitude = getPolar(destination - self.position)

            if magnitude < WAYPOINT_RADIUS:
                self.instructions.popleft()
                continue

            angle_difference = self.car_angle - angle

            coarse_angle = Angle(math.atan((WAYPOINT_RADIUS-CAR_WIDTH)/magnitude))

            if abs(angle_difference.value) < coarse_angle.value:
                if self.wheel_angle > ZERO_ANGLE:
                    self.wheel_angle = max(self.wheel_angle-angle_change, ZERO_ANGLE)
                elif self.wheel_angle < ZERO_ANGLE:
                    self.wheel_angle = min(self.wheel_angle+angle_change, ZERO_ANGLE)

                if self.speed > STRAIGHT_SPEED:
                    self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)
                elif self.speed < STRAIGHT_SPEED:
                    self.engine_force = min(self.engine_force+engine_change, MAX_ENGINE_FORCE)

            else:

                if angle_difference > coarse_angle: # left turn
#                    if self.circle_centre:
#                        angle, distance_from_circle = getPolar(destination - self.circle_centre)
#
#                        diff = distance_from_circle - abs(self.radius)
#
#                        if diff < 0:
#                            self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)
#                        elif diff > 0:
#                            self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)
#
#                    else:
                    self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)

                elif angle_difference < -coarse_angle: # right turn
#                    if self.circle_centre:
#                        angle, distance_from_circle = getPolar(destination - self.circle_centre)
#
#                        diff = distance_from_circle - abs(self.radius)
#
#                        if diff > 0:
#                            self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)
#                        elif diff < 0:
#                            self.wheel_angle = max(self.wheel_angle-angle_change, LOWER_LIMIT)
#
#                    else:
                    self.wheel_angle = min(self.wheel_angle+angle_change, UPPER_LIMIT)

                if self.speed > TURNING_SPEED:
                    self.engine_force = max(self.engine_force-engine_change, MIN_ENGINE_FORCE)
                elif self.speed < TURNING_SPEED:
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

        #print(self.engine_force, self.speed, self.car_angle, self.wheel_angle)

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
        if self.circle_centre and abs(self.radius) < 200:
            radius = abs(round(self.radius))
            pygame.draw.line(self.screen, GREY, self.front_left_wheel.coords(), self.circle_centre.coords(), 1)
            pygame.draw.line(self.screen, GREY, self.front_right_wheel.coords(), self.circle_centre.coords(), 1)
            pygame.draw.line(self.screen, GREY, self.rear_left_wheel.coords(), self.circle_centre.coords(), 1)
            pygame.draw.line(self.screen, GREY, self.rear_right_wheel.coords(), self.circle_centre.coords(), 1)
            pygame.draw.circle(self.screen, GREY, self.circle_centre.coords(), radius, 1)

        chassis = [self.front_left.coords(), self.front_right.coords(),
                   self.rear_right.coords(), self.rear_left.coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        # draw wheels
        #forward       = self.heading
        #right         = self.heading.right90()
        #wheel_forward = getVector(self.car_angle + self.wheel_angle)
        #wheel_right   = wheel_forward.right90()

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
    colours = [RED, GREEN, BLUE]#[RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    cars = []
    for colour in colours:
        x = random.randint(CAR_LENGTH, WIDTH-CAR_LENGTH-1)
        y = random.randint(CAR_LENGTH, HEIGHT-CAR_LENGTH-1)
        a = random.random()*math.pi*2
        cars.append(Car(screen, colour, (x, y), a))

    #cars = [Car(screen, BLUE, (CAR_LENGTH, HEIGHT//2), 0)]

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


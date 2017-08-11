import math
import pygame
import time

import util

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

CAR_SIZE   = 100
MULTIPLIER = 100000

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right90(self):
        return Vector2(-self.y, self.x)

    def coords(self):
        return [self.x*CAR_SIZE//MULTIPLIER, self.y*CAR_SIZE//MULTIPLIER]

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector2(self.x // scalar, self.y // scalar)

    def __repr__(self):
        return repr([self.x, self.y])

class Car:
    def __init__(self, screen, colour, position,
                 speed=0, engine_force=0, car_angle=0):

        self.screen = screen
        self.colour = colour

        self.position  = Vector2(*position)
        self.velocity  = Vector2(*velocity)
        self.direction = Vector2(*util.side_lengths[self.car_angle])

        self.speed        = speed
        self.engine_force = engine_force
        self.car_angle    = car_angle

        self.timer = 0
        self.instructions = [(10, None, None), (None, 15, None),
                             (None, None, 100), (None, -10, None),
                             (None, None, 50), (None, 0, 50),
                             (0, 0, None)]
        self.instructions.reverse()

    def update(self):
        # update position and velocity
        traction           = self.direction * self.engine_force
        drag               = self.velocity * self.speed // 1000
        rolling_resistance = self.velocity * 30 // 1000

        acceleration = traction + drag + rolling_resistance
        dt = 1

        self.velocity += acceleration * dt
        self.position += self.velocity * dt

        # follow instructions
        while self.instructions:
            target_force, target_angle, target_time = self.instructions.pop()

            change = False

            if target_force != None:
                if target_force > self.engine_force:
                    self.engine_force += 1
                    change = True
                elif target_force < self.engine_force:
                    self.engine_force -= 1
                    change = True

            if target_angle != None:
                if target_angle > self.car_angle:
                    self.car_angle += 1
                    change = True
                elif target_angle < self.car_angle:
                    self.car_angle -= 1
                    change = True

            if targe_time != None:
                if target_time > self.timer:
                    self.timer += 1
                    change = True

            if change:
                self.instructions.append((target_force, target_angle, target_time))
                break

            else:
                print("DONE", target_force, target_angle, target_time)
                self.timer = 0

        # update direction
        self.direction = Vector2(*util.side_lengths[self.car_angle])

    def draw(self):
        forward = self.direction * 2
        right   = self.direction.right90()

        chassis_A = self.position + forward - right
        chassis_B = self.position + forward + right
        chassis_C = self.position - forward + right
        chassis_D = self.position - forward - right

        chassis = [chassis_A.coords(), chassis_B.coords(),
                   chassis_C.coords(), chassis_D.coords()]

        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

WIDTH  = 1200
HEIGHT = 800

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Here we go!")
    clock = pygame.time.Clock()

    # create car
    car = Car(screen, BLUE, (2*WIDTH//4, 2*HEIGHT//4))

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the while loop to 10 times per second
        clock.tick(30)

        for event in pygame.event.get():
            # user did something

            if event.type == pygame.QUIT:
                # user clicked close
                done = True

        # clear the screen and set the screen background
        screen.fill(WHITE)

        # animate the car
        car.update()
        car.draw() # we start from the 2nd frame, for some reason

        # update the screen
        pygame.display.flip()

    pygame.quit()

main()


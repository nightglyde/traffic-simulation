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

CAR_SIZE   = 10
MULTIPLIER = 100000

plan = [[600, 400], [300, 600], [1100, 200], [200, 100], [800, 500]]

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right90(self):
        return Vector2(-self.y, self.x)

    def coords(self):
        return [self.x//MULTIPLIER, self.y//MULTIPLIER]

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
                 speed=100, car_angle=0):

        self.screen = screen
        self.colour = colour

        self.position = Vector2(*position)*MULTIPLIER
        self.heading = Vector2(*util.side_lengths[car_angle])

        self.speed     = speed
        self.car_angle = car_angle

        self.instructions = []
        for item in plan:
            #corners = []
            #corners.append((item + Vector2( 10,  10))*MULTIPLIER)
            #corners.append((item + Vector2( 10, -10))*MULTIPLIER)
            #corners.append((item + Vector2(-10,  10))*MULTIPLIER)
            #corners.append((item + Vector2(-10, -10))*MULTIPLIER)
            #self.instructions.append(item, corners)
            self.instructions.append(Vector2(*item) * MULTIPLIER)
        self.instructions.reverse()

        self.path = [self.position.coords()]
        self.time = pygame.time.get_ticks()

    def update(self):
        # update position and velocity
        time = pygame.time.get_ticks()
        dt = time - self.time
        print("dt:", dt)
        self.time = time

        self.position += self.heading * self.speed * dt // 1000
        self.path.append(self.position.coords())

        # follow instructions
        while self.instructions:
            #corners = self.instructions[-1]
            target_position = self.instructions[-1]

            if abs(self.position.x-target_position.x) < MULTIPLIER*10:
                if abs(self.position.y-target_position.y) < MULTIPLIER*10:
                    print("DONE", target_position)
                    self.instructions.pop()
                    continue

            to_dest = target_position - self.position
            turn = self.heading.x * to_dest.y - self.heading.y * to_dest.x

            if turn < 0:
                self.car_angle -= (dt / 1000) * 45
            elif turn > 0:
                self.car_angle += (dt / 1000) * 45

            break

            #change = False

            #if target_speed != None:
            #    if target_speed > self.speed:
            #        self.speed += 1
            #        change = True
            #    elif target_speed < self.speed:
            #        self.speed -= 1
            #        change = True

            #if target_angle != None:
            #    angle_difference = (self.car_angle-target_angle)%360
            #    if 0 < angle_difference < 180:
            #        self.car_angle -= 1
            #        change = True
            #    elif angle_difference >= 180:
            #        self.car_angle += 1
            #        change = True

            #if target_time != None:
            #    if target_time > self.timer:
            #        self.timer += 1
            #        change = True

            #if change:
            #    self.instructions.append((target_speed, target_angle, target_time))
            #    break

            #else:
            #    print("DONE", target_speed, target_angle, target_time)
            #    self.timer = 0

        # update direction
        self.car_angle %= 360
        #self.heading = Vector2(*util.side_lengths[round(self.car_angle)])
        angle = math.radians(self.car_angle)
        self.heading = Vector2(MULTIPLIER * math.cos(angle),
                               MULTIPLIER * math.sin(angle))

    def draw(self):
        forward = self.heading * 5 * CAR_SIZE
        right   = self.heading.right90() * 2 * CAR_SIZE

        chassis_A = self.position + forward - right
        chassis_B = self.position + forward + right
        chassis_C = self.position - forward + right
        chassis_D = self.position - forward - right

        chassis = [chassis_A.coords(), chassis_B.coords(),
                   chassis_C.coords(), chassis_D.coords()]

        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        pygame.draw.lines(self.screen, RED, False, self.path, 1)
        pygame.draw.lines(self.screen, GREEN, False, plan, 1)

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
    car = Car(screen, BLUE, (WIDTH//2, HEIGHT//2))

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the while loop to 10 times per second
        clock.tick(100)

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


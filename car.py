import math
import pygame
import time

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

# here are some things
SIZE_UNIT = 10

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coords(self):
        return [self.x, self.y]

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return repr(self.coords())

def getCartesian(magnitude, angle):
    rad = math.radians(angle)
    a = magnitude * math.cos(rad)
    b = magnitude * math.sin(rad)

    #return Vector2(int(round(a)), int(round(b)))
    return Vector2(a, b)

def getPolar(vector):
    x = vector.x
    y = vector.y

    magnitude = math.sqrt(x**2 + y**2)

    if x == 0:
        angle = 90
    else:
        angle = math.degrees(math.atan(y / x))

    if x < 0:
        angle += 180

    elif y < 0:
        angle += 360

    return magnitude, angle

class Car:
    def __init__(self, screen, colour,
                 position, velocity=(0,0), force=0,
                 car_angle=0, wheel_angle=0):

        self.screen = screen
        self.colour = colour

        self.position    = Vector2(*position) # centre of vehicle
        self.velocity    = Vector2(*velocity)

        self.force       = force
        self.car_angle   = car_angle
        self.wheel_angle = wheel_angle

        self.centre_path  = [self.position.coords()]
        self.wheel_A_path = [self.position.coords()]
        self.wheel_B_path = [self.position.coords()]
        self.wheel_C_path = [self.position.coords()]
        self.wheel_D_path = [self.position.coords()]

        self.timer = 0
        self.instructions = [(1, None, None),   (None, 45, None),
                             (None, None, 100), (None, -30, None),
                             (None, None, 50),  (None, 0, 50),
                             (0, 0, None)]
        self.instructions.reverse()

    def update(self):
        while self.instructions:
            target_force, target_angle, target_time = self.instructions.pop()

            change = False

            if target_force != None:
                if target_force > self.force:
                    self.force = min(target_force, self.force+0.1)
                    change = True

                elif target_force < self.force:
                    self.force = max(target_force, self.force-0.1)
                    change = True

            if target_angle != None:
                if target_angle > self.wheel_angle:
                    self.wheel_angle = min(target_angle, self.wheel_angle+1)
                    change = True

                elif target_angle < self.wheel_angle:
                    self.wheel_angle = max(target_angle, self.wheel_angle-1)
                    change = True

            if target_time != None:
                if target_time > self.timer:
                    self.timer += 1
                    change = True

            if change:
                self.instructions.append((target_force, target_angle, target_time))
                break

            else:
                print("DONE", target_force, target_angle, target_time)
                self.timer = 0

        # slow down
        self.velocity *= 0.90

        # speed up
        acceleration = getCartesian(self.force, self.car_angle + self.wheel_angle)
        self.velocity += acceleration

        # move car
        self.position += self.velocity
        magnitude, angle = getPolar(self.velocity)
        self.car_angle = angle

        #if magnitude > 0.1 or self.instructions:
        #    self.path.append(self.position.coords())

        # print update message
        #print(self.force, self.wheel_angle, self.velocity)

    def draw(self):
        # outer shell
        car_forward = getCartesian(SIZE_UNIT*12, self.car_angle)
        car_right   = getCartesian(SIZE_UNIT*6,  self.car_angle + 90)

        chassis_A = self.position + car_forward - car_right
        chassis_B = self.position + car_forward + car_right
        chassis_C = self.position - car_forward + car_right
        chassis_D = self.position - car_forward - car_right

        chassis = [chassis_A.coords(), chassis_B.coords(),
                   chassis_C.coords(), chassis_D.coords()]

        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen,       BLACK, chassis, 2)

        # axles
        axle_forward = getCartesian(SIZE_UNIT*8, self.car_angle)
        axle_right   = getCartesian(SIZE_UNIT*4, self.car_angle + 90)

        front_axle   = self.position + axle_forward
        wheel_A_axle = front_axle    - axle_right
        wheel_B_axle = front_axle    + axle_right

        rear_axle    = self.position - axle_forward
        wheel_C_axle = rear_axle     + axle_right
        wheel_D_axle = rear_axle     - axle_right

        pygame.draw.line(self.screen, BLACK,   front_axle.coords(),    rear_axle.coords(), 3)
        pygame.draw.line(self.screen, BLACK, wheel_A_axle.coords(), wheel_B_axle.coords(), 3)
        pygame.draw.line(self.screen, BLACK, wheel_C_axle.coords(), wheel_D_axle.coords(), 3)

        # front left wheel
        front_wheel_forward = getCartesian(SIZE_UNIT*2, self.car_angle + self.wheel_angle)
        front_wheel_right   = getCartesian(SIZE_UNIT*2, self.car_angle + self.wheel_angle + 90)

        wheel_A_inner_front = wheel_A_axle        + front_wheel_forward
        wheel_A_inner_back  = wheel_A_axle        - front_wheel_forward
        wheel_A_outer_front = wheel_A_inner_front - front_wheel_right
        wheel_A_outer_back  = wheel_A_inner_back  - front_wheel_right

        wheel_A = [wheel_A_inner_front.coords(), wheel_A_outer_front.coords(),
                   wheel_A_outer_back.coords(),  wheel_A_inner_back.coords()]

        pygame.draw.polygon(self.screen,  GREY, wheel_A)
        pygame.draw.polygon(self.screen, BLACK, wheel_A, 2)

        # front right wheel
        wheel_B_inner_front = wheel_B_axle        + front_wheel_forward
        wheel_B_inner_back  = wheel_B_axle        - front_wheel_forward
        wheel_B_outer_front = wheel_B_inner_front + front_wheel_right
        wheel_B_outer_back  = wheel_B_inner_back  + front_wheel_right

        wheel_B = [wheel_B_inner_front.coords(), wheel_B_outer_front.coords(),
                   wheel_B_outer_back.coords(),  wheel_B_inner_back.coords()]

        pygame.draw.polygon(self.screen,  GREY, wheel_B)
        pygame.draw.polygon(self.screen, BLACK, wheel_B, 2)

        # rear right wheel
        rear_wheel_forward  = getCartesian(SIZE_UNIT*2, self.car_angle)
        rear_wheel_right    = getCartesian(SIZE_UNIT*2, self.car_angle + 90)

        wheel_C_inner_front = wheel_C_axle        + rear_wheel_forward
        wheel_C_inner_back  = wheel_C_axle        - rear_wheel_forward
        wheel_C_outer_front = wheel_C_inner_front + rear_wheel_right
        wheel_C_outer_back  = wheel_C_inner_back  + rear_wheel_right

        wheel_C = [wheel_C_inner_front.coords(), wheel_C_outer_front.coords(),
                   wheel_C_outer_back.coords(),  wheel_C_inner_back.coords()]

        pygame.draw.polygon(self.screen,  GREY, wheel_C)
        pygame.draw.polygon(self.screen, BLACK, wheel_C, 2)

        # rear left wheel
        wheel_D_inner_front = wheel_D_axle        + rear_wheel_forward
        wheel_D_inner_back  = wheel_D_axle        - rear_wheel_forward
        wheel_D_outer_front = wheel_D_inner_front - rear_wheel_right
        wheel_D_outer_back  = wheel_D_inner_back  - rear_wheel_right

        wheel_D = [wheel_D_inner_front.coords(), wheel_D_outer_front.coords(),
                   wheel_D_outer_back.coords(),  wheel_D_inner_back.coords()]

        pygame.draw.polygon(self.screen,  GREY, wheel_D)
        pygame.draw.polygon(self.screen, BLACK, wheel_D, 2)

        wheel_A_centre = wheel_A_axle - getCartesian(SIZE_UNIT, self.car_angle + self.wheel_angle + 90)
        wheel_B_centre = wheel_B_axle + getCartesian(SIZE_UNIT, self.car_angle + self.wheel_angle + 90)
        wheel_C_centre = wheel_C_axle + getCartesian(SIZE_UNIT, self.car_angle + 90)
        wheel_D_centre = wheel_D_axle - getCartesian(SIZE_UNIT, self.car_angle + 90)

        self.centre_path.append(self.position.coords())
        self.wheel_A_path.append(wheel_A_centre.coords())
        self.wheel_B_path.append(wheel_B_centre.coords())
        self.wheel_C_path.append(wheel_C_centre.coords())
        self.wheel_D_path.append(wheel_D_centre.coords())

        pygame.draw.lines(self.screen, BLUE,    False, self.centre_path, 1)
        pygame.draw.lines(self.screen, RED,     False, self.wheel_A_path, 1)
        pygame.draw.lines(self.screen, GREEN,   False, self.wheel_B_path, 1)
        pygame.draw.lines(self.screen, CYAN,    False, self.wheel_C_path, 1)
        pygame.draw.lines(self.screen, MAGENTA, False, self.wheel_D_path, 1)

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
    car = Car(screen, BLUE, (1*WIDTH//4, 1*HEIGHT//4), (0, 0), 0, 0, 0)

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


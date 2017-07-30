import math
import time

from graphics import *
# find a better animation library. perhaps pygame or matplotlib???
# also, maybe numpy does vectors better???

WIDTH  = 1200
HEIGHT =  800

CAR_SIZE   = 50
AXLE_SIZE  = (CAR_SIZE*2)//3
WHEEL_SIZE = CAR_SIZE//3

class Vector2(Point):
    def __init__(self, x, y):
        Point.__init__(self, x, y)

    def right90(self):
        return Vector2(-self.y, self.x)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

def generateVector(magnitude, angle):
    rad = math.radians(angle)
    a = magnitude * math.cos(rad)
    b = magnitude * math.sin(rad)

    return Vector2(int(round(a)), int(round(b)))

#
# front wheels add velocity to the car
# rear wheels roll forwards
# whole chassis turns in response to velocity, tending towards facing the direction of motion
# if the chassis is facing the direction of motion, that makes it easier for the rear wheels to turn
#

class Car:
    def __init__(self, position, velocity, car_angle, wheel_angle):
        self.position        = Vector2(*position)        # centre of vehicle, relative to world
        self.velocity        = Vector2(*velocity)        # current velocity, relative to world

        self.car_angle   = car_angle
        self.wheel_angle = wheel_angle

        self.shapes = []

    def setAngles(self, car_angle, wheel_angle):
        self.car_angle = car_angle
        self.wheel_angle = wheel_angle

    def draw(self, window, colour):
        # outer shell
        car_forward         = generateVector(CAR_SIZE, self.car_angle)
        car_right           = car_forward.right90()

        chassis_A = self.position + car_forward*2 - car_right
        chassis_B = self.position + car_forward*2 + car_right
        chassis_C = self.position - car_forward*2 + car_right
        chassis_D = self.position - car_forward*2 - car_right

        chassis = Polygon(chassis_A, chassis_B, chassis_C, chassis_D)
        chassis.setFill(colour)

        # axles
        axle_forward        = generateVector(AXLE_SIZE, self.car_angle)
        axle_right          = axle_forward.right90()

        front_axle   = self.position + axle_forward*2
        wheel_A_axle = front_axle    - axle_right
        wheel_B_axle = front_axle    + axle_right

        rear_axle    = self.position - axle_forward*2
        wheel_C_axle = rear_axle     + axle_right
        wheel_D_axle = rear_axle     - axle_right

        mid_line = Line(front_axle, rear_axle)
        front_line = Line(wheel_A_axle, wheel_B_axle)
        rear_line = Line(wheel_C_axle, wheel_D_axle)

        # front left wheel
        front_wheel_forward = generateVector(WHEEL_SIZE, self.car_angle + self.wheel_angle)
        front_wheel_right   = front_wheel_forward.right90()

        wheel_A_inner_front = wheel_A_axle        + front_wheel_forward
        wheel_A_inner_back  = wheel_A_axle        - front_wheel_forward
        wheel_A_outer_front = wheel_A_inner_front - front_wheel_right
        wheel_A_outer_back  = wheel_A_inner_back  - front_wheel_right

        wheel_A = Polygon(
            wheel_A_inner_front, wheel_A_outer_front,
            wheel_A_outer_back,  wheel_A_inner_back)
        wheel_A.setFill("gray")

        # front right wheel
        wheel_B_inner_front = wheel_B_axle        + front_wheel_forward
        wheel_B_inner_back  = wheel_B_axle        - front_wheel_forward
        wheel_B_outer_front = wheel_B_inner_front + front_wheel_right
        wheel_B_outer_back  = wheel_B_inner_back  + front_wheel_right

        wheel_B = Polygon(
            wheel_B_inner_front, wheel_B_outer_front,
            wheel_B_outer_back,  wheel_B_inner_back)
        wheel_B.setFill("gray")

        # rear right wheel
        rear_wheel_forward  = generateVector(WHEEL_SIZE, self.car_angle)
        rear_wheel_right    = rear_wheel_forward.right90()

        wheel_C_inner_front = wheel_C_axle        + rear_wheel_forward
        wheel_C_inner_back  = wheel_C_axle        - rear_wheel_forward
        wheel_C_outer_front = wheel_C_inner_front + rear_wheel_right
        wheel_C_outer_back  = wheel_C_inner_back  + rear_wheel_right

        wheel_C = Polygon(
            wheel_C_inner_front, wheel_C_outer_front,
            wheel_C_outer_back,  wheel_C_inner_back)
        wheel_C.setFill("gray")

        # rear left wheel
        wheel_D_inner_front = wheel_D_axle        + rear_wheel_forward
        wheel_D_inner_back  = wheel_D_axle        - rear_wheel_forward
        wheel_D_outer_front = wheel_D_inner_front - rear_wheel_right
        wheel_D_outer_back  = wheel_D_inner_back  - rear_wheel_right

        wheel_D = Polygon(
            wheel_D_inner_front, wheel_D_outer_front,
            wheel_D_outer_back,  wheel_D_inner_back)
        wheel_D.setFill("gray")

        # draw new shapes
        chassis.draw(window)
        wheel_A.draw(window)
        wheel_B.draw(window)
        wheel_C.draw(window)
        wheel_D.draw(window)
        mid_line.draw(window)
        front_line.draw(window)
        rear_line.draw(window)

        # undraw old shapes
        while self.shapes:
            shape = self.shapes.pop()
            shape.undraw()

        # save new shapes
        self.shapes.append(chassis)
        self.shapes.append(wheel_A)
        self.shapes.append(wheel_B)
        self.shapes.append(wheel_C)
        self.shapes.append(wheel_D)
        self.shapes.append(mid_line)
        self.shapes.append(front_line)
        self.shapes.append(rear_line)

def main():
    window = GraphWin("It's a car!", WIDTH, HEIGHT)

    colours = ["blue", "magenta", "red", "yellow", "green", "cyan"]

    car = Car((600, 400), (0, 0), 0, 0)

    now = time.time()

    for i in range(1000):
        car.setAngles(i*5, 0)
        car.draw(window, colours[0])
        time.sleep(0.03)

    #for i in range(72, -1, -1):
    #    car = Car((300, 400), (0, 0), i*5, i*5)
    #    car.draw(window, colours[i%6])

    #for i in range(73):
    #    car = Car((900, 400), (0, 0), i*5, i*5)
    #    car.draw(window, colours[i%6])

    time_elapsed = time.time() - now
    print(time_elapsed)

    window.getMouse() # pause to view result
    window.close()

main()


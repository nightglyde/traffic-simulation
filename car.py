import math
from graphics import *

class Vector2(Point):
    def __init__(self, x, y):
        Point.__init__(self, x, y)
        #self.x = x
        #self.y = y

    def right90(self):
        return Vector2(-self.y, self.x)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __tuple__(self):
        return (self.x, self.y)

    def __repr__(self):
        return repr(tuple(self))

class Car:
    def __init__(self, position, velocity, direction, wheel_direction):
        self.position        = Vector2(*position)        # centre of vehicle, relative to world
        self.velocity        = Vector2(*velocity)        # current velocity, relative to world
        self.direction       = Vector2(*direction)       # direction the vehicle is facing
        self.wheel_direction = Vector2(*wheel_direction) # direction the front wheels are facing

    def draw(self, window):
        forward       = self.direction
        right         = self.direction.right90()
        wheel_forward = self.wheel_direction
        wheel_right   = self.wheel_direction.right90()

        front_axle = self.position + forward*4
        rear_axle  = self.position - forward*4

        # front left wheel
        wheel_A_axle        = front_axle          - right*2
        wheel_A_inner_front = wheel_A_axle        + wheel_forward
        wheel_A_inner_back  = wheel_A_axle        - wheel_forward
        wheel_A_outer_front = wheel_A_inner_front - wheel_right
        wheel_A_outer_back  = wheel_A_inner_back  - wheel_right

        wheel_A = Polygon(wheel_A_inner_front, wheel_A_outer_front,
                          wheel_A_outer_back,  wheel_A_inner_back)
        wheel_A.draw(window)

        #wheel_A_triangle = Polygon(wheel_A_axle, wheel_A_outer_front, wheel_A_outer_back)
        #wheel_A_triangle.draw(window)

        # front right wheel
        wheel_B_axle        = front_axle          + right*2
        wheel_B_inner_front = wheel_B_axle        + wheel_forward
        wheel_B_inner_back  = wheel_B_axle        - wheel_forward
        wheel_B_outer_front = wheel_B_inner_front + wheel_right
        wheel_B_outer_back  = wheel_B_inner_back  + wheel_right

        wheel_B = Polygon(wheel_B_inner_front, wheel_B_outer_front,
                          wheel_B_outer_back,  wheel_B_inner_back)
        wheel_B.draw(window)

        #wheel_B_triangle = Polygon(wheel_B_axle, wheel_B_outer_front, wheel_B_outer_back)
        #wheel_B_triangle.draw(window)

        # rear right wheel
        wheel_C_axle        = rear_axle           + right*2
        wheel_C_inner_front = wheel_C_axle        + forward
        wheel_C_inner_back  = wheel_C_axle        - forward
        wheel_C_outer_front = wheel_C_inner_front + right
        wheel_C_outer_back  = wheel_C_inner_back  + right

        wheel_C = Polygon(wheel_C_inner_front, wheel_C_outer_front,
                          wheel_C_outer_back,  wheel_C_inner_back)
        wheel_C.draw(window)

        #wheel_C_triangle = Polygon(wheel_C_axle, wheel_C_outer_front, wheel_C_outer_back)
        #wheel_C_triangle.draw(window)

        # rear left wheel
        wheel_D_axle        = rear_axle           - right*2
        wheel_D_inner_front = wheel_D_axle        + forward
        wheel_D_inner_back  = wheel_D_axle        - forward
        wheel_D_outer_front = wheel_D_inner_front - right
        wheel_D_outer_back  = wheel_D_inner_back  - right

        wheel_D = Polygon(wheel_D_inner_front, wheel_D_outer_front,
                          wheel_D_outer_back,  wheel_D_inner_back)
        wheel_D.draw(window)

        #wheel_D_triangle = Polygon(wheel_D_axle, wheel_D_outer_front, wheel_D_outer_back)
        #wheel_D_triangle.draw(window)

        # outer shell
        chassis_A = wheel_A_axle + forward*2 - right
        chassis_B = wheel_B_axle + forward*2 + right
        chassis_C = wheel_C_axle - forward*2 + right
        chassis_D = wheel_D_axle - forward*2 - right

        chassis = Polygon(chassis_A, chassis_B, chassis_C, chassis_D)
        chassis.draw(window)

        mid_line = Line(front_axle, rear_axle)
        mid_line.draw(window)

        front_line = Line(wheel_A_axle, wheel_B_axle)
        front_line.draw(window)

        rear_line = Line(wheel_C_axle, wheel_D_axle)
        rear_line.draw(window)

def generateVector(magnitude, side_length):
    if side_length > magnitude or side_length <= 0:
        return (int(magnitude), 0)

    other_side_length = math.sqrt(magnitude**2 - side_length**2)

    return (int(other_side_length), int(side_length))

def main():
    window = GraphWin("It's a car!", 800, 800)

    car = Car((400, 400), (0, 0), (50, 0), generateVector(50, 10))
    car.draw(window)

    window.getMouse() # pause to view result
    window.close()

main()


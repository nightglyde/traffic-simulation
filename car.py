
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def right90(self):
        return Vector2(-self.y, self.x)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

class Car:
    def __init__(self, position, velocity, direction, wheel_direction):
        self.position        = Vector2(*position)        # centre of vehicle, relative to world
        self.velocity        = Vector2(*velocity)        # current velocity, relative to world
        self.direction       = Vector2(*direction)       # direction the vehicle is facing
        self.wheel_direction = Vector2(*wheel_direction) # direction the front wheels are facing

    def draw(self):
        forward = self.direction
        right   = self.direction.right90()

        wheel_forward = self.wheel_direction
        wheel_right   = self.wheel_direction.right90()

        # front left corner
        wheel_A_axle  = self.position + forward*4     - right*2
        wheel_A_front = wheel_A_axle  + wheel_forward - wheel_right
        wheel_A_back  = wheel_A_axle  - wheel_forward - wheel_right
        chassis_A     = wheel_A_axle  + forward*2     - right

        # front right corner
        wheel_B_axle  = self.position + forward*4     + right*2
        wheel_B_front = wheel_A_axle  + wheel_forward + wheel_right
        wheel_B_back  = wheel_A_axle  - wheel_forward + wheel_right
        chassis_B     = wheel_B_axle  + forward*2     + right

        # rear left corner
        wheel_C_axle  = self.position - forward*4 - right*2
        wheel_C_front = wheel_C_axle  + forward   - right
        wheel_C_back  = wheel_C_axle  - forward   - right
        chassis_C     = wheel_C_back  - forward

        # rear right corner
        wheel_D_axle  = self.position - forward*4 + right*2
        wheel_D_front = wheel_D_axle  + forward   + right
        wheel_D_back  = wheel_D_axle  - forward   + right
        chassis_D     = wheel_D_back  - forward

        print(chassis_A, chassis_B, chassis_C, chassis_D)
        print(wheel_A_axle, wheel_A_front, wheel_A_back)
        print(wheel_B_axle, wheel_B_front, wheel_B_back)
        print(wheel_C_axle, wheel_C_front, wheel_C_back)
        print(wheel_D_axle, wheel_D_front, wheel_D_back)

car = Car((0, 0), (0, 0), (10, 20), (20, 10))

car.draw()


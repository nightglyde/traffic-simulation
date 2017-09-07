import math
import random
import pygame

from collections import deque

FRAMES_PER_SECOND = 120

SCREEN_UNIT = 10
WORLD_UNIT  = 0.45

PIXELS_PER_METRE = SCREEN_UNIT / WORLD_UNIT

SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800

WORLD_WIDTH  = SCREEN_WIDTH  / PIXELS_PER_METRE
WORLD_HEIGHT = SCREEN_HEIGHT / PIXELS_PER_METRE

SCREEN_CAR_LENGTH  = SCREEN_UNIT * 10
SCREEN_CAR_WIDTH   = SCREEN_UNIT * 4
SCREEN_AXLE_LENGTH = SCREEN_UNIT * 6
SCREEN_AXLE_WIDTH  = SCREEN_UNIT * 4

SCREEN_WHEEL_LENGTH = SCREEN_UNIT * 2
SCREEN_WHEEL_WIDTH  = SCREEN_UNIT * 0.5

ARROW_LENGTH      = SCREEN_UNIT * 4
ARROW_WIDTH       = SCREEN_UNIT * 2
ARROW_STEM_LENGTH = SCREEN_UNIT * 3
ARROW_STEM_WIDTH  = SCREEN_UNIT * 1

WAYPOINT_OUTER = SCREEN_UNIT * 5
WAYPOINT_INNER = SCREEN_UNIT * 9 // 2

LEFT   = -1
RIGHT  = 1
CENTRE = 0

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left90(self):
        return Vector(self.y, -self.x)

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

def getVector(angle):
    return Vector(math.cos(angle.value), math.sin(angle.value))

VECTOR_0 = Vector(0, 0)

SCREEN_LEFT         = Vector(0,              SCREEN_HEIGHT/2)
SCREEN_RIGHT        = Vector(SCREEN_WIDTH,   SCREEN_HEIGHT/2)
SCREEN_TOP          = Vector(SCREEN_WIDTH/2, 0)
SCREEN_BOTTOM       = Vector(SCREEN_WIDTH/2, SCREEN_HEIGHT)
SCREEN_CENTRE       = Vector(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
SCREEN_TOP_LEFT     = Vector(0,              0)
SCREEN_TOP_RIGHT    = Vector(SCREEN_WIDTH,   0)
SCREEN_BOTTOM_LEFT  = Vector(0,              SCREEN_HEIGHT)
SCREEN_BOTTOM_RIGHT = Vector(SCREEN_WIDTH,   SCREEN_HEIGHT)

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

    def __truediv__(self, scalar):
        return Angle(self.value / scalar)

    def __floordiv__(self, scalar):
        return Angle(self.value // scalar)

    def __neg__(self):
        return Angle(-self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return repr(math.degrees(self.value))

def getAngle(vector):
    x = vector.x

    if x == 0:
        angle = math.pi / 2
    else:
        angle = math.atan(vector.y / x)

    if x < 0:
        angle += math.pi

    return Angle(angle)

def getMagnitude(vector):
    return math.sqrt(vector.x**2 + vector.y**2)

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

ANGLE_0   = Angle(math.radians(0))
ANGLE_5   = Angle(math.radians(5))
ANGLE_10  = Angle(math.radians(10))
ANGLE_15  = Angle(math.radians(15))
ANGLE_20  = Angle(math.radians(20))
ANGLE_25  = Angle(math.radians(25))
ANGLE_30  = Angle(math.radians(30))
ANGLE_35  = Angle(math.radians(35))
ANGLE_40  = Angle(math.radians(40))
ANGLE_45  = Angle(math.radians(45))
ANGLE_50  = Angle(math.radians(50))
ANGLE_55  = Angle(math.radians(55))
ANGLE_60  = Angle(math.radians(60))
ANGLE_65  = Angle(math.radians(65))
ANGLE_70  = Angle(math.radians(70))
ANGLE_75  = Angle(math.radians(75))
ANGLE_80  = Angle(math.radians(80))
ANGLE_85  = Angle(math.radians(85))
ANGLE_90  = Angle(math.radians(90))
ANGLE_120 = Angle(math.radians(120))

def generateRandomWorldPosition():
    x = random.random() * WORLD_WIDTH
    y = random.random() * WORLD_HEIGHT
    pos = Vector(x, y)
    angle = Angle(random.random()*2*math.pi)
    return pos, angle

# grey
BLACK      = (  0,   0,   0)
DARK_GREY  = ( 64,  64,  64)
GREY       = (128, 128, 128)
LIGHT_GREY = (191, 191, 191)
WHITE      = (255, 255, 255)

# red
DARK_RED  = (128,   0,   0)
RED       = (255,   0,   0)
LIGHT_RED = (255, 128, 128)

# yellow
DARK_YELLOW  = (128, 128,   0)
YELLOW       = (255, 255,   0)
LIGHT_YELLOW = (255, 255, 128)

# green
DARK_GREEN  = (  0, 128,   0)
GREEN       = (  0, 255,   0)
LIGHT_GREEN = (128, 255, 128)

# cyan
DARK_CYAN  = (  0, 128, 128)
CYAN       = (  0, 255, 255)
LIGHT_CYAN = (128, 255, 255)

# blue
DARK_BLUE  = (  0,   0, 128)
BLUE       = (  0,   0, 255)
LIGHT_BLUE = (128, 128, 255)

# magenta
DARK_MAGENTA  = (128,   0, 128)
MAGENTA       = (255,   0, 255)
LIGHT_MAGENTA = (255, 128, 255)

LIGHTER = {BLACK: DARK_GREY,                               WHITE: WHITE,
       DARK_GREY: GREY,       GREY: LIGHT_GREY,       LIGHT_GREY: WHITE,
        DARK_RED: RED,         RED: LIGHT_RED,         LIGHT_RED: WHITE,
     DARK_YELLOW: YELLOW,   YELLOW: LIGHT_YELLOW,   LIGHT_YELLOW: WHITE,
      DARK_GREEN: GREEN,     GREEN: LIGHT_GREEN,     LIGHT_GREEN: WHITE,
       DARK_CYAN: CYAN,       CYAN: LIGHT_CYAN,       LIGHT_CYAN: WHITE,
       DARK_BLUE: BLUE,       BLUE: LIGHT_BLUE,       LIGHT_BLUE: WHITE,
    DARK_MAGENTA: MAGENTA, MAGENTA: LIGHT_MAGENTA, LIGHT_MAGENTA: WHITE,
}

DARKER = {  WHITE: LIGHT_GREY,                            BLACK: BLACK,
       LIGHT_GREY: GREY,       GREY: DARK_GREY,       DARK_GREY: BLACK,
        LIGHT_RED: RED,         RED: DARK_RED,         DARK_RED: BLACK,
     LIGHT_YELLOW: YELLOW,   YELLOW: DARK_YELLOW,   DARK_YELLOW: BLACK,
      LIGHT_GREEN: GREEN,     GREEN: DARK_GREEN,     DARK_GREEN: BLACK,
       LIGHT_CYAN: CYAN,       CYAN: DARK_CYAN,       DARK_CYAN: BLACK,
       LIGHT_BLUE: BLUE,       BLUE: DARK_BLUE,       DARK_BLUE: BLACK,
    LIGHT_MAGENTA: MAGENTA, MAGENTA: DARK_MAGENTA, DARK_MAGENTA: BLACK,
}

def sign(n):
    return (n > 0) - (n < 0)


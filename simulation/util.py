import math
import random
import pygame

from collections import deque

SCREEN_WIDTH  = 1200 # pixels
SCREEN_HEIGHT = 800

CAR_LENGTH  = 4.5 # metres
CAR_WIDTH   = 1.8
AXLE_LENGTH = 2.7
AXLE_WIDTH  = 1.8

WHEEL_LENGTH = 0.9
WHEEL_WIDTH  = 0.225

ARROW_LENGTH      = 1.8
ARROW_WIDTH       = 0.9
ARROW_STEM_LENGTH = 1.35
ARROW_STEM_WIDTH  = 0.45

LEFT   = -1
RIGHT  = 1
CENTRE = 0

##########
# VECTOR #
##########

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left90(self):
        return Vector(-self.y, self.x)

    def right90(self):
        return Vector(self.y, -self.x)

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

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __repr__(self):
        return repr([self.x, self.y])

def getVector(angle):
    return Vector(math.cos(angle.value), math.sin(angle.value))

VECTOR_0 = Vector(0, 0)

#########
# ANGLE #
#########

class Angle:
    def __init__(self, value):

        if value > math.pi:
            value -= math.pi*2

        elif value < -math.pi:
            value += math.pi*2

        self.value = value

    def norm(self):
        value = -self.value

        if value < 0:
            value += math.pi*2

        return value

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

#########
# WORLD #
#########

WORLD_WIDTH  = 120 # metres
WORLD_HEIGHT = 80

WORLD_MIN_X = 0
WORLD_MIN_Y = 0
WORLD_MAX_X = WORLD_WIDTH
WORLD_MAX_Y = WORLD_HEIGHT
WORLD_MID_X = (WORLD_MIN_X + WORLD_MAX_X) / 2
WORLD_MID_Y = (WORLD_MIN_Y + WORLD_MAX_Y) / 2

WORLD_CENTRE = Vector(WORLD_MID_X, WORLD_MID_Y)
WORLD_TOP    = Vector(WORLD_MID_X, WORLD_MIN_Y)
WORLD_BOTTOM = Vector(WORLD_MID_X, WORLD_MAX_Y)
WORLD_LEFT   = Vector(WORLD_MIN_X, WORLD_MID_Y)
WORLD_RIGHT  = Vector(WORLD_MAX_X, WORLD_MID_Y)

WORLD_TOP_LEFT     = Vector(WORLD_MIN_X, WORLD_MIN_Y)
WORLD_TOP_RIGHT    = Vector(WORLD_MAX_X, WORLD_MIN_Y)
WORLD_BOTTOM_LEFT  = Vector(WORLD_MIN_X, WORLD_MAX_Y)
WORLD_BOTTOM_RIGHT = Vector(WORLD_MAX_X, WORLD_MAX_Y)

WORLD_BOX = [WORLD_TOP_LEFT,     WORLD_TOP_RIGHT,
             WORLD_BOTTOM_RIGHT, WORLD_BOTTOM_LEFT]

def checkWorldBoundary(point):
    if point.x < WORLD_MIN_X:
        return False

    if point.x > WORLD_MAX_X:
        return False

    if point.y < WORLD_MIN_Y:
        return False

    if point.y > WORLD_MAX_Y:
        return False

    return True

#############
# WAYPOINTS #
#############

ESTIMATED_ANGLE = ANGLE_45
TURNING_RADIUS  = AXLE_LENGTH / math.sin(ESTIMATED_ANGLE.value)

WAYPOINT_OUTER     = 2.5
WAYPOINT_INNER     = 2.25
WAYPOINT_THRESHOLD = 1

WORLD_MARGIN = WAYPOINT_OUTER + TURNING_RADIUS

WAYPOINT_INTERVAL = TURNING_RADIUS * 3
WAYPOINT_BIG_GAP  = TURNING_RADIUS * 4

WAYPOINT_MIN_X = WORLD_MIN_X + WORLD_MARGIN
WAYPOINT_MIN_Y = WORLD_MIN_Y + WORLD_MARGIN
WAYPOINT_MAX_X = WORLD_MAX_X - WORLD_MARGIN
WAYPOINT_MAX_Y = WORLD_MAX_Y - WORLD_MARGIN

def checkWaypointBoundary(point):
    if point.x < WAYPOINT_MIN_X:
        return False

    if point.x > WAYPOINT_MAX_X:
        return False

    if point.y < WAYPOINT_MIN_Y:
        return False

    if point.y > WAYPOINT_MAX_Y:
        return False

    return True

def generateRandomWaypointPosition(prev):
    x = WAYPOINT_MIN_X + random.random()*(WAYPOINT_MAX_X - WAYPOINT_MIN_X)
    y = WAYPOINT_MIN_Y + random.random()*(WAYPOINT_MAX_Y - WAYPOINT_MIN_Y)
    pos = Vector(x, y)
    angle = getAngle(pos - prev)
    return pos, angle

MAX_WAYPOINTS      = 100
STARTING_WAYPOINTS = 5

class Waypoint:
    def __init__(self, position, angle):
        self.position = position
        self.angle    = angle
        self.time     = None

################
# PAN AND ZOOM #
################

SCALE_START  = min(SCREEN_HEIGHT / WORLD_HEIGHT * 0.9,
                   SCREEN_WIDTH  / WORLD_WIDTH  * 0.9)
SCALE_CHANGE = 1.5

SCALE_MIN = min(SCREEN_HEIGHT / WORLD_HEIGHT * 0.4,
                SCREEN_WIDTH  / WORLD_WIDTH  * 0.4)
SCALE_MAX = min(SCREEN_HEIGHT / CAR_LENGTH * 0.5,
                SCREEN_WIDTH  / CAR_LENGTH * 0.5)

OFFSET_START = Vector((SCREEN_WIDTH  / SCALE_START - WORLD_WIDTH)  / 2,
                      (SCREEN_HEIGHT / SCALE_START - WORLD_HEIGHT) / 2)
class Zoom:
    def __init__(self):
        self.starting_position = None
        self.starting_offset   = None

        self.offset = OFFSET_START
        self.scale  = SCALE_START

    def scaleDistance(self, distance):
        return round(distance * self.scale)

    def getScreenPosition(self, true_position):
        return (true_position + self.offset) * self.scale

    def getDrawable(self, point):
        point = self.getScreenPosition(point)
        return [round(point.x), round(point.y)]

    def getTruePosition(self, screen_position):
        return screen_position/self.scale - self.offset

    def zoomIn(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        if not checkWorldBoundary(true_mouse_position):
            return

        new_scale = min(self.scale * SCALE_CHANGE, SCALE_MAX)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def zoomOut(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        if not checkWorldBoundary(true_mouse_position):
            return

        new_scale = max(self.scale / SCALE_CHANGE, SCALE_MIN)

        self.offset = mouse_position/new_scale - true_mouse_position
        self.scale  = new_scale

    def startPan(self, mouse_position):
        true_mouse_position = self.getTruePosition(mouse_position)
        if not checkWorldBoundary(true_mouse_position):
            return False

        self.starting_position = mouse_position
        self.starting_offset   = self.offset
        return True

    def updatePan(self, mouse_position):
        if self.starting_position == None:
            return

        diff = (mouse_position - self.starting_position) / self.scale
        self.offset = self.starting_offset + diff

    def stopPan(self):
        self.starting_position = None
        self.starting_offset   = None

###########
# COLOURS #
###########

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

# orange
DARK_ORANGE  = (128,  64,   0)
ORANGE       = (255, 128,   0)
LIGHT_ORANGE = (255, 191, 128)

# yellow
DARK_YELLOW  = (128, 128,   0)
YELLOW       = (255, 255,   0)
LIGHT_YELLOW = (255, 255, 128)

# chartreuse / lime
DARK_LIME  = ( 64, 128,   0)
LIME       = (128, 255,   0)
LIGHT_LIME = (191, 255, 128)

# green
DARK_GREEN  = (  0, 128,   0)
GREEN       = (  0, 255,   0)
LIGHT_GREEN = (128, 255, 128)

# spring green
DARK_SPRING  = (  0, 128,  64)
SPRING       = (  0, 255, 128)
LIGHT_SPRING = (128, 255, 191)

# cyan
DARK_CYAN  = (  0, 128, 128)
CYAN       = (  0, 255, 255)
LIGHT_CYAN = (128, 255, 255)

# azure
DARK_AZURE  = (  0,  64, 128)
AZURE       = (  0, 128, 255)
LIGHT_AZURE = (128, 191, 255)

# blue
DARK_BLUE  = (  0,   0, 128)
BLUE       = (  0,   0, 255)
LIGHT_BLUE = (128, 128, 255)

# violet
DARK_VIOLET  = ( 64,   0, 128)
VIOLET       = (128,   0, 255)
LIGHT_VIOLET = (191, 128, 255)

# magenta
DARK_MAGENTA  = (128,   0, 128)
MAGENTA       = (255,   0, 255)
LIGHT_MAGENTA = (255, 128, 255)

# rose
DARK_ROSE  = (128,   0,  64)
ROSE       = (255,   0, 128)
LIGHT_ROSE = (255, 128, 191)

LIGHTER = {BLACK: DARK_GREY,                               WHITE: WHITE,
       DARK_GREY: GREY,       GREY: LIGHT_GREY,       LIGHT_GREY: WHITE,
        DARK_RED: RED,         RED: LIGHT_RED,         LIGHT_RED: WHITE,
     DARK_ORANGE: ORANGE,   ORANGE: LIGHT_ORANGE,   LIGHT_ORANGE: WHITE,
     DARK_YELLOW: YELLOW,   YELLOW: LIGHT_YELLOW,   LIGHT_YELLOW: WHITE,
       DARK_LIME: LIME,       LIME: LIGHT_LIME,       LIGHT_LIME: WHITE,
      DARK_GREEN: GREEN,     GREEN: LIGHT_GREEN,     LIGHT_GREEN: WHITE,
     DARK_SPRING: SPRING,   SPRING: LIGHT_SPRING,   LIGHT_SPRING: WHITE,
       DARK_CYAN: CYAN,       CYAN: LIGHT_CYAN,       LIGHT_CYAN: WHITE,
      DARK_AZURE: AZURE,     AZURE: LIGHT_AZURE,     LIGHT_AZURE: WHITE,
       DARK_BLUE: BLUE,       BLUE: LIGHT_BLUE,       LIGHT_BLUE: WHITE,
     DARK_VIOLET: VIOLET,   VIOLET: LIGHT_VIOLET,   LIGHT_VIOLET: WHITE,
    DARK_MAGENTA: MAGENTA, MAGENTA: LIGHT_MAGENTA, LIGHT_MAGENTA: WHITE,
       DARK_ROSE: ROSE,       ROSE: LIGHT_ROSE,       LIGHT_ROSE: WHITE,
}

DARKER = {  WHITE: LIGHT_GREY,                            BLACK: BLACK,
       LIGHT_GREY: GREY,       GREY: DARK_GREY,       DARK_GREY: BLACK,
        LIGHT_RED: RED,         RED: DARK_RED,         DARK_RED: BLACK,
     LIGHT_ORANGE: ORANGE,   ORANGE: DARK_ORANGE,   DARK_ORANGE: BLACK,
     LIGHT_YELLOW: YELLOW,   YELLOW: DARK_YELLOW,   DARK_YELLOW: BLACK,
       LIGHT_LIME: LIME,       LIME: DARK_LIME,       DARK_LIME: BLACK,
      LIGHT_GREEN: GREEN,     GREEN: DARK_GREEN,     DARK_GREEN: BLACK,
     LIGHT_SPRING: SPRING,   SPRING: DARK_SPRING,   DARK_SPRING: BLACK,
       LIGHT_CYAN: CYAN,       CYAN: DARK_CYAN,       DARK_CYAN: BLACK,
      LIGHT_AZURE: AZURE,     AZURE: DARK_AZURE,     DARK_AZURE: BLACK,
       LIGHT_BLUE: BLUE,       BLUE: DARK_BLUE,       DARK_BLUE: BLACK,
     LIGHT_VIOLET: VIOLET,   VIOLET: DARK_VIOLET,   DARK_VIOLET: BLACK,
    LIGHT_MAGENTA: MAGENTA, MAGENTA: DARK_MAGENTA, DARK_MAGENTA: BLACK,
       LIGHT_ROSE: ROSE,       ROSE: DARK_ROSE,       DARK_ROSE: BLACK,
}

#################
# MISCELLANEOUS #
#################

def generateRect(circle_centre, radius):
    left  = round(circle_centre.x - radius)
    top   = round(circle_centre.y - radius)
    width = round(radius * 2)
    return [left, top, width, width]

def sign(n):
    return (n > 0) - (n < 0)

def ccw(a, b, c):
    return (b.x-a.x) * (c.y-a.y) - (b.y-a.y) * (c.x-a.x)

def angleBetween(a, b):
    dot_product = (a.x * b.x) + (a.y * b.y)

    ratio = dot_product / (getMagnitude(a) * getMagnitude(b))
    ratio = max(min(ratio, 1), -1)

    return math.acos(ratio)

def turnDirection(a, b):
    cross_product = (a.x * b.y) - (a.y * b.x)
    return sign(cross_product)

def leftTurn(a, b):
    angle = angleBetween(a, b)

    if turnDirection(a, b) == RIGHT:
        return 2*math.pi - angle

    return angle

def rightTurn(a, b):
    angle = angleBetween(a, b)

    if turnDirection(a, b) == LEFT:
        return 2*math.pi - angle

    return angle


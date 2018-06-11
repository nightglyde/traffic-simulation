import math
import random
import pygame
import string

from collections import deque

random.seed(0)

FRAMES_PER_SECOND = 30
TIME_STEP         = 1000 // FRAMES_PER_SECOND
STEP_TIME         = TIME_STEP / 1000

SCREEN_WIDTH  = 1200 # pixels
SCREEN_HEIGHT = 800

# physics constants
DRAG_CONSTANT    = 0.761
RR_CONSTANT      = DRAG_CONSTANT * 30
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.807

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CAR_MASS   = 1250
CAR_WEIGHT = CAR_MASS * GRAVITY_CONSTANT

BRAKING_FORCE = min(BRAKING_CONSTANT, CAR_WEIGHT)
BRAKING_DECEL = BRAKING_FORCE / CAR_MASS

MAX_SPEED  = 15
SLOW_SPEED = 5

# car size
CAR_LENGTH   = 4.5 # metres
CAR_WIDTH    = 1.8
WHEEL_LENGTH = 0.9
WHEEL_WIDTH  = 0.225
AXLE_LENGTH  = 2.7
AXLE_WIDTH   = 1.5

PIVOT_TO_CENTRE = AXLE_LENGTH/2 # 1.35
PIVOT_TO_FRONT  = PIVOT_TO_CENTRE + CAR_LENGTH/2 # 3.6 + AXLE_LENGTH/2 # 3.6
PIVOT_TO_REAR   = CAR_LENGTH - PIVOT_TO_FRONT # 0.9

PIVOT_TO_AXLE = AXLE_LENGTH #PIVOT_TO_FRONT - (CAR_LENGTH - AXLE_LENGTH) / 2

ARROW_LENGTH      = PIVOT_TO_AXLE #1.35 #2.7
ARROW_WIDTH       = 0.9
ARROW_STEM_LENGTH = ARROW_LENGTH - 0.5
ARROW_STEM_WIDTH  = 0.45

LIGHT_FRONT  = PIVOT_TO_FRONT - 0.1
LIGHT_BACK   = LIGHT_FRONT    - 0.2

LIGHT_OUTER = CAR_WIDTH/2 #- 0.1
LIGHT_MID   = LIGHT_OUTER - 0.3
LIGHT_INNER = LIGHT_MID   - 0.3

SAFETY_GAP = 2 # gap between cars

MIN_DIST_APART = SAFETY_GAP + CAR_LENGTH

# (not currently in use
MAX_STOPPING_DIST = 15
# must be big enough so that
# getSpeedToStop(MAX_STOPPING_DIST, MAX_SPEED) >= MAX_SPEED
DIST_APART_THRESHOLD = MIN_DIST_APART + MAX_STOPPING_DIST
# )

# turns
LEFT   = -1
RIGHT  = 1
CENTRE = 0

# traffic control
RED_LIGHT   = 0
AMBER_LIGHT = 1
GREEN_LIGHT = 2

# traffic control modes
TRAFFIC_LIGHTS_MODE         = 0
VIRTUAL_TRAFFIC_LIGHTS_MODE = 1
MY_TRAFFIC_CONTROLLER_MODE  = 2

#CONTROLLER_MODE = TRAFFIC_LIGHTS_MODE
CONTROLLER_MODE = VIRTUAL_TRAFFIC_LIGHTS_MODE
#CONTROLLER_MODE = MY_TRAFFIC_CONTROLLER_MODE

#################
# MESSAGE TYPES #
#################

# traffic lights
VISIBLE_DETAILS = 0

# virtual traffic lights
VTL_STATUS        = 1
VTL_GREEN_REQUEST = 2
VTL_ACKNOWLEDGE   = 3
VTL_REFUSAL       = 4
VTL_RETRY         = 5
VTL_GREEN         = 6

# my traffic controller
MTC_CAR_STATUS          =  7 #
MTC_QUERY_STATUS        =  8
MTC_INTERSECTION_STATUS =  9
MTC_CHANGE_LEADER       = 10 #
MTC_CROSS_INTERSECTION  = 11 #
MTC_LEAVE_INTERSECTION  = 12 #

#####################
# MESSAGE ADDRESSES #
#####################
SEND_TO_ALL    = 0
LINE_OF_SIGHT  = 1
CONTROL_CENTRE = 2
# for direct messages, use the destination car's name

########
# MISC #
########
SIGHT_RADIUS = 50 # metres, maximum range for line-of-sight messages
# must be at least
# sqrt(2*((ROAD_WIDTH + CORNER_OFFSET*2 + CAR_LENGTH - HALF_LANE)**2))

# traffic lights
AMBER_PHASE    = 4000
RED_PHASE      = AMBER_PHASE + 1000
CYCLE_DURATION = RED_PHASE   + 1000

# virtual traffic lights
VTL_NR_MAX     = 10
VTL_NF_DEFAULT = 5

VTL_THRESHOLD   = 20
VTL_LEADER_DIST = 10
VTL_FOLLOW_DIST = MIN_DIST_APART + 2#10

VTL_TIMEOUT = 1000#100#5000

VTL_INTERSECTION_LEADER = 0
VTL_LEADER              = 1
VTL_FOLLOWER            = 2
VTL_CROSSING            = 3

VTL_NO_INTERSECTION   = 0
VTL_JOIN_INTERSECTION = 1
VTL_CALCULATE_LEADERS = 2
VTL_GET_APPROVALS     = 3
VTL_CHOOSE_NEW_LEADER = 4

# my traffic controller
MTC_CROSS_TIME = 1000

##########
# VECTOR #
##########

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left90(self):
        return Vector(-self.y, self.x)
        #return Vector(self.y, -self.x)

    def right90(self):
        return Vector(self.y, -self.x)
        #return Vector(-self.y, self.x)

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm(self):
        mag = self.mag()
        return Vector(self.x/mag, self.y/mag)

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

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

def getVector(angle):
    return Vector(math.cos(angle.value), math.sin(angle.value))

#VECTOR_0      = Vector(0, 0)
SCREEN_CENTRE = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#SCREEN_TOP_LEFT     = Vector(0,            0)
#SCREEN_TOP_RIGHT    = Vector(SCREEN_WIDTH, 0)
#SCREEN_BOTTOM_LEFT  = Vector(0,            SCREEN_HEIGHT)
#SCREEN_BOTTOM_RIGHT = Vector(SCREEN_WIDTH, SCREEN_HEIGHT)

#########
# ANGLE #
#########

class Angle:
    def __init__(self, value):
        value = value % (2*math.pi)

        if value > math.pi:
            value -= math.pi*2
        #elif value < -math.pi:
        #    value += math.pi*2
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
        return "Angle({})".format(self.value)

def getAngle(vector):
    x = vector.x
    y = vector.y
    if x == 0:
        if y < 0:
            angle = -math.pi / 2
        else:
            angle = math.pi / 2
    else:
        angle = math.atan(y / x)

    if x < 0:
        angle += math.pi
    return Angle(angle)

def getPolar(vector):
    x = vector.x
    y = vector.y
    magnitude = math.sqrt(x**2 + y**2)
    if x == 0:
        if y < 0:
            angle = -math.pi / 2
        else:
            angle = math.pi / 2
    else:
        angle = math.atan(y / x)

    if x < 0:
        angle += math.pi
    return Angle(angle), magnitude

ANGLE_0  = Angle(math.radians(0))
#ANGLE_1  = Angle(math.radians(1))
#ANGLE_5  = Angle(math.radians(5))
#ANGLE_10 = Angle(math.radians(10))
#ANGLE_15 = Angle(math.radians(15))
#ANGLE_20 = Angle(math.radians(20))
#ANGLE_25 = Angle(math.radians(25))
ANGLE_30 = Angle(math.radians(30))
#ANGLE_35 = Angle(math.radians(35))
#ANGLE_40 = Angle(math.radians(40))
#ANGLE_45 = Angle(math.radians(45))
#ANGLE_50 = Angle(math.radians(50))
#ANGLE_55 = Angle(math.radians(55))
#ANGLE_60 = Angle(math.radians(60))
#ANGLE_65 = Angle(math.radians(65))
#ANGLE_70 = Angle(math.radians(70))
#ANGLE_75 = Angle(math.radians(75))
#ANGLE_80 = Angle(math.radians(80))
#ANGLE_85 = Angle(math.radians(85))
ANGLE_90 = Angle(math.radians(90))

#ANGLE_120 = Angle(math.radians(120))
#ANGLE_180 = Angle(math.radians(180))

MAX_WHEEL_ANGLE = ANGLE_30
TURN_RADIUS     = PIVOT_TO_AXLE / math.sin(MAX_WHEEL_ANGLE.value)

#TINY_ANGLE = math.radians(1)

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

# amber
AMBER = (255, 191, 0)

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

CAR_COLOURS = [
    RED,   ORANGE, YELLOW,  LIME,
    GREEN, SPRING, CYAN,    AZURE,
    BLUE,  VIOLET, MAGENTA, ROSE,
]

def nextColour(cars_list):

    colour_indices = {colour: 0 for colour in CAR_COLOURS}

    while True:

        colour_counts = {colour: 0 for colour in CAR_COLOURS}
        for car in cars_list:
            colour_counts[car.colour] += 1

        min_count = 10000000000
        for colour in colour_counts:
            min_count = min(colour_counts[colour], min_count)

        random.shuffle(CAR_COLOURS)
        for colour in CAR_COLOURS:
            if colour_counts[colour] == min_count:

                index = colour_indices[colour]
                colour_indices[colour] += 1

                name = COLOUR_NAME[colour] + "_" + str(index)
                yield colour, name

                break

COLOUR_NAME = {RED:   "RED", ORANGE: "ORA", YELLOW:  "YEL", LIME:  "LIM",
               GREEN: "GRN", SPRING: "SPR", CYAN:    "CYA", AZURE: "AZU",
               BLUE:  "BLU", VIOLET: "VIO", MAGENTA: "MAG", ROSE:  "ROS"}

NAME_TO_COLOUR = {"RED": RED,   "ORA": ORANGE, "YEL": YELLOW,  "LIM": LIME,
                  "GRN": GREEN, "SPR": SPRING, "CYA": CYAN,    "AZU": AZURE,
                  "BLU": BLUE,  "VIO": VIOLET, "MAG": MAGENTA, "ROS": ROSE}

#################
# MISCELLANEOUS #
#################
def getTurn(entrance, exit):
    return ((exit - entrance) % 4 + 2) % 3 - 1

def getExit(entrance, turn):
    return ((turn + 1) % 3 + entrance + 1) % 4

def getSpeedToStop(distance, curr_speed):
    dt = TIME_STEP / 1000
    new_speed = curr_speed + (MAX_ENGINE_FORCE / CAR_MASS) * dt

    distance -= new_speed * dt
    if distance <= 0:
        return 0

    speed_to_stop = math.sqrt(2 * BRAKING_DECEL * distance)
    return min(speed_to_stop, MAX_SPEED)

def getStopDistance(speed):
    if speed <= 0:
        return 0
    return (speed**2) / (2 * BRAKING_DECEL)

def getTurningCircle(direction, position, angle, radius=TURN_RADIUS):
    if direction == LEFT:
        centre_vector = getVector(angle - ANGLE_90) * radius
    else:
        centre_vector = getVector(angle + ANGLE_90) * radius
    return position + centre_vector

def sign(n):
    return (n > 0) - (n < 0)

def ccw(a, b, c):
    return (b.x-a.x) * (c.y-a.y) - (b.y-a.y) * (c.x-a.x)

def dotProduct(a, b):
    return a.x * b.x + a.y * b.y

def crossProduct(a, b):
    return a.x * b.y - a.y * b.x

def turnDirection(a, b):
    return sign(crossProduct(a, b))

def generateRect(circle_centre, radius, zoom):
    top, left = zoom.getDrawable(circle_centre - Vector(radius, radius))
    width = zoom.scaleDistance(radius) * 2
    return [top, left, width, width]


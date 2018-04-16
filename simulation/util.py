import math
import random
import pygame

from collections import deque

FRAMES_PER_SECOND = 30
TIME_STEP         = 1000 // FRAMES_PER_SECOND
STEP_TIME         = TIME_STEP / 1000

MAX_CARS            = 12
CAR_ADDING_INTERVAL = TIME_STEP * 100

#ACTION_DELAY = 500
#ACTION_TIME  = ACTION_DELAY / 1000

SCREEN_WIDTH  = 1200 # pixels
SCREEN_HEIGHT = 800

# these variables are modified later on in this file
WORLD_WIDTH  = 100 # metres
WORLD_HEIGHT = 100 # must be at least 30

ROAD_WIDTH = 3.5
#COLLISION_DISTANCE = 10
#BUBBLE_SIZE = 0.5
#BUBBLE_DIAG = math.sqrt(BUBBLE_SIZE**2 / 2)

CAR_LENGTH   = 4.5
CAR_WIDTH    = 1.8
WHEEL_LENGTH = 0.9
WHEEL_WIDTH  = 0.225
AXLE_LENGTH  = 2.7
AXLE_WIDTH   = CAR_WIDTH - WHEEL_WIDTH

PIVOT_TO_FRONT = CAR_LENGTH/2 + AXLE_LENGTH/2 # 3.6
PIVOT_TO_REAR  = CAR_LENGTH - PIVOT_TO_FRONT

PIVOT_TO_AXLE = PIVOT_TO_FRONT - (CAR_LENGTH - AXLE_LENGTH) / 2

ARROW_LENGTH      = PIVOT_TO_AXLE #1.35 #2.7
ARROW_WIDTH       = 0.9
ARROW_STEM_LENGTH = ARROW_LENGTH - 0.5
ARROW_STEM_WIDTH  = 0.45

LEFT   = -1
RIGHT  = 1
CENTRE = 0

# messaging
SEND_TO_ALL = -1

# public message types
CURRENT_DETAILS = 0
FUTURE_DETAILS  = 1

# private message types

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
        return repr([self.x, self.y])

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
        return repr(math.degrees(self.value))

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
ANGLE_1  = Angle(math.radians(1))
ANGLE_5  = Angle(math.radians(5))
ANGLE_10 = Angle(math.radians(10))
ANGLE_15 = Angle(math.radians(15))
ANGLE_20 = Angle(math.radians(20))
ANGLE_25 = Angle(math.radians(25))
ANGLE_30 = Angle(math.radians(30))
ANGLE_35 = Angle(math.radians(35))
ANGLE_40 = Angle(math.radians(40))
ANGLE_45 = Angle(math.radians(45))
ANGLE_50 = Angle(math.radians(50))
ANGLE_55 = Angle(math.radians(55))
ANGLE_60 = Angle(math.radians(60))
ANGLE_65 = Angle(math.radians(65))
ANGLE_70 = Angle(math.radians(70))
ANGLE_75 = Angle(math.radians(75))
ANGLE_80 = Angle(math.radians(80))
ANGLE_85 = Angle(math.radians(85))
ANGLE_90 = Angle(math.radians(90))

ANGLE_120 = Angle(math.radians(120))
ANGLE_180 = Angle(math.radians(180))

MAX_WHEEL_ANGLE = ANGLE_30
TURN_RADIUS     = PIVOT_TO_AXLE / math.sin(MAX_WHEEL_ANGLE.value)

TINY_ANGLE = math.radians(1)

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

CAR_COLOURS = [
    RED,   ORANGE, YELLOW,  LIME,
    GREEN, SPRING, CYAN,    AZURE,
    BLUE,  VIOLET, MAGENTA, ROSE,
]

def nextColour():
    index = 0
    while True:
        random.shuffle(CAR_COLOURS)
        for colour in CAR_COLOURS:
            name = COLOUR_NAME[colour] + "_" + str(index)
            yield colour, name
        index += 1

COLOUR_NAME = {RED:   "RED", ORANGE: "ORA", YELLOW:  "YEL", LIME:  "LIM",
               GREEN: "GRN", SPRING: "SPR", CYAN:    "CYA", AZURE: "AZU",
               BLUE:  "BLU", VIOLET: "VIO", MAGENTA: "MAG", ROSE:  "ROS"}

NAME_TO_COLOUR = {"RED": RED,   "ORA": ORANGE, "YEL": YELLOW,  "LIM": LIME,
                  "GRN": GREEN, "SPR": SPRING, "CYA": CYAN,    "AZU": AZURE,
                  "BLU": BLUE,  "VIO": VIOLET, "MAG": MAGENTA, "ROS": ROSE}

#################
# MISCELLANEOUS #
#################

#def generateCarHull(position, angle):
#    forward = getVector(angle)
#    left    = forward.left90() * CAR_WIDTH/2
#
#    front = position + forward * PIVOT_TO_FRONT
#    rear  = position - forward * PIVOT_TO_REAR
#    return [front - left, front + left, rear + left, rear - left]

def getTurningCircle(direction, car, radius=TURN_RADIUS):
    if direction == LEFT:
        centre_vector = getVector(car.angle - ANGLE_90) * radius
    else:
        centre_vector = getVector(car.angle + ANGLE_90) * radius
    return car.position + centre_vector

def generateRect(circle_centre, radius, zoom):
    top, left = zoom.getDrawable(circle_centre - Vector(radius, radius))
    width = zoom.scaleDistance(radius) * 2
    return [top, left, width, width]

def sign(n):
    return (n > 0) - (n < 0)

def ccw(a, b, c):
    return (b.x-a.x) * (c.y-a.y) - (b.y-a.y) * (c.x-a.x)

def dotProduct(a, b):
    return a.x * b.x + a.y * b.y

def crossProduct(a, b):
    return a.x * b.y - a.y * b.x

def angleBetween(a, b):
    dot_product = dotProduct(a, b)
    ratio = dot_product / a.mag() * b.mag()
    ratio = max(min(ratio, 1), -1)
    return math.acos(ratio)

def turnDirection(a, b):
    return sign(crossProduct(a, b))

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

def getIntersection(a, b, x, y):

    ab = b-a
    xy = y-x
    ax = z-a

    ab_cross_xy = crossProduct(ab, xy)
    ax_cross_ab = crossProduct(ax, ab)

    if ab_cross_xy == 0.0:
        # lines are parallel

        if ax_cross_ab == 0.0:
            # lines are collinear
            pass

    else:
        # lines are not parallel
        xy_dist = ax_cross_ab / ab_cross_xy
        if 0 <= xy_dist <= 1:
            ab_dist = crossProduct(ax, xy) / ab_cross_xy
            if 0 <= ab_dist <= 1:
                intersection = a + ab.norm() * ab_dist
                return [a, intersection, b], [x, intersection, y]

    return [a, b], [x, y]

def getBoundaryLines(shapes):
    num_shapes = len(shapes)

    for i in range(num_shapes-1):
        shape_i = shapes[i].hull

        num_i = len(shape_i)
        for a in range(num_i):
            point_a = shape_i[a]
            point_b = shape_i[(a+1) % num_i]

            for j in range(i+1, num_shapes):
                shape_j = shapes[j].hull

                num_j = len(shape_j)
                for x in range(num_j):
                    point_x = shape_j[x]
                    point_y = shape_j[(x+1) % num_j]

                    ab_points, xy_points = getIntersection(point_a, point_b,
                                                           point_x, point_y)

def crashCircle(line, circle_centre, direction, details):
    point_i, point_j = line

    ij      = point_j - point_i
    ij_dist = ij.mag()
    ij_norm = ij / ij_dist

    ic      = circle_centre - point_i
    jc      = circle_centre - point_j
    ic_dist = ic.mag()
    jc_dist = jc.mag()

    if max(ic_dist, jc_dist) < details[-1][0]: # smallest radius
        return None

    near_dist = dotProduct(ic, ij_norm)
    nearest   = point_i + ij_norm * near_dist
    circ_dist = (nearest - circle_centre).mag()

    if near_dist <= 0:
        if ic_dist > details[0][0]: # biggest radius
            return None
    elif near_dist >= ij_dist:
        if jc_dist > details[0][0]:
            return None
    else:
        if circ_dist > details[0][0]:
            return None

    closest_crash = None
    for i in range(len(details)):
        radius, car_angle, speed, car_point = details[i]

        if circ_dist > radius:
            continue

        offset = math.sqrt(radius**2 - circ_dist**2)
        dists  = [near_dist - offset, near_dist + offset]

        for dist in dists:
            if 0 <= dist <= ij_dist:
                crash_point = point_i + ij_norm * dist

                if (crash_point - car_point).mag() > COLLISION_DISTANCE:
                    continue

                abs_angle = getAngle(crash_point - circle_centre)

                if direction == LEFT:
                    rel_angle = (abs_angle - car_angle).norm()
                else:
                    rel_angle = (car_angle - abs_angle).norm()

                time  = rel_angle * radius / speed
                crash = (time, car_point, crash_point, line)
                if closest_crash is None or crash < closest_crash:
                    closest_crash = crash
    return closest_crash

def crashLine(line, car_points, forward, speed):
    closest_crash = None

    point_i, point_j = line

    ij = point_j - point_i
    f_cross_ij = crossProduct(forward, ij)

    if f_cross_ij == 0.0:
        # lines are parallel
        print("Z")

        for car_point in car_points:
            ic = point_i - car_point

            ic_cross_f = crossProduct(ic, forward)
            if ic_cross_f == 0.0:
                # collinear
                ij_dot_f = dotProduct(ij, forward)

                if ij_dot_f > 0:
                    crash_point = point_i
                    print("A")
                else:
                    crash_point = point_j
                    ic = crash_point - car_point
                    print("B")

                f_dot_f = dotProduct(forward, forward)
                ray_dist = dotProduct(ic, forward) / f_dot_f

                if 0 <= ray_dist <= COLLISION_DISTANCE:
                    time  = ray_dist / speed
                    crash = (time, car_point, crash_point, line)
                    if closest_crash is None or crash < closest_crash:
                        closest_crash = crash
    else:
        # lines are not parallel
        for car_point in car_points:
            ic = point_i - car_point

            ij_dist = crossProduct(ic, forward) / f_cross_ij
            if 0 <= ij_dist <= 1:

                ray_dist = crossProduct(ic, ij)     / f_cross_ij
                if 0 <= ray_dist <= COLLISION_DISTANCE:
                    time        = ray_dist / speed
                    crash_point = car_point + forward * ray_dist

                    crash = (time, car_point, crash_point, line)
                    if closest_crash is None or crash < closest_crash:
                        closest_crash = crash
    return closest_crash

starting_positions = [
    Vector(12.5,12.5), Vector(37.5,12.5), Vector(62.5,12.5), Vector(87.5,12.5),
    Vector(12.5,37.5), Vector(37.5,37.5), Vector(62.5,37.5), Vector(87.5,37.5),
    Vector(12.5,62.5), Vector(37.5,62.5), Vector(62.5,62.5), Vector(87.5,62.5),
    Vector(12.5,87.5), Vector(37.5,87.5), Vector(62.5,87.5), Vector(87.5,87.5),
]

waypoint_options = [
                                          Vector(12.5,17.5), Vector(17.5,12.5),
    Vector(32.5,12.5),                    Vector(37.5,17.5), Vector(42.5,12.5),
    Vector(57.5,12.5),                    Vector(62.5,17.5), Vector(67.5,12.5),
    Vector(82.5,12.5),                    Vector(87.5,17.5),

                       Vector(12.5,32.5), Vector(12.5,42.5), Vector(17.5,37.5),
    Vector(32.5,37.5), Vector(37.5,32.5), Vector(37.5,42.5), Vector(42.5,37.5),
    Vector(57.5,37.5), Vector(62.5,32.5), Vector(62.5,42.5), Vector(67.5,37.5),
    Vector(82.5,37.5), Vector(87.5,32.5), Vector(87.5,42.5),

                       Vector(12.5,57.5), Vector(12.5,67.5), Vector(17.5,62.5),
    Vector(32.5,62.5), Vector(37.5,57.5), Vector(37.5,67.5), Vector(42.5,62.5),
    Vector(57.5,62.5), Vector(62.5,57.5), Vector(62.5,67.5), Vector(67.5,62.5),
    Vector(82.5,62.5), Vector(87.5,57.5), Vector(87.5,67.5),

                       Vector(12.5,82.5),                    Vector(17.5,87.5),
    Vector(32.5,87.5), Vector(37.5,82.5),                    Vector(42.5,87.5),
    Vector(57.5,87.5), Vector(62.5,82.5),                    Vector(67.5,87.5),
    Vector(82.5,87.5), Vector(87.5,82.5),

    Vector(25, 12.5), Vector(50, 12.5), Vector(75, 12.5),
    Vector(25, 37.5), Vector(50, 37.5), Vector(75, 37.5),
    Vector(25, 62.5), Vector(50, 62.5), Vector(75, 62.5),
    Vector(25, 87.5), Vector(50, 87.5), Vector(75, 87.5),

    Vector(12.5, 25), Vector(12.5, 50), Vector(12.5, 75),
    Vector(37.5, 25), Vector(37.5, 50), Vector(37.5, 75),
    Vector(62.5, 25), Vector(62.5, 50), Vector(62.5, 75),
    Vector(87.5, 25), Vector(87.5, 50), Vector(87.5, 75),

]

# generate grass
border_size = 10
road_size   = ROAD_WIDTH * 2
block_size  = 30
corner_offset = TURN_RADIUS
num_blocks = 3#3

next_block = block_size + road_size

world_size = border_size + road_size + next_block*num_blocks + border_size

WORLD_WIDTH  = world_size
WORLD_HEIGHT = world_size

predefined_grass = [
    [
        Vector(0, 0),
        Vector(world_size, 0),
        Vector(world_size, border_size),
        Vector(0, border_size),
    ],
    [
        Vector(0, 0),
        Vector(border_size, 0),
        Vector(border_size, world_size),
        Vector(0, world_size),
    ],
    [
        Vector(world_size-border_size, 0),
        Vector(world_size, 0),
        Vector(world_size, world_size),
        Vector(world_size-border_size, world_size),
    ],
    [
        Vector(0, world_size-border_size),
        Vector(world_size, world_size-border_size),
        Vector(world_size, world_size),
        Vector(0, world_size),
    ],
]

# block
x_start = border_size + road_size
y_start = border_size + road_size
for i in range(num_blocks):
    x = x_start + next_block * i
    for j in range(num_blocks):
        y = y_start + next_block * j

        predefined_grass.append([
            Vector(x+corner_offset, y),
            Vector(x+block_size-corner_offset, y),
            Vector(x+block_size, y+corner_offset),
            Vector(x+block_size, y+block_size-corner_offset),
            Vector(x+block_size-corner_offset, y+block_size),
            Vector(x+corner_offset, y+block_size),
            Vector(x, y+block_size-corner_offset),
            Vector(x, y+corner_offset),
        ])

lane_size = road_size / 2
half_lane = road_size / 4

RAMP_POSITION = Vector(0,           border_size + half_lane)
RAMP_END      = Vector(border_size, border_size + half_lane)

RAMP_ANGLE = getAngle(RAMP_END - RAMP_POSITION)


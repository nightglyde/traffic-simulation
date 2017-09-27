from util import *

from obstacle import Obstacle

HULL_POINTS = 8

class Waypoint(Obstacle):
    def __init__(self, controller, position, radius):
        self.controller = controller
        self.world      = controller.world
        self.colour     = controller.colour

        self.position     = position
        self.outer_radius = radius
        self.inner_radius = radius * 0.8
        self.generateHull()

        self.time  = None
        self.path  = None
        self.car   = None
        self.angle = None

    def generateHull(self):
        self.hull = []
        for i in range(HULL_POINTS):
            angle  = Angle(2*math.pi * i/HULL_POINTS)
            vector = getVector(angle) * self.outer_radius
            self.hull.append(self.position + vector)

    def alt_update(self, time, path, pos, angle, speed,
               velocity, engine_force, wheel_angle, braking, reverse):

        self.time = time
        self.path = path

        self.car_pos = pos
        self.angle   = angle
        self.speed   = speed

        self.velocity     = velocity
        self.engine_force = engine_force
        self.wheel_angle  = wheel_angle
        self.braking      = braking
        self.reverse      = reverse

    def update(self, time, path, car):
        self.time  = time
        self.path  = path
        self.car   = car
        self.angle = car.angle

    def limited_update(self, time, path, angle):
        self.time  = time
        self.path  = path
        self.angle = angle

    def drawPath(self):
        if len(self.path) > 1:
            path = [self.world.getDrawable(point) for point in self.path]
            pygame.draw.lines(self.world.screen, self.colour, False, path, 1)

    def draw(self):
        inner_radius = self.world.scaleDistance(self.inner_radius)
        if inner_radius <= 0:
            return
        outer_radius = self.world.scaleDistance(self.outer_radius)

        screen = self.world.screen
        pos    = self.position

        colour       = self.colour
        light_colour = LIGHTER[colour]
        dark_colour  = DARKER[colour]

        centre = self.world.getDrawable(pos)
        pygame.draw.circle(screen, colour,       centre, outer_radius)
        pygame.draw.circle(screen, light_colour, centre, inner_radius)
        pygame.draw.circle(screen, dark_colour,  centre, outer_radius, 1)
        pygame.draw.circle(screen, dark_colour,  centre, inner_radius, 1)

        front = pos + getVector(self.angle)             * self.inner_radius
        right = pos + getVector(self.angle + ANGLE_120) * self.inner_radius
        left  = pos + getVector(self.angle - ANGLE_120) * self.inner_radius

        arrow = [centre,
            self.world.getDrawable(right),
            self.world.getDrawable(front),
            self.world.getDrawable(left)]
        pygame.draw.polygon(screen, colour,  arrow)
        pygame.draw.polygon(screen, dark_colour, arrow, 1)


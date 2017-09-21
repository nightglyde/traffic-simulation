from util import *

from obstacle import Obstacle

HULL_POINTS = 12

class Waypoint(Obstacle):
    def __init__(self, controller, position, radius):
        self.controller = controller
        self.world      = controller.world

        self.position     = position
        self.outer_radius = radius
        self.inner_radius = radius * 0.8
        self.generateHull()

        self.angle = None
        self.time  = None
        self.turn  = None
        self.arcs  = None
        self.tans  = None

    def generateHull(self):
        self.hull = []
        for i in range(HULL_POINTS):
            angle  = Angle(2*math.pi * i/HULL_POINTS)
            vector = getVector(angle) * self.outer_radius
            self.hull.append(self.position + vector)

    def update(self, angle, time, turn, arcs, tans):
        self.angle = angle
        self.time  = time
        self.turn  = turn
        self.arcs  = arcs
        self.tans  = tans

    def drawPath(self):
        screen = self.world.screen
        colour = DARKER[self.controller.colour]

        for circle_centre, angle_1, angle_2 in self.arcs:
            rect    = generateRect(circle_centre, TURN_RADIUS, self.world)
            angle_1 = angle_1.norm()
            angle_2 = angle_2.norm()
            pygame.draw.arc(screen, colour, rect, angle_1, angle_2, 1)

        for point_1, point_2 in self.tans:
            point_1 = self.world.getDrawable(point_1)
            point_2 = self.world.getDrawable(point_2)
            pygame.draw.line(screen, colour, point_1, point_2, 1)

    def draw(self):
        screen = self.world.screen
        pos    = self.position

        colour       = self.controller.colour
        light_colour = LIGHTER[colour]
        dark_colour  = DARKER[colour]

        outer_radius = self.world.scaleDistance(self.outer_radius)
        inner_radius = self.world.scaleDistance(self.inner_radius)

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


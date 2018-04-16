from util import *
from obstacle import Obstacle, convexHull

WAYPOINT_RADIUS     = ROAD_WIDTH / 2
FUTURE_POINT_RADIUS = CAR_WIDTH  / 2

class Waypoint:
    def __init__(self, controller, position, angle):
        self.world    = controller.world
        self.colour   = controller.colour
        self.position = position
        self.angle    = angle

        self.radius       = WAYPOINT_RADIUS
        self.inner_radius = self.radius * 0.8

    def checkInside(self, point):
        return (self.position - point).mag() <= self.radius

    def checkBorder(self, obstacle):
        for point in obstacle.hull:
            if self.checkInside(point):
                return True

        num_points = len(obstacle.hull)
        for i in range(num_points):
            point_i = obstacle.hull[i]
            point_j = obstacle.hull[(i+1) % num_points]

            ij      = point_j - point_i
            ic      = self.position - point_i
            ij_norm = ij.norm()

            nearest_dist = dotProduct(ic, ij_norm)
            if 0 < nearest_dist < ij.mag():
                nearest_point = point_i + ij_norm * nearest_dist
                if self.checkInside(nearest_point):
                    return True

        return False

    def checkCollision(self, obstacle):
        if obstacle.checkInside(self.position):
            return True

        return self.checkBorder(obstacle)

    def draw(self):
        inner_radius = self.world.scaleDistance(self.inner_radius)
        if inner_radius <= 0:
            return
        outer_radius = self.world.scaleDistance(self.radius)

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

class FuturePoint(Obstacle):
    def __init__(self, car, prev_hull):
        self.name     = car.name # temporary, cos i don't know how to deal with
                                 # giving way when they're parallel yet
        self.world    = car.world
        self.colour   = car.colour
        self.position = car.centre
        self.angle    = car.angle

        self.orig_hull = car.hull
        self.hull      = convexHull(self.orig_hull + prev_hull)

        self.radius       = FUTURE_POINT_RADIUS
        self.inner_radius = self.radius * 0.8

        self.time = car.time

    def draw(self):
        inner_radius = self.world.scaleDistance(self.inner_radius)
        if inner_radius <= 0:
            return
        outer_radius = self.world.scaleDistance(self.radius)

        screen = self.world.screen
        pos    = self.position

        colour       = self.colour
        light_colour = LIGHTER[colour]
        dark_colour  = DARKER[colour]

        centre = self.world.getDrawable(pos)
        #pygame.draw.circle(screen, colour,       centre, outer_radius)
        #pygame.draw.circle(screen, light_colour, centre, inner_radius)
        #pygame.draw.circle(screen, dark_colour,  centre, outer_radius, 1)
        #pygame.draw.circle(screen, dark_colour,  centre, inner_radius, 1)

        front = pos + getVector(self.angle)             * self.inner_radius
        right = pos + getVector(self.angle + ANGLE_120) * self.inner_radius
        left  = pos + getVector(self.angle - ANGLE_120) * self.inner_radius

        arrow = [centre,
                 self.world.getDrawable(right),
                 self.world.getDrawable(front),
                 self.world.getDrawable(left)]
        pygame.draw.polygon(screen, colour,  arrow)
        pygame.draw.polygon(screen, dark_colour, arrow, 1)


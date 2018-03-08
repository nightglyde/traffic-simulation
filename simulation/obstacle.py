from util import *

def convexHull(points):
    if len(points) <= 2:
        return sorted(set(points))

    points.sort()
    if points[0] == points[-1]:
        return [points[0]]

    hull = [points[0], points[1]]
    limit = len(hull)
    for i in range(2, len(points)):
        point = points[i]
        while len(hull) >= limit and ccw(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    hull.append(points[-2])
    limit = len(hull)
    for i in range(len(points)-3, -1, -1):
        point = points[i]
        while len(hull) >= limit and ccw(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    hull.pop()

    return hull

class Obstacle:
    def __init__(self, world, name, colour, points):
        self.world   = world
        self.name    = name
        self.colour  = colour
        self.hull    = convexHull(points)

    def checkInside(self, point):
        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % len(self.hull)]
            if ccw(point_i, point, point_k) > 0:
                return False
        return True

    def checkCollision(self, other):
        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % len(self.hull)]

            for point_j in other.hull:
                if ccw(point_i, point_j, point_k) <= 0:
                    break
            else:
                return False
        for i in range(len(other.hull)):
            point_i = other.hull[i]
            point_k = other.hull[(i+1) % len(other.hull)]

            for point_j in self.hull:
                if ccw(point_i, point_j, point_k) <= 0:
                    break
            else:
                return False
        return True

    def linesWithinRadius(self, centre, radius, forward):
        lines = []

        if self.checkInside(centre):
            return lines

        num_points = len(self.hull)
        for i in range(num_points):
            point_i = self.hull[i]
            point_j = self.hull[(i+1) % num_points]

            ic = centre - point_i
            jc = centre - point_j
            if angleBetween(forward, ic) < math.pi and \
               angleBetween(forward, jc) < math.pi:
                continue

            if ic.mag() <= radius:
                lines.append((point_i, point_j))
                continue

            if jc.mag() <= radius:
                lines.append((point_i, point_j))
                continue

            ij      = point_j - point_i
            ij_norm = ij.norm()

            nearest_dist = dotProduct(ic, ij_norm)
            if 0 < nearest_dist < ij.mag():
                nearest_point = point_i + ij_norm * nearest_dist
                if (centre - nearest_point).mag() <= radius:
                    lines.append((point_i, point_j))

        return lines

    def draw(self, outline=False):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, self.colour, polygon)
        if outline:
            pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)

    def drawOutline(self):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)


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
    def __init__(self, world, name, colour, points, outline=True):
        self.world   = world
        self.name    = name
        self.colour  = colour
        self.hull    = convexHull(points)
        self.outline = outline

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

    def checkInside(self, point):
        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % len(self.hull)]
            if ccw(point_i, point, point_k) > 0:
                return False
        return True

    def findNearestLine(self, point):
        best_line = None
        best_dist = None
        safe_dist = ROAD_WIDTH/2
        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_k = self.hull[(i+1) % len(self.hull)]
            dist_ij  = getMagnitude(point_i - point)
            dist_kj  = getMagnitude(point_k - point)
            dist_ik  = getMagnitude(point_i - point_k)
            if max(dist_ij, dist_kj)**2 - safe_dist**2 <= dist_ik**2:
                dist = ccw(point_i, point, point_k) / dist_ik
            else:
                dist = min(dist_ij, dist_ik)

            if best_dist is None or abs(dist) < abs(best_dist):
                best_dist = dist
                best_line = (point_i, point_k)

        if best_line:
            angle, mag = getPolar((point - best_line[1]))
            angle_away = Angle(math.acos(best_dist/mag)) + angle
            vec = getVector(angle_away)
        else:
            vec = None
        return best_line, best_dist, vec

    def draw(self):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, self.colour, polygon)

        if self.outline:
            pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)


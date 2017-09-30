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
            dist_ij  = (point_i - point).mag()
            dist_kj  = (point_k - point).mag()
            dist_ik  = (point_i - point_k).mag()
            if max(dist_ij, dist_kj)**2 - safe_dist**2 <= dist_ik**2:
                dist = ccw(point_i, point, point_k) / dist_ik
            else:
                dist = min(dist_ij, dist_ik)

            if best_dist is None or abs(dist) < abs(best_dist):
                best_dist = dist
                best_line = (point_i, point_k)

        if best_line:
            angle, mag = getPolar(point - best_line[1])
            angle_away = Angle(math.acos(best_dist/mag)) + angle
            vec = getVector(angle_away)
        else:
            vec = None
        return best_line, best_dist, vec

    def crashCircle(self, circle_centre, direction, radii, angles, speeds):
        least_time = -1
        results    = (None, None, None)

        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_j = self.hull[(i+1) % len(self.hull)]

            i_j      = point_j - point_i
            i_j_dist = i_j.mag()
            i_j_norm = i_j / i_j_dist

            c_i      = circle_centre - point_i
            c_j      = circle_centre - point_j
            c_i_dist = c_i.mag()
            c_j_dist = c_j.mag()

            if max(c_i_dist, c_j_dist) < radii[-1]:
                continue

            near_dist = dotProduct(c_i, i_j_norm)
            nearest   = point_i + i_j_norm * near_dist
            circ_dist = (nearest - circle_centre).mag()

            if near_dist <= 0:
                if c_i_dist > radii[0]:
                    continue
            elif near_dist >= i_j_dist:
                if c_j_dist > radii[0]:
                    continue
            else:
                if circ_dist > radii[0]:
                    continue

            for i in range(len(radii)):
                radius = radii[i]
                if circ_dist > radius:
                    break
                angle  = angles[i]
                speed  = speeds[i]

                offset = math.sqrt(radius**2 - circ_dist**2)
                dists  = [near_dist - offset, near_dist + offset]

                for dist in dists:
                    if 0 <= dist <= i_j_dist:
                        point     = point_i + i_j_norm * dist
                        abs_angle = getAngle(point - circle_centre)
                        if direction == LEFT:
                            rel_angle = (abs_angle - angle).norm()
                        else:
                            rel_angle = (angle - abs_angle).norm()

                        time = rel_angle * radius / speed
                        if time < least_time or least_time == -1:
                            least_time = time
                            results = (i, point, time)
        return results

    def crashLine(self, left_point, right_point, forward):
        least_time = -1
        results    = (None, None, None)

        # go through all the lines in the hull, and see where they interect
        # the lines cast by left_point and right_point in the forwards
        # direction

        # maybe use dot product like in the other function

        return results

    def draw(self):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, self.colour, polygon)

        if self.outline:
            pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)


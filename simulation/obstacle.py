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

    def withinRadius(self, centre, radius):
        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_j = self.hull[(i+1) % len(self.hull)]

            i_j      = point_j - point_i
            i_j_dist = i_j.mag()
            i_j_norm = i_j / i_j_dist

            c_i      = centre - point_i
            c_j      = centre - point_j
            c_i_dist = c_i.mag()
            c_j_dist = c_j.mag()

            if min(c_i_dist, c_j_dist) <= radius:
                return True

            near_dist = dotProduct(c_i, i_j_norm)
            if near_dist <= 0:
                if c_i_dist > radius:
                    continue
            elif near_dist >= i_j_dist:
                if c_j_dist > radius:
                    continue
            else:
                nearest   = point_i + i_j_norm * near_dist
                circ_dist = (nearest - centre).mag()
                if circ_dist > radius:
                    continue
            return True
        return False

    def crashCircle(self, circle_centre, direction, details):
        closest_crash = None

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

            if max(c_i_dist, c_j_dist) < details[-1][0]: # smallest radius
                continue

            near_dist = dotProduct(c_i, i_j_norm)
            nearest   = point_i + i_j_norm * near_dist
            circ_dist = (nearest - circle_centre).mag()

            if near_dist <= 0:
                if c_i_dist > details[0][0]: # biggest radius
                    continue
            elif near_dist >= i_j_dist:
                if c_j_dist > details[0][0]:
                    continue
            else:
                if circ_dist > details[0][0]:
                    continue

            for i in range(len(details)):
                radius, car_angle, speed, car_point = details[i]

                if circ_dist > radius:
                    break

                offset = math.sqrt(radius**2 - circ_dist**2)
                dists  = [near_dist - offset, near_dist + offset]

                for dist in dists:
                    if 0 <= dist <= i_j_dist:
                        crash_point = point_i + i_j_norm * dist
                        abs_angle   = getAngle(crash_point - circle_centre)
                        if direction == LEFT:
                            rel_angle = (abs_angle - car_angle).norm()
                        else:
                            rel_angle = (car_angle - abs_angle).norm()

                        arc_len = rel_angle * radius
                        if arc_len <= COLLISION_DISTANCE:
                            time = arc_len / speed
                            crash = (time, car_point, crash_point)
                            if closest_crash is None or crash < closest_crash:
                                closest_crash = crash
        return closest_crash

    def crashLine(self, car_points, forward, speed):
        closest_crash = None

        for i in range(len(self.hull)):
            point_i = self.hull[i]
            point_j = self.hull[(i+1) % len(self.hull)]

            i_j = point_j - point_i
            f_cross_ij = crossProduct(forward, i_j)

            if f_cross_ij == 0.0:
                # lines are parallel
                print("Z")

                for car_point in car_points:
                    c_i = point_i - car_point

                    ci_cross_f = crossProduct(c_i, forward)
                    if ci_cross_f == 0.0:
                        # collinear
                        ij_dot_f = dotProduct(i_j, forward)

                        if ij_dot_f > 0:
                            crash_point = point_i
                            print("A")
                        else:
                            crash_point = point_j
                            print("B")

                        c_i = crash_point - car_point
                        f_dot_f = dotProduct(forward, forward)
                        ray_dist = dotProduct(c_i, forward) / f_dot_f

                        if 0 <= ray_dist <= COLLISION_DISTANCE:
                            time  = ray_dist / speed
                            crash = (time, car_point, crash_point)
                            if closest_crash is None or crash < closest_crash:
                                closest_crash = crash
            else:
                # lines are not parallel
                for car_point in car_points:
                    c_i = point_i - car_point

                    ij_dist  = crossProduct(c_i, forward) / f_cross_ij
                    if 0 <= ij_dist <= 1:

                        ray_dist = crossProduct(c_i, i_j)     / f_cross_ij
                        if 0 <= ray_dist <= COLLISION_DISTANCE:
                            time        = ray_dist / speed
                            crash_point = car_point + forward * ray_dist
                            crash       = (time, car_point, crash_point)
                            if closest_crash is None or crash < closest_crash:
                                closest_crash = crash
        return closest_crash

    def draw(self, outline=False):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, self.colour, polygon)
        if outline:
            pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)

    def drawOutline(self):
        polygon = [self.world.getDrawable(point) for point in self.hull]
        pygame.draw.polygon(self.world.screen, BLACK, polygon, 1)


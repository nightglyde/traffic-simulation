from util import *

roads_list = []

class Road:
    def __init__(self, start, end):
        self.start  = start
        self.end    = end

        self.next_roads = []
        self.prev_roads = []

        roads_list.append(self)

    def connect(self, other):
        # is it a right turn, or a left turn, or straight ahead?
        # look at the directions of the two roads
        # you can work out the turn from the angle between the directions
        # you don't need to consider the position of the roads yet

        a = self.start
        b = self.end
        x = other.start
        y = other.end

        ab = b-a
        xy = y-x
        ax = x-a

        ab_cross_xy = crossProduct(ab, xy)

        turn = sign(ab_cross_xy)

        if turn == LEFT:
            print("LEFT")

        elif turn == RIGHT:
            print("RIGHT")

        else: # turn == CENTRE
            print("CENTRE")
            return False

        ax_cross_ab = crossProduct(ax, ab)
        ax_cross_xy = crossProduct(ax, xy)

        ab_rel_dist = ax_cross_xy / ab_cross_xy
        xy_rel_dist = ax_cross_ab / ab_cross_xy

        intersect = a + ab * ab_rel_dist

        print(ab_rel_dist, xy_rel_dist, intersect)

        if ab_rel_dist < 1 or xy_rel_dist > 0:
            print("BAD")
            return False
        print("GOOD")

        bi_dist = (b-intersect).mag()
        xi_dist = (x-intersect).mag()

        if bi_dist < xi_dist:
            turn_start = b
            turn_end   = intersect + xy.norm() * bi_dist

            prev_road  = self
            next_road  = Road(turn_end, x)
            extra_road = next_road

            next_road.next_roads.append(other)
            other.prev_roads.append(next_road)

        else:
            turn_start = intersect + ab.norm() * xi_dist * -1
            turn_end   = x

            prev_road  = Road(b, turn_start)
            next_road  = other
            extra_road = prev_road

            self.next_roads.append(prev_road)
            prev_road.prev_roads.append(self)

        if turn == LEFT:
            bj_ray = ab.left90().norm()
            xj_ray = xy.left90().norm()

        elif turn == RIGHT:
            bj_ray = ab.right90().norm()
            xj_ray = xy.right90().norm()

        b_cross_x = crossProduct(bj_ray, xj_ray)

        bj_dist = crossProduct(turn_end-turn_start, xj_ray) / b_cross_x

        # centre of turning circle
        centre = turn_start + bj_ray * bj_dist

        turn_radius = abs(bj_dist)

        if turn_radius < TURN_RADIUS:
            print("BAD CONNECTION", turn_radius, TURN_RADIUS)
            #raise Exception('Bad road connection: {} to {}'.format(self, other))

            roads_list.remove(extra_road)

            return False

        centre_start = turn_start - centre
        centre_end   = turn_end   - centre

        centre_start_angle = getAngle(centre_start)
        centre_end_angle   = getAngle(centre_end)

        ang_diff = centre_end_angle - centre_start_angle
        print("ANGLE:", ang_diff, ang_diff.value)

        prev_point = turn_start

        thingy = turn_radius / 4

        if turn == LEFT:
            for i in range(1, abs(int(ang_diff.value*thingy))):
                curr_angle = centre_start_angle - Angle(i/thingy)
                curr_point = centre + getVector(curr_angle) * turn_radius

                curr_road = Road(prev_point, curr_point)
                curr_road.prev_roads.append(prev_road)
                prev_road.next_roads.append(curr_road)

                prev_road  = curr_road
                prev_point = curr_point


        elif turn == RIGHT:
            for i in range(1, int(ang_diff.value*thingy)):
                curr_angle = centre_start_angle + Angle(i/thingy)
                curr_point = centre + getVector(curr_angle) * turn_radius

                curr_road = Road(prev_point, curr_point)
                curr_road.prev_roads.append(prev_road)
                prev_road.next_roads.append(curr_road)

                prev_road  = curr_road
                prev_point = curr_point

        curr_road = Road(prev_point, turn_end)
        curr_road.prev_roads.append(prev_road)
        prev_road.next_roads.append(curr_road)
        next_road.prev_roads.append(curr_road)
        curr_road.next_roads.append(next_road)

        # does the path of one cross the other one?
        # (line projected from the end   of the first  road, forwards)
        # (line projected from the start of the second road, backwards)
        # there needs to be at least enough gap to fit a simple turning circle


        # how big of a turning circle should it be?
        # we want to make sure we only turn left or right, not both
        # also, we should have as big a turning circle as possible (i think)

        return True

    def __repr__(self):
        return "Road({}, {})".format(self.start, self.end)


a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
d = random.randint(0, 100)

road1 = Road(Vector(a, b), Vector(c, d))

if True:
    for i in range(500):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 100)
        d = random.randint(0, 100)

        road2 = Road(Vector(a, b), Vector(c, d))
        result = road1.connect(road2)

        if result == False:
            roads_list.remove(road2)


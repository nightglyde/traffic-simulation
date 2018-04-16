from util import *

roads_list = []

class Road:
    def __init__(self, start, end):
        self.start  = start
        self.end    = end

        self.next_roads = []
        self.prev_roads = []

        self.intersection = None

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

        if turn == CENTRE:
            bx = x-b

            ab_cross_bx = crossProduct(ab, bx)

            if ab_cross_bx < 0.0001:
                joiny_road = Road(b, x)
                joiny_road.prev_roads.append(self)
                self.next_roads.append(joiny_road)
                other.prev_roads.append(joiny_road)
                joiny_road.next_roads.append(other)
                return True
            else:
                return False

        ax_cross_ab = crossProduct(ax, ab)
        ax_cross_xy = crossProduct(ax, xy)

        ab_rel_dist = ax_cross_xy / ab_cross_xy
        xy_rel_dist = ax_cross_ab / ab_cross_xy

        intersect = a + ab * ab_rel_dist

        #print(ab_rel_dist, xy_rel_dist, intersect)

        if ab_rel_dist < 1 or xy_rel_dist > 0:
            #print("BAD")
            return False
        #print("GOOD")

        bi_dist = (b-intersect).mag()
        xi_dist = (x-intersect).mag()

        if abs(bi_dist - xi_dist) < 0.000001:
            turn_start = b
            turn_end   = x

            prev_road = self
            next_road = other

            extra_road = None

        elif bi_dist < xi_dist:
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

            if extra_road != None:
                roads_list.remove(extra_road)
                if extra_road in self.next_roads:
                    self.next_roads.remove(extra_road)
                if extra_road in other.prev_roads:
                    other.prev_roads.remove(extra_road)

            return False

        centre_start = turn_start - centre
        centre_end   = turn_end   - centre

        centre_start_angle = getAngle(centre_start)
        centre_end_angle   = getAngle(centre_end)

        ang_diff = centre_end_angle - centre_start_angle
        #print("ANGLE:", ang_diff, ang_diff.value)

        prev_point = turn_start

        thingy = turn_radius / 2

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

        return True

    def __repr__(self):
        return "Road({}, {})".format(self.start, self.end)

class Intersection:
    def __init__(self):
        self.inputs  = []
        self.outputs = []

    def addInput(self, road):
        self.inputs.append(road)
        road.intersection = self

    def addOutput(self, road):
        self.outputs.append(road)

    def joinRoads(self):
        for in_road in self.inputs:
            for out_road in self.outputs:
                result = in_road.connect(out_road)
                #if result == False:
                #    print(in_road, out_road, result)

if True:
    intersections = [[Intersection() for i in range(num_blocks+1)] for j in range(num_blocks+1)]

    offset = TURN_RADIUS

    x_start = border_size + road_size
    y_start = border_size + half_lane
    for i in range(num_blocks):
        x = x_start + next_block * i
        for j in range(num_blocks+1):
            y = y_start + next_block * j

            # roads pointing right
            right_road = Road(
                Vector(x + offset, y),
                Vector(x + block_size - offset, y)
            )
            intersections[i][j].addOutput(right_road)
            intersections[i+1][j].addInput(right_road)

            # roads pointing left
            left_road = Road(
                Vector(x + block_size - offset, y + lane_size),
                Vector(x + offset, y + lane_size)
            )
            intersections[i+1][j].addOutput(left_road)
            intersections[i][j].addInput(left_road)

            # roads pointing up
            up_road = Road(
                Vector(y, x + block_size - offset),
                Vector(y, x + offset)
            )
            intersections[j][i+1].addOutput(up_road)
            intersections[j][i].addInput(up_road)

            # roads pointing down
            down_road = Road(
                Vector(y + lane_size, x + offset),
                Vector(y + lane_size, x + block_size - offset)
            )
            intersections[j][i].addOutput(down_road)
            intersections[j][i+1].addInput(down_road)

    for intersection_list in intersections:
        for intersection in intersection_list:
            intersection.joinRoads()

    ramp_road = Road(RAMP_POSITION, RAMP_END)
    for road in roads_list:
        if ramp_road.connect(road):
            print("Connected", ramp_road, "to", road)
            break
        else:
            print("Could not connect", ramp_road, "to", road)

else:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)

    road1 = Road(Vector(a, b), Vector(c, d))

    for i in range(500):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 100)
        d = random.randint(0, 100)

        road2 = Road(Vector(a, b), Vector(c, d))
        result = road1.connect(road2)

        if result == False:
            roads_list.remove(road2)


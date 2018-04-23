from util import *

entry_roads = []

all_roads = []
all_intersections = []

class Road:
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.setup()

        self.next_road = None

    def setup(self):
        self.vec    = self.end - self.start
        self.angle  = getAngle(self.vec)
        self.length = self.vec.mag()

        all_roads.append(self)

    def setNext(self, next_road):
        self.next_road = next_road

    def getDistanceAlong(self, car_position):
        car_vec  = car_position - self.start
        car_dist = dotProduct(car_vec, self.vec) / self.length
        return car_dist

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return "Road({}, {})".format(self.start, self.end)

class IntersectionRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.setup()

        self.intersection = None
        self.input_index  = None
        self.valid_paths  = None

    def setIntersection(self, intersection, index):
        self.intersection = intersection
        self.input_index  = index
        self.valid_paths  = intersection.connections[index]

    def getPathOptions(self):
        return self.valid_paths

    def getPath(self, output_index):
        return self.intersection.paths[(self.input_index, output_index)]

class TerminalRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.setup()

def connectRoads(in_road, out_road):
    joining_roads = []
    extra_road    = None

    a = in_road.start
    b = in_road.end
    x = out_road.start
    y = out_road.end

    ab = b-a
    xy = y-x
    ax = x-a

    ab_cross_xy = crossProduct(ab, xy)

    turn = sign(ab_cross_xy)

    if turn == CENTRE:
        bx = x-b

        ab_cross_bx = crossProduct(ab, bx)

        if ab_cross_bx < 0.0001:
            road = Road(b, x)
            road.setNext(out_road)
            return [road]
        else:
            raise Exception('Bad road connection: {} to {}'.format(in_road,
                                                                   out_road))

    ax_cross_ab = crossProduct(ax, ab)
    ax_cross_xy = crossProduct(ax, xy)

    ab_rel_dist = ax_cross_xy / ab_cross_xy
    xy_rel_dist = ax_cross_ab / ab_cross_xy

    intersect = a + ab * ab_rel_dist

    if ab_rel_dist < 1 or xy_rel_dist > 0:
        raise Exception('Bad road connection: {} to {}'.format(in_road,
                                                               out_road))

    bi_dist = (b-intersect).mag()
    xi_dist = (x-intersect).mag()

    if abs(bi_dist - xi_dist) < 0.000001:
        turn_start = b
        turn_end   = x

        prev_road  = None
        extra_road = None

    elif bi_dist < xi_dist:
        turn_start = b
        turn_end   = intersect + xy.norm() * bi_dist

        prev_road  = None
        extra_road = Road(turn_end, x)

    else:
        turn_start = intersect + ab.norm() * xi_dist * -1
        turn_end   = x

        prev_road  = Road(b, turn_start)
        extra_road = None

        joining_roads.append(prev_road)

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
        raise Exception('Bad road connection: {} to {}'.format(in_road,
                                                               out_road))

    centre_start = turn_start - centre
    centre_end   = turn_end   - centre

    centre_start_angle = getAngle(centre_start)
    centre_end_angle   = getAngle(centre_end)

    ang_diff = centre_end_angle - centre_start_angle

    prev_point = turn_start

    thingy = turn_radius / 2

    if turn == LEFT:
        for i in range(1, abs(int(ang_diff.value*thingy))):
            curr_angle = centre_start_angle - Angle(i/thingy)
            curr_point = centre + getVector(curr_angle) * turn_radius

            curr_road = Road(prev_point, curr_point)
            joining_roads.append(curr_road)

            if prev_road:
                prev_road.setNext(curr_road)

            prev_road  = curr_road
            prev_point = curr_point


    elif turn == RIGHT:
        for i in range(1, int(ang_diff.value*thingy)):
            curr_angle = centre_start_angle + Angle(i/thingy)
            curr_point = centre + getVector(curr_angle) * turn_radius

            curr_road = Road(prev_point, curr_point)
            joining_roads.append(curr_road)

            if prev_road:
                prev_road.setNext(curr_road)

            prev_road  = curr_road
            prev_point = curr_point

    curr_road = Road(prev_point, turn_end)
    joining_roads.append(curr_road)
    if prev_road:
        prev_road.setNext(curr_road)

    if extra_road:
        joining_roads.append(extra_road)
        curr_road.setNext(extra_road)
        curr_road = extra_road

    curr_road.setNext(out_road)

    return joining_roads

class Intersection:
    def __init__(self):
        self.inputs  = []
        self.outputs = []

        all_intersections.append(self)

        self.pairs = []
        self.paths = {}
        self.lights = {}

        self.connections = []

        self.offset = random.randint(0, CYCLE_DURATION-1)

        self.phase = AMBER_LIGHT

        self.input_num = 0

    def updateTrafficLights(self, time):
        cycle_time = (time + self.offset) % CYCLE_DURATION

        if self.phase == GREEN_LIGHT:
            if cycle_time >= AMBER_PHASE:
                self.phase = AMBER_LIGHT

                for pair in self.pairs:
                    if self.lights[pair] == GREEN_LIGHT:
                        self.lights[pair] = AMBER_LIGHT

        elif self.phase == AMBER_LIGHT:
            if cycle_time < AMBER_PHASE:
                self.phase = GREEN_LIGHT

                self.input_num = (self.input_num + 1) % len(self.inputs)

                for pair in self.pairs:
                    if pair[0] == self.input_num:
                        self.lights[pair] = GREEN_LIGHT
                    else:
                        self.lights[pair] = RED_LIGHT

    def checkTrafficLights(self, entrance, exit):
        return self.lights[(entrance, exit)] == GREEN_LIGHT

    def addRoad(self, inputs, outputs):
        old_in_count  = len(self.inputs)
        old_out_count = len(self.outputs)

        self.inputs  += inputs
        self.outputs += outputs

        new_in_count  = len(self.inputs)
        new_out_count = len(self.outputs)

        for i in range(old_in_count):
            in_road = self.inputs[i]
            for j in range(old_out_count, new_out_count):
                out_road = self.outputs[j]

                path = connectRoads(in_road, out_road)
                if path:
                    pair = (i, j)
                    self.pairs.append(pair)
                    self.paths[pair]  = path
                    self.lights[pair] = RED_LIGHT

                    self.connections[i].append(j)

        for i in range(old_in_count, new_in_count):
            in_road = self.inputs[i]

            valid_paths = []

            for j in range(old_out_count):
                out_road = self.outputs[j]

                path = connectRoads(in_road, out_road)
                if path:
                    pair = (i, j)
                    self.pairs.append(pair)
                    self.paths[pair]  = path
                    self.lights[pair] = RED_LIGHT

                    valid_paths.append(j)

            self.connections.append(valid_paths)
            in_road.setIntersection(self, i)


intersections = [[Intersection() for i in range(num_blocks+1)] for j in range(num_blocks+1)]

x_start = border_size + road_size
y_start = border_size + half_lane
for i in range(num_blocks):
    x = x_start + next_block * i
    for j in range(num_blocks+1):
        y = y_start + next_block * j

        # horizontal roads
        left_road = IntersectionRoad(
            Vector(x + block_size - corner_offset, y + lane_size),
            Vector(x + corner_offset, y + lane_size)
        )
        right_road = IntersectionRoad(
            Vector(x + corner_offset, y),
            Vector(x + block_size - corner_offset, y)
        )

        intersections[i][j].addRoad(  [left_road],  [right_road])
        intersections[i+1][j].addRoad([right_road], [left_road])

        # vertical roads
        up_road = IntersectionRoad(
            Vector(y, x + block_size - corner_offset),
            Vector(y, x + corner_offset)
        )
        down_road = IntersectionRoad(
            Vector(y + lane_size, x + corner_offset),
            Vector(y + lane_size, x + block_size - corner_offset)
        )

        intersections[j][i].addRoad(  [up_road],   [down_road])
        intersections[j][i+1].addRoad([down_road], [up_road])

x_start = border_size - block_size + corner_offset
x_end   = border_size - corner_offset
y_start = border_size + half_lane
for i in range(num_blocks+1):
    y = y_start + next_block * i

    # left entry
    entry_road = IntersectionRoad(
        Vector(x_start, y),
        Vector(x_end,   y)
    )
    exit_road = TerminalRoad(
        Vector(x_end,   y+lane_size),
        Vector(x_start, y+lane_size)
    )
    entry_roads.append(entry_road)
    intersections[0][i].addRoad([entry_road], [exit_road])

    # right entry
    entry_road = IntersectionRoad(
        Vector(world_size-x_start, world_size-y),
        Vector(world_size-x_end,   world_size-y)
    )
    exit_road = TerminalRoad(
        Vector(world_size-x_end,   world_size-y-lane_size),
        Vector(world_size-x_start, world_size-y-lane_size)
    )
    entry_roads.append(entry_road)
    intersections[num_blocks][num_blocks-i].addRoad([entry_road], [exit_road])

    # top entry
    entry_road = IntersectionRoad(
        Vector(y+lane_size, x_start),
        Vector(y+lane_size, x_end)
    )
    exit_road = TerminalRoad(
        Vector(y, x_end),
        Vector(y, x_start)
    )
    entry_roads.append(entry_road)
    intersections[i][0].addRoad([entry_road], [exit_road])

    # bottom entry
    entry_road = IntersectionRoad(
        Vector(world_size-y-lane_size, world_size-x_start),
        Vector(world_size-y-lane_size, world_size-x_end)
    )
    exit_road = TerminalRoad(
        Vector(world_size-y, world_size-x_end),
        Vector(world_size-y, world_size-x_start)
    )
    entry_roads.append(entry_road)
    intersections[num_blocks-i][num_blocks].addRoad([entry_road], [exit_road])


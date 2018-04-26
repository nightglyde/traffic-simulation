from util import *

# world size
LANE_WIDTH = 3.5
ROAD_WIDTH = LANE_WIDTH*2
HALF_LANE  = LANE_WIDTH/2

BORDER_SIZE   = 10
BLOCK_SIZE    = 50
CORNER_OFFSET = 5.4
NUM_BLOCKS    = 2

NEXT_BLOCK = BLOCK_SIZE + ROAD_WIDTH
WORLD_SIZE = BORDER_SIZE*2 + ROAD_WIDTH + NEXT_BLOCK*NUM_BLOCKS

WORLD_WIDTH  = WORLD_SIZE
WORLD_HEIGHT = WORLD_SIZE

all_intersections = []

all_roads          = []
entry_roads        = []
normal_roads       = []
intersection_roads = []
terminal_roads     = []

def nameGenerator():
    chars = string.ascii_lowercase

    a = "a"
    z_num = ord("z")

    name = "a"
    while True:
        yield name

        num_zeds = 0
        for i in range(len(name)-1, -1, -1):
            char_num = ord(name[i])

            if char_num < z_num:
                name = name[:i] + chr(char_num+1) + a*num_zeds
                break

            else:
                num_zeds += 1
        else:
            name = a*(num_zeds+1)

name_generator = nameGenerator()

class Road:
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.type_name = "Road"
        normal_roads.append(self)
        self.setup()

        self.next_road = None

    def setup(self):
        self.vec    = self.end - self.start
        self.angle  = getAngle(self.vec)
        self.length = self.vec.mag()

        all_roads.append(self)
        self.name = "{}_{}".format(self.type_name.lower(), next(name_generator))

    def setNext(self, next_road):
        self.next_road = next_road

    def getDistanceAlong(self, car_position):
        car_vec  = car_position - self.start
        car_dist = dotProduct(car_vec, self.vec) / self.length
        return car_dist

    def __eq__(self, other):
        if isinstance(other, Road):
            return self.start == other.start and self.end == other.end
        return False

    def __repr__(self):
        return "{}({}, {})".format(self.type_name, self.start, self.end)

class IntersectionRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        intersection_roads.append(self)
        self.type_name = "IntersectionRoad"
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

        terminal_roads.append(self)
        self.type_name = "TerminalRoad"
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
    def __init__(self, i, j):
        self.id = (i, j)

        self.name = "intersection_{}_{}".format(i, j)

        self.inputs  = []
        self.outputs = []

        all_intersections.append(self)

        self.pairs = []
        self.paths = {}

        self.connections = []

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

                    valid_paths.append(j)

            self.connections.append(valid_paths)
            in_road.setIntersection(self, i)

    def __eq__(self, other):
        if isinstance(other, Intersection):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        inputs = [road.name for road in self.inputs]
        inputs = "[" + ",".join(inputs) + "]"

        outputs = [road.name for road in self.outputs]
        outputs = "[" + ",".join(outputs) + "]"

        return "Intersection({}, {}, {}, {})".format(self.id[0], self.id[1],
                                                     inputs, outputs)

intersections = [[Intersection(i, j) for i in range(NUM_BLOCKS+1)] for j in range(NUM_BLOCKS+1)]

x_start = BORDER_SIZE + ROAD_WIDTH
y_start = BORDER_SIZE + HALF_LANE
for i in range(NUM_BLOCKS):
    x = x_start + NEXT_BLOCK * i
    for j in range(NUM_BLOCKS+1):
        y = y_start + NEXT_BLOCK * j

        # horizontal roads
        left_road = IntersectionRoad(
            Vector(x + BLOCK_SIZE - CORNER_OFFSET, y + LANE_WIDTH),
            Vector(x + CORNER_OFFSET, y + LANE_WIDTH)
        )
        right_road = IntersectionRoad(
            Vector(x + CORNER_OFFSET, y),
            Vector(x + BLOCK_SIZE - CORNER_OFFSET, y)
        )

        intersections[i][j].addRoad(  [left_road],  [right_road])
        intersections[i+1][j].addRoad([right_road], [left_road])

        # vertical roads
        up_road = IntersectionRoad(
            Vector(y, x + BLOCK_SIZE - CORNER_OFFSET),
            Vector(y, x + CORNER_OFFSET)
        )
        down_road = IntersectionRoad(
            Vector(y + LANE_WIDTH, x + CORNER_OFFSET),
            Vector(y + LANE_WIDTH, x + BLOCK_SIZE - CORNER_OFFSET)
        )

        intersections[j][i].addRoad(  [up_road],   [down_road])
        intersections[j][i+1].addRoad([down_road], [up_road])

x_start = BORDER_SIZE - BLOCK_SIZE + CORNER_OFFSET
x_end   = BORDER_SIZE - CORNER_OFFSET
y_start = BORDER_SIZE + HALF_LANE
for i in range(NUM_BLOCKS+1):
    y = y_start + NEXT_BLOCK * i

    # left entry
    entry_road = IntersectionRoad(
        Vector(x_start, y),
        Vector(x_end,   y)
    )
    exit_road = TerminalRoad(
        Vector(x_end,   y+LANE_WIDTH),
        Vector(x_start, y+LANE_WIDTH)
    )
    entry_roads.append(entry_road)
    intersections[0][i].addRoad([entry_road], [exit_road])

    # right entry
    entry_road = IntersectionRoad(
        Vector(WORLD_SIZE-x_start, WORLD_SIZE-y),
        Vector(WORLD_SIZE-x_end,   WORLD_SIZE-y)
    )
    exit_road = TerminalRoad(
        Vector(WORLD_SIZE-x_end,   WORLD_SIZE-y-LANE_WIDTH),
        Vector(WORLD_SIZE-x_start, WORLD_SIZE-y-LANE_WIDTH)
    )
    entry_roads.append(entry_road)
    intersections[NUM_BLOCKS][NUM_BLOCKS-i].addRoad([entry_road], [exit_road])

    # top entry
    entry_road = IntersectionRoad(
        Vector(y+LANE_WIDTH, x_start),
        Vector(y+LANE_WIDTH, x_end)
    )
    exit_road = TerminalRoad(
        Vector(y, x_end),
        Vector(y, x_start)
    )
    entry_roads.append(entry_road)
    intersections[i][0].addRoad([entry_road], [exit_road])

    # bottom entry
    entry_road = IntersectionRoad(
        Vector(WORLD_SIZE-y-LANE_WIDTH, WORLD_SIZE-x_start),
        Vector(WORLD_SIZE-y-LANE_WIDTH, WORLD_SIZE-x_end)
    )
    exit_road = TerminalRoad(
        Vector(WORLD_SIZE-y, WORLD_SIZE-x_end),
        Vector(WORLD_SIZE-y, WORLD_SIZE-x_start)
    )
    entry_roads.append(entry_road)
    intersections[NUM_BLOCKS-i][NUM_BLOCKS].addRoad([entry_road], [exit_road])

grass = []

x_start = BORDER_SIZE + ROAD_WIDTH
y_start = BORDER_SIZE + ROAD_WIDTH
for i in range(-1, NUM_BLOCKS+1):
    x = x_start + NEXT_BLOCK * i
    for j in range(-1, NUM_BLOCKS+1):
        y = y_start + NEXT_BLOCK * j

        grass.append([
            Vector(x+CORNER_OFFSET, y),
            Vector(x+BLOCK_SIZE-CORNER_OFFSET, y),
            Vector(x+BLOCK_SIZE, y+CORNER_OFFSET),
            Vector(x+BLOCK_SIZE, y+BLOCK_SIZE-CORNER_OFFSET),
            Vector(x+BLOCK_SIZE-CORNER_OFFSET, y+BLOCK_SIZE),
            Vector(x+CORNER_OFFSET, y+BLOCK_SIZE),
            Vector(x, y+BLOCK_SIZE-CORNER_OFFSET),
            Vector(x, y+CORNER_OFFSET),
        ])
if __name__ == "__main__":
    print("from util import *")
    print("from road_network import Road, IntersectionRoad, TerminalRoad, Intersection")

    print()

    for road in all_roads:
        print("{} = {}".format(road.name, road))

    print()

    for intersection in all_intersections:
        print("{} = {}".format(intersection.name, intersection))

        for i in range(len(intersection.inputs)):
            road = intersection.inputs[i]
            print("{}.setIntersection({}, {})".format(
                road.name, intersection.name, i))

            for j in range(len(intersection.outputs)):
                pair = (i, j)

                if pair in intersection.pairs:
                    path = [road.name for road in intersection.paths[pair]]
                    path = "[" + ",".join(path) + "]"

                    print("{}.addConnection({}, {}, {})".format(
                        intersection.name, i, j, path))

    print()

    for road in normal_roads:
        print("{}.setNext({})".format(road.name, road.next_road.name))

    print()

    names = [road.name for road in all_roads]
    print("roads = [" + ",".join(names) + "]")

    print()

    names = [road.name for road in entry_roads]
    print("entry_roads = [" + ",".join(names) + "]")

    print()

    names = [intersection.name for intersection in all_intersections]
    print("intersections = [" + ",".join(names) + "]")

    print()

    print("grass = [")
    for grass_area in grass:
        print("{},".format(grass_area))
    print("]")

    print()

    print("world_width  = {}".format(WORLD_WIDTH))
    print("world_height = {}".format(WORLD_HEIGHT))

    print()


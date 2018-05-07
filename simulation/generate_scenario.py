from util import *

# world size
LANE_WIDTH = 3.5
ROAD_WIDTH = LANE_WIDTH*2
HALF_LANE  = LANE_WIDTH/2

BORDER_SIZE   = 50
BLOCK_SIZE    = 50
CORNER_OFFSET = 5.4

NUM_COLS = 1
NUM_ROWS = 1

NEXT_BLOCK   = BLOCK_SIZE + ROAD_WIDTH
WORLD_WIDTH  = BORDER_SIZE*2 + ROAD_WIDTH + NEXT_BLOCK*NUM_COLS
WORLD_HEIGHT = BORDER_SIZE*2 + ROAD_WIDTH + NEXT_BLOCK*NUM_ROWS

TURNS = [LEFT, RIGHT, CENTRE]

all_intersections = []

all_roads          = []
entry_roads        = []
normal_roads       = []
intersection_roads = []
crossing_roads     = []
terminal_roads     = []

##############
# ROAD TYPES #
##############

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

road_name_generator = nameGenerator()

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

    def generateName(self):
        prefix = self.type_name.lower()
        prefix = prefix[:5] + prefix[5:][-4:] + "_"
        self.name = prefix + next(road_name_generator)

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
        return "{}({}, {}, {})".format(self.type_name,
                                       self.start, self.end, self.danger)

class IntersectionRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.type_name = "IntersectionRoad"
        intersection_roads.append(self)
        self.setup()

        self.intersection = None
        self.input_index  = None
        self.valid_paths  = None

        self.danger = False

    def setIntersection(self, intersection, index):
        self.intersection = intersection
        self.input_index  = index
        self.valid_paths  = intersection.connections[index]

    def getExit(self, turn):
        return self.valid_paths[turn]

    def getPath(self, output_index):
        path, turn = self.intersection.paths[(self.input_index, output_index)]
        return path

class CrossingRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.type_name = "Road"#CrossingRoad"
        crossing_roads.append(self)
        self.setup()

        self.next_road = None
        self.next_turn = None

        self.danger = True

class TerminalRoad(Road):
    def __init__(self, start, end):
        self.start = start
        self.end   = end

        self.type_name = "Road"#TerminalRoad"
        terminal_roads.append(self)
        self.setup()

        self.next_road = None
        self.next_turn = None

        self.danger = False

######################
# Route instructions #
######################

def findRoutes(road, last_turn=None, turns=[], route=[]):
    routes = []

    while road != None:
        if isinstance(road, IntersectionRoad):
            for turn in TURNS:

                if turn == last_turn:
                    continue

                exit = road.getExit(turn)
                if exit == None:
                    continue

                instruction = EnterIntersection(road, turn)

                if turn != CENTRE:
                    new_last_turn = turn
                else:
                    new_last_turn = last_turn

                new_turns = turns + [turn]

                new_route = route + [instruction]

                routes += findRoutes(instruction.getNextRoad(),
                                     new_last_turn, new_turns, new_route)
            return routes

        instruction = FollowRoad(road)
        route.append(instruction)
        road = instruction.getNextRoad()

    routes.append(route.copy())
    return routes

class FollowRoad:
    def __init__(self, road):
        self.road      = road
        self.turn      = road.next_turn
        self.next_road = road.next_road

        self.danger = road.danger

    def checkLights(self):
        return GREEN_LIGHT

    def getNextRoad(self):
        return self.next_road

    def __repr__(self):
        return "FollowRoad({})".format(self.road.name)

class EnterIntersection:
    def __init__(self, road, turn):
        self.road = road
        self.turn = turn

        exit = road.getExit(turn)
        self.pair      = (road.input_index, exit)
        self.next_road = road.getPath(exit)[0]

        self.danger = road.danger

    def getNextRoad(self):
        return self.next_road

    def __repr__(self):
        turn = self.turn
        if turn == LEFT:
            turn = "LEFT"
        elif turn == RIGHT:
            turn = "RIGHT"
        else:
            turn = "CENTRE"

        return "EnterIntersection({}, {})".format(self.road.name, turn)

################
# Intersection #
################

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
            road = CrossingRoad(b, x)
            road.setNext(out_road)
            return [road], turn
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
        extra_road = CrossingRoad(turn_end, x)

    else:
        turn_start = intersect + ab.norm() * xi_dist * -1
        turn_end   = x

        prev_road  = CrossingRoad(b, turn_start)
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

            curr_road = CrossingRoad(prev_point, curr_point)
            joining_roads.append(curr_road)

            if prev_road:
                prev_road.setNext(curr_road)

            prev_road  = curr_road
            prev_point = curr_point


    elif turn == RIGHT:
        for i in range(1, int(ang_diff.value*thingy)):
            curr_angle = centre_start_angle + Angle(i/thingy)
            curr_point = centre + getVector(curr_angle) * turn_radius

            curr_road = CrossingRoad(prev_point, curr_point)
            joining_roads.append(curr_road)

            if prev_road:
                prev_road.setNext(curr_road)

            prev_road  = curr_road
            prev_point = curr_point

    curr_road = CrossingRoad(prev_point, turn_end)
    joining_roads.append(curr_road)
    if prev_road:
        prev_road.setNext(curr_road)

    if extra_road:
        joining_roads.append(extra_road)
        curr_road.setNext(extra_road)
        curr_road = extra_road

    curr_road.setNext(out_road)

    return joining_roads, turn

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

                path, turn = connectRoads(in_road, out_road)
                if path:
                    pair = (i, j)
                    self.pairs.append(pair)
                    self.paths[pair] = (path, turn)

                    self.connections[i][turn] = j #.append(j)

        for i in range(old_in_count, new_in_count):
            in_road = self.inputs[i]

            self.connections.append([None, None, None])

            for j in range(old_out_count):
                out_road = self.outputs[j]

                path, turn = connectRoads(in_road, out_road)
                if path:
                    pair = (i, j)
                    self.pairs.append(pair)
                    self.paths[pair] = (path, turn)

                    self.connections[i][turn] = j
                    #self.connections[i][1] = j
                    #self.connections[i][2] = j

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

##################
# GENERATE STUFF #
##################

# generate intersections
intersections = [[Intersection(i, j) for j in range(NUM_ROWS+1)] for i in range(NUM_COLS+1)]

# generate horizontal internal roads
x_start = BORDER_SIZE + ROAD_WIDTH
y_start = BORDER_SIZE + HALF_LANE
for i in range(NUM_COLS):
    x = x_start + NEXT_BLOCK * i
    for j in range(NUM_ROWS+1):
        y = y_start + NEXT_BLOCK * j

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

# generate vertical internal roads
x_start = BORDER_SIZE + HALF_LANE
y_start = BORDER_SIZE + ROAD_WIDTH
for j in range(NUM_ROWS):
    y = y_start + NEXT_BLOCK * j
    for i in range(NUM_COLS+1):
        x = x_start + NEXT_BLOCK * i

        up_road = IntersectionRoad(
            Vector(x, y + BLOCK_SIZE - CORNER_OFFSET),
            Vector(x, y + CORNER_OFFSET)
        )
        down_road = IntersectionRoad(
            Vector(x + LANE_WIDTH, y + CORNER_OFFSET),
            Vector(x + LANE_WIDTH, y + BLOCK_SIZE - CORNER_OFFSET)
        )

        intersections[i][j].addRoad(  [up_road],   [down_road])
        intersections[i][j+1].addRoad([down_road], [up_road])

# generate horizontal external roads
x_start = BORDER_SIZE - BLOCK_SIZE + CORNER_OFFSET
x_end   = BORDER_SIZE - CORNER_OFFSET
y_start = BORDER_SIZE + HALF_LANE
for j in range(NUM_ROWS+1):
    y = y_start + NEXT_BLOCK * j

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
    intersections[0][j].addRoad([entry_road], [exit_road])

    # right entry
    entry_road = IntersectionRoad(
        Vector(WORLD_WIDTH-x_start, WORLD_HEIGHT-y),
        Vector(WORLD_WIDTH-x_end,   WORLD_HEIGHT-y)
    )
    exit_road = TerminalRoad(
        Vector(WORLD_WIDTH-x_end,   WORLD_HEIGHT-y-LANE_WIDTH),
        Vector(WORLD_WIDTH-x_start, WORLD_HEIGHT-y-LANE_WIDTH)
    )
    entry_roads.append(entry_road)
    intersections[NUM_COLS][NUM_ROWS-j].addRoad([entry_road], [exit_road])

# generate vertical external roads
x_start = BORDER_SIZE + HALF_LANE
y_start = BORDER_SIZE - BLOCK_SIZE + CORNER_OFFSET
y_end   = BORDER_SIZE - CORNER_OFFSET
for i in range(NUM_COLS+1):
    x = x_start + NEXT_BLOCK * i

    # top entry
    entry_road = IntersectionRoad(
        Vector(x+LANE_WIDTH, y_start),
        Vector(x+LANE_WIDTH, y_end)
    )
    exit_road = TerminalRoad(
        Vector(x, y_end),
        Vector(x, y_start)
    )
    entry_roads.append(entry_road)
    intersections[i][0].addRoad([entry_road], [exit_road])

    # bottom entry
    entry_road = IntersectionRoad(
        Vector(WORLD_WIDTH-x-LANE_WIDTH, WORLD_HEIGHT-y_start),
        Vector(WORLD_WIDTH-x-LANE_WIDTH, WORLD_HEIGHT-y_end)
    )
    exit_road = TerminalRoad(
        Vector(WORLD_WIDTH-x, WORLD_HEIGHT-y_end),
        Vector(WORLD_WIDTH-x, WORLD_HEIGHT-y_start)
    )
    entry_roads.append(entry_road)
    intersections[NUM_COLS-i][NUM_ROWS].addRoad([entry_road], [exit_road])

# generate valid routes
valid_routes = []
for i, entry_road in enumerate(entry_roads):
    routes = findRoutes(entry_road)
    valid_routes.append(routes)

# generate grass
grass = []

x_start = BORDER_SIZE + ROAD_WIDTH
y_start = BORDER_SIZE + ROAD_WIDTH
for i in range(-1, NUM_COLS+1):
    x = x_start + NEXT_BLOCK * i
    for j in range(-1, NUM_ROWS+1):
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

#####################
# CREATE WORLD FILE #
#####################

if __name__ == "__main__":
    print("from util import *")
    print("from road_network import Road, IntersectionRoad, Intersection, FollowRoad, EnterIntersection")

    print()

    print("world_width  = {}".format(WORLD_WIDTH))
    print("world_height = {}".format(WORLD_HEIGHT))

    print()

    for road in intersection_roads:
        road.generateName()
        print("{} = {}".format(road.name, road))

    for road in normal_roads:
        road.generateName()
        print("{} = {}".format(road.name, road))

    for road in terminal_roads:
        road.generateName()
        print("{} = {}".format(road.name, road))

    for road in crossing_roads:
        road.generateName()
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
                    path, turn = intersection.paths[pair]

                    path = [road.name for road in path]
                    path = "[" + ",".join(path) + "]"

                    if turn == LEFT:
                        turn = "LEFT"
                    elif turn == RIGHT:
                        turn = "RIGHT"
                    else:
                        turn = "CENTRE"

                    print("{}.addConnection({}, {}, {}, {})".format(
                        intersection.name, i, j, path, turn))

    print()

    for road in normal_roads:
        print("{}.setNext({})".format(road.name, road.next_road.name))

    for road in crossing_roads:
        print("{}.setNext({})".format(road.name, road.next_road.name))

    print()

    names = [road.name for road in all_roads]
    print("roads = [" + ",".join(names) + "]")

    print()

    names = [road.name for road in entry_roads]
    print("entry_roads = [" + ",".join(names) + "]")

    print()

    print("valid_routes = [")
    for i in range(len(entry_roads)):
        routes = valid_routes[i]
        print("  [")
        for route in routes:
            print("    {},".format(route))
        print("  ],")
    print("]")

    print()

    names = [intersection.name for intersection in all_intersections]
    print("intersections = [" + ",".join(names) + "]")

    print()

    print("grass = [")
    for grass_area in grass:
        print("{},".format(grass_area))
    print("]")

    print()


from util import *

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

class Intersection:
    def __init__(self, i, j, inputs, outputs):
        self.id = (i, j)

        self.inputs  = inputs
        self.outputs = outputs

        self.pairs = []
        self.paths = {}

        self.connections = [[] for i in range(len(inputs))]

    def addConnection(self, entrance, exit, path):
        pair = (entrance, exit)
        self.pairs.append(pair)
        self.paths[pair] = path
        self.connections[entrance].append(exit)

    def __eq__(self, other):
        if isinstance(other, Intersection):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

class TrafficLights:
    def __init__(self, intersection):
        self.intersection = intersection

        self.lights = {}
        for pair in intersection.pairs:
            self.lights[pair] = RED_LIGHT

        self.num_inputs = len(intersection.inputs)
        self.input_num  = 0

        self.offset    = random.randint(0, CYCLE_DURATION-1)

        self.phase = RED_LIGHT

    def update(self, time):
        cycle_time = (time + self.offset) % CYCLE_DURATION

        if self.phase == GREEN_LIGHT:
            if cycle_time >= AMBER_PHASE:
                self.phase = AMBER_LIGHT

                for pair in self.lights:
                    if self.lights[pair] == GREEN_LIGHT:
                        self.lights[pair] = AMBER_LIGHT

        elif self.phase == AMBER_LIGHT:
            if cycle_time >= RED_PHASE:
                self.phase = RED_LIGHT

                for pair in self.lights:
                    self.lights[pair] = RED_LIGHT

        elif self.phase == RED_LIGHT:
            if cycle_time < AMBER_PHASE:
                self.phase = GREEN_LIGHT

                self.input_num = (self.input_num + 1) % self.num_inputs

                for pair in self.lights:
                    if pair[0] == self.input_num:
                        self.lights[pair] = GREEN_LIGHT


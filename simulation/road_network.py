from util import *

################
# Road Objects #
################

class Road:
    def __init__(self, start, end, danger):
        self.start  = start
        self.end    = end
        self.danger = danger

        self.setup()

        self.next_road = None
        self.next_turn = None

    def setup(self):
        self.vec    = self.end - self.start
        self.angle  = getAngle(self.vec)
        self.length = self.vec.mag()

    def setNext(self, next_road):
        self.next_road = next_road

    def setTurn(self, turn):
        self.next_turn = turn

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
    def __init__(self, start, end, danger):
        self.start  = start
        self.end    = end
        self.danger = danger

        self.setup()

        self.intersection = None
        self.input_index  = None
        self.valid_paths  = None

    def setIntersection(self, intersection, index):
        self.intersection = intersection
        self.input_index  = index
        self.valid_paths  = intersection.connections[index]

    def getExit(self, turn):
        return self.valid_paths[turn]

    def getPath(self, output_index):
        return self.intersection.paths[(self.input_index, output_index)]

class Intersection:
    def __init__(self, i, j, inputs, outputs):
        self.id = (i, j)

        self.inputs  = inputs
        self.outputs = outputs

        self.pairs = []
        self.paths = {}

        self.connections = [[None, None, None] for i in range(len(inputs))]

    def addConnection(self, entrance, exit, path, turn):
        pair = (entrance, exit)
        self.pairs.append(pair)
        self.paths[pair] = path

        self.connections[entrance][turn] = exit

        for road in path:
            road.setTurn(turn)

    def __eq__(self, other):
        if isinstance(other, Intersection):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

######################
# Route Instructions #
######################

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
        return "FollowRoad({})".format(self.road)

class EnterIntersection:
    def __init__(self, road, turn):
        self.road       = road
        self.turn       = turn
        self.controller = None

        exit = road.getExit(turn)
        self.pair      = (road.input_index, exit)
        self.next_road = road.getPath(exit)[0]

        self.danger = road.danger

    def setController(self, controller):
        self.controller = controller

    def checkLights(self):
        if self.controller != None:
            return self.controller.lights[self.pair]
        return RED_LIGHT

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

        return "EnterIntersection({})".format(self.road, turn)

#######################
# Traffic Controllers #
#######################

class TrafficLights:
    def __init__(self, intersection):
        self.intersection = intersection

        self.lights = {}
        for pair in intersection.pairs:
            self.lights[pair] = RED_LIGHT

        self.num_inputs = len(intersection.inputs)
        self.input_num  = 0

        self.batches = []
        for entrance in range(self.num_inputs):

            batch = []
            for exit in intersection.connections[entrance]:
                batch.append((entrance, exit))
            right_exit = intersection.connections[entrance][RIGHT]
            batch.append((right_exit, entrance))

            self.batches.append(batch)

        self.offset = random.randint(0, CYCLE_DURATION-1)

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

                for pair in self.batches[self.input_num]:
                    self.lights[pair] = GREEN_LIGHT

                #for pair in self.lights:
                #    if pair[0] == self.input_num:
                #        self.lights[pair] = GREEN_LIGHT

                #right_exit = self.intersection.connections[self.input_num][RIGHT]

                #self.lights[(right_exit, self.input_num)] = GREEN_LIGHT


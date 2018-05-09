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

        self.tup = (self.start, self.end)

    def setNext(self, next_road):
        self.next_road = next_road

    def setTurn(self, turn):
        self.next_turn = turn

    def getDistanceAlong(self, car_position):
        car_vec  = car_position - self.start
        car_dist = dotProduct(car_vec, self.vec) / self.length
        return car_dist

    def __hash__(self):
        return hash(self.tup)

    def __eq__(self, other):
        if isinstance(other, Road):
            return self.tup == other.tup
        return False

    def __lt__(self, other):
        if isinstance(other, Road):
            return self.tup < other.tup
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

        self.intersection = road.intersection
        self.entrance     = road.input_index
        self.exit         = road.getExit(turn)

        self.next_road = road.getPath(self.exit)[0]

        self.danger = road.danger

    def setController(self, controller):
        self.controller = controller

    def copy(self):
        copy = EnterIntersection(self.road, self.turn)
        copy.setController(self.controller)
        return copy

    def checkLights(self):
        if self.controller != None:
            return self.controller.getLight(self.entrance, self.exit)
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
    def __init__(self, world, intersection):
        self.world        = world
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

    def getLight(self, entrance, exit):
        return self.lights[(entrance, exit)]

    def draw(self):
        world  = self.world
        screen = world.screen

        for pair in self.lights:
            light = self.lights[pair]

            if light == RED_LIGHT:
                continue
            elif light == AMBER_LIGHT:
                colour = AMBER
            else:
                colour = GREEN

            for road in self.intersection.paths[pair]:
                start = world.getDrawable(road.start)
                end   = world.getDrawable(road.end)
                pygame.draw.line(screen, colour, start, end, 2)

class VirtualTrafficLights:
    def __init__(self, car_controller):
        self.car_controller = car_controller

        self.world  = car_controller.world
        self.name   = car_controller.name
        self.colour = car_controller.colour
        self.car    = car_controller.car

        self.intersection = None
        self.entrance     = None
        #self.exit         = None

        self.light = RED_LIGHT

        self.nr = None

        self.messages  = []
        self.knowledge = {}

    def update(self, instruction):
        # STEP 2: Enter VTL area

        if isinstance(instruction, EnterIntersection):
            intersection = instruction.intersection
            if intersection == self.intersection:
                return

            self.intersection = intersection
            self.entrance     = instruction.entrance
            #self.exit         = instruction.exit

            self.light = AMBER_LIGHT
            self.nr    = 1
            # go to step 3
            return

        # if we're not in VTL area, go back to step 1
        if not instruction.danger:
            self.intersection = None

    def sendMessages(self):

        # STEP 1: Update own position
        self.knowledge[self.name] = (self.car.centre, self.entrance)
        content = (self.intersection, self.car.centre, self.entrance)
        self.messages.append((SEND_TO_ALL, VTL_STATUS, content))
        # go to step 2

        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        if self.intersection == None:
            return

        for message in messages:
            source, destination, message_type, content = message

            if source == self.name:
                continue

            if message_type == VTL_STATUS:
                intersection, position, entrance = content

                if intersection != self.intersection:
                    if source in self.knowledge:
                        del self.knowledge[source]
                    continue

                self.knowledge[source] = (position, entrance)

        # STEP 3: find the leader of each road segment
        roads = self.intersection.inputs
        leaders = {}

        for car_name in self.knowledge:
            position, entrance = self.knowledge[car_name]

            road = roads[entrance]
            dist_along = road.getDistanceAlong(position)
            dist_left  = road.length - dist_along

            if not road in leaders:
                leaders[road] = (dist_left, car_name)
                continue

            curr_dist_left, curr_leader = leaders[road]
            if dist_left < curr_dist_left:
                leaders[road] = (dist_left, car_name)

        # STEP 4: Put the leaders in order
        if self.nr >= NR_MAX:
            # go to step 5

            # STEP 5: sort by road ID
            roads = [road for road in leaders.keys()]
            roads.sort()
            leaders = [leaders[road] for road in roads]
            # go to step 6

        else:
            # sort by normalised distance
            leaders = [leaders[road] for road in leaders.keys()]
            leaders.sort()
            # go to step 6

        # STEP 6: Get the intersection leader
        dist_left, intersection_leader = leaders[0]
        if dist_left >= 1:
            # if the minimum normalised distance >= 1, go back to step 3
            return
        # got to step 7

        # STEP 7: Check if you're the intersection leader
        if intersection_leader == self.name:
            # you're the intersection leader
            # go to step 9

            # STEP 9: Check how many other leaders there are
            if len(leaders) > 1:
                # send a message to all the other leaders
                for dist_left, leader in leaders:
                    if leader != intersection_leader:
                        message = (leader, VTL_GREEN_REQUEST, None)
                        self.messages.append(message)
                # go to step 11

            else:
                # you're the only leader, go to step 10

                # STEP 10: Alert mode
                # send a message to the control centre, and start a timer
                message = (CONTROL_CENTRE, VTL_GREEN_REQUEST, None)
                self.messages.append(message)
                # go to step 11

        else:
            # you're not the intersection leader
            # go to step 8

            # STEP 8: Set traffic light to red
            self.light = RED_LIGHT

            # check if you are a leader or a follower
            is_leader = False
            for dist_left, leader in leaders:
                if leader == self.name:
                    is_leader = True
                    break
            # go to step 11

    def getLight(self, entrance, exit):
        return self.light

    def draw(self):
        world  = self.world
        screen = world.screen
        colour = self.colour

        a = world.getDrawable(self.car.centre)

        for car_name in self.knowledge:
            position, entrance = self.knowledge[car_name]

            b = world.getDrawable(position)
            pygame.draw.line(screen, colour, a, b, 3)


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

    def __repr__(self):
        return "Intersection{}".format(self.id)

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
        self.time   = car_controller.time

        self.intersection = None
        self.entrance     = None

        self.light = RED_LIGHT

        self.messages  = []
        self.knowledge = {}

        self.step       = 1
        self.leaders    = None
        self.role       = None

        self.nr   = None
        self.acks = None
        self.nf   = None

        self.timeout = -1

    def getLight(self, entrance, exit):
        return self.light

    def resetAll(self):
        self.intersection = None
        self.entrance     = None

        self.light = RED_LIGHT

        self.step    = 1
        self.leaders = None
        self.role    = None

        self.nr   = None
        self.acks = None

        self.timeout = None

    def chooseNewLeader(self):
        N = len(self.intersection.inputs)

        priorities = [None for i in range(N)]
        for car_name in self.knowledge:
            dist_left, entrance = self.knowledge[car_name]

            if not priorities[entrance]:
                priorities[entrance] = (dist_left, car_name)

            elif dist_left < priorities[entrance][0]:
                priorities[entrance] = (dist_left, car_name)

        for i in range(1, N):
            w = (self.entrance + i) % N

            if not priorities[w]:
                continue

            dist_left, car_name = priorities[w]

            if dist_left < VTL_LEADER_DIST:
                self.messages.append((car_name,          VTL_GREEN,
                                      self.intersection, VTL_NF_DEFAULT))
                print(self.intersection, self.name, "new leader chosen:", car_name)
                break

        self.resetAll()

    def update(self, time, instruction):
        self.time = time

        if isinstance(instruction, EnterIntersection):
            intersection = instruction.intersection
            if intersection == self.intersection:
                return

            if self.step == 23:
                self.resetAll()

            elif self.step == 24:
                self.chooseNewLeader()

            self.intersection = intersection
            self.entrance     = instruction.entrance

            self.light = AMBER_LIGHT
            self.nr    = 1
            self.step  = 3

        #elif not instruction.danger:
        #    if self.step == 23:
        #        self.resetAll()

        #    elif self.step == 24:
        #        self.chooseNewLeader()

    def assignRoles(self):
        roads = self.intersection.inputs
        priorities = [None for road in roads]
        for car_name in self.knowledge:
            dist_left, entrance = self.knowledge[car_name]

            if not priorities[entrance]:
                priorities[entrance] = (dist_left, car_name)

            elif dist_left < priorities[entrance][0]:
                priorities[entrance] = (dist_left, car_name)

        if self.nr >= VTL_NR_MAX:
            order = [(road, i) for i, road in enumerate(roads) \
                               if priorities[i]]
            order.sort()
            priorities = [priorities[i] for road, i in order]

        else:
            # sort by normalised distance
            priorities = [pair for pair in priorities if pair]
            priorities.sort()

        dist_left, intersection_leader = priorities[0]
        if dist_left >= VTL_LEADER_DIST:
            return

        self.leaders = [car_name for dist, car_name in priorities]

        if intersection_leader == self.name:
            self.role = VTL_INTERSECTION_LEADER
            self.acks = set()
            self.acks.add(self.name)

            if len(self.leaders) > 1:
                # send a message to all the other leaders
                for leader in self.leaders:
                    if leader != intersection_leader:

                        self.messages.append((leader, VTL_GREEN_REQUEST,
                                              self.intersection, None))
            else:
                # send a message to the control centre, and start a timer
                self.messages.append((CONTROL_CENTRE,    VTL_GREEN_REQUEST,
                                      self.intersection, None))
        else:
            # you're not the intersection leader
            self.light = RED_LIGHT

            # check if you are a leader or a follower
            self.role = VTL_FOLLOWER
            for leader in self.leaders:
                if leader == self.name:
                    self.role = VTL_LEADER
                    break

        # start a timer
        self.timeout = self.time + VTL_TIMEOUT
        self.step = 12

    def activateGreenLight(self, source, nf=None):

        if nf is None:
            print(self.intersection, self.name, "leader by priority")
            nf = VTL_NF_DEFAULT
        else:
            print(self.intersection, self.name, "leader by gift")

        # check if this car can cross the intersection
        if self.car_controller.blocked:
            print(self.intersection, self.name, "gives up leadership")
            self.chooseNewLeader()
            return

        self.light = GREEN_LIGHT
        self.role  = VTL_INTERSECTION_LEADER

        if source != CONTROL_CENTRE:
            self.messages.append((CONTROL_CENTRE, VTL_GREEN,
                                  self.intersection, None))

        if nf > 0:
            my_dist, my_entrance = self.knowledge[self.name]

            followers = []
            for car_name in self.knowledge:
                if car_name == self.name:
                    continue

                dist_left, entrance = self.knowledge[car_name]
                if entrance != my_entrance:
                    continue

                if dist_left > my_dist:
                    followers.append((dist_left, car_name))

            if followers:
                followers.sort()
                dist_left, car_name = followers[0]

                if dist_left - my_dist < VTL_FOLLOW_DIST:
                    self.messages.append((car_name,          VTL_GREEN,
                                          self.intersection, nf-1))

                    self.step = 23
                    return

        self.step = 24
        return

    def sendResponse(self, source):
        if self.leaders[0] == source:
            self.messages.append((source, VTL_ACKNOWLEDGE,
                                  self.intersection, None))
        else:
            self.messages.append((source, VTL_REFUSAL, self.intersection, None))
        self.step = 12

    def sendRetry(self):
        for leader in self.leaders:
            self.messages.append((leader, VTL_RETRY, self.intersection, None))
        self.nr += 1

    def checkResponses(self):
        # check timer
        if self.time >= self.timeout:
            #print(self.name, "timed out")

            if self.role != VTL_FOLLOWER:
                self.sendRetry()

            self.light = RED_LIGHT
            self.step  = 3
            return

        if self.role != VTL_INTERSECTION_LEADER:
            return

        # if there are no other leaders, check if the control centre responded
        if len(self.leaders) == 1:
            if True: # for now, let's just assume the controller said yes
            #if CONTROL_CENTRE in self.acks:
                self.activateGreenLight(CONTROL_CENTRE)
            return

        # check responses received
        for leader in self.leaders:
            if not leader in self.acks:
                return

        self.activateGreenLight(leader)

    def sendMessages(self):

        #self.knowledge.clear()

        position = self.car.centre
        road     = self.car_controller.road

        dist_along = road.getDistanceAlong(position)
        dist_left  = road.length - dist_along - CAR_LENGTH/2

        self.knowledge[self.name] = (dist_left, self.entrance)

        self.messages.append((SEND_TO_ALL, VTL_STATUS, self.intersection,
                              (dist_left, self.entrance)))
        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        new_knowledge = {}

        new_knowledge[self.name] = self.knowledge[self.name]

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if context != self.intersection:
                #if source in self.knowledge:
                #    del self.knowledge[source]
                continue

            if message_type == VTL_STATUS:
                dist_left, entrance = content

                if self.step == 12 and self.role != VTL_FOLLOWER:
                    if not source in self.leaders:
                        if dist_left < VTL_LEADER_DIST:
                            self.sendRetry()
                            self.light = RED_LIGHT
                            self.step  = 3

                new_knowledge[source] = (dist_left, entrance)

            elif message_type == VTL_REFUSAL:
                #print(source, destination, "VTL_REFUSAL")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.sendRetry()
                    self.light = RED_LIGHT
                    self.step  = 3

            elif message_type == VTL_RETRY:
                #print(source, destination, "VTL_RETRY")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.nr += 1
                    self.light = RED_LIGHT
                    self.step  = 3

            elif message_type == VTL_GREEN_REQUEST:
                #print(source, destination, "VTL_GREEN_REQUEST")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.sendResponse(source)

            elif message_type == VTL_ACKNOWLEDGE:
                #print(source, destination, "VTL_ACKNOWLEDGE")
                if self.step == 12 and self.role == VTL_INTERSECTION_LEADER:
                    #print(self.leaders)
                    self.acks.add(source)

            elif message_type == VTL_GREEN:
                print(source, destination, "VTL_GREEN", content)
                print(self.step)
                if self.step == 12:
                    self.activateGreenLight(source, content)

        self.knowledge = new_knowledge

        if self.step == 3:
            self.assignRoles()

        elif self.step == 12:
            self.checkResponses()

    def draw(self):
        world  = self.world
        screen = world.screen

        point = world.getDrawable(self.car.centre)

        if self.role == VTL_INTERSECTION_LEADER:
            pygame.draw.circle(screen, BLACK, point, 5)

            #for leader in self.leaders:
            #    if leader == self.name:
            #        continue

            #    for car in world.cars:
            #        if car.name == leader:
            #            b = world.getDrawable(car.centre)
            #            pygame.draw.line(screen, DARKER[self.colour], point, b, 5)

        else:
            if self.leaders:
                leader = self.leaders[0]
                for car in world.cars:
                    if car.name == leader:
                        b = world.getDrawable(car.centre)
                        pygame.draw.line(screen, car.colour, point, b, 3)
                        break

            if self.role == VTL_LEADER:
                pygame.draw.circle(screen, BLACK, point, 5, 1)


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

        self.pairs = {}
        self.paths = {}

        self.connections = [[None, None, None] for i in range(len(inputs))]

    def addConnection(self, entrance, exit, path, turn):
        pair = (entrance, exit)
        self.pairs[pair] = turn
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

EMPTY_LIGHTS   = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
ALL_THE_LIGHTS = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

LIGHT_COMBINATIONS = [
    # [CENTRE, RIGHT, LEFT]

    # lane 0     lane 1     lane 2     lane 3

    # three branches from one road, and one left turn
    [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 1], [1, 1, 1]],

    # one road straight across, and three left turns
    [[1, 0, 1], [0, 0, 0], [0, 0, 1], [0, 0, 1]],
    [[0, 0, 1], [1, 0, 1], [0, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 1], [1, 0, 1]],

    # two lanes straight across, and two left turns
    [[1, 0, 1], [0, 0, 0], [1, 0, 1], [0, 0, 0]],
    [[0, 0, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1]],

    # one right turn, and three left turns
    [[0, 1, 1], [0, 0, 1], [0, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 0, 1]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 1, 1]],

    # two right turns, and two left turns
    [[0, 1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]],

    # four left turns
    [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
]

##################
# TRAFFIC LIGHTS #
##################

SIMPLE_SEQUENCE = [0, 1, 2, 3]

def loopingIterator(items, start):
    for i in range(start, len(items)):
        yield items[i]

    while True:
        for item in items:
            yield item

class TrafficLights:
    def __init__(self, world, intersection):
        self.world        = world
        self.intersection = intersection

        combs = [LIGHT_COMBINATIONS[i] for i in SIMPLE_SEQUENCE]
        start = random.randint(0, len(combs)-1)
        self.comb_gen = loopingIterator(combs, start)

        self.prev_lights = EMPTY_LIGHTS
        self.curr_lights = next(self.comb_gen)

        self.offset = random.randint(0, CYCLE_DURATION-1)

        self.phase = GREEN_LIGHT

    def update(self, time):
        cycle_time = (time + self.offset) % CYCLE_DURATION

        if self.phase == GREEN_LIGHT:
            if cycle_time >= AMBER_PHASE:
                self.phase = AMBER_LIGHT

                self.prev_lights = self.curr_lights
                self.curr_lights = next(self.comb_gen)

        elif self.phase == AMBER_LIGHT:
            if cycle_time >= RED_PHASE:
                self.phase = RED_LIGHT

        elif self.phase == RED_LIGHT:
            if cycle_time < AMBER_PHASE:
                self.phase = GREEN_LIGHT

    def getLight(self, entrance, exit):
        turn = getTurn(entrance, exit)

        prev_light = self.prev_lights[entrance][turn]
        curr_light = self.curr_lights[entrance][turn]
        if self.phase == GREEN_LIGHT:
            if curr_light:
                return GREEN_LIGHT
            else:
                return RED_LIGHT

        if prev_light and curr_light:
            return GREEN_LIGHT

        if self.phase == RED_LIGHT:
            return RED_LIGHT

        if prev_light:
            return AMBER_LIGHT
        else:
            return RED_LIGHT

    def draw(self):
        world  = self.world
        screen = world.screen

        for entrance in range(4):
            for turn in range(3):

                exit  = getExit(entrance, turn)

                light = self.getLight(entrance, exit)
                if light == RED_LIGHT:
                    continue
                elif light == AMBER_LIGHT:
                    colour = AMBER
                else:
                    colour = GREEN

                for road in self.intersection.paths[(entrance, exit)]:
                    start = world.getDrawable(road.start)
                    end   = world.getDrawable(road.end)
                    pygame.draw.line(screen, colour, start, end, 2)

##########################
# VIRTUAL TRAFFIC LIGHTS #
##########################

class VirtualTrafficLights:
    def __init__(self, car_controller):
        self.car_controller = car_controller

        self.world  = car_controller.world
        self.name   = car_controller.name
        self.colour = car_controller.colour
        self.car    = car_controller.car
        self.time   = car_controller.time

        self.intersection = None
        self.road         = None
        self.entrance     = None

        self.light = RED_LIGHT

        self.messages  = []
        self.knowledge = {}

        self.vehicles = set()

        self.stage = VTL_NO_INTERSECTION

        # STAGE 1
        self.num_retries = None

        # STAGE 2
        self.leaders     = None
        self.role        = None
        self.acks        = None
        self.timeout     = -1

        # STAGE 3
        self.num_followers  = None
        self.first_follower = None

    def getLight(self, entrance, exit):
        return self.light

    def chooseNewLeader(self):
        N = len(self.intersection.inputs)

        priorities = [None for i in range(N)]
        for car_name in self.knowledge:
            dist_left, entrance, spaces = self.knowledge[car_name]

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
                #print(self.intersection, self.name,
                #      "new leader chosen:", car_name, "D")
                break

    def update(self, time, instruction):
        self.time = time

        if isinstance(instruction, EnterIntersection):
            intersection = instruction.intersection
            if intersection == self.intersection:
                return

            if self.stage == VTL_CHOOSE_NEW_LEADER:
                self.chooseNewLeader()

            self.intersection = intersection
            self.road         = instruction.road
            self.entrance     = instruction.entrance

            self.light       = AMBER_LIGHT
            self.num_retries = 1
            self.stage       = VTL_JOIN_INTERSECTION

        elif not instruction.danger:

            if self.stage == VTL_CHOOSE_NEW_LEADER:
                self.chooseNewLeader()

            self.stage = VTL_NO_INTERSECTION

            self.intersection = None
            self.road         = None
            self.entrance     = None

    def retry(self, broadcast=True):
        self.light = RED_LIGHT
        self.stage = VTL_CALCULATE_LEADERS

        if broadcast and self.role != VTL_FOLLOWER:#self.role == VTL_INTERSECTION_LEADER:
            for leader in self.leaders:
                self.messages.append((leader,            VTL_RETRY,
                                      self.intersection, None))
        return

    def assignRoles(self):
        roads = self.intersection.inputs
        priorities = [None for road in roads]
        for car_name in self.knowledge:
            dist_left, entrance, spaces = self.knowledge[car_name]

            blocked = spaces < 1

            if not priorities[entrance]:
                priorities[entrance] = (blocked, dist_left, car_name)

            elif dist_left < priorities[entrance][1]:
                priorities[entrance] = (blocked, dist_left, car_name)

        if self.num_retries >= VTL_NR_MAX:
            order = [(priorities[i][0], road, i) for i, road \
                      in enumerate(roads) if priorities[i]]
            order.sort()
            priorities = [priorities[i] for road, i in order]

        else:
            # sort by normalised distance
            priorities = [trio for trio in priorities if trio]
            priorities.sort()

        blocked, dist_left, intersection_leader = priorities[0]
        if dist_left > VTL_LEADER_DIST:
            return

        self.leaders = [car_name for blocked, dist, car_name in priorities]

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

        self.stage   = VTL_GET_APPROVALS
        self.timeout = self.time + VTL_TIMEOUT

    def getApprovals(self, new_vehicles, requests, acks, refusals, retries):

        if self.time >= self.timeout:
            self.retry()
            return False

        if retries:
            self.retry(False)
            return False

        if self.role != VTL_FOLLOWER:
            for car_name in new_vehicles:
                dist_left, entrance, spaces = self.knowledge[car_name]

                if dist_left < VTL_LEADER_DIST:
                    self.retry()
                    return False

        if requests:
            if self.role == VTL_LEADER:
                intersection_leader = self.leaders[0]
                for car_name in requests:
                    if car_name == intersection_leader:
                        self.messages.append((car_name, VTL_ACKNOWLEDGE,
                                              self.intersection, None))
                    else:
                        self.messages.append((car_name, VTL_REFUSAL,
                                              self.intersection, None))
            else:
                for car_name in requests:
                    self.messages.append((car_name, VTL_REFUSAL,
                                          self.intersection, None))

        if self.role != VTL_INTERSECTION_LEADER:
            return False

        if refusals:
            self.retry()
            return False

        self.acks |= acks

        if len(self.leaders) == 1:
            if True: # for now, let's just assume the controller said yes
            #if CONTROL_CENTRE in self.acks:
                #print(self.intersection,
                #      "new leader chosen by control centre:",
                #      self.name, "A")
                return True

        # check responses received
        for leader in self.leaders:
            if not leader in self.acks:
                return False

        #print(self.intersection,
        #      "new leader approved:", self.name, "B", self.acks)
        # TODO: Notify control centre
        return True

    def activateGreenLight(self):
        if self.car_controller.spaces_left < 1:#blocked:
            #print(self.name, "gave up leadership")
            self.retry()
            return

        self.light   = GREEN_LIGHT
        self.role    = VTL_CROSSING
        self.leaders = None

        self.stage = VTL_CHOOSE_NEW_LEADER
        self.first_follower = None

    def checkFollower(self):
        if self.num_followers <= 0:
            return

        my_dist, my_entrance, spaces = self.knowledge[self.name]

        if self.first_follower == None:

            followers = []
            for car_name in self.knowledge:
                if car_name == self.name:
                    continue

                dist_left, entrance, spaces = self.knowledge[car_name]
                if entrance != my_entrance:
                    continue

                if dist_left > my_dist:
                    followers.append((dist_left, car_name, spaces))

            if not followers:
                return

            followers.sort()
            dist_left, car_name, spaces = followers[0]
            self.first_follower = car_name

        else:
            dist_left, entrance, spaces = self.knowledge[self.first_follower]

        if spaces < 1 or dist_left - my_dist > VTL_FOLLOW_DIST:
            return

        self.messages.append((self.first_follower, VTL_GREEN,
                              self.intersection,  self.num_followers-1))
        #print(self.intersection, self.name, "new leader chosen:",
        #      self.first_follower, "C")
        self.stage = VTL_NO_INTERSECTION

    def sendMessages(self):

        if self.intersection == None:
            return self.messages

        position = self.car.centre
        road     = self.road

        dist_along = road.getDistanceAlong(position)
        dist_left  = road.length - dist_along

        if self.stage == VTL_JOIN_INTERSECTION:
            if dist_left > VTL_THRESHOLD:
                return self.messages

            self.stage = VTL_CALCULATE_LEADERS

        content = (dist_left, self.entrance, self.car_controller.spaces_left)

        self.knowledge[self.name] = content

        self.messages.append((SEND_TO_ALL,       VTL_STATUS,
                              self.intersection, content))
        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        new_vehicles = set()
        vehicles     = set()

        requests = []
        acks     = set()
        refusals = []
        retries  = []
        greens   = []

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if context != self.intersection:
                continue

            if message_type == VTL_STATUS:

                if not source in self.knowledge:
                    new_vehicles.add(source)

                vehicles.add(source)
                self.knowledge[source] = content

            elif message_type == VTL_GREEN_REQUEST:
                requests.append(source)

            elif message_type == VTL_ACKNOWLEDGE:
                acks.add(source)

            elif message_type == VTL_REFUSAL:
                refusals.append(source)

            elif message_type == VTL_RETRY:
                retries.append(source)

            elif message_type == VTL_GREEN:
                greens.append((source, content))

        # remove the vehicles that aren't in this intersection anymore
        for vehicle in self.vehicles - vehicles:
            del self.knowledge[vehicle]

        if self.stage == VTL_CALCULATE_LEADERS:
            self.assignRoles()

            new_vehicles = set()

        # update vehicles list
        self.vehicles = vehicles

        if self.stage == VTL_GET_APPROVALS:
            #print(self.name, "new_vehicles:", new_vehicles,
            #      "requests:", requests, "acks:", acks,
            #      "refusals:", refusals, "retries", retries)

            turn_green = self.getApprovals(new_vehicles, requests,
                                           acks, refusals, retries)

            if turn_green:
                self.num_followers = VTL_NF_DEFAULT

            else:
                for car_name, num_followers in greens:
                    turn_green = True
                    self.num_followers = num_followers
                    # TODO: Notify control centre
                    break

            if turn_green:
                self.activateGreenLight()

        if self.stage == VTL_CHOOSE_NEW_LEADER:
            self.checkFollower()

    def draw(self):
        world  = self.world
        screen = world.screen

        point  = world.getDrawable(self.car.centre)
        radius = world.scaleDistance(CAR_WIDTH/2 + 0.1)

        if self.light == GREEN_LIGHT:
            colour = GREEN
        elif self.light == AMBER_LIGHT:
            colour = AMBER
        else:
            colour = RED

        pygame.draw.circle(screen, colour, point, radius)
        pygame.draw.circle(screen, BLACK,  point, radius, 1)

        if False:

            if self.role == VTL_INTERSECTION_LEADER:
                pygame.draw.circle(screen, BLACK, point, 10)

                for leader in self.leaders:
                    if leader == self.name:
                        continue

                    for car in world.cars:
                        if car.name == leader:
                            b = world.getDrawable(car.centre)
                            pygame.draw.circle(screen, self.colour, b, 15, 2)

            elif self.role == VTL_CROSSING:
                pygame.draw.circle(screen, WHITE, point, 10)
                pygame.draw.circle(screen, BLACK, point, 10, 2)

            else:
                if self.leaders:
                    leader = self.leaders[0]
                    for car in world.cars:
                        if car.name == leader:
                            b = world.getDrawable(car.centre)
                            pygame.draw.line(screen, car.colour, point, b, 3)
                            break

                elif self.role == VTL_LEADER:
                    pygame.draw.circle(screen, BLACK, point, 10, 2)

#########################
# MY TRAFFIC CONTROLLER #
#########################

combs_including_connection = {}
for entrance in range(4):
    for turn in range(-1, 2):

        combs = set()
        for i, comb in enumerate(LIGHT_COMBINATIONS):
            if comb[entrance][turn]:
                combs.add(i)

        connection = (entrance, getExit(entrance, turn))
        combs_including_connection[connection] = combs

VALID_PAIRS = {}
for connectionA in combs_including_connection:
    combsA = combs_including_connection[connectionA]

    valid_B = set()

    for connectionB in combs_including_connection:
        combsB = combs_including_connection[connectionB]

        if combsA & combsB:
            valid_B.add(connectionB)

    VALID_PAIRS[connectionA] = valid_B

class MyTrafficController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

        self.world  = car_controller.world
        self.name   = car_controller.name
        self.colour = car_controller.colour
        self.car    = car_controller.car
        self.time   = car_controller.time

        self.intersection = None
        self.road         = None
        self.route        = None
        self.start_time   = None

        self.messages      = []
        self.knowledge     = {}
        self.existing_cars = {}

        self.leader = None
        self.stage  = MTC_NO_INTERSECTION

        self.crossing_cars = {}

    def getLight(self, entrance, exit):
        if self.stage == MTC_CROSSING:
            return GREEN_LIGHT
        return RED_LIGHT

    def chooseNextLeader(self):
        options = []
        for car_name in self.existing_cars:
            #if car_name == self.name:
            #    continue

            wait_time = self.existing_cars[car_name]
            options.append((-wait_time, car_name))

        #if not options:
        #    return None

        options.sort()
        # return options[0][-1]
        return [option[-1] for option in options]

    def announceCrossed(self):
        if self.leader == self.name:

            for car_name in self.chooseNextLeader():
                if car_name != self.name:
                    new_leader = car_name
                    break
            else:
                new_leader = None

            if self.route in self.crossing_cars:
                if self.crossing_cars[self.route] == self.name:
                    del self.crossing_cars[self.route]

            self.messages.append(
                (SEND_TO_ALL, MTC_NEW_LEADER, self.intersection,
                 (new_leader, self.crossing_cars.copy()))
            )

            self.leader = None

        else:
            self.messages.append((SEND_TO_ALL, MTC_FINISHED_CROSSING,
                                  self.intersection, self.route))


    def update(self, time, instruction):
        self.time = time

        if isinstance(instruction, EnterIntersection):
            intersection = instruction.intersection
            if intersection == self.intersection:
                return

            if self.stage == MTC_CROSSING:
                self.announceCrossed()

            self.intersection = intersection
            self.road         = instruction.road
            self.route        = (instruction.entrance, instruction.exit)
            self.start_time   = time

            self.leader = None
            self.stage  = MTC_OUT_OF_RANGE

            self.crossing_cars.clear()

        #elif instruction.danger:
        #    self.stage = MTC_CROSSING

        elif not instruction.danger:
            if self.stage == MTC_CROSSING:
                self.announceCrossed()

            self.stage = MTC_NO_INTERSECTION

    def getLeadCars(self):
        car_queues = [[] for entrance_road in self.intersection.inputs]

        for car_name in self.knowledge:
            dist_left, wait_time, route, spaces = self.knowledge[car_name]
            entrance, exit = route
            car_queues[entrance].append((dist_left, car_name))

        lead_cars = []
        for car_queue in car_queues:
            if car_queue:
                car_queue.sort()

                car_name = car_queue[0][-1]
                dist_left, wait_time, route, spaces = self.knowledge[car_name]

                lead_cars.append((-wait_time, car_name, route))

        lead_cars.sort()
        return [(name, route) for wait, name, route in lead_cars]

    def carCanCross(self, car_name):
        dist_left, wait_time, route, spaces = self.knowledge[car_name]
        if spaces < 1 or dist_left > MTC_CROSS_DIST:
            return False
        return self.crossing_cars.keys() <= VALID_PAIRS[route]

    def sendMessages(self):
        self.knowledge.clear()
        self.existing_cars.clear()

        if self.stage == MTC_NO_INTERSECTION:
            return self.messages

        position = self.car.centre
        road     = self.road

        dist_along = road.getDistanceAlong(position)
        dist_left  = road.length - dist_along

        if self.stage == MTC_OUT_OF_RANGE:
            if dist_left > MTC_THRESHOLD:
                return self.messages
            else:
                self.stage = MTC_IN_QUEUE

        wait_time = self.time - self.start_time

        self.messages.append((SEND_TO_ALL, MTC_CAR_EXISTS,
                              self.intersection, wait_time))

        self.existing_cars[self.name] = wait_time

        if self.stage == MTC_CROSSING:
            return self.messages

        content = (dist_left, wait_time, self.route,
                   self.car_controller.spaces_left)

        self.knowledge[self.name] = content

        self.messages.append((SEND_TO_ALL,       MTC_CAR_STATUS,
                              self.intersection, content))
        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        if self.stage in {MTC_NO_INTERSECTION, MTC_OUT_OF_RANGE}:
            return

        #lights_announce = []

        green_lights = []
        new_leaders  = []
        crossed      = []

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if context != self.intersection:
                continue

            if message_type == MTC_CAR_STATUS:
                self.knowledge[source] = content

            elif message_type == MTC_CAR_EXISTS:
                self.existing_cars[source] = content

            #elif message_type == MTC_ANNOUNCE_LIGHTS:
            #    lights_announce.append((source, content))

            elif message_type == MTC_GREEN_LIGHT:
                green_lights.append((source, destination))

            elif message_type == MTC_NEW_LEADER:
                new_leaders.append((source, content))

            elif message_type == MTC_FINISHED_CROSSING:
                crossed.append((source, content))

        for source, content in new_leaders:
            if source == self.leader or self.leader == None:
                new_leader, crossing_cars = content

                self.crossing_cars = crossing_cars.copy()

                if new_leader in self.existing_cars:
                    self.leader = new_leader
                else:
                    self.leader = None

        for source, destination in green_lights:
            if source == self.leader or self.leader == None:
                if destination == self.name:
                    self.stage = MTC_CROSSING
                    return

        if self.leader == None:
            # decide who the leader is

            # this is just a placeholder
            #self.leader = self.chooseLeader()

            if len(self.existing_cars) == 1:
                self.leader = self.name

            else:
                self.leader = self.chooseNextLeader()[0]

        # lead intersection
        if self.leader == self.name:

            # light time out
            #timed_out = []
            #for route in self.lights:
            #    red_time = self.lights[route][1]
            #    if red_time <= self.time:
            #        timed_out.append(route)
            #for route in timed_out:
            #    del self.lights[route]

            for source, route in crossed:
                if route in self.crossing_cars:
                    if self.crossing_cars[route] == source:
                        del self.crossing_cars[route]

            if self.stage != MTC_CROSSING:

                if self.carCanCross(self.name):
                    self.crossing_cars[self.route] = self.name

                    self.stage = MTC_CROSSING

                    print(self.name, self.crossing_cars)

                    #new_leader = self.chooseLeader()

                    #self.messages.append(
                    #    (SEND_TO_ALL, MTC_NEW_LEADER, self.intersection,
                    #     (new_leader, self.crossing_cars))
                    #)
                    #return

            lead_cars = self.getLeadCars()
            for car_name, route in lead_cars:

                if self.carCanCross(car_name):

                    self.crossing_cars[route] = car_name

                    self.messages.append((car_name, MTC_GREEN_LIGHT,
                                          self.intersection, None))

                    print(self.name, self.crossing_cars)

                    #amber_time = self.time  + MTC_GREEN_TIME
                    #red_time   = amber_time + MTC_TURN_TIMES[getTurn(*route)]

                    #self.lights[route] = (amber_time, red_time)

            #self.messages.append(
            #    (SEND_TO_ALL, MTC_ANNOUNCE_LIGHTS, self.intersection,
            #     (self.lights.copy(), self.exit_counts.copy()))
            #)

    def drawBackground(self):
        if self.leader != self.name:
            return

        world  = self.world
        screen = world.screen

        for route in self.crossing_cars:
            colour = GREEN

            for road in self.intersection.paths[route]:
                start = world.getDrawable(road.start)
                end   = world.getDrawable(road.end)
                pygame.draw.line(screen, colour, start, end, 2)

    def draw(self):

        if self.stage == MTC_NO_INTERSECTION:
            return

        world  = self.world
        screen = world.screen

        if self.leader == self.name:
            colour = YELLOW
        elif self.stage == MTC_CROSSING:
            colour = GREEN
        elif self.stage == MTC_OUT_OF_RANGE:
            colour = GREY
        else:
            colour = WHITE

        radius = CAR_WIDTH/2 + 0.1

        pos = world.getDrawable(self.car.centre)
        rad = world.scaleDistance(CAR_WIDTH/2 + 0.1)

        pygame.draw.circle(screen, colour, pos, rad)
        pygame.draw.circle(screen, BLACK,  pos, rad, 1)

class alt_MyTrafficController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

        self.world  = car_controller.world
        self.name   = car_controller.name
        self.colour = car_controller.colour
        self.car    = car_controller.car
        self.time   = car_controller.time

        self.intersection = None
        self.road         = None
        self.route        = None
        self.start_time   = None

        self.lights      = {}
        self.exit_counts = {}

        self.messages  = []
        self.knowledge = {}

        self.leader = None
        self.stage  = MTC_NO_INTERSECTION

    def getLight(self, entrance, exit):
        route = (entrance, exit)
        if route in self.lights:
            amber_time = self.lights[route][0]

            if amber_time <= self.time:
                return AMBER_LIGHT

            return GREEN_LIGHT

        return RED_LIGHT

    def update(self, time, instruction):
        self.time = time

        if isinstance(instruction, EnterIntersection):
            intersection = instruction.intersection
            if intersection == self.intersection:
                return

            self.intersection = intersection
            self.road         = instruction.road
            self.route        = (instruction.entrance, instruction.exit)
            self.start_time   = time

            self.leader = None
            self.stage  = MTC_OUT_OF_RANGE

            self.lights      = {}
            self.exit_counts = {}

        elif instruction.danger:
            self.stage = MTC_CROSSING
        else:
            self.stage = MTC_NO_INTERSECTION

    def getLeadCars(self):
        car_queues = [[] for entrance_road in self.intersection.inputs]

        for car_name in self.knowledge:
            dist_left, wait_time, route, spaces = self.knowledge[car_name]
            entrance, exit = route
            car_queues[entrance].append((dist_left, car_name))

        lead_cars = []
        for car_queue in car_queues:
            if car_queue:
                car_queue.sort()

                car_name = car_queue[0][-1]
                dist_left, wait_time, route, spaces = self.knowledge[car_name]

                entrance, exit = route

                #if exit in self.exit_counts:
                #    bias = self.exit_counts[exit]
                #else:
                #    bias = 0

                #turn = getTurn(*route)
                #if turn == RIGHT:
                #    turn_advantage = 0
                #else:
                #    turn_advantage = 1

                if spaces >= 1:
                    lead_cars.append((-wait_time, car_name))

        lead_cars.sort()
        return [details[-1] for details in lead_cars]

    def chooseLeader(self):
        options = []
        for car_name in self.knowledge:
            dist_left, wait_time, route, spaces = self.knowledge[car_name]
            options.append((-wait_time, car_name))
        options.sort()
        return options[0][1]

    def sendMessages(self):
        self.knowledge.clear()

        if self.stage in {MTC_NO_INTERSECTION, MTC_CROSSING}:
            return self.messages

        position = self.car.centre
        road     = self.road

        dist_along = road.getDistanceAlong(position)
        dist_left  = road.length - dist_along

        if self.stage == MTC_OUT_OF_RANGE:
            if dist_left > MTC_THRESHOLD:
                return self.messages
            else:
                self.stage = MTC_IN_QUEUE

        wait_time = self.time - self.start_time

        content = (dist_left, wait_time, self.route,
                   self.car_controller.spaces_left)

        self.knowledge[self.name] = content

        self.messages.append((SEND_TO_ALL,       MTC_CAR_STATUS,
                              self.intersection, content))
        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        if self.stage != MTC_IN_QUEUE:
            return

        lights_announce = []

        for message in messages:
            source, destination, message_type, context, content = message

            if source == self.name:
                continue

            if context != self.intersection:
                continue

            if message_type == MTC_CAR_STATUS:
                self.knowledge[source] = content

            elif message_type == MTC_ANNOUNCE_LIGHTS:
                lights_announce.append((source, content))

        # update lights
        for car_name, content in lights_announce:
            #if car_name == self.leader or self.leader == None:
            lights, exit_counts = content

            self.lights      = lights.copy()
            self.exit_counts = exit_counts.copy()

        # choose leader
        self.leader = self.chooseLeader()

        # lead intersection
        if self.leader == self.name:

            # light time out
            timed_out = []
            for route in self.lights:
                red_time = self.lights[route][1]
                if red_time <= self.time:
                    timed_out.append(route)
            for route in timed_out:
                del self.lights[route]

            #dont_block_me = VALID_PAIRS[self.route]

            lead_cars = self.getLeadCars()
            for car_name in lead_cars:

                dist_left, wait_time, route, spaces = self.knowledge[car_name]

                if dist_left > MTC_CROSS_DIST:
                    continue

                if self.lights.keys() <= VALID_PAIRS[route]:

                    amber_time = self.time  + MTC_GREEN_TIME
                    red_time   = amber_time + MTC_TURN_TIMES[getTurn(*route)]

                    #if not route in dont_block_me:
                    #    continue

                    self.lights[route] = (amber_time, red_time)

                    #entrance, exit = route
                    #if exit in self.exit_counts:
                    #    self.exit_counts[exit] += 1
                    #else:
                    #    self.exit_counts[exit] = 1
                #break

            self.messages.append(
                (SEND_TO_ALL, MTC_ANNOUNCE_LIGHTS, self.intersection,
                 (self.lights.copy(), self.exit_counts.copy()))
            )

    def drawBackground(self):
        if self.stage != MTC_IN_QUEUE or self.leader != self.name:
            return

        world  = self.world
        screen = world.screen

        for route in self.lights:
            amber_time = self.lights[route][0]
            if amber_time <= self.time:
                colour = AMBER
            else:
                colour = GREEN

            for road in self.intersection.paths[route]:
                start = world.getDrawable(road.start)
                end   = world.getDrawable(road.end)
                pygame.draw.line(screen, colour, start, end, 2)

    def draw(self):

        if self.stage == MTC_NO_INTERSECTION:
            return

        world  = self.world
        screen = world.screen

        if self.stage == MTC_CROSSING:
            colour = GREEN
        elif self.stage == MTC_OUT_OF_RANGE:
            colour = GREY
        elif self.leader == self.name:
            colour = YELLOW
        else:
            colour = WHITE

        radius = CAR_WIDTH/2 + 0.1

        pos = world.getDrawable(self.car.centre)
        rad = world.scaleDistance(CAR_WIDTH/2 + 0.1)

        pygame.draw.circle(screen, colour, pos, rad)
        pygame.draw.circle(screen, BLACK,  pos, rad, 1)

        #if self.leader == self.name:

            #rad1 = world.scaleDistance(radius*0.65)
            #rad2 = world.scaleDistance(radius*0.3)

            #pygame.draw.circle(screen, BLACK, pos, rad1)
            #pygame.draw.circle(screen, WHITE, pos, rad2)

            #rect = generateRect(self.car.centre, radius/2, self.world)

            #pygame.draw.rect(screen, BLACK, rect)

            #font = pygame.font.SysFont('Helvetica', radius, bold=True)

            #text = font.render(" L ", False, BLACK)
            #rect = text.get_rect(center=point)
            #screen.blit(text, rect)

            #border = rect.inflate(8, 2)
            #pygame.draw.rect(screen, BLACK, rect, 1)

            #pygame.draw.circle(screen, AMBER, point, radius//2)


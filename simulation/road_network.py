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
            dist_left, entrance, blocked = self.knowledge[car_name]

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
            self.stage       = VTL_CALCULATE_LEADERS

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
            dist_left, entrance, blocked = self.knowledge[car_name]

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
        if dist_left >= VTL_LEADER_DIST:
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
                dist_left, entrance, blocked = self.knowledge[car_name]

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
        if self.car_controller.blocked:
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

        my_dist, my_entrance, blocked = self.knowledge[self.name]

        if self.first_follower == None:

            followers = []
            for car_name in self.knowledge:
                if car_name == self.name:
                    continue

                dist_left, entrance, blocked = self.knowledge[car_name]
                if entrance != my_entrance:
                    continue

                if dist_left > my_dist:
                    followers.append((dist_left, car_name, blocked))

            if not followers:
                return

            followers.sort()
            dist_left, car_name, blocked = followers[0]
            self.first_follower = car_name

        else:
            dist_left, entrance, blocked = self.knowledge[self.first_follower]

        if blocked or dist_left - my_dist > VTL_FOLLOW_DIST:
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
        dist_left  = road.length - dist_along - CAR_LENGTH/2

        content = (dist_left, self.entrance, self.car_controller.blocked)

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


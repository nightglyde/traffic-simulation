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

    def resetAll(self):
        self.intersection = None
        self.entrance     = None

        self.light = RED_LIGHT

        self.step    = 1
        self.leaders = None
        self.role    = None

        self.nr   = None
        self.acks = None
        self.nf   = None

        self.timeout = None

    def stepTwentyFour(self):
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
                self.stepTwentyFour()

            self.intersection = intersection
            self.entrance     = instruction.entrance

            self.light = AMBER_LIGHT
            self.nr    = 1

            self.step = 3

            self.my_priority = None


        elif not instruction.danger:
            if self.step == 23:
                self.resetAll()

            elif self.step == 24:
                self.stepTwentyFour()

        if self.step == 23 and not instruction.danger:
            self.resetAll()

        if self.step == 24 and not instruction.danger:
            self.stepTwentyFour()

        #if self.step == 1 and not instruction.danger:
        #    if self.next_car != None:
        #        self.messages.append(
        #            (self.next_car, VTL_GREEN, VTL_NF_DEFAULT))

        #if isinstance(instruction, EnterIntersection):
        #    intersection = instruction.intersection
        #    if intersection == self.intersection:
        #        return

        #    self.intersection = intersection
        #    self.entrance     = instruction.entrance

        #    self.light = AMBER_LIGHT
        #    self.nr    = 1

        #    self.step = 3

        #    self.my_priority = None

        #elif not instruction.danger:
        #    self.intersection = None
        #    self.step = 1

    def stepThree(self):
        # STEP 3: find the leader of each road segment
        roads = self.intersection.inputs
        priorities = [[] for road in roads]
        for car_name in self.knowledge:
            position, entrance = self.knowledge[car_name]

            if car_name == self.name:
                my_entrance = entrance

            road = roads[entrance]
            dist_along = road.getDistanceAlong(position)
            dist_left  = road.length - dist_along - CAR_LENGTH/2

            priorities[entrance].append((dist_left, car_name))

        for car_list in priorities:
            car_list.sort()

        # STEP 4: Put the leaders in order
        if self.nr >= VTL_NR_MAX:
            # go to step 5

            # STEP 5: sort by road ID

            order = [(road, i) for i, road in enumerate(roads) \
                               if priorities[i]]
            order.sort()
            priorities = [priorities[i] for road, i in order]
            # go to step 6

        else:
            # sort by normalised distance
            order = [(priorities[i][0], i) for i in range(len(roads)) \
                                           if priorities[i]]
            order.sort()
            priorities = [priorities[i] for entry, i in order]
            # go to step 6

        # STEP 6: Get the intersection leader
        dist_left, intersection_leader = priorities[0][0]
        if dist_left >= VTL_LEADER_DIST:
            # if the minimum normalised distance >= 1, go back to step 3
            return
        # got to step 7

        self.leaders = [car_list[0][1] for car_list in priorities]

        # STEP 7: Check if you're the intersection leader
        if intersection_leader == self.name:
            self.role = VTL_INTERSECTION_LEADER
            self.acks = set()
            #self.acks.clear()
            self.acks.add(self.name)

            # go to step 9

            # STEP 9: Check how many other leaders there are
            if len(self.leaders) > 1:
                # send a message to all the other leaders
                for leader in self.leaders:
                    if leader != intersection_leader:
                        self.messages.append((leader, VTL_GREEN_REQUEST, None))
                # go to step 11

            else:
                # you're the only leader, go to step 10

                # STEP 10: Alert mode
                # send a message to the control centre, and start a timer
                self.messages.append((CONTROL_CENTRE, VTL_GREEN_REQUEST, None))
                # go to step 11

        else:
            # you're not the intersection leader
            # go to step 8

            # STEP 8: Set traffic light to red
            self.light = RED_LIGHT

            # check if you are a leader or a follower
            self.role = VTL_FOLLOWER
            for leader in self.leaders:
                if leader == self.name:
                    self.role = VTL_LEADER
                    break
            # go to step 11

        # STEP 11: Start a timer
        self.timeout = self.time + VTL_TIMEOUT
        #print(self.name, "set a timer", self.timeout, "at time", self.time)
        # go to step 12

        # STEP 12: Wait
        self.step = 12

    def stepSixteen(self):
        self.light = RED_LIGHT
        self.step = 3

    def stepFifteen(self):
        self.nr += 1
        self.stepSixteen()

    def stepFourteen(self):
        for leader in self.leaders:
            self.messages.append((leader, VTL_RETRY, None))
        self.stepFifteen()

    def stepThirteen(self, position, entrance):
        road = self.intersection.inputs[entrance]

        dist_along = road.getDistanceAlong(position)
        dist_left  = road.length - dist_along

        if dist_left < VTL_LEADER_DIST:
            self.stepFourteen()

    def stepSeventeen(self, source):
        if self.leaders[0] == source:
            self.messages.append((source, VTL_ACKNOWLEDGE, None))
        else:
            self.messages.append((source, VTL_REFUSAL, None))
        self.step = 12

    def stepTwentyOne(self, source):
        self.light = GREEN_LIGHT
        print(self.name, "GREEN")

        if source != CONTROL_CENTRE:
            self.messages.append((CONTROL_CENTRE, VTL_GREEN, None))

        #if True:
        #    self.step = 1
        #    return

        # THE BIT BELOW IS BROKEN
        # Also, it might be a good idea to re-calculate all the probabilities
        # every time a new car appears
        # And then, once that's working, I could make it so that I only need
        # to update the probabilities

        if self.nf > 0:

            my_position, my_entrance = self.knowledge[self.name]

            road = self.intersection.inputs[my_entrance]
            dist = road.length - CAR_LENGTH/2

            my_dist = dist - road.getDistanceAlong(my_position)

            followers = []
            for car_name in self.knowledge:
                if car_name == self.name:
                    continue

                position, entrance = self.knowledge[car_name]
                if entrance != my_entrance:
                    continue

                dist_left = dist - road.getDistanceAlong(position)

                print(self.name, car_name, dist_left, my_dist, dist_left > my_dist)

                if dist_left > my_dist:
                    followers.append((dist_left, car_name))

            if followers:
                followers.sort()

                dist_left, car_name = followers[0]

                print(self.name, car_name, dist_left, my_dist, dist_left-my_dist)

                if dist_left - my_dist < VTL_FOLLOW_DIST:
                    self.messages.append((car_name, VTL_GREEN, self.nf-1))

                    self.step = 23
                    #self.role = None
                    return

            #car_list = self.priorities[self.my_priority]

            #if len(car_list) > 1:
            #    my_dist = car_list[0][0]

            #    dist_left, car_name = car_list[1]

            #    if dist_left - my_dist < VTL_FOLLOW_DIST:
            #        self.messages.append((car_name, VTL_GREEN, self.nf-1))

            #        self.step = 1
            #        self.role = None
            #        return

        self.step = 24

        #for i in range(1, len(self.leaders)):
        #    dist_left, car_name = self.priorities[i][0]

        #    if dist_left < VTL_LEADER_DIST:
        #        self.next_car = car_name

        #        self.step = 1
        #        return

        #self.step = 1
        return

    def stepEighteen(self):
        if self.role != VTL_INTERSECTION_LEADER:
            return

        if len(self.leaders) == 1:
            if True: # for now, let's just assume the controller said yes
            #if CONTROL_CENTRE in self.acks:
                self.nf = VTL_NF_DEFAULT
                self.stepTwentyOne(CONTROL_CENTRE)
            return

        for leader in self.leaders:
            if not leader in self.acks:
                return

        self.nf = VTL_NF_DEFAULT
        self.stepTwentyOne(leader)

    def stepTwelve(self):
        if self.time < self.timeout:
            self.stepEighteen()
            return

        #print(self.name, "ran out of time at time", self.time)

        print(self.name, "timed out")

        # timer timed out
        if self.role == VTL_FOLLOWER:
            self.stepSixteen()
        else:
            self.stepFourteen()

    def sendMessages(self):

        #self.knowledge.clear()

        # STEP 1: Update own position
        self.knowledge[self.name] = (self.car.centre, self.entrance)
        content = (self.intersection, self.car.centre, self.entrance)
        self.messages.append((SEND_TO_ALL, VTL_STATUS, content))
        # go to step 2

        #print(self.name, self.messages)

        return self.messages

    def receiveMessages(self, messages):
        self.messages.clear()

        #if self.intersection == None:
        #    return

        for message in messages:
            source, destination, message_type, content = message

            if source == self.name:
                continue

            if message_type == VTL_STATUS:
                intersection, position, entrance = content

                #if intersection != self.intersection:

                if intersection != self.intersection:
                    if source in self.knowledge:
                        del self.knowledge[source]
                    continue

                if self.step == 12 and self.role != VTL_FOLLOWER:
                    if not source in self.leaders:
                        self.stepThirteen(position, entrance)

                self.knowledge[source] = (position, entrance)

            elif not source in self.knowledge:
                continue

            elif message_type == VTL_REFUSAL:
                print(source, destination, "VTL_REFUSAL")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.stepFourteen()

            elif message_type == VTL_RETRY:
                print(source, destination, "VTL_RETRY")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.stepFifteen()

            elif message_type == VTL_GREEN_REQUEST:
                print(source, destination, "VTL_GREEN_REQUEST")
                if self.step == 12 and self.role != VTL_FOLLOWER:
                    self.stepSeventeen(source)

            elif message_type == VTL_ACKNOWLEDGE:
                print(source, destination, "VTL_ACKNOWLEDGE")
                if self.step == 12 and self.role == VTL_INTERSECTION_LEADER:
                    self.acks.add(source)

            elif message_type == VTL_GREEN:
                print(source, destination, "VTL_GREEN", content)
                if self.step == 12:
                    self.nf = content
                    self.stepTwentyOne(source)

        if self.step == 3:
            self.stepThree()

        if self.step == 12:
            self.stepTwelve()

    def getLight(self, entrance, exit):
        return self.light

    def draw(self):
        world  = self.world
        screen = world.screen
        #colour = self.colour

        point = world.getDrawable(self.car.centre)

        if self.role == VTL_INTERSECTION_LEADER:
            pygame.draw.circle(screen, BLACK, point, 5)

        elif self.role == VTL_LEADER:
            pygame.draw.circle(screen, BLACK, point, 5, 1)

        #a = world.getDrawable(self.car.centre)

        #for car_name in self.knowledge:
        #    position, entrance = self.knowledge[car_name]

        #    b = world.getDrawable(position)
        #    pygame.draw.line(screen, colour, a, b, 3)


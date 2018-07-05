from util import *

from road_network import EnterIntersection

random.seed()

from pregen.scenario_1x1 import NUM_ROWS, NUM_COLS, entry_roads, valid_routes

PATH_PREFIX = "pregen/datasets_1x1/mass_generation/dataset_1x1"

SECOND_DURATION = 1000
MINUTE_DURATION = SECOND_DURATION * 60
HOUR_DURATION   = MINUTE_DURATION * 60

TIME_DURATION = HOUR_DURATION
NUM_MINUTES   = TIME_DURATION // MINUTE_DURATION

NUM_TRIALS = 5

# probability of car turning
LEFT_PROB   = 1
RIGHT_PROB  = 1
CENTRE_PROB = 3

TURN_CODE = "{}{}{}".format(LEFT_PROB, RIGHT_PROB, CENTRE_PROB)

DIVISOR = LEFT_PROB + RIGHT_PROB + CENTRE_PROB

MAX_TURNS = NUM_ROWS + NUM_COLS + 1 # maximum number of turns given world size

MAX_SCORE = DIVISOR**MAX_TURNS

def generateScore(route):
    score = MAX_SCORE

    for instruction in route:
        if isinstance(instruction, EnterIntersection):
            turn = instruction.turn

            score //= DIVISOR
            if turn == LEFT:
                score *= LEFT_PROB
            elif turn == RIGHT:
                score *= RIGHT_PROB
            else:
                score *= CENTRE_PROB

    return score

# find scores and make cumulative arrays
route_scores = []
for routes_from_entry in valid_routes:
    cumulative_scores = []

    total = 0
    for route in routes_from_entry:
        total += generateScore(route)
        cumulative_scores.append(total)

    route_scores.append(cumulative_scores)

# select route for schedule
def findRoute(scores, choice):
    bot = 0
    top = len(scores)-1

    while bot != top:
        n = (top + bot) // 2
        score = scores[n]

        if n == 0:
            break

        if score > choice:

            if scores[n-1] < choice:
                break

            top = n

        elif score < choice:

            if scores[n+1] >= choice:
                n += 1
                break
            bot = n

        else:
            break
    return n

def chooseRoute(entry):
    cumulative_scores = route_scores[entry]

    max_score = cumulative_scores[-1]
    choice = random.randint(1, max_score)

    return findRoute(cumulative_scores, choice)

ENTRY_OPTIONS = len(entry_roads)

def makeSchedule(num_cars):
    schedule = []
    for car_num in range(num_cars):
        time  = random.randint(0, TIME_DURATION-1)
        entry = random.randint(0, ENTRY_OPTIONS-1)
        route = chooseRoute(entry)
        schedule.append((time, entry, route))

    schedule.sort()
    return schedule

def generateDataset(cars_per_minute):
    num_cars = cars_per_minute * NUM_MINUTES

    schedule = makeSchedule(num_cars)

    filename_start = "{}_{:03}_{}".format(PATH_PREFIX, car_density, TURN_CODE)

    for i in range(100):
        filename = "{}_{:02}.py".format(filename_start, i)

        try:
            f = open(filename)
            f.close()

        except FileNotFoundError:

            f = open(filename, 'w')

            f.write("from util import *\n")
            f.write("schedule = deque([\n")
            for item in schedule:
                f.write("  {},\n".format(item))
            f.write("])\n")

            f.close()
            break

car_densities = [(i+1)*10 for i in range(15)]

if __name__ == "__main__":
    for i in range(NUM_TRIALS):
        for car_density in car_densities:
            generateDataset(car_density)


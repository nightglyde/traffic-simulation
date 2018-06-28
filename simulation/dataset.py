from util import *

from road_network import EnterIntersection

random.seed()

from pregen.scenario_2x2 import NUM_ROWS, NUM_COLS, entry_roads, valid_routes

SECOND_DURATION = 1000
MINUTE_DURATION = SECOND_DURATION * 60
HOUR_DURATION   = MINUTE_DURATION * 60

# scenario density and duration
TIME_DURATION   = HOUR_DURATION
CARS_PER_MINUTE = 600

NUM_CARS = int(TIME_DURATION / MINUTE_DURATION * CARS_PER_MINUTE)

# probability of car turning
LEFT_PROB   = 1
RIGHT_PROB  = 1
CENTRE_PROB = 1

DIVISOR = LEFT_PROB + RIGHT_PROB + CENTRE_PROB

LEFT_CENTRE_PROB  = DIVISOR - LEFT_PROB
RIGHT_CENTRE_PROB = DIVISOR - RIGHT_PROB

MAX_TURNS = NUM_ROWS + NUM_COLS + 1 # maximum number of turns given world size

MAX_SCORE = DIVISOR**MAX_TURNS

def generateScore(route):

    score = MAX_SCORE

    prev_turn = None

    for instruction in route:

        if isinstance(instruction, EnterIntersection):

            turn = instruction.turn

            score //= DIVISOR

            if turn == LEFT:
                score *= LEFT_PROB
            elif turn == RIGHT:
                score *= RIGHT_PROB
            elif prev_turn == LEFT:
                score *= LEFT_CENTRE_PROB
            elif prev_turn == RIGHT:
                score *= RIGHT_CENTRE_PROB
            else:
                score *= CENTRE_PROB

            prev_turn = instruction.turn

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

entry_options = len(entry_roads)

schedule = []
for car_num in range(NUM_CARS):
    time  = random.randint(0, TIME_DURATION-1)
    entry = random.randint(0, entry_options-1)
    route = chooseRoute(entry)
    schedule.append((time, entry, route))

schedule.sort()

if __name__ == "__main__":
    print("from util import *")
    print("schedule = deque([")
    for item in schedule:
        print("  {},".format(item))
    print("])")


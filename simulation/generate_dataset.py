from util import *

random.seed()

from two_grid import entry_roads, valid_routes

entry_options = len(entry_roads)
num_routes    = [len(valid_routes[i]) for i in range(entry_options)]

SECOND_DURATION = 1000
MINUTE_DURATION = SECOND_DURATION * 60
HOUR_DURATION   = MINUTE_DURATION * 60

TIME_DURATION   = HOUR_DURATION
CARS_PER_MINUTE = 120

NUM_CARS = int(TIME_DURATION / MINUTE_DURATION * CARS_PER_MINUTE)

schedule = []
for car_num in range(NUM_CARS):
    time = random.randint(0, TIME_DURATION-1)

    entry = random.randint(0, entry_options-1)

    route_options = num_routes[entry]
    route = random.randint(0, route_options-1)

    schedule.append((time, entry, route))

schedule.sort()

if __name__ == "__main__":
    print("from util import *")
    print("schedule = deque([")
    for item in schedule:
        print("  {},".format(item))
    print("])")


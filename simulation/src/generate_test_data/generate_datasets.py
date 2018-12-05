import sys, os

ABS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ABS_PATH)

import pkgutil
import re

from src.util import *
from src.simulation.road_network import EnterIntersection

random.seed()

import datasets.scenarios as scenarios

SECOND_DURATION = 1000
MINUTE_DURATION = SECOND_DURATION * 60
HOUR_DURATION   = MINUTE_DURATION * 60

########################################################

class DatasetGenerator:
    def __init__(self, module_name, scenario_code):

        path_dir = ABS_PATH + "/datasets/datasets_{}".format(scenario_code)
        self.path_prefix = path_dir + "/dataset_{}".format(scenario_code)

        if not os.path.exists(path_dir):
            os.mkdir(path_dir)

        module = __import__(module_name, fromlist="dummy")

        self.entry_options = len(module.entry_roads)

        # dataset duration
        self.duration    = HOUR_DURATION
        self.num_minutes = self.duration // MINUTE_DURATION

        # probability of car turning
        self.left_prob   = 1
        self.right_prob  = 1
        self.centre_prob = 1

        self.turn_code = "{}{}{}".format(
            self.left_prob, self.right_prob, self.centre_prob)

        self.divisor = self.left_prob + self.right_prob + self.centre_prob
        max_turns = module.NUM_ROWS + module.NUM_COLS + 1 # maximum number of turns given world size
        self.max_score = self.divisor**max_turns

        # find scores and make cumulative arrays
        self.route_scores = []
        for routes_from_entry in module.valid_routes:
            cumulative_scores = []

            total = 0
            for route in routes_from_entry:
                total += self.generateScore(route)
                cumulative_scores.append(total)

            self.route_scores.append(cumulative_scores)

    def generateScore(self, route):
        score = self.max_score

        for instruction in route:
            if isinstance(instruction, EnterIntersection):
                turn = instruction.turn

                score //= self.divisor
                if turn == LEFT:
                    score *= self.left_prob
                elif turn == RIGHT:
                    score *= self.right_prob
                else:
                    score *= self.centre_prob

        return score

    def chooseRoute(self, entry):
        scores = self.route_scores[entry]

        max_score = scores[-1]
        choice = random.randint(1, max_score)

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

    def generateDataset(self, cars_per_minute):
        num_cars = cars_per_minute * self.num_minutes

        schedule = []
        for car_num in range(num_cars):
            time  = random.randint(0, self.duration-1)
            entry = random.randint(0, self.entry_options-1)
            route = self.chooseRoute(entry)
            schedule.append((time, entry, route))
        schedule.sort()

        filename_start = "{}_{:03}_{}".format(
            self.path_prefix, cars_per_minute, self.turn_code)

        for i in range(100):
            filename = "{}_{:02}.py".format(filename_start, i)

            try:
                f = open(filename)
                f.close()

            except FileNotFoundError:

                f = open(filename, 'w')

                f.write("from src.util import *\n")
                f.write("schedule = deque([\n")
                for item in schedule:
                    f.write("  {},\n".format(item))
                f.write("])\n")

                f.close()

                break

def run(module_name, scenario_code, num_trials, min_density, max_density):
    datasetGenerator = DatasetGenerator(module_name, scenario_code)

    car_densities = [i for i in range(min_density, max_density+1, 10)]

    for i in range(num_trials):
        for car_density in car_densities:
            datasetGenerator.generateDataset(car_density)

if __name__ == "__main__":

    module_names = []

    package = scenarios
    prefix = package.__name__ + "."
    for importer, module_name, ispkg in pkgutil.iter_modules(package.__path__,
                                                             prefix):

        m = re.match(".*([0-9]+x[0-9]+_[0-9]+).*", module_name)
        if m:
            print("Module found: {}, Scenario code: {}".format(
                module_name, m.group(1)))
        else:
            print("Module found: {}, Unrecognised filename format".format(
                module_name))
        module_names.append(module_name)

    while True:
        scenario_code = input("\nEnter scenario code: ")

        for module_name in module_names:
            if re.match(".*({}).*".format(scenario_code), module_name):
                break
        else:
            print("This scenario code is not recognised.")
            continue

        break

    while True:
        try:
            num_trials = int(input("\nNumber of trials: "))
            if num_trials >= 0:
                break
        except ValueError:
            pass
        print("Number of trials must be an integer greater than 0.")

    while True:
        try:
            min_density = int(input("\nMinimum traffic density (cars per minute): "))
            if min_density >= 10 and min_density % 10 == 0:
                break
        except ValueError:
            pass
        print("Traffic density must be a positive multiple of 10.")

    while True:
        try:
            max_density = int(input("\nMaximum traffic density (cars per minute): "))
            if max_density >= 10 and max_density % 10 == 0:
                break
        except ValueError:
            pass
        print("Traffic density must be a positive multiple of 10.")

    run(module_name, scenario_code, num_trials, min_density, max_density)


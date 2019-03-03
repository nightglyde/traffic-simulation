import sys, os
import statistics

ABS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ABS_PATH)

RAW_RESULTS_PATH      = os.path.join(ABS_PATH, "results", "raw_results")
COMPILED_RESULTS_PATH = os.path.join(ABS_PATH, "results", "compiled_results")

import pkgutil
import re

from src.util import *

import datasets.scenarios as scenarios

#strategy_codes = [
#    "TrafficLights",
#    #"VirtualTrafficLights",
#    "VirtualTrafficLights2",
#    "GreedyController",
#    "MyTrafficController",
#]

#short_names = [
#    "tl",
#    "vtl",
#    #"vtl2",
#    "gc",
#    "mtc",
#]

#density_codes = [
#    "010",
#    "020",
#    "030",
#    "040",
#    "050",
#    "060",
#    "070",
#    "080",
#    "090",
#    "100",
#    "110",
#    "120",
#    "130",
#    "140",
#    "150",
#]

#num_test_cases = 5#20

#dataset_prefix = "dataset_1x1_50"
#dataset_suffix = "111"

#NUM_STRATEGIES = len(strategy_codes)

def getDurations(filename, expected_count):

    f = open(filename)

    durations = []

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        durations.append(duration)

    f.close()

    if len(durations) == expected_count:
        return durations

    return []

def run(scenario_code, strategies_list, num_test_cases):

    dataset_prefix = "dataset_{}".format(scenario_code)
    dataset_suffix = "111"

    density_codes = []

    minimums = []
    maximums = []
    averages = []
    std_devs = []
    fails    = []

    for d in range(1, 100):
        density = "{:03}".format(d*10)

        expected_count = int(density) * 60

        found_a_file = False

        good_datasets = []
        bad_datasets  = []
        for i in range(num_test_cases):
            dataset = "{}_{}_{}_{:02}".format(
                dataset_prefix, density, dataset_suffix, i)

            for strategy in strategies_list:

                filename = os.path.join(RAW_RESULTS_PATH,
                                        "{}_{}.txt".format(strategy, dataset))
                try:
                    durations = getDurations(filename, expected_count)
                    found_a_file = True
                    if not durations:
                        bad_datasets.append(dataset)
                        break

                except FileNotFoundError:
                    bad_datasets.append(dataset)
                    break

            else:
                good_datasets.append(dataset)

        if not found_a_file:
            break

        density_codes.append(density)

        minimums_line = [density]
        maximums_line = [density]
        averages_line = [density]
        std_devs_line = [density]
        fails_line    = [density]
        for strategy in strategies_list:

            all_durations = []
            num_fails = 0

            for dataset in good_datasets:
                filename = os.path.join(RAW_RESULTS_PATH,
                                        "{}_{}.txt".format(strategy, dataset))

                all_durations += getDurations(filename, expected_count)

            for dataset in bad_datasets:
                filename = os.path.join(RAW_RESULTS_PATH,
                                        "{}_{}.txt".format(strategy, dataset))

                try:
                    durations = getDurations(filename, expected_count)
                    if not durations:
                        num_fails += 1

                except FileNotFoundError:
                    pass

            fails_line.append(str(num_fails))

            if all_durations:
                minimums_line.append(str(min(all_durations)/1000))
                maximums_line.append(str(max(all_durations)/1000))
                averages_line.append(str(statistics.mean(all_durations)/1000))
                std_devs_line.append(str(statistics.stdev(all_durations)/1000))
            else:
                minimums_line.append(str("NaN"))
                maximums_line.append(str("NaN"))
                averages_line.append(str("NaN"))
                std_devs_line.append(str("NaN"))

        fails.append(fails_line)

        minimums.append(minimums_line)
        maximums.append(maximums_line)
        averages.append(averages_line)
        std_devs.append(std_devs_line)

    first_line = "density " + " ".join(strategies_list) + "\n"

    # MINIMUM
    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "duration_min_{}_{}.txt".format(dataset_prefix, dataset_suffix))

    f = open(filename, 'w')
    try:
        f.write(first_line)
        for line in minimums:
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

    # MAXIMUM
    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "duration_max_{}_{}.txt".format(dataset_prefix, dataset_suffix))
    f = open(filename, 'w')
    try:
        f.write(first_line)
        for line in maximums:
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

    # MEAN
    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "duration_mean_{}_{}.txt".format(dataset_prefix, dataset_suffix))
    f = open(filename, 'w')
    try:
        f.write(first_line)
        for line in averages:
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

    # STANDARD DEVIATION
    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "duration_stdev_{}_{}.txt".format(dataset_prefix, dataset_suffix))
    f = open(filename, 'w')
    try:
        f.write(first_line)
        for line in std_devs:
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

    # NUMBER OF FAILED TEST CASES
    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "fails_{}_{}.txt".format(dataset_prefix, dataset_suffix))
    f = open(filename, 'w')
    try:
        f.write(first_line)
        for line in fails:
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

    first_line_for_strategy = "density mean min max stdev\n"

    # DISTRIBUTION OF SINGLE STRATEGY
    def writeFileForStrategy(strategy_num, strategy_name):
        filename = os.path.join(
            COMPILED_RESULTS_PATH, "duration_{}_{}_{}.txt".format(
                strategy_name, dataset_prefix, dataset_suffix))

        f = open(filename, 'w')
        try:
            f.write(first_line_for_strategy)

            for i, density in enumerate(density_codes):
                line = [
                    density,
                    averages[i][strategy_num+1],
                    minimums[i][strategy_num+1],
                    maximums[i][strategy_num+1],
                    std_devs[i][strategy_num+1],
                ]
                f.write(" ".join(line) + "\n")

        except BaseException as exception:
            removeFile(f, filename)
            raise exception

        f.close()

    #for i, short_name in enumerate(short_names):
    #    writeFileForStrategy(i, short_name)

    for i, strategy_name in enumerate(strategies_list):
        writeFileForStrategy(i, strategy_name)

    # COMBINED

    first_line_for_combined = "density"
    for strategy in strategies_list:
        first_line_for_combined += " {}_mean {}_min {}_max {}_stdev".format(
            strategy, strategy, strategy, strategy)
    first_line_for_combined += "\n"

    filename = os.path.join(
        COMPILED_RESULTS_PATH,
        "duration_combined_{}_{}.txt".format(dataset_prefix, dataset_suffix))
    f = open(filename, 'w')
    try:
        f.write(first_line_for_combined)
        for i, density in enumerate(density_codes):
            line = [density]

            for j in range(len(strategies_list)):
                line += [
                    averages[i][j+1],
                    minimums[i][j+1],
                    maximums[i][j+1],
                    std_devs[i][j+1],
                ]

            f.write(" ".join(line) + "\n")

    except BaseException as exception:
        removeFile(f, filename)
        raise exception

    f.close()

def main():
    module_names = []

    package = scenarios
    prefix = package.__name__ + "."
    for importer, module_name, ispkg in pkgutil.iter_modules(package.__path__,
                                                             prefix):

        m = re.match(".*([0-9]+x[0-9]+_[0-9]+).*", module_name)
        if m:
            scenario_code = m.group(1)
            print("Module found: {}, Scenario code: {}".format(
                module_name, scenario_code))
            module_names.append((module_name, scenario_code))
        else:
            print("Module found: {}, Unrecognised filename format".format(
                module_name))

    while True:
        scenario_code = input("\nEnter scenario code: ")

        for module_name, scenario in module_names:
            if scenario_code == scenario:
                break
        else:
            print("This scenario code is not recognised.")
            continue

        break

    strategies_list = []

    for i, strategy_name in ALL_STRATEGIES:

        while True:
            response = input("\nUse {} strategy? ".format(strategy_name))
            response.lower()

            if response in {"y", "yes", "t", "true"}:
                strategies_list.append(strategy_name)
                break

            if response in {"n", "no", "f", "false"}:
                break

            print("Valid responses: y, yes, t, true, n, no, f, false")

    while True:
        try:
            num_test_cases = int(input("\nNumber of test cases to consider: "))
            if num_test_cases >= 0:
                break
        except ValueError:
            pass
        print("Number of test cases must be an integer greater than 0.")

    run(scenario_code, strategies_list, num_test_cases)

if __name__ == "__main__":
    main()


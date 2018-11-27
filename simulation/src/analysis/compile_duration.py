import os
import statistics

ABS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_RESULTS_PATH      = ABS_PATH + "/results/raw_results"
COMPILED_RESULTS_PATH = ABS_PATH + "/results/compiled_results"

strategy_codes = [
    "TrafficLights",
    #"VirtualTrafficLights",
    "VirtualTrafficLights2",
    "GreedyController",
    "MyTrafficController",
]

short_names = [
    "tl",
    "vtl",
    #"vtl2",
    "gc",
    "mtc",
]

density_codes = [
    "010",
    "020",
    "030",
    "040",
    "050",
    "060",
    "070",
    "080",
    "090",
    "100",
    "110",
    "120",
    "130",
    "140",
    "150",
]

num_test_cases = 5#20

dataset_prefix = "dataset_1x1"
dataset_suffix = "111"

NUM_STRATEGIES = len(strategy_codes)

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

def main():

    minimums = []
    maximums = []
    averages = []
    std_devs = []
    fails    = []
    for density in density_codes:

        expected_count = int(density) * 60

        good_datasets = []
        bad_datasets  = []
        for i in range(num_test_cases):
            dataset = "{}_{}_{}_{:02}".format(
                dataset_prefix, density, dataset_suffix, i)

            for strategy in strategy_codes:

                filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset)

                try:
                    if not getDurations(filename, expected_count):
                        bad_datasets.append(dataset)
                        break

                except FileNotFoundError:
                    bad_datasets.append(dataset)
                    break

            else:
                good_datasets.append(dataset)


        minimums_line = [density]
        maximums_line = [density]
        averages_line = [density]
        std_devs_line = [density]
        fails_line    = [density]
        for strategy in strategy_codes:

            all_durations = []
            num_fails = 0

            for dataset in good_datasets:
                filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset)

                all_durations += getDurations(filename, expected_count)

            for dataset in bad_datasets:
                filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset)

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

    # MINIMUM
    filename = "{}/duration_min_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for line in minimums:
        f.write(" ".join(line) + "\n")
    f.close()

    # MAXIMUM
    filename = "{}/duration_max_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for line in maximums:
        f.write(" ".join(line) + "\n")
    f.close()

    # MEAN
    filename = "{}/duration_mean_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for line in averages:
        f.write(" ".join(line) + "\n")
    f.close()

    # STANDARD DEVIATION
    filename = "{}/duration_stdev_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for line in std_devs:
        f.write(" ".join(line) + "\n")
    f.close()

    # NUMBER OF FAILED TEST CASES
    filename = "{}/fails_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for line in fails:
        f.write(" ".join(line) + "\n")
    f.close()

    # DISTRIBUTION OF SINGLE STRATEGY
    def writeFileForStrategy(strategy_num, strategy_name):
        filename = "{}/duration_{}_{}_{}.txt".format(
            COMPILED_RESULTS_PATH, strategy_name, dataset_prefix, dataset_suffix)

        f = open(filename, 'w')

        for i, density in enumerate(density_codes):
            line = [
                density,
                averages[i][strategy_num+1],
                minimums[i][strategy_num+1],
                maximums[i][strategy_num+1],
                std_devs[i][strategy_num+1],
            ]
            f.write(" ".join(line) + "\n")
        f.close()

    for i, short_name in enumerate(short_names):
        writeFileForStrategy(i, short_name)

    # COMBINED

    filename = "{}/duration_combined_{}_{}.txt".format(
        COMPILED_RESULTS_PATH, dataset_prefix, dataset_suffix)
    f = open(filename, 'w')
    for i, density in enumerate(density_codes):
        line = [density]

        for j in range(len(strategy_codes)):
            line += [
                averages[i][j+1],
                minimums[i][j+1],
                maximums[i][j+1],
                std_devs[i][j+1],
            ]

        f.write(" ".join(line) + "\n")

    f.close()

if __name__ == "__main__":
    main()


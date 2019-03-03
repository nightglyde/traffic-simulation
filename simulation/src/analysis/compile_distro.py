import os
import statistics

ABS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_RESULTS_PATH      = ABS_PATH + "/results/raw_results"
COMPILED_RESULTS_PATH = ABS_PATH + "/results/compiled_results"

strategy_codes = [
    "TrafficLights",
    "VirtualTrafficLights2",
    "GreedyController",
    "MyTrafficController",
]

NUM_STRATEGIES = len(strategy_codes)

num_test_cases = 5#10

density = "100"
dataset_prefix = "dataset_1x1_50_{}_111".format(density)

expected_count = int(density) * 60

def getDurations(filename):

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
    good_datasets = []
    for i in range(num_test_cases):

        dataset = "{}_{:02}".format(dataset_prefix, i)

        for strategy in strategy_codes:

            filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset)

            try:
                if not getDurations(filename):
                    break

            except FileNotFoundError:
                break

        else:
            good_datasets.append(dataset)

    durations = [[] for s in range(NUM_STRATEGIES)]
    for dataset in good_datasets:

        for s, strategy in enumerate(strategy_codes):

            filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset)

            durations[s] += getDurations(filename)

    filename = "{}/distribution_{}.txt".format(COMPILED_RESULTS_PATH, dataset_prefix)
    f = open(filename, 'w')
    try:
        for i in range(len(durations[0])):
            line = []
            for s in range(NUM_STRATEGIES):
                line.append(str(durations[s][i]/1000))
            f.write(" ".join(line) + "\n")
    except BaseException as exception:
        removeFile(f, filename)
        raise exception
    f.close()

if __name__ == "__main__":
    main()


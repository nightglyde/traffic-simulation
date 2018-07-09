
import statistics

strategy_codes = [
    "TrafficLights",
    "VirtualTrafficLights",
    "MyTrafficController",
    "GreedyController",
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

num_test_cases = 10

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

#cumulative_fails = []
#for strategy in strategy_codes:
#    cumulative_fails.append(0)

#stop_calculating = False

minimums = []
maximums = []
averages = []
std_devs = []
fails    = []
for density in density_codes:

    expected_count = int(density) * 60

    minimums_line = [density]
    maximums_line = [density]
    averages_line = [density]
    std_devs_line = [density]
    fails_line    = [density]
    for s, strategy in enumerate(strategy_codes):

        durations = []
        num_success = 0
        num_fails = 0
        #num_fails = cumulative_fails[s]

        for i in range(num_test_cases):

            filename = "results/{}_{}_{}_{}_{:02}.txt".format(
                strategy, dataset_prefix, density, dataset_suffix, i)

            try:
                new_durations = getDurations(filename, expected_count)

                if new_durations:

                    #if stop_calculating:
                    #    continue

                    durations += new_durations

                    num_success += 1
                else:
                    num_fails += 1

            except FileNotFoundError:
                continue

            if num_success >= 1:
                break

        fails_line.append(str(num_fails))

        #if stop_calculating:
        #    continue

        if durations:
            minimums_line.append(str(min(durations)/1000))
            maximums_line.append(str(max(durations)/1000))
            averages_line.append(str(statistics.mean(durations)/1000))
            std_devs_line.append(str(statistics.stdev(durations)/1000))
        else:
            minimums_line.append(str("NaN"))
            maximums_line.append(str("NaN"))
            averages_line.append(str("NaN"))
            std_devs_line.append(str("NaN"))

            #stop_calculating = True

        #cumulative_fails[s] = num_fails

    fails.append(fails_line)

    #if stop_calculating:
    #    continue

    minimums.append(minimums_line)
    maximums.append(maximums_line)
    averages.append(averages_line)
    std_devs.append(std_devs_line)

# MINIMUM
filename = "results/compiled_results/duration_min_{}_{}.txt".format(
    dataset_prefix, dataset_suffix)
f = open(filename, 'w')
for line in minimums:
    f.write(" ".join(line) + "\n")
f.close()

# MAXIMUM
filename = "results/compiled_results/duration_max_{}_{}.txt".format(
    dataset_prefix, dataset_suffix)
f = open(filename, 'w')
for line in maximums:
    f.write(" ".join(line) + "\n")
f.close()

# MEAN
filename = "results/compiled_results/duration_mean_{}_{}.txt".format(
    dataset_prefix, dataset_suffix)
f = open(filename, 'w')
for line in averages:
    f.write(" ".join(line) + "\n")
f.close()

# STANDARD DEVIATION
filename = "results/compiled_results/duration_stdev_{}_{}.txt".format(
    dataset_prefix, dataset_suffix)
f = open(filename, 'w')
for line in std_devs:
    f.write(" ".join(line) + "\n")
f.close()

# NUMBER OF FAILED TEST CASES
filename = "results/compiled_results/fails_{}_{}.txt".format(
    dataset_prefix, dataset_suffix)
f = open(filename, 'w')
for line in fails:
    f.write(" ".join(line) + "\n")
f.close()


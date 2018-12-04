import os
import statistics

RESULTS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) \
                    + "/results/raw_results"

strategy_codes = [
    "TrafficLights",
#    "VirtualTrafficLights",
    "VirtualTrafficLights2",
    "GreedyController",
    "MyTrafficController",
]

short_codes = [
    "TL",
#    "VTL",
    "VTL2",
    "GC",
    "MTC",
]

scenario_codes = [
    "1x1_50",
    #"2x2_50",
]

density_codes = [
    "010", "020", "030",
    "040", "050", "060",
    "070", "080", "090",
    "100", "110", "120",
    "130", "140", "150",
]

turn_distro_codes = [
    "111",
    #"112",
    #"113",
    #"114",
    #"115",
    #"116",
]

num_test_cases    = 20
chosen_test_cases = 5

def getDurations(filename, expected_count):

    f = open(filename)

    durations = []

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        durations.append(duration)

    f.close()

    if len(durations) < 1:
        return None

    mean_duration = statistics.mean(durations)
    max_duration  = max(durations)

    if len(durations) == expected_count:
        return mean_duration, max_duration
    else:
        return None

NARROW_COLUMN = 5
WIDE_COLUMN   = 18 + 11 + 8 - 6

SPECIAL_WIDTH = 13

NORMAL_DIV  = "|"
DIVIDER_DIV = "+"
EMPTY_DIV   = " "

COLUMNS_IN_BATCH = len(strategy_codes)
BATCH_WIDTH = WIDE_COLUMN*COLUMNS_IN_BATCH + len(NORMAL_DIV)*(COLUMNS_IN_BATCH-1)

empty_narr = " "*NARROW_COLUMN

full_narr  = "-"*NARROW_COLUMN
full_wide  = "-"*WIDE_COLUMN
full_batch = "-"*BATCH_WIDTH

def centreText(text, width):

    oddness = width % 2

    text = str(text)

    if len(text) % 2 != oddness:
        text = " " + text

    while len(text) < width:
        text = " " + text + " "

    return text

def main():
    strategy_batch = []
    for strategy in short_codes:
        strategy_batch.append(centreText(strategy, WIDE_COLUMN))
    strategy_batch = NORMAL_DIV.join(strategy_batch)

    hori_div_0    = [empty_narr]
    hori_div_1    = [empty_narr]
    hori_div_2    = [full_narr]
    strategy_line = [centreText("", NARROW_COLUMN)]
    for scenario in scenario_codes:
        hori_div_0.append(full_batch)

        for strategy in strategy_codes:
            hori_div_1.append(full_wide)
            hori_div_2.append(full_wide)

        strategy_line.append(strategy_batch)
    strategy_line = EMPTY_DIV + NORMAL_DIV.join(strategy_line) + NORMAL_DIV

    hori_div_0 = EMPTY_DIV   + DIVIDER_DIV.join(hori_div_0) + DIVIDER_DIV
    hori_div_1 = EMPTY_DIV   + DIVIDER_DIV.join(hori_div_1) + DIVIDER_DIV
    hori_div_2 = DIVIDER_DIV + DIVIDER_DIV.join(hori_div_2) + DIVIDER_DIV

    for turn_distro in turn_distro_codes:

        scenario_line = [empty_narr]
        for scenario in scenario_codes:
            scenario_line.append(centreText("{},{}".format(scenario, turn_distro),
                                 BATCH_WIDTH))
        scenario_line = EMPTY_DIV + NORMAL_DIV.join(scenario_line) + NORMAL_DIV

        print(hori_div_0)
        print(scenario_line)
        print(hori_div_1)
        print(strategy_line)
        print(hori_div_2)

        bad_datasets = []

        for density in density_codes:

            expected_count = int(density) * 60

            items = [centreText(density, NARROW_COLUMN)]

            for scenario in scenario_codes:

                good_datasets = []
                for i in range(num_test_cases):

                    dataset = "dataset_{}_{}_{}_{:02}.txt".format(
                        scenario, density, turn_distro, i)

                    if int(density) > 110:
                        if i >= chosen_test_cases:
                            break
                        bad_datasets.append((dataset, expected_count, density))
                        continue

                    for strategy in strategy_codes:

                        filename = "{}/{}_{}".format(RESULTS_PATH,strategy, dataset)

                        try:
                            if not getDurations(filename, expected_count):
                                if int(density) <= 110 or i < chosen_test_cases:
                                    bad_datasets.append((dataset, expected_count, density))
                                break
                        except FileNotFoundError:
                            #bad_datasets.append((dataset, expected_count, density))
                            #break
                            pass

                    else:
                        good_datasets.append(dataset)

                    #if len(good_datasets) >= chosen_test_cases:
                    #    break


                for strategy in strategy_codes:

                    mean_durations = []
                    max_durations  = []

                    num_results = 0

                    for dataset in good_datasets:

                        filename = "{}/{}_{}".format(RESULTS_PATH, strategy, dataset)

                        try:
                            mean_duration, max_duration = getDurations(filename, expected_count)

                            mean_durations.append(mean_duration)
                            max_durations.append(max_duration)

                            num_results += 1

                        except FileNotFoundError:
                            pass

                    if mean_durations:
                    #if num_results > 1:
                        average_mean_duration = statistics.mean(mean_durations) / 1000
                        average_max_duration  = max(max_durations)  / 1000

                        text = "mean:{:7.2f} max:{:7.2f} ({:02})".format(
                            average_mean_duration, average_max_duration,
                            num_results)
                        items.append(centreText(text, WIDE_COLUMN))

                    else:
                        items.append(centreText("-", WIDE_COLUMN))

            print(NORMAL_DIV + NORMAL_DIV.join(items) + NORMAL_DIV)

        print(hori_div_2)

        for dataset, expected_count, density in bad_datasets:

            line = [centreText(int(density), 3), centreText(int(dataset[-6:-4]), 2)]

            for strategy in strategy_codes:

                filename = "{}/{}_{}".format(RESULTS_PATH, strategy, dataset)

                try:

                    result = getDurations(filename, expected_count)

                    if result:
                        mean_duration, max_duration = result
                        text = "{:.2f}".format(mean_duration/1000)

                    else:
                        text = "Traffic Jam"

                except:
                    text = "-"

                line.append(centreText(text, SPECIAL_WIDTH))

            print(" & ".join(line) + " \\\\")

        print(hori_div_2)
        print()

if __name__ == "__main__":
    main()


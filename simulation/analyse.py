
import statistics

strategy_codes    = ["TrafficLights",
                     "VirtualTrafficLights",
                     "MyTrafficController",
                     "GreedyController"]
short_codes       = ["TL", "VTL", "MTC", "GC"]
scenario_codes    = ["1x1"]#, "2x2"]
density_codes     = ["010", "020", "030", "040", "050",
                     "060", "070", "080", "090", "100",
                     "110", "120", "130", "140", "150"]
turn_distro_codes = [
    "111",# "112", "113",
    #"114", "115", "116"
]

num_test_cases = 10

def getDurations(filename, expected_count):

    f = open(filename)

    #count = 0
    #total = 0

    durations = []

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        #count += 1
        #total += duration

        durations.append(duration)

    f.close()

    if len(durations) < 1:
        return None, None, False

    mean_duration = statistics.mean(durations)
    max_duration  = max(durations)

    if len(durations) == expected_count:
        return mean_duration, max_duration, True
    else:
        return mean_duration, max_duration, False

    #if count == expected_count:
    #    return total / count

    #return None

NARROW_COLUMN = 5
WIDE_COLUMN   = 18 + 11 + 8

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

    for density in density_codes:

        expected_count = int(density) * 60

        items = [centreText(density, NARROW_COLUMN)]

        for scenario in scenario_codes:

            for strategy in strategy_codes:

                #all_durations = []
                #total       = 0.0
                mean_durations = []
                max_durations  = []

                num_fails   = 0
                num_missing = 0

                for i in range(num_test_cases):

                    filename = "results/{}_dataset_{}_{}_{}_{:02}.txt".format(
                        strategy, scenario, density, turn_distro, i)

                    try:
                        #average_duration = getAverageDuration(filename,
                        #                                      expected_count)

                        #if average_duration is None:
                        #    num_fails += 1
                        #else:
                        #    total += average_duration

                        mean_duration, max_duration, passed = getDurations(filename, expected_count)

                        if mean_duration:
                            mean_durations.append(mean_duration)

                        if max_duration:
                            max_durations.append(max_duration)

                        if not passed:
                            num_fails += 1
                            continue

                    except FileNotFoundError:
                        num_missing += 1

                num_results = num_test_cases - num_missing
                num_success = num_results - num_fails

                if num_success > 0:
                    average_mean_duration = statistics.mean(mean_durations) / 1000
                    average_max_duration  = max(max_durations)  / 1000

                    text = "mean:{:7.2f} max:{:7.2f} fail:{:2}/{:2}".format(
                        average_mean_duration, average_max_duration,
                        num_fails, num_results)
                    items.append(centreText(text, WIDE_COLUMN))

                elif num_results > 0:
                    text = "{:2}/{:2} fails".format(num_fails, num_results)
                    items.append(centreText(text, WIDE_COLUMN))

                else:
                    items.append(centreText("-", WIDE_COLUMN))

                #if num_success > 0:
                #    average_over_trials = total / num_success

                #    text = "{:10.2f} {:02}/{:02}".format(
                #        average_over_trials, num_success, num_results)
                #    items.append(centreText(text, WIDE_COLUMN))

                #elif num_results > 0:
                #    text = "{:02}/{:02} fails".format(num_fails, num_results)
                #    items.append(centreText(text, WIDE_COLUMN))

                #else:
                #    items.append(centreText("-", WIDE_COLUMN))

        print(NORMAL_DIV + NORMAL_DIV.join(items) + NORMAL_DIV)

    print(hori_div_2)
    print()


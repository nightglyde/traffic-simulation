
strategy_codes    = ["TrafficLights_dataset",
                     "VirtualTrafficLights_dataset",
                     "MyTrafficController_dataset",
                     "GreedyController_dataset"]
short_codes       = ["TL", "VTL", "MTC", "GC"]
#scenario_codes    = ["1x1", "2x2"]
scenario_codes    = ["old", "new", "new2"]
density_codes     = ["030", "060", "090", "120", "150"]
turn_distro_codes = ["111A", "112A", "113A", "114A", "115A", "116A"]

def getAverageDuration(filename, expected_count):

    f = open(filename)

    count = 0
    total = 0

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        count += 1
        total += duration

    f.close()

    if count == expected_count:
        return total / count

    return None

NARROW_COLUMN = 5
WIDE_COLUMN   = 12

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

                if scenario == "old":
                    filename = "results/zzz_before_fix/{}_1x1_{}_{}.txt".format(
                        strategy, density, turn_distro)
                elif scenario == "new":
                    filename = "results/{}_1x1_{}_{}.txt".format(
                        strategy, density, turn_distro)
                else:
                    filename = "results/zzz_new2/{}_1x1_{}_{}.txt".format(
                        strategy, density, turn_distro)

                try:
                    average_duration = getAverageDuration(filename, expected_count)

                    if average_duration is None:
                        items.append(centreText("-", WIDE_COLUMN))
                    else:
                        items.append(
                            centreText("{:10.2f}".format(average_duration),
                                       WIDE_COLUMN))
                except FileNotFoundError:
                    items.append(centreText("", WIDE_COLUMN))

        print(NORMAL_DIV + NORMAL_DIV.join(items) + NORMAL_DIV)

    print(hori_div_2)
    print()



NARROW_COLUMN = 3
WIDE_COLUMN   = 10
BATCH_WIDTH   = 32
BATCH_GAP     = 3

strategy_codes    = ["TrafficLights", "VirtualTrafficLights", "MyTrafficController"]
short_codes       = ["TL", "VTL", "MTC"]

scenario_codes    = ["1x1", "2x2"]
density_codes     = [30, 60, 90, 120, 150]
turn_distro_codes = ["111", "111A", "112", "112A", "113", "113A",
                     "114", "114A", "115", "115A", "116", "116A"]

def getAverageDuration(f):
    count = 0
    total = 0

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        count += 1
        total += duration

    if count > 1:
        return total / count

    return None

def centreText(text, width):

    oddness = width % 2

    text = str(text)

    if len(text) % 2 != oddness:
        text = " " + text

    while len(text) < width:
        text = " " + text + " "

    return text

strategy_line = ""
for strategy in short_codes:
    strategy_line += centreText(strategy, WIDE_COLUMN+1)

for turn_distro in turn_distro_codes:

    line1 = [centreText("", NARROW_COLUMN)]
    line2 = [centreText("", NARROW_COLUMN)]
    for scenario in scenario_codes:
        line1.append(centreText("{},{}".format(scenario, turn_distro),
                     BATCH_WIDTH))

        line2.append(strategy_line)

    print(" ".join(line1))
    print(" ".join(line2))

    for density in density_codes:

        items = [centreText(density, NARROW_COLUMN)]

        for scenario in scenario_codes:

            for strategy in strategy_codes:

                filename = "results/{}_dataset_{}_{}_{}.txt".format(
                    strategy, scenario, density, turn_distro)

                try:
                    f = open(filename)
                    average_duration = getAverageDuration(f)
                    f.close()

                    if average_duration is None:
                        items.append(centreText("", WIDE_COLUMN))
                    else:
                        items.append("{:10.2f}".format(average_duration))

                except FileNotFoundError:
                    items.append(centreText("", WIDE_COLUMN))

        print(" ".join(items))

    print()


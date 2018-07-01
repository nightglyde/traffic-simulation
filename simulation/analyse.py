
NARROW_COLUMN = 3
WIDE_COLUMN   = 10
BATCH_WIDTH   = 32
BATCH_GAP     = 3

strategy_codes    = ["tl", "vtl", "mtc"]
scenario_codes    = ["1x1", "2x2"]
density_codes     = [30, 60, 90, 120, 150]
turn_distro_codes = ["111", "112", "113", "114", "115", "116"]

def getAverageDuration(f):

    count = 0
    total = 0

    for line in f:
        car_num, end_time, start_time, duration = [int(x) for x in line.split()]

        count += 1
        total += duration

    return total / count

def centreText(text, width):

    oddness = width % 2

    text = str(text)

    if len(text) % 2 != oddness:
        text = " " + text

    while len(text) < width:
        text = " " + text + " "

    return text

strategy_line = ""
for strategy in strategy_codes:
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

                filename = "results/{}_{}_{}_{}.txt".format(
                    strategy, scenario, density, turn_distro)

                try:
                    f = open(filename)

                    average_duration = getAverageDuration(f)

                    items.append("{:10.2f}".format(average_duration))

                    f.close()
                except FileNotFoundError:
                    items.append(centreText("", WIDE_COLUMN))

        print(" ".join(items))

    print()


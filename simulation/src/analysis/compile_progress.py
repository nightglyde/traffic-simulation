import os

ABS_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_RESULTS_PATH      = ABS_PATH + "/results/raw_results"
COMPILED_RESULTS_PATH = ABS_PATH + "/results/compiled_results"

strategy_codes = [
    "TrafficLights",
    "VirtualTrafficLights2",
    "GreedyController",
    "MyTrafficController",
]

#dataset_name = "dataset_1x1_150_111_00"
#dataset_name = "dataset_1x1_120_111A"
#dataset_name = "dataset_1x1_090_115A"

dataset_name = "dataset_1x1_090_111_00"

NUM_STRATEGIES = len(strategy_codes)

SECOND_DURATION = 1000
MINUTE_DURATION = SECOND_DURATION * 60
HOUR_DURATION   = MINUTE_DURATION * 60

BUCKET_SIZE = SECOND_DURATION

BUCKET_MINUTES = BUCKET_SIZE / MINUTE_DURATION

NUM_BUCKETS = 60 * 70

TIME_LIMIT = BUCKET_SIZE*NUM_BUCKETS

def progressOverTime(filename):

    f = open(filename)

    successful_cars = 0

    curr_time = BUCKET_SIZE

    progress = [0]

    for line in f:
        start_time, end_time, duration = [int(x) for x in line.split()]

        while end_time > curr_time:
            progress.append(successful_cars)
            curr_time += BUCKET_SIZE

        successful_cars += 1

        if curr_time > TIME_LIMIT:
            f.close()
            return progress

    f.close()

    while curr_time <= TIME_LIMIT:
        progress.append(successful_cars)
        curr_time += BUCKET_SIZE

    return progress

def main():
    all_results = []
    for strategy in strategy_codes:

        filename = "{}/{}_{}.txt".format(RAW_RESULTS_PATH, strategy, dataset_name)

        results = progressOverTime(filename)

        all_results.append(results)

    filename = "{}/progress_{}.txt".format(COMPILED_RESULTS_PATH, dataset_name)

    f = open(filename, 'w')

    for t in range(NUM_BUCKETS+1):
        line = [str(t*BUCKET_MINUTES)]
        for s in range(NUM_STRATEGIES):
            line.append(str(all_results[s][t]))

        line = " ".join(line)

        f.write(line + '\n')

    f.close()

if __name__ == "__main__":
    main()


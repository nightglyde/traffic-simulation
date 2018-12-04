import sys, os

ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ABS_PATH)

RESULTS_PATH = ABS_PATH + "/results/raw_results"

import pkgutil
import time as time_module
import re

from src.util import *
from src.simulation.world import World

from datasets.scenarios.scenario_2x2_50 import roads, entry_roads, intersections,\
                                valid_routes, grass, world_width, world_height

import datasets.datasets_2x2_50 as datasets

# time formatting
TIME_FORMAT = "%H:%M:%S"

def worldGenerator():
    module_names = []

    #blacklist = {
    #    "datasets.datasets_1x1_50.dataset_1x1_50_120_111_00",
    #    "datasets.datasets_1x1_50.dataset_1x1_50_120_111_01",
    #    "datasets.datasets_1x1_50.dataset_1x1_50_120_111_02",
    #    "datasets.datasets_1x1_50.dataset_1x1_50_120_111_03",
    #    "datasets.datasets_1x1_50.dataset_1x1_50_120_111_04",
    #}

    #pattern = re.compile("dataset_1x1_50_150_116")
    #pattern = re.compile("_116_00")
    pattern = re.compile("_111_")

    package = datasets
    prefix  = package.__name__ + "."
    for importer, module_name, ispkg in pkgutil.iter_modules(package.__path__,
                                                             prefix):
        if not pattern.search(module_name):
            continue

        #if module_name in blacklist:
        #    continue

        density = int(module_name[-10:-7])
        #turn_number = int(module_name[-6:-3])
        case_number = int(module_name[-2:])

        #if case_number >= 5:
        #    continue

        #if density > 110:
        #    continue

        #if density == 110:
        #    case_number -= 4

        #if density != 100:
        #    continue

        print("Found module:", module_name)
        module_names.append(module_name)

        #module_names.append((case_number, module_name))

    module_names.sort()
    #module_names = [module_name for case_number, module_name in module_names]

    #for module_name in module_names:
    #    print(module_name)

    for module_name in module_names:

        module   = __import__(module_name, fromlist="dummy")
        schedule = module.schedule

        print("Imported", module)

        short_name = module_name.split(".")[-1]

        for strategy, strategy_name in ALL_STRATEGIES:

            # skip this strategy, because we're not using it
            if strategy == VIRTUAL_TRAFFIC_LIGHTS_MODE:
                continue

            filename_short = "{}_{}.txt".format(strategy_name, short_name)
            filename = "{}/{}".format(RESULTS_PATH, filename_short)

            try:
                f = open(filename)
                f.close()

            except FileNotFoundError:
                yield schedule, strategy, filename, filename_short

class WorldHandler:
    def __init__(self, screen):
        self.screen = screen

        self.world          = None
        self.world_time     = None
        self.filename       = None
        self.filename_short = None

        self.generator  = worldGenerator()

        self.start_time = None

    def generateNext(self, time):
        try:
            schedule, strategy, filename, filename_short = next(self.generator)
        except StopIteration:
            return True

        self.world = World(self.screen, world_width, world_height)
        self.world.setup(roads, intersections, grass, entry_roads,
                         valid_routes, schedule, strategy)

        self.world_time = 0

        self.start_time = time
        start_time = time_module.strftime(TIME_FORMAT,
                                          time_module.gmtime(time/1000))

        print("Starting scenario at time:", start_time)
        print("Results will be found at:", filename)
        self.filename       = filename
        self.filename_short = filename_short

        return False

    def printDuration(self, time):
        duration = (time - self.start_time) / 1000
        duration = time_module.strftime(TIME_FORMAT,
                                        time_module.gmtime(duration))
        print("Test duration: {}".format(duration))

    def recordResults(self, time):
        self.printDuration(time)
        print("Writing results to file...")
        f = open(self.filename, 'w')

        total = 0
        count = 0
        for start_time, end_time, duration in self.world.results:
            total += duration
            count += 1

            f.write("{} {} {}\n".format(start_time, end_time, duration))

        f.close()

        average = total / count
        print("Average duration:", average)

    #def blankResults(self, time):
    #    self.printDuration(time)
    #    print("Creating empty file...")
    #    f = open(self.filename, 'w')
    #    f.close()

    def update(self, time):
        if self.world == None:
            return self.generateNext(time)

        if self.world.checkFinished() or self.world.checkAbort():
            self.recordResults(time)
            return self.generateNext(time)

        #if self.world.checkAbort():
        #    self.blankResults(time)
        #    return self.generateNext(time)

    def updateTime(self):
        self.world_time += TIME_STEP

def main():
    # initialise game engine
    pygame.init()

    # set some options
    size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    world_handler = WorldHandler(screen)

    prev_time  = pygame.time.get_ticks()

    render          = True
    limit_fps       = True
    include_caption = True
    paused          = False

    # set up for FPS
    if include_caption:
        fps = 0
        frames = [0 for f in range(10)]
        f = 0

    # loop until the user clicks the close button
    done = False
    while not done:

        # limit the frames per second
        if limit_fps:
            clock.tick(FRAMES_PER_SECOND)

        time      = pygame.time.get_ticks()
        time_step = time - prev_time
        prev_time = time

        done = world_handler.update(time)
        if done:
            break
        world = world_handler.world

        # generate caption
        if include_caption:

            # find time between frames
            frames[f] = time_step / 1000
            f += 1
            if f == 10:
                f = 0

            # calculate fps
            total = 0.0
            for frame in frames:
                total += frame
            if total == 0.0:
                fps = time_rate = "UNDEFINED"
            else:
                fps = min(round(10/total), 999)
                time_rate = "{:.2f}".format(10/(total*FRAMES_PER_SECOND))

            F_Name  = world_handler.filename_short
            C_Upto  = world.cars_added
            C_Crash = world.crashed_cars
            C_Done  = world.successful_cars
            T_Sim   = time_module.strftime(TIME_FORMAT, time_module.gmtime(world.time/1000))
            T_Real  = time_module.strftime(TIME_FORMAT, time_module.gmtime(time/1000))
            T_Rate  = time_rate

            # generate screen caption
            string  = "{} | FPS: {}".format(F_Name, fps)
            string += " | C_Upto: {} | C_Crash: {} | C_Done: {}".format(
                C_Upto, C_Crash, C_Done)
            string += " | T_Sim: {} | T_Real: {} | T_Rate: {}".format(
                T_Sim, T_Real, T_Rate)

            if paused:
                string += " | PAUSED"
            elif not render:
                string += " | RENDER=False"

            pygame.display.set_caption(string)

        # deal with events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    world.stopPan()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    world.startPan(Vector(*event.pos))

                elif event.button == 4:
                    world.zoomIn(Vector(*event.pos))

                elif event.button == 5:
                    world.zoomOut(Vector(*event.pos))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    world.resetZoom()

                if event.key == pygame.K_SPACE:
                    if paused:
                        paused = False

                    else:
                        paused = True
                        render = True
                        include_caption = True

                if event.key == pygame.K_r:
                    if not paused:
                        if render:
                            render    = False
                            limit_fps = False
                        else:
                            render = True

                if event.key == pygame.K_c:
                    if not paused:
                        include_caption = not include_caption

                if event.key == pygame.K_f:
                    if not paused:
                        if limit_fps:
                            limit_fps = False
                        else:
                            limit_fps = True
                            render    = True

        # update world
        if not paused:
            world_handler.updateTime()
            world.update(world_handler.world_time)

        # draw to screen
        if render:
            screen.fill(WHITE)
            world.draw(paused)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


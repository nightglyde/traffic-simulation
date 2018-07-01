import pkgutil
import time as time_module
#import re

from util import *

from world import World

from pregen.scenario_1x1 import roads, entry_roads, intersections,\
                                valid_routes, grass, world_width, world_height

import pregen.datasets_1x1 as datasets
package = datasets
prefix  = package.__name__ + "."

#pattern = re.compile("dataset_1x1_30")

module_names = []

#schedules = []
for importer, module_name, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix):

    print("Found module:", module_name)

    module_names.append(module_name)

    #if pattern.search(modname):

TIME_FORMAT = "%H:%M:%S"

# initialise game engine
pygame.init()

# set some options
size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

def worldGenerator():

    for module_name in module_names:

        module   = __import__(module_name, fromlist="dummy")
        schedule = module.schedule

        print("Imported", module)

        short_name = module_name.split(".")[-1]

        for strategy, strategy_name in ALL_STRATEGIES:

            filename = "results/{}_{}.txt".format(strategy_name, short_name)

            try:
                f = open(filename)
                f.close()

            except FileNotFoundError:
                yield schedule, strategy, filename

class WorldHandler:
    def __init__(self):
        self.world      = None
        self.world_time = None
        self.filename   = None
        self.generator  = worldGenerator()

    def generateNext(self):
        try:
            schedule, strategy, filename = next(self.generator)
        except StopIteration:
            return True

        self.world = World(screen, world_width, world_height)
        self.world.setup(roads, intersections, grass, entry_roads,
                         valid_routes, schedule, strategy)

        self.world_time = 0

        print("Running scenario. Results will be found at:", filename)
        self.filename = filename

        return False

    def recordResults(self):

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

    def blankResults(self):
        print("Creating empty file...")
        f = open(self.filename, 'w')
        f.close()

    def check(self):
        if self.world == None:
            return self.generateNext()

        if self.world.checkFinished():
            self.recordResults()
            return self.generateNext()

        if self.world.checkAbort():
            self.blankResults()
            return self.generateNext()

    def updateTime(self):
        self.world_time += TIME_STEP

world_handler = WorldHandler()

prev_time  = pygame.time.get_ticks()

render          = True
limit_fps       = True
include_caption = True
paused          = False

# set up for FPS
if include_caption:
    fps = 0
    pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

    frames = [0 for f in range(10)]
    f = 0

# loop until the user clicks the close button
done = False
while not done:

    done = world_handler.check()
    world = world_handler.world

    # limit the frames per second
    if limit_fps:
        clock.tick(FRAMES_PER_SECOND)

    time      = pygame.time.get_ticks()
    time_step = time - prev_time
    prev_time = time

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

        F_Name  = world_handler.filename
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

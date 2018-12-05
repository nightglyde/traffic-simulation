import sys, os

ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ABS_PATH)

from time import gmtime, strftime

from src.util import *
from src.simulation.world import World

from datasets.scenarios.scenario_2x2_50 import\
    roads, entry_roads, intersections, valid_routes,\
    grass, world_width, world_height
from datasets.datasets_2x2_50.dataset_2x2_50_030_111_02 import schedule

INCLUDE_CAPTION = True

def generateFilename(world):
    timestamp = strftime("%Y-%m-%d_%H-%M", gmtime())
    strategy_name = ALL_STRATEGIES[world.strategy][1]

    batch_name = "{}_{}".format(timestamp, strategy_name)

    for i in range(1000):
        yield "{}/results/screenshots/img_{}_{:03}.png".format(ABS_PATH, batch_name, i)

def run(strategy):
    # initialise game engine
    pygame.init()

    # set some options
    size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    world = World(screen, world_width, world_height)

    # build world
    world.setup(roads, intersections, grass, entry_roads, valid_routes, schedule, strategy)

    filenames = generateFilename(world)

    world_time = 0
    prev_time  = pygame.time.get_ticks()

    # set up for FPS
    if INCLUDE_CAPTION:
        fps = 0
        pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

        frames = [0 for f in range(10)]
        f = 0

    # loop until the user clicks the close button
    paused = False
    done   = False
    while not done:

        # limit the frames per second
        clock.tick(FRAMES_PER_SECOND)

        time      = pygame.time.get_ticks()
        time_step = time - prev_time
        prev_time = time

        # generate caption
        if INCLUDE_CAPTION:

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
                fps = round(10/total)
                time_rate = "{:.2f}".format(10/(total*FRAMES_PER_SECOND))

            # generate screen caption
            string  = "Car Simulator | FPS: {}".format(fps)
            string += " | Score: {} | Crash: {} | Active cars: {}".format(
                world.successful_cars, world.crashed_cars, len(world.cars))
            string += " | Time Rate: {} | T: {}".format(time_rate, world_time/1000)
            if paused:
                string += " | PAUSED"

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
                if event.key == pygame.K_SPACE:
                    paused = not paused

                if event.key == pygame.K_ESCAPE:
                    world.resetZoom()

                if event.key == pygame.K_RETURN:
                    pygame.image.save(screen, next(filenames))

            #elif event.type == pygame.USEREVENT:
            #    paused = True


        # update world
        if not paused:
            world_time += TIME_STEP
            world.update(world_time)

        # draw to screen
        screen.fill(WHITE)
        world.drawAll(paused)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    strategy = int(input("Enter strategy {0, 2, 4}: "))

    while not strategy in {TRAFFIC_LIGHTS_MODE,
                           VIRTUAL_TRAFFIC_LIGHTS_2_MODE,
                           GREEDY_CONTROLLER_MODE}:
        strategy = int(input("Enter strategy {0, 2, 4}: "))

    #strategy = TRAFFIC_LIGHTS_MODE
    #strategy = VIRTUAL_TRAFFIC_LIGHTS_MODE
    #strategy = VIRTUAL_TRAFFIC_LIGHTS_2_MODE
    #strategy = GREEDY_CONTROLLER_MODE
    #strategy = MY_TRAFFIC_CONTROLLER_MODE

    run(strategy)


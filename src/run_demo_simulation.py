import sys, os

ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ABS_PATH)

from time import gmtime, strftime

from src.util import *
from src.simulation.world import World

INCLUDE_CAPTION = True

def run(scenario_name, dataset_name, strategy):
    scenario = __import__(scenario_name, fromlist="dummy")
    dataset  = __import__(dataset_name,  fromlist="dummy")

    # initialise game engine
    pygame.init()

    # set some options
    size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock  = pygame.time.Clock()

    world = World(screen, scenario.world_width, scenario.world_height)

    # build world
    world.setup(scenario.roads, scenario.intersections, scenario.grass,
                scenario.entry_roads, scenario.valid_routes, dataset.schedule,
                strategy)

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

        # update world
        if not paused:
            world_time += TIME_STEP
            world.update(world_time)

        # draw to screen
        screen.fill(WHITE)
        world.drawAll(paused)
        pygame.display.flip()

    pygame.quit()

def main():
    print("0: Traffic Lights\n2: Virtual Traffic Lights\n4: Clique-Based Traffic Controller")
    strategy = int(input("Enter strategy {0, 2, 4}: "))

    scenario = "datasets.scenarios.scenario_1x1_50"
    dataset  = "datasets.datasets_1x1_50.dataset_1x1_50_120_111_00"

    while not strategy in {TRAFFIC_LIGHTS_MODE,
                           VIRTUAL_TRAFFIC_LIGHTS_2_MODE,
                           GREEDY_CONTROLLER_MODE}:
        print("0: Traffic Lights\n2: Virtual Traffic Lights\n4: Clique-Based Traffic Controller")
        strategy = int(input("Enter strategy {0, 2, 4}: "))

    #strategy = TRAFFIC_LIGHTS_MODE
    #strategy = VIRTUAL_TRAFFIC_LIGHTS_MODE
    #strategy = VIRTUAL_TRAFFIC_LIGHTS_2_MODE
    #strategy = GREEDY_CONTROLLER_MODE
    #strategy = MY_TRAFFIC_CONTROLLER_MODE

    run(scenario, dataset, strategy)

if __name__ == "__main__":
    main()


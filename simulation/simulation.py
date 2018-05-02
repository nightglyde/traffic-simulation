from util import *

from world import World
from pregen_4 import roads, entry_roads, intersections, \
                     grass, world_width, world_height

INCLUDE_CAPTION = True

# initialise game engine
pygame.init()

# set some options
size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

world = World(screen, world_width, world_height)

# build world
world.buildWorld(roads, entry_roads, intersections, grass)

world_time = 0
prev_time  = pygame.time.get_ticks()

print()

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
        fps = round(10/total)

        # generate screen caption
        string  = "Car Simulator | FPS: {}".format(fps)
        string += " | Score: {} | Crash: {} | Active cars: {}".format(
            world.successful_cars, world.crashed_cars, len(world.cars))
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

        #elif event.type == pygame.USEREVENT:
        #    paused = True


    # update world
    if not paused:
        world_time += TIME_STEP
        world.update(world_time)

    # draw to screen
    screen.fill(WHITE)
    world.draw()
    pygame.display.flip()

pygame.quit()


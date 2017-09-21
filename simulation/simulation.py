from util import *

from world import World

FRAMES_PER_SECOND = 60
INCLUDE_CAPTION   = True
MAX_CARS          = 1

CAR_COLOURS = {"RED": RED,   "ORA": ORANGE, "YEL": YELLOW,  "LIM": LIME,
               "GRN": GREEN, "SPR": SPRING, "CYA": CYAN,    "AZU": AZURE,
               "BLU": BLUE,  "VIO": VIOLET, "MAG": MAGENTA, "ROS": ROSE}

# initialise game engine
pygame.init()

# set some options
size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

world = World(screen, WORLD_WIDTH, WORLD_HEIGHT)

# create grass
for points in predefined_grass:
    world.addGrass(points)

# create cars
time  = pygame.time.get_ticks()
count = 0
for colour_name in CAR_COLOURS:
    world.addCar(colour_name, CAR_COLOURS[colour_name], time)

    print(colour_name, end=" ")

    count += 1
    if count == MAX_CARS:
        break

print()

# update car models
world.firstUpdate(pygame.time.get_ticks())

# set up for FPS
if INCLUDE_CAPTION:
    fps = 0
    pygame.display.set_caption("Car Simulator | FPS: {}".format(fps))

    frames = [0 for f in range(10)]
    f = 0
    prev_time = time

# loop until the user clicks the close button
done = False

while not done:

    # limit the frames per second
    clock.tick(FRAMES_PER_SECOND)

    # generate caption
    time = pygame.time.get_ticks()
    if INCLUDE_CAPTION:
        # find time between frames
        dt = (time - prev_time) / 1000
        prev_time = time

        frames[f] = dt
        f += 1
        if f == 10:
            f = 0

        # calculate fps
        total = 0.0
        for frame in frames:
            total += frame
        fps = round(10/total)

        # get car scores
        scores = []
        for controller in world.controllers:
            scores.append((-controller.score,
                            controller.duration,
                            controller.name))
        scores.sort()

        # generate screen caption
        string = "Car Simulator | FPS: {}".format(fps)

        for score, duration, name in scores:
            string += " | {:3} {:3}".format(name, -score)

        if world.paused:
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
                world.pause(pygame.time.get_ticks())

    # update world
    world.update(pygame.time.get_ticks())

    # draw to screen
    screen.fill(WHITE)
    world.draw()
    pygame.display.flip()

pygame.quit()


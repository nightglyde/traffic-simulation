from util import *

from world import World

INCLUDE_CAPTION = True

#MAX_CARS    = 12
#CAR_COLOURS = {"RED": RED,   "ORA": ORANGE, "YEL": YELLOW,  "LIM": LIME,
#               "GRN": GREEN, "SPR": SPRING, "CYA": CYAN,    "AZU": AZURE,
#               "BLU": BLUE,  "VIO": VIOLET, "MAG": MAGENTA, "ROS": ROSE}

#CAR_COLOURS = {"YEL": YELLOW}

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

# create starting positions
for point in starting_positions:
    world.addStartingPosition(point)

# create waypoint options
for point in waypoint_options:
    world.addWaypointOption(point)

world_time = 0
prev_time  = pygame.time.get_ticks()

# create cars
#count = 0
#for i in range(1000):
#    for colour_name in CAR_COLOURS:
#        name   = colour_name + "_" + str(i)
#        colour = CAR_COLOURS[colour_name]
#
#        world.addCar(name, colour, world_time)
#
#        print(name)
#
#        count += 1
#        if count == MAX_CARS:
#            break
#    else:
#        continue
#    break

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

        # get car scores
        scores = []
        for controller in world.controllers:
            scores.append((-controller.score,
                            controller.waypoint_time,
                            controller.car.name))
        scores.sort()

        # generate screen caption
        string = "Car Simulator | FPS: {}".format(fps)
        for score, time, name in scores:
            #string += " | {:4} {:3}".format(name, -score)
            string += " | {:4}".format(name)
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

        elif event.type == pygame.USEREVENT:
            paused = True


    # update world
    if not paused:
        world_time += TIME_STEP #min(time_step, TIME_STEP)
        world.update(world_time)

    # draw to screen
    screen.fill(WHITE)
    world.draw()
    pygame.display.flip()

pygame.quit()


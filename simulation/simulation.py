import pygame

from util import *
from car import Car
from controller import CarController

INCLUDE_CAPTION   = True
MAX_CARS          = 6

CAR_COLOURS = {"RED": RED,  "YEL": YELLOW, "GRN": GREEN,
               "CYA": CYAN, "BLU": BLUE,   "MAG": MAGENTA}

# initialise game engine
pygame.init()

# set some options
size   = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock  = pygame.time.Clock()

# create cars
time = pygame.time.get_ticks()

cars        = []
controllers = []
num_cars    = 0

for colour_name in CAR_COLOURS:
    print(colour_name, end=" ")

    colour = CAR_COLOURS[colour_name]

    # create car
    pos, angle = generateRandomWorldPosition()
    car = Car(colour_name, screen, colour, pos, angle, time)
    cars.append(car)

    # create car controller
    controller = CarController(colour_name, screen, colour)
    controllers.append(controller)

    # count the number of cars
    num_cars += 1
    if num_cars == MAX_CARS:
        break

print()

# update car models
time = pygame.time.get_ticks()

updates = []
for i in range(num_cars):
    position, angle = cars[i].update(time)
    position *= PIXELS_PER_METRE
    updates.append((position, angle))

for i in range(num_cars):
    position, angle = updates[i]
    controllers[i].firstUpdate(position, angle, time)

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

        # get car points
        pairs = []
        for controller in controllers:
            pairs.append((-controller.points, controller.duration, controller.name))
        pairs.sort()

        # generate screen caption
        string = "Car Simulator | FPS: {}".format(fps)
        for points, duration, name in pairs:
            string += " | {:3} {:4}".format(name, -points)
        pygame.display.set_caption(string)

    # deal with events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # provide controllers with updated information
    time = pygame.time.get_ticks()

    updates = []
    for i in range(num_cars):
        position, angle = cars[i].update(time)
        position *= PIXELS_PER_METRE
        updates.append((position, angle))

    for i in range(num_cars):
        position, angle = updates[i]
        controllers[i].update(position, angle, time)

    # check for crashes
    for i in range(num_cars):
        for j in range(i+1, num_cars):
            if controllers[i].checkCollision(controllers[j]):
                controllers[i].stop()
                controllers[j].stop()
                cars[i].stop()
                cars[j].stop()

    # send controller instructions to cars
    controls = []
    for i in range(num_cars):
        engine, steering, braking = controllers[i].control()
        controls.append((engine, steering, braking))

    time = pygame.time.get_ticks()
    for i in range(num_cars):
        engine, steering, braking = controls[i]
        cars[i].control(engine, steering, braking, time)

    # draw to screen
    screen.fill(WHITE)

    for controller in controllers:
        controller.draw()

    for car in cars:
        car.draw()

    # update the screen
    pygame.display.flip()

pygame.quit()


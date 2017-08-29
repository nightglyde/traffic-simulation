import pygame

from util import *
from car import Car
from controller import CarController

FRAMES_PER_SECOND = 60
INCLUDE_CAPTION   = True
MAX_CARS          = 6

CAR_COLOURS = {"RED": RED,  "YEL": YELLOW, "GRN": GREEN,
               "CYA": CYAN, "BLU": BLUE,   "MAG": MAGENTA}

WAYPOINT_OUTER = SCREEN_UNIT * 5      # 50
WAYPOINT_INNER = SCREEN_UNIT * 9 // 2 # 45

print(WAYPOINT_OUTER, WAYPOINT_INNER)

def drawBackground(screen, controller):
    colour          = controller.colour
    darker_colour   = DARKER[colour]
    lighter_colour  = LIGHTER[colour]

    prev = controller.position
    for waypoint in controller.waypoints:
        pos, angle = waypoint
        pygame.draw.line(screen, darker_colour, pos.coords(), prev.coords(), 1)

        prev = pos

    for waypoint in controller.waypoints:
        pos, angle = waypoint

        centre = pos.coords()
        pygame.draw.circle(screen, colour,         centre, WAYPOINT_OUTER)
        pygame.draw.circle(screen, lighter_colour, centre, WAYPOINT_INNER)
        pygame.draw.circle(screen, darker_colour, centre, WAYPOINT_OUTER, 1)
        pygame.draw.circle(screen, darker_colour,  centre, WAYPOINT_INNER, 1)

        front = pos + getVector(angle)             * WAYPOINT_INNER
        right = pos + getVector(angle + ANGLE_120) * WAYPOINT_INNER
        left  = pos + getVector(angle - ANGLE_120) * WAYPOINT_INNER

        arrow = [pos.coords(),   right.coords(),
                 front.coords(), left.coords()]
        pygame.draw.polygon(screen, colour, arrow)
        pygame.draw.polygon(screen, darker_colour, arrow, 1)

ARROW_LENGTH      = SCREEN_UNIT * 4 # 40
ARROW_WIDTH       = SCREEN_UNIT * 2 # 20
ARROW_STEM_LENGTH = SCREEN_UNIT * 3 # 30
ARROW_STEM_WIDTH  = SCREEN_UNIT * 1 # 10

def drawCar(screen, controller):
    heading = getVector(controller.car_angle)
    pos     = controller.position

    # draw car
    forward = heading * SCREEN_CAR_LENGTH / 2
    right   = heading.right90() * SCREEN_CAR_WIDTH / 2

    front = pos + forward
    rear  = pos - forward

    front_left  = front - right
    front_right = front + right
    rear_left   = rear  - right
    rear_right  = rear  + right

    chassis = [front_left.coords(), front_right.coords(),
               rear_right.coords(), rear_left.coords()]
    pygame.draw.polygon(screen, controller.colour, chassis)
    pygame.draw.polygon(screen, BLACK, chassis, 2)

    # draw arrow
    forward = heading
    right   = heading.right90()

    stem_front = forward * ARROW_STEM_LENGTH
    stem_right = right   * ARROW_STEM_WIDTH / 2
    head_front = forward * ARROW_LENGTH
    head_right = right   * ARROW_WIDTH / 2

    arrow = [(pos              - stem_right).coords(),
             (pos + stem_front - stem_right).coords(),
             (pos + stem_front - head_right).coords(),
             (pos + head_front             ).coords(),
             (pos + stem_front + head_right).coords(),
             (pos + stem_front + stem_right).coords(),
             (pos              + stem_right).coords()]
    pygame.draw.polygon(screen, BLACK, arrow, 1)

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
    # create car
    pos, angle = generateRandomWorldPosition()
    car = Car(colour_name, pos, angle, time)
    cars.append(car)

    # create car controller
    controller = CarController(colour_name, CAR_COLOURS[colour_name])
    controllers.append(controller)

    # count the number of cars
    num_cars += 1
    if num_cars == MAX_CARS:
        break

# update car models
time = pygame.time.get_ticks()

updates = []
for i in range(num_cars):
    position, car_angle = cars[i].update(time)
    position *= PIXELS_PER_METRE
    updates.append((position, car_angle))

for i in range(num_cars):
    position, car_angle = updates[i]
    controllers[i].firstUpdate(position, car_angle, time)

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
        position, car_angle = cars[i].update(time)
        position *= PIXELS_PER_METRE
        updates.append((position, car_angle))

    for i in range(num_cars):
        position, car_angle = updates[i]
        controllers[i].update(position, car_angle, time)

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
        drawBackground(screen, controller)

    for controller in controllers:
        drawCar(screen, controller)

    # update the screen
    pygame.display.flip()

pygame.quit()


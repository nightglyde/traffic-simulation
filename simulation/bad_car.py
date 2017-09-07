from util import *

# physics constants
DRAG_CONSTANT    = 0.760358
RR_CONSTANT      = DRAG_CONSTANT * 30
FR_CONSTANT      = 1
BRAKING_CONSTANT = 10000
GRAVITY_CONSTANT = 9.8

MIN_ENGINE_FORCE = 0
MAX_ENGINE_FORCE = 10000

CAR_LENGTH  = WORLD_UNIT * 10 # 4.5
CAR_WIDTH   = WORLD_UNIT * 4  # 1.8
AXLE_LENGTH = WORLD_UNIT * 6  # 2.7

CENTRE_TO_FRONT  = WORLD_UNIT * 3 #4 # 1.8
CENTRE_TO_REAR   = WORLD_UNIT * 3 #2 # 0.9
CENTRE_TO_GROUND = WORLD_UNIT * 1.5 # 0.675

CAR_MASS    = 1250
CAR_WEIGHT  = CAR_MASS * GRAVITY_CONSTANT
CAR_INERTIA = (CAR_MASS / 12) * (CAR_LENGTH**2 + CAR_WIDTH**2)

STATIC_FRONT_WEIGHT = (CENTRE_TO_REAR   / AXLE_LENGTH) * CAR_WEIGHT
STATIC_REAR_WEIGHT  = (CENTRE_TO_FRONT  / AXLE_LENGTH) * CAR_WEIGHT
HLM                 = (CENTRE_TO_GROUND / AXLE_LENGTH) * CAR_MASS

MIN_LAT_FORCE = -10000
MAX_LAT_FORCE =  10000

MAX_ANGLE   = ANGLE_15
LOWER_LIMIT = -MAX_ANGLE
UPPER_LIMIT = MAX_ANGLE

STEERING_RATE = 1

SHOW_WHEELS = True

class Car:
    def __init__(self, name, screen, colour, position, car_angle, time):
        self.name   = name
        self.screen = screen
        self.colour = colour

        self.position     = position         # metres
        self.velocity     = VECTOR_0         # metres per second
        self.acceleration = VECTOR_0         # metres per second^2
        self.engine_force = MIN_ENGINE_FORCE # newtons

        self.car_angle        = car_angle # radians
        self.angular_velocity = 0.0       # radians per second
        self.wheel_angle      = ANGLE_0   # radians

        self.braking = False

        self.control_time = time
        self.update_time  = time

        self.forces = []

    def update(self, time):
        v_angle, v_magnitude = getPolar(self.velocity)
        a_angle, a_magnitude = getPolar(self.acceleration)

        car_forward   = getVector(self.car_angle)
        wheel_forward = getVector(self.car_angle + self.wheel_angle)
        v_forward     = getVector(v_angle)
        a_forward     = getVector(a_angle)

        car_left   = car_forward.left90()
        wheel_left = wheel_forward.left90()
        v_left     = v_forward.left90()
        a_left     = a_forward.left90()

        v_car_angle = (v_angle - self.car_angle).value
        v_car_long  = v_magnitude * math.cos(v_car_angle)
        v_car_lat   = v_magnitude * math.sin(v_car_angle)

        v_wheel_angle = (v_angle - self.wheel_angle).value
        v_wheel_long  = v_magnitude * math.cos(v_wheel_angle)
        v_wheel_lat   = v_magnitude * math.sin(v_wheel_angle)

        a_car_angle = (a_angle - self.car_angle).value
        a_car_long  = a_magnitude * math.cos(a_car_angle)
        a_car_lat   = a_magnitude * math.sin(a_car_angle)

        a_wheel_angle = (a_angle - self.wheel_angle).value
        a_wheel_long  = a_magnitude * math.cos(a_wheel_angle)
        a_wheel_lat   = a_magnitude * math.sin(a_wheel_angle)

        force  = VECTOR_0
        torque = 0.0
        self.forces = []

        front_weight = STATIC_FRONT_WEIGHT - HLM * a_car_long
        rear_weight  = STATIC_REAR_WEIGHT  + HLM * a_car_long

        if not self.braking:
            # traction force
            traction_mag = min(self.engine_force, front_weight)
            traction_force = wheel_forward * traction_mag

            force  += traction_force
            torque += CENTRE_TO_FRONT * traction_mag * math.sin(self.wheel_angle.value)

            self.forces.append(traction_force)
            self.forces.append(VECTOR_0)

        else:
            # force of front wheel brakes
            front_brakes_mag   = -min(BRAKING_CONSTANT/2, front_weight)
            front_brakes_force = wheel_forward * forward_brakes_mag

            force  += front_brakes_force
            torque += CENTRE_TO_FRONT * front_brakes_mag * math.sin(self.wheel_angle.value)

            # force of rear wheel brakes
            rear_brakes_mag   = -min(BRAKING_CONSTANT/2, rear_weight)
            rear_brakes_force = car_forward * rear_brakes_mag

            force  += rear_brakes_force
            # don't add torque, because wheels are perfectly in line with centre of car

            self.forces.append(front_brakes_force)
            self.forces.append(rear_brakes_force)

        if v_magnitude > 0:
            # drag / air resistance
            drag = self.velocity * v_magnitude * (-DRAG_CONSTANT)
            force += drag

            # longitudinal resistance on front wheels
            if sign(v_wheel_long) == sign(self.engine_force):
                # rolling resistance
                f_mag = -min(v_wheel_long * RR_CONSTANT/2, front_weight)
            else:
                # friction
                f_mag = FR_CONSTANT * front_weight * sign(-v_wheel_long) * abs(v_wheel_long / v_magnitude)
            f_f = wheel_forward * f_mag
            force  += f_f
            torque += CENTRE_TO_FRONT * f_mag * math.sin(self.wheel_angle.value)

            # longitudinal resistance on rear wheels
            if sign(v_car_long) == sign(self.engine_force):
                # rolling resistance
                r_mag = -min(v_car_long * RR_CONSTANT/2, rear_weight)
            else:
                # friction
                r_mag = FR_CONSTANT * rear_weight * sign(-v_car_long) * abs(v_car_long / v_magnitude)
            r_f = wheel_forward * r_mag
            force += r_f

            # lateral resistance on front wheels
            f_mag = FR_CONSTANT * front_weight * sign(-v_wheel_lat) * abs(v_wheel_lat / v_magnitude)
            f_r = wheel_left * f_mag

            force  += f_r
            torque += CENTRE_TO_FRONT * f_mag * math.sin((self.wheel_angle - ANGLE_90).value)

            # lateral resistance on rear wheels
            r_mag = FR_CONSTANT * rear_weight * sign(v_car_lat) * abs(v_car_lat / v_magnitude)
            r_r = car_left * r_mag

            force  += r_r
            torque += CENTRE_TO_REAR * r_mag * math.sin((self.wheel_angle - ANGLE_90).value)

            self.forces.append(drag)
            self.forces.append(f_f)
            self.forces.append(r_f)
            self.forces.append(f_r)
            self.forces.append(r_r)
            self.forces.append(car_left * -torque)

        else:
            for i in range(6):
                self.forces.append(VECTOR_0)

        # convert force to motion
        dt = (time - self.update_time) / 1000
        self.update_time = time

        self.acceleration = force / CAR_MASS
        self.velocity    += self.acceleration  * dt
        self.position    += self.velocity * dt

        angular_acceleration  = torque / CAR_INERTIA * 10
        self.angular_velocity = angular_acceleration * dt
        self.car_angle       += Angle(self.angular_velocity * dt)

        print(self.engine_force, v_magnitude, angular_acceleration)

        # cornering
        #if self.wheel_angle.value != ANGLE_0.value:
        #    angle, speed = getPolar(self.velocity)

        #    radius                = AXLE_LENGTH / math.sin(self.wheel_angle.value)
        #    self.angular_velocity = speed / radius

        #    self.car_angle += Angle(self.angular_velocity * dt)

        return self.position, self.car_angle

    def control(self, engine_control, steering_control, braking_control, time):
        dt                = (time - self.control_time) / 1000
        self.control_time = time

        # adjust engine force
        engine_change  = 10000 * dt

        if engine_control > 0:
            self.engine_force = min(self.engine_force+engine_change,
                                    MAX_ENGINE_FORCE)
        elif engine_control < 0:
            self.engine_force = max(self.engine_force-engine_change*2,
                                    MIN_ENGINE_FORCE)

        # adjust wheel angle
        angle_change = Angle(2*math.pi * dt * STEERING_RATE)

        angliness = (self.wheel_angle.value / MAX_ANGLE.value)**2
        if self.wheel_angle < ANGLE_0:
            self.wheel_angle += angle_change * angliness
        else:
            self.wheel_angle -= angle_change * angliness

        if steering_control == RIGHT:
            self.wheel_angle += angle_change
        elif steering_control == LEFT:
            self.wheel_angle -= angle_change

        # toggle brakes
        if braking_control:
            self.braking = True
        else:
            self.braking = False

    def draw(self):
        pos = self.position * PIXELS_PER_METRE

        forward = getVector(self.car_angle)
        left    = forward.left90()

        # draw car
        car_front = forward * SCREEN_CAR_LENGTH / 2
        car_left  = left    * SCREEN_CAR_WIDTH / 2

        chassis = [(pos + car_front + car_left).coords(),
                   (pos + car_front - car_left).coords(),
                   (pos - car_front - car_left).coords(),
                   (pos - car_front + car_left).coords()]
        pygame.draw.polygon(self.screen, self.colour, chassis)
        pygame.draw.polygon(self.screen, BLACK,       chassis, 1)

        # draw arrow
        stem_front = forward * ARROW_STEM_LENGTH
        stem_left  = left    * ARROW_STEM_WIDTH / 2
        head_front = forward * ARROW_LENGTH
        head_left  = left    * ARROW_WIDTH / 2

        arrow = [(pos              + stem_left).coords(),
                 (pos + stem_front + stem_left).coords(),
                 (pos + stem_front + head_left).coords(),
                 (pos + head_front             ).coords(),
                 (pos + stem_front - head_left).coords(),
                 (pos + stem_front - stem_left).coords(),
                 (pos              - stem_left).coords()]
        pygame.draw.polygon(self.screen, BLACK, arrow, 1)

        if SHOW_WHEELS:
            # draw wheels
            wheel_forward = getVector(self.car_angle + self.wheel_angle)

            f_wheel_front = wheel_forward          * SCREEN_WHEEL_LENGTH / 2
            f_wheel_left  = wheel_forward.left90() * SCREEN_WHEEL_WIDTH  / 2

            r_wheel_front = forward * SCREEN_WHEEL_LENGTH / 2
            r_wheel_left  = left    * SCREEN_WHEEL_WIDTH / 2

            axle_front = forward * SCREEN_AXLE_LENGTH / 2
            axle_left  = left    * SCREEN_AXLE_WIDTH / 2

            # front left wheel
            f_l = pos + axle_front + axle_left
            front_left_wheel = [(f_l - f_wheel_left + f_wheel_front).coords(),
                                (f_l + f_wheel_left + f_wheel_front).coords(),
                                (f_l + f_wheel_left - f_wheel_front).coords(),
                                (f_l - f_wheel_left - f_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, front_left_wheel)
            pygame.draw.polygon(self.screen, GREEN,     front_left_wheel, 1)

            # front right wheel
            f_r = pos + axle_front - axle_left
            front_right_wheel = [(f_r + f_wheel_left + f_wheel_front).coords(),
                                 (f_r - f_wheel_left + f_wheel_front).coords(),
                                 (f_r - f_wheel_left - f_wheel_front).coords(),
                                 (f_r + f_wheel_left - f_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, front_right_wheel)
            pygame.draw.polygon(self.screen, RED,     front_right_wheel, 1)

            # rear left wheel
            r_l = pos - axle_front + axle_left
            rear_left_wheel = [(r_l - r_wheel_left + r_wheel_front).coords(),
                               (r_l + r_wheel_left + r_wheel_front).coords(),
                               (r_l + r_wheel_left - r_wheel_front).coords(),
                               (r_l - r_wheel_left - r_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_left_wheel)
            pygame.draw.polygon(self.screen, YELLOW,     rear_left_wheel, 1)

            # rear right wheel
            r_r = pos - axle_front - axle_left
            rear_right_wheel = [(r_r + r_wheel_left + r_wheel_front).coords(),
                                (r_r - r_wheel_left + r_wheel_front).coords(),
                                (r_r - r_wheel_left - r_wheel_front).coords(),
                                (r_r + r_wheel_left - r_wheel_front).coords()]
            pygame.draw.polygon(self.screen, DARK_GREY, rear_right_wheel)
            pygame.draw.polygon(self.screen, BLUE,     rear_right_wheel, 1)

        #if self.wheel_angle.value != 0.0:
        #    radius = AXLE_LENGTH / math.sin(self.wheel_angle.value) * PIXELS_PER_METRE

        #    centre_vector = getVector(self.car_angle + ANGLE_90) * radius
        #    circle_centre = (pos + centre_vector).coords()
        #    radius = abs(round(radius))

        #    if radius < 200:
        #        pygame.draw.circle(self.screen, BLACK, circle_centre, radius, 1)

        if self.forces:
            f_w_o = pos + axle_front
            r_w_o = pos - axle_front

            main_force = (f_w_o + self.forces[0]).coords()
            rear_force = (r_w_o + self.forces[1]).coords()
            drag_force = (pos   + self.forces[2]).coords()
            front_rr   = (f_w_o + self.forces[3]).coords()
            rear_rr    = (r_w_o + self.forces[4]).coords()
            front_fr   = (f_w_o + self.forces[5]).coords()
            rear_fr    = (r_w_o + self.forces[6]).coords()
            torque     = (pos   + self.forces[7]).coords()

            pygame.draw.line(self.screen, BLACK,        f_w_o.coords(), main_force, 1)
            pygame.draw.line(self.screen, CYAN,         r_w_o.coords(), rear_force, 1)
            pygame.draw.line(self.screen, GREY,         pos.coords(),   drag_force, 1)
            pygame.draw.line(self.screen, MAGENTA,      f_w_o.coords(), front_rr, 1)
            pygame.draw.line(self.screen, DARK_BLUE,    f_w_o.coords(), front_fr, 1)
            pygame.draw.line(self.screen, DARK_YELLOW,  r_w_o.coords(), rear_rr, 1)
            pygame.draw.line(self.screen, DARK_RED,     r_w_o.coords(), rear_fr, 1)
            pygame.draw.line(self.screen, GREEN,        pos.coords(), torque, 2)

            wheel_dir = (pos + wheel_forward * 100).coords()
            pygame.draw.line(self.screen, RED, pos.coords(), wheel_dir, 3)


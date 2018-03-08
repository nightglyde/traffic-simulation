import sys

from util import *

DT = STEP_TIME

STEERING_RATE = 2*math.pi * 0.1
ANGLE_CHANGE  = STEERING_RATE * DT

def vectorise(angle):
    return Vector(math.cos(angle), math.sin(angle))

def predictCarAngle(start_angle, peak_angle, speed):
    calculus = math.cos(start_angle) - 2*math.cos(peak_angle) + 1
    return calculus * speed / (STEERING_RATE * AXLE_LENGTH)

def squarePredict(start_angle, peak_angle, speed):
    not_calculus = peak_angle**2 - start_angle**2/2
    return not_calculus * speed / (STEERING_RATE * AXLE_LENGTH)

def peakTest(start_angle, peak_angle, speed, groups):

    time        = 0
    wheel_angle = start_angle
    car_angle   = 0.0
    position    = VECTOR_0

    while wheel_angle < peak_angle:
        wheel_angle = min(wheel_angle + ANGLE_CHANGE, peak_angle)

        ang_vel    = speed * math.sin(wheel_angle) / AXLE_LENGTH
        car_angle += ang_vel * DT
        position  += vectorise(car_angle) * speed
        time      += 1

    wheel_angle = max(wheel_angle - ANGLE_CHANGE, 0.0)

    while wheel_angle > 0.0:
        ang_vel    = speed * math.sin(wheel_angle) / AXLE_LENGTH
        car_angle += ang_vel * DT
        position  += vectorise(car_angle) * speed
        time      += 1

        wheel_angle = max(wheel_angle - ANGLE_CHANGE, 0.0)

    pangle = getAngle(position).value

    distance = position.mag()

    cos_prediction = predictCarAngle(start_angle, peak_angle, speed)
    sqr_prediction = squarePredict(start_angle, peak_angle, speed)

    things = sorted([car_angle, cos_prediction, sqr_prediction])
    thingy = things[-1] / things[0]

    if thingy > 1.5:
        print(*groups)
        print(car_angle, cos_prediction, sqr_prediction, thingy)

    #print(math.degrees(start_angle), speed,
    #      math.degrees(peak_angle),  math.degrees(car_angle),
    #      math.degrees(predictCarAngle(start_angle, peak_angle, speed)),
    #      math.degrees(squarePredict(start_angle, peak_angle, speed)))

def getPeakAngle(wheel_angle, speed, desired_angle):
    #desired_angle %= 2*math.pi

    turn  = desired_angle * STEERING_RATE * AXLE_LENGTH / speed
    ratio = (math.cos(wheel_angle) + 1 - turn)/2
    peak_angle = math.acos(max(-1.0, min(ratio, 1.0)))
    peak_angle = min(peak_angle, ANGLE_45.value)

    return peak_angle

def angleTest(wheel_angle, speed, desired_angle):
    time = 0
    car_angle = 0.0
    position = VECTOR_0

    peak_angle = getPeakAngle(wheel_angle, speed, desired_angle)

    if wheel_angle < peak_angle:
        wheel_angle = min(wheel_angle + ANGLE_CHANGE, peak_angle)
    else:
        wheel_angle = max(wheel_angle - ANGLE_CHANGE, peak_angle)

    while car_angle < desired_angle or abs(wheel_angle) > 0.001:
        ang_vel    = math.sin(wheel_angle) * speed / AXLE_LENGTH
        car_angle += ang_vel * DT
        position  += getVector(Angle(car_angle)) * speed


        time += 1
        peak_angle = getPeakAngle(wheel_angle, speed, desired_angle - car_angle)
        #print(math.degrees(car_angle), math.degrees(wheel_angle), math.degrees(peak_angle), time, time*DT*speed)

        if wheel_angle < peak_angle:
            wheel_angle = min(wheel_angle + ANGLE_CHANGE, peak_angle)
        else:
            wheel_angle = max(wheel_angle - ANGLE_CHANGE, peak_angle)

    time += 1
    print(math.degrees(car_angle), math.degrees(wheel_angle), time, time*DT*speed)

#d = int(input("> "))
#desired_angle = math.radians(d)

for d in range(1, 360):
    desired_angle = math.radians(d)

    for w in range(-45, 46):
        wheel_angle = math.radians(w)

        for speed in range(1, 21):

            peak_angle = getPeakAngle(wheel_angle, speed, desired_angle)

            if peak_angle >= wheel_angle:
                #print(d, w, speed)
                peakTest(wheel_angle, peak_angle, speed, (d, w, speed))
                #angleTest(wheel_angle, speed, desired_angle)


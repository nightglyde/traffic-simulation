from util import *

def checkGiveWay(car1, car2):
    a = car1.position
    x = car2.position

    ab = car1.vec#getVector(car1.angle)
    xy = car2.vec#getVector(car2.angle)
    ax = x - a

    ab_cross_xy = crossProduct(ab, xy)

    turn = sign(ab_cross_xy)
    if turn == CENTRE:
        # parallel

        if dotProduct(ab, xy) <= 0:
            # facing opposite directions
            return car1.name > car2.name, a + ax * 0.5

        ax_dot_xy = dotProduct(ax, xy)
        if ax_dot_xy > 0:
            # car 1 is behind car 2
            return True, car2.position

        if ax_dot_xy < 0:
            # car 1 is in front of car 2
            return False, car1.position

        ax_cross_ab = crossProduct(ax, ab)
        if ax_cross_ab < 0:
            # car 1 is to the left of car 2
            return True, car2.position

        if ax_cross_ab > 0:
            # car 1 is to the right of car 2
            return False, car1.position

        # car 1 is on top of car 2
        return car1.name > car2.name, a

    ax_cross_ab = crossProduct(ax, ab)
    ax_cross_xy = crossProduct(ax, xy)

    ab_rel_dist = ax_cross_xy / ab_cross_xy
    xy_rel_dist = ax_cross_ab / ab_cross_xy

    intersect = a + ab * ab_rel_dist

    if ab_rel_dist > xy_rel_dist:
        return True, intersect

    if ab_rel_dist < xy_rel_dist:
        return False, intersect

    if turn == RIGHT:
        return True, intersect

    return False, intersect


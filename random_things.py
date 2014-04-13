"""
Several methods to generate random things. Shared among several exercises.
"""
__author__ = 'tiago'
from __init__ import BOX_A, BOX_BA
import numpy as np
import math


def random_line():
    """
    Generate a random line crossing the board.
    @return: w (vector), and px[], py[]
    """
    px = BOX_BA * np.random .random_sample(2) + BOX_A
    py = BOX_BA * np.random.random_sample(2) + BOX_A
    #
    # Line as A * x + B * y + C = 0
    _a = py[0] - py[1]
    _b = px[1] - px[0]
    _c = px[0]*py[1] - px[1]*py[0]
    return [_a, _b, _c], px, py


def random_points(number_of_points, line=None, func=None):
    """
    Throw some random points and evaluate whether they are above or below the given line
    If above RED, else BLUE
    @Return: points (numpy.array), solution (array)
    """
    points = []
    f = []
    if line:
        for i in range(number_of_points):
            point = BOX_BA * np.random.random_sample(2) + BOX_A
            if not -1 < point[0] < 1 or not -1 < point[1] < 1:
                print ' ERROR WITH THE POINTS!!! ', point, BOX_BA, BOX_A
            points.append(point)
            _v_line = line[:2]
            f.append(math.copysign(1, np.dot(_v_line, point) + line[2]))
        points = np.array(points)
    elif func:
        points = BOX_BA * np.random.random_sample((number_of_points, 2)) + BOX_A
        f = func.eval(points)
    return points, f

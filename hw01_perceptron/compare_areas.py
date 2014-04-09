"""
Compare areas under lines.
"""
import math

__author__ = 'tiago'
import numpy as np

N = 10000
# Limits of the board. Constant for the random generators
ba = 2  # Side of board
a = -1  # Left edge of board


def area_misclassified(fm, fb, gw):
    """
    Calculates the "misclassified" area or area between the two lines
    """
    bad_points = 0
    f = []
    _w = np.array([gw[1], gw[2]])
    _w_0 = gw[0]
    for i in range(N):
        x = ba*np.random.random_sample() + a
        y = ba*np.random.random_sample() + a
        f = 1 if y > fm*x+fb else -1    # true value
        # perceptron:
        # sign(np.dot(w, _point) + _w0)
        _p = np.array([x, y])
        g = np.dot(_w, _p) + _w_0
        math.copysign(1, g)
        if f * g < 0:
            bad_points += 1
    bad_area = float(bad_points) / float(N)
    return bad_area

if __name__ == "__main__":
    area_misclassified(0,0, 0,1)
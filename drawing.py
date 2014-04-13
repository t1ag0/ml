"""
Drawing methods shared among several exercises.
"""
from __init__ import BOX_A, BOX_BA
from matplotlib import pyplot as plt

__author__ = 'tiago'


def draw_board(size=BOX_BA):
    """
    Draw a square from (-1,-1) to (1,1)
    """
    plt.ylim([-size, size])
    plt.xlim([-size, size])
    # Area
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1])


def draw_points(points, f):
    """
    Draw an array of points based on their true value.
    """
    if len(f) != len(points):
        return
    for i in range(len(points)):
        point = points[i]
        if f[i] > 0:
            plt.plot(point[0], point[1], 'ro')
        else:
            plt.plot(point[0], point[1], 'bx')


def draw_line(w, opts=''):
    """
    Draw a line: w[0] * x + w[1] * y + w[2] = 0
    """
    if w[0] == 0:
        print ' horizontal'
        x_left, x_right = -1, 1
        y_left = y_right = -w[2] / w[1]
    elif w[1] == 0:
        print ' vertical '
        y_left, y_right = -1, 1
        x_left = x_right = -w[2]/w[0]
    else:
        # y = -w[0]/w[1] * x - w[2]/w[1]
        # left
        m = float(-w[0]/w[1])
        b = float(-w[2]/w[1])
        if -1 < (-m + b) < 1:   # left
            x_left = -1
            y_left = -m + b
        elif (-m + b) > 1:      # top
            x_left = (1 - b) / m
            y_left = 1
        else:                   # bottom
            x_left = (-1 - b) / m
            y_left = -1
        # Right
        # y_right = m + b
        if -1 < (m + b) < 1:   # ~horizontal
            x_right = 1
            y_right = m + b
        elif (m+b) < -1:        # bottom
            x_right = (-1 - b) / m
            y_right = -1
        else:                   # top
            x_right = (1 - b) / m
            y_right = 1
    plt.plot([x_left, x_right], [y_left, y_right], opts)


def draw_line_2(m, b, opts=''):
    """
    Draw a line given m and b (y = m*x + b)
    """
    # left
    m = float(m)
    b = float(b)
    if -1 < (-m + b) < 1:   # left
        x_left = -1
        y_left = -m + b
    elif (-m + b) > 1:      # top
        x_left = (1 - b) / m
        y_left = 1
    else:                   # bottom
        x_left = (-1 - b) / m
        y_left = -1

    # Right
    # y_right = m + b
    if -1 < (m + b) < 1:   # ~horizontal
        x_right = 1
        y_right = m + b
    elif (m+b) < -1:        # bottom
        x_right = (-1 - b) / m
        y_right = -1
    else:                   # top
        x_right = (1 - b) / m
        y_right = 1
    plt.plot([x_left, x_right], [y_left, y_right], opts)
    return m, b

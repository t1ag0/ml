import math
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'tiago'


def init_board(size=2):
    """
    Draw a square form (-1,-1) to (1,1)
    """
    plt.ylim([-size, size])
    plt.xlim([-size, size])
    # Area
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1])


def draw_line(m, b, opts=''):
    """
    Draw a line
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


def draw_vector(w):
    # w0 + w1 * x + w2 * y = 0
    x_0 = 0
    y_0 = (-w[0] / w[2])
    x_1 = w[1]
    y_1 = y_0 + w[2]
    dx = x_1-x_0
    dy = y_1-y_0
    n = np.linalg.norm([dx, dy])
    dx /= n
    dy /= n
    #
    x_0 = (w[0]/w[2]) / (-w[1]/w[2] - dy/dx)
    y_0 = (-w[0]/w[2]) - (w[1]/w[2]) * x_0
    plt.arrow(x_0, y_0, dx, dy, fc="k", ec="k", head_width=0.05, head_length=0.1)


def draw_board(training_sample, training_true_results, fm, fb, g_w):
    #draw.draw_board(training_sample, fm, fb, g_w)
    init_board()
    # draw f
    draw_line(fm, fb)
    draw_points(training_sample, training_true_results)
    # draw perceptron output
    _gm = -g_w[1] / g_w[2]
    _gb = -g_w[0] / g_w[2]
    draw_line(_gm, _gb, 'r--')
    #draw_vector(w)
    draw_vector([-_gb, -_gm, 1])
    #
    _w_0 = g_w[0]
    _w = [g_w[1], g_w[2]]
    _t = [0.9, 0.9]
    g = np.dot(_w, _t) + _w_0
    #print ' G, +.9: ', g
    g = math.copysign(1, g)
    if g > 0:
        plt.plot(0.9, 0.9, 'go')
    else:
        plt.plot(0.9, 0.9, 'gx')
    _t = [-0.9, -0.9]
    g = math.copysign(1, np.dot(_w, _t) + _w_0)
    if g > 0:
        plt.plot(-0.9, -0.9, 'go')
    else:
        plt.plot(-0.9, -0.9, 'gx')
    plt.show()

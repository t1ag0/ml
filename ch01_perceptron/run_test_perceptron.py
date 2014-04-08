import matplotlib.pyplot as plt
import numpy as np
from perceptron import perceptron
import compare_areas
import draw_board as draw

__author__ = 'tiago'

# Limits of the board. Constant for the random generators
ba = 2  # Side of board
a = -1  # Left edge of board


def random_line():
    """
    Generate a random line crossing the board.
    @return: slope and Y_0
    """
    px = []
    py = []
    for i in range(2):
        px.append(float(ba)*np.random.random_sample() + a)
        py.append(float(ba)*np.random.random_sample() + a)
    m = float(py[1] - py[0]) / float(px[1] - px[0])
    b = py[0] - m*px[0]
    return m, b


def throw_random_points(number_of_points):
    """
    Draw a random line and throw some random points to the board.
    If above the line they are red, else blue
    @Return: points (numpy.array), solution (array)
    """
    _m, _b = random_line()
    points = []
    f = []
    for i in range(number_of_points):
        x = ba*np.random.random_sample() + a
        y = ba*np.random.random_sample() + a
        points.append([x, y])
        if y > _m * x + _b:
            f.append(1)
        else:
            f.append(-1)
    points = np.array(points)
    return points, f, _m, _b


def throw_test_points(dir=0):
    """
    Draw 4 points at definite position to test perceptron learning.
    @dir: 0: horizontal
        1: vertical
        3: diagonal
    @Return: points (numpy.array), solution (array)
    """
    points = np.array([[-0.5, 0.5],
                       [0.5, 0.5],
                       [-0.5,  -0.27879628],
                       [0.58493426, -0.79988819]])
    _f = np.array([1, 1,  -1, -1])
    if dir == 2:
        _f = np.array([-1, 1,  -1, 1])
    elif dir == 3:
        _f = np.array([-1, -1,  -1, 1])
    for idx in range(len(_f)):
        _f = _f[idx]
        _x = points[idx][0]
        _y = points[idx][1]
        if _f > 0:
            plt.plot(_x, _y, 'ro')
        else:
            plt.plot(_x, _y, 'bx')
    return points, _f, 0, 0


def train_and_test_perceptron():
    """
    Produce a random "True" line, throw some random points and classify
    them based on "true" line.
    Train a perceptron based on the data.
    Test perceptron output vs "true" function.
    """
    # Random points
    training_sample, true_values, fm, fb = throw_random_points(10)

    # Train perceptron
    gm, gb, number_iterations, g_w = perceptron(training_sample, true_values)

    # compare "true" vs " calculated" areas
    bad_area = compare_areas.area_misclassified(fm, fb, g_w)
    return fm, fb, gm, gb, training_sample, true_values, number_iterations, bad_area, g_w


if __name__ == "__main__":
    number_tests = 10
    error_avg = 0
    iterations_avg = 0
    for i in range(number_tests):
        fm, fb, gm, gb, training_sample, training_f,  number_iterations, bad_area, g_w = train_and_test_perceptron()
        error_avg += bad_area
        iterations_avg += number_iterations
        print i, ' Iterations: ', number_iterations, ' Error: ', bad_area
    error_avg /= number_tests
    iterations_avg /= number_tests
    print ' Avg: Iterations: ', iterations_avg, ' Error: ', error_avg
    #draw.draw_board(training_sample, training_f, fm, fb, g_w)

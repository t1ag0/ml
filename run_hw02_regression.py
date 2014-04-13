"""
hw 02
Test regression.

Results 4, 5:
    In-Sample      Freq: 313 // Error:  0.0313
    Out-of-Sample  Freq: 3989 // Error:  0.03989

Results 6:
 iterations perceptron:  17.089 Min: 1 Max: 2040
"""
__author__ = 'tiago'

from matplotlib import pyplot as plt
import numpy as np
from sklearn import linear_model

import drawing as draw
import random_things as rdn
from hw01_perceptron import perceptron


def init_board(number_points):
    line = [0, 0, 0]
    px = py = [0, 0]
    # With N=10, it happens often that there is no point in one of hte sides of the line.
    # There is no point in trying to fit this, this skip event without at least on point in each side.
    bad = True
    while bad:
        line, px, py = rdn.random_line()
        points, f = rdn.random_points(number_points, line)
        if -9 < np.sum(f) < 9:
            bad = False
    return points, f, line, px, py


def regression_fit(points, f):
    #
    # linear regression: Scikit-learn
    #
    regr = linear_model.LinearRegression()
    regr.fit(points, f)
    # Results of the fit
    # F = A * x1 + B * x2 + C
    # F(0) = C
    g_fit = [regr.coef_[0], regr.coef_[1], regr.decision_function([0, 0])]
    return g_fit, regr


def draw_all(_points, _f, f_line, g_line, g_line_2=None):
    draw.draw_board()
    draw.draw_line(f_line, 'g--')
    draw.draw_points(_points, _f)
    draw.draw_line(g_line, 'r--')
    if g_line_2:
        draw.draw_line(g_line_2, 'b--')
    plt.show()


def test_regression(number_points):
    """
    Generates a random line, throws several random points using the random line to classufy them
    Fits using regression and test fit.
    """
    #
    # Create random line
    #
    line = [0, 0, 0]
    px = py = [0, 0]
    # With N=10, it happens often that there is no point in one of hte sides of the line.
    # There is no point in trying to fit this, this skip event without at least on point in each side.
    bad = True
    while bad:
        line, px, py = rdn.random_line()
        points, f = rdn.random_points(number_points, line)
        if -9 < np.sum(f) < 9:
            bad = False

    #
    # linear regression: Scikit-learn
    #
    regr = linear_model.LinearRegression()
    regr.fit(points, f)
    # Results of the fit
    # F = A * x1 + B * x2 + C
    # F(0) = C
    g_fit = [regr.coef_[0], regr.coef_[1], regr.decision_function([0, 0])]
    #
    ## Error in-sample
    _g = regr.decision_function(points)
    _g = f * _g
    _g = _g[_g < 0]
    e_in = len(_g)
    #
    ## Error out-of-sample
    _out_points, _out_f = rdn.random_points(1000, line)
    _g = _out_f * regr.decision_function(_out_points)
    _g = _g[_g < 0]
    e_out = len(_g)
    return e_in, e_out, line, px, py, points, f, g_fit


def test_regression_n_times(number_of_points, number_of_tests):
    e_in_avg = 0
    e_out_avg = 0
    for _test_ in range(number_of_tests):
        _e_in, _e_out, _line, _px, _py, _points, _f, _g_ = test_regression(number_of_points)
        # print 'E_in:', _e_in, '   E_out:', _e_out
        e_in_avg += _e_in
        #
        #  Sanity check
        if _e_in > 30:
            print ' break at test ', _test_
            break
        e_out_avg += _e_out
    print ''
    print ' In-Sample      Freq:', e_in_avg, '// Error: ', float(e_in_avg) / (number_of_points * number_of_tests)
    print ' Out-of-Sample  Freq:', e_out_avg, '// Error: ',  float(e_out_avg) / (number_of_tests*1000)
    #
    # Draw last try.
    draw.draw_board()
    draw.draw_line(_line, 'g--')
    draw.draw_points(_points, _f)
    draw.draw_line(_g_, 'r--')
    plt.show()


def test_regression_pla():
    """
    Use regression as initial weight for Perceptron
    Note: Colors on plot
        Green line: "true" function
        Red:    Fit PLA
        Blue:   Fit Regression
    """
    _N_ = 10
    _M_ = 1000
    iteration_avg = []
    for i in range(_M_):
        points, f, line, px, py = init_board(_N_)
        g_regression, regr = regression_fit(points, f)
        g_pla, iterations = perceptron.perceptron(points, f, g_regression)
        iteration_avg.append(iterations)
    # print g_pla
    # print g_regression
    print ' iterations perceptron: ', np.mean(iteration_avg), np.min(iteration_avg), np.max(iteration_avg)
    draw_all(points, f, line, g_pla, g_regression)


if __name__ == "__main__":
    # n_points = 100
    # n_tests = 100
    # test_regression_n_times(n_points, n_tests)
    #
    test_regression_pla()

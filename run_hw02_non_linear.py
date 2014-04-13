"""
HW 02 exercise 8, 9 & 10
"""
__author__ = 'tiago'

from matplotlib import pyplot as plt
import numpy as np
#
import drawing as dr
import random_things as rt
#
import run_hw02_regression as reg
#
from sklearn import linear_model


class NoisyFunc:
    """
    The function
    """
    noise_prob = 0.10

    @staticmethod
    def eval(x):
        if len(x.shape) == 1:
            x1 = x[0]
            x2 = x[1]
        else:
            x1 = x[:, 0]
            x2 = x[:, 1]
        _f = np.sign(x1*x1 + x2*x2 - 0.6)
        flip = np.random.binomial(1, NoisyFunc.noise_prob, len(_f))
        _f[flip == True] *= -1
        return _f


def basic_fit(N=1000, M=10):
    """
    Try to fit a regression line without transform.
    Fails: Err In Sample ~ 0.5
    """
    error_in = []
    for i in range(M):
        points, f = rt.random_points(N, func=NoisyFunc)
        regr = linear_model.LinearRegression()
        regr.fit(points, f)
        #
        ## Error in-sample
        _g = f * regr.decision_function(points)
        e_in = len(_g[_g < 0])
        error_in.append(e_in)
    error_in = np.mean(error_in) / N
    gfit = [regr.coef_[0], regr.coef_[1], regr.decision_function([0, 0])]
    return error_in, points, f, gfit


def transform(points):
    ## Transform
    x1x2 = points[:, 0]*points[:, 1]
    x1x1 = points[:, 0]*points[:, 0]
    x2x2 = points[:, 1]*points[:, 1]
    points_t = np.transpose(np.array([points[:, 0], points[:, 1], x1x2, x1x1, x2x2]))
    return points_t


def transform_fit(N=1000, M=10, _p=None):
    """
    Use a non-linear transformation before the fit
        Transformation: 1, x1, x2, x1*x2, x1**2, x2**2
    Results:
        E_out:  0.126216
        Coeficients: -1.41235081e-03  -1.93377357e-03   4.67326156e-03   1.55868881e+00 1.55731603e+00
    """
    error_in = []
    error_out = []
    coefs = []
    for i in range(M):
        points, f = rt.random_points(N, func=NoisyFunc)
        #
        ## Transform
        points_t = transform(points)
        regr = linear_model.LinearRegression()
        regr.fit(points_t, f)
        coefs.append(regr.coef_)
        #
        ## Error in-sample
        _g = f * regr.decision_function(points_t)
        e_in = len(_g[_g < 0])
        error_in.append(e_in)
        #
        ## Err out-of-sample
        _out_points, _out_f = rt.random_points(1000, func=NoisyFunc)
        ## Transform
        _out_points = transform(_out_points)
        ## Evaluate
        _g = _out_f * regr.decision_function(_out_points)
        _g = _g[_g < 0]
        error_out.append(len(_g))
    error_in = np.mean(error_in) / N
    error_out = np.mean(error_out) / N
    return error_in, points, f, coefs, error_out


if __name__ == "__main__":
    N = 1000
    M = 1000
    #
    ## Basic fit
    # error_in, points, f, g_fit = basic_fit(N, M)
    # dr.draw_points(points, f)
    # dr.draw_line(g_fit, 'g-')
    # plt.show()
    #
    ## Transform and fit
    error_in, points, f, coefs, error_out = transform_fit(N, M)
    print ' Err In ', error_in, M, N
    print ' Eout: ', error_out
    coefs = np.mean(coefs, axis=0)
    print coefs

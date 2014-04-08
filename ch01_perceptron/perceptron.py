import numpy as np
__author__ = 'tiago'


def perceptron(x, y, learning_rate=1):
    """
    Variation of basic perceptron. This version only changes ONCE per iteration.
    it takes RANDOMLY only one of the points with errors, actualizes W, and B and back again.

    x = Array of (X1,X2)   // Test cases
    y = 1D vector           // Solutions
    """
    #
    npoints, ncols = x.shape
    w = np.zeros(ncols, dtype=int)    # Initialize the parameter
    b = 0
    R = 2   # math.sqrt(20)
    #
    iterations = 0  # iterations
    mistakes = True
    while mistakes:
        iterations += 1
        mistakes = []
        for p_idx in range(npoints):
            _point = x[p_idx]
            dot_product = np.dot(w, _point) + b
            if not y[p_idx] * dot_product > 0:    # diff sign
                _w = learning_rate * y[p_idx] * _point
                _b = learning_rate * y[p_idx] * R*R
                mistakes.append([_w, _b])
        ## print i, mistakes
        if mistakes:
            idx = np.random.randint(len(mistakes))
            w = w + mistakes[idx][0]
            b = b + mistakes[idx][1]
    _gm = -w[0] / w[1]
    _gb = -b / w[1]
    return _gm, _gb, iterations, [b, w[0], w[1]]

import numpy as np
__author__ = 'tiago'


def perceptron(x, y, initial_weights=None, learning_rate=1):
    """
    Variation of basic perceptron. This version only changes ONCE per iteration.
    it takes RANDOMLY only one of the points with errors, actualizes W, and B and back again.

    x = Array of (X1,X2)   // Test cases
    y = 1D vector           // Solutions
    """
    #
    npoints, ncols = x.shape
    if initial_weights:
        w = np.array(initial_weights[:ncols])
        b = initial_weights[-1]
    else:
        w = np.zeros(ncols, dtype=int)    # Initialize the weights to 0
        b = 0
    #
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
    # _gm = -w[0] / w[1]
    # _gb = -b / w[1]
    _g = [w[0], w[1], b]
    return _g, iterations

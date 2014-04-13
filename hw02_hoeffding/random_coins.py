"""
Convention:
Head : 1
Tail : 0

Note: It takes 1 min seconds to run 100,000 iterations
numpy.random.randint        returns random between [first, last) (last exclusive)
numpy.random.random_integer returns random between [first, last] (las inclusive)


RESULTS:
    Shape of random cube :  (100000, 10, 1000)
     Time Rdm      : 23.235396
     Time Mean     : 40.066345
     Time Mean2    : 1.151342
     Time For Loop : 0.225075

    Total time for 100,000 experiments :  65.09665

    Freq heads 1st coin    : 0.500007
    Freq heads Random coin : 0.500232
    Min Freq of head       : 0.037624
"""
import time

__author__ = 'tiago'
import numpy as np
from numpy import random


# initial constants
M = 100000
coins = 1000    # number of coins
flips = 10      # number of tosses


def toss_coins_forloop(n_coins=coins, n_toss=flips, repetition=M):
    """
    Classic way of doing this with FOR loops.
    This is VERY  SLOW, 30 sec / 100.000 experiments
    """
    # Results
    nu_1 = 0.0
    nu_rnd = 0.0
    nu_min = 0.0

    for i in range(M):
        frequencies = np.zeros(n_coins, dtype=int)
        for toss in range(n_toss):
            frequencies += random.random_integers(0, 1, n_coins)
        nu_1 += frequencies[0]                              # first coin
        nu_rnd += frequencies[random.randint(0, n_coins)]   # random coin
        nu_min += np.amin(frequencies)                      # min heads
    nu_1 /= repetition
    nu_rnd /= repetition
    nu_min /= repetition
    return nu_1, nu_rnd, nu_min


def toss_coins(n_rep, n_flips, n_coins):
    """
    Flip n_coins, n_flips times and repeat this n_rep times.
    Everything using numpy here. It should be way faster than above
    ... but it is not really.
    """
    t0 = time.clock()
    cube_rep_flip_coin = random.random_integers(0, 1, [n_rep, n_flips, n_coins])
    tRdm = time.clock()

    # Average on number of flips
    matix_rep_coins = np.mean(cube_rep_flip_coin, axis=1)
    tMean = time.clock()
    #
    # control
    #print matix_rep_coins.shape
    c1 = matix_rep_coins[:, 0]
    #print c1.shape
    mu_1 = np.mean(c1)

    mu_mins = np.min(matix_rep_coins, axis=1)
    mu_min = np.mean(mu_mins)
    mu_min_min = np.min(mu_mins)
    #print mu_mins.shape
    tMean_coins = time.clock()
    #
    # Get a random coin for each repetition
    random_indices = random.random_integers(0, 1, n_rep)
    #print 'random indices', random_indices.shape
    mu_rnd_col = []
    for i in range(n_rep):
        idx = random_indices[i]
        mu_rnd_col.append(matix_rep_coins[i][idx])
    mu_rnd_col = np.array(mu_rnd_col)
    mu_rnd = np.mean(mu_rnd_col)
    t_forLoop = time.clock()

    print ' Shape of random cube : ', cube_rep_flip_coin.shape
    print ' Time Rdm      :', tRdm - t0
    print ' Time Mean     :', tMean - tRdm
    print ' Time Mean2    :', tMean_coins - tMean
    print ' Time For Loop :', t_forLoop - tMean_coins

    return mu_1, mu_rnd, mu_min, mu_min_min


if __name__ == "__main__":
    t0 = time.clock()
    n_rep = 100000
    _nu_1, _nu_rnd, _nu_min, _nu_min_min = toss_coins(n_rep=n_rep, n_flips=10, n_coins=1000)
    t1 = time.clock() - t0
    print '\n Total time for', n_rep, 'experiments : ', t1
    print ' Results: '
    print ' Freq heads 1st coin    :', _nu_1
    print ' Freq heads Random coin :', _nu_rnd
    print ' Min Freq of head       :', _nu_min, _nu_min_min

"""
Convention:
Head : 1
Tail : 0

Note:
numpy.random.randint        returns random between [first, last) (last exclusive)
numpy.random.random_integer returns random between [first, last] (las inclusive)
"""
import time

__author__ = 'tiago'
import numpy as np
from numpy import random


# initial constants
M = 100000
coins = 1000    # number of coins
tosses = 10      # number of tosses

# Results
nu_1 = 0.0
nu_rnd = 0.0
nu_min = 0.0

t0 = time.clock()
for i in range(M):
    frequencies = np.zeros(coins, dtype=int)
    #for coin in range(coins):
    for toss in range(tosses):
        frequencies += random.random_integers(0, 1, coins)
    #print i, len(frequencies), frequencies
    nu_1 += frequencies[0]                           # first coin
    nu_rnd += frequencies[random.randint(0, coins)]  # random coin
    nu_min += np.amin(frequencies)                   # min heads
t1 = time.clock()
nu_1 /= M
nu_rnd /= M
nu_min /= M

print ' M : ', M
print ' Number of coins : ', coins
print ' Number of tosses: ', tosses
print ' First:', nu_1
print ' Rnd  :', nu_rnd
print ' Min  :', nu_min
print ' Time :', t1-t0
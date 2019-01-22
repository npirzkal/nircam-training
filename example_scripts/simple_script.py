#! /usr/bin/env python

"""Just a simple file for github/git training"""

import numpy as np


def values_and_noise(max_val):
    test = np.arange(max_val)
    noise = np.random.random(max_val)
    total = test + noise
    return total
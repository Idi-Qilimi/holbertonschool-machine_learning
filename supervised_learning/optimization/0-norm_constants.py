#!/usr/bin/env python3
"""Calculates the mean and standard deviation"""


import numpy as np
"""Calculates the mean and standard deviation"""


def normalization_constants(X):
    """Calculates the mean and standard deviation"""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return mean, std

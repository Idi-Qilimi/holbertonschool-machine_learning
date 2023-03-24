#!/usr/bin/env python3
"""Calculate mean and covariance of data set"""


import numpy as np
"""Calculate mean and covariance of data set"""


def mean_cov(X):
    """Calculate mean and covariance of data set"""
    n, d = X.shape
    if len(X.shape) < 2:
        raise ValueError("X must contain multiple data points")
    if len(n) < 2:
        raise TypeError("X must must be a 2D numpy.ndarray")
    mean = np.mean(X, axis=0)
    cov = np.zeros((d, d))
    for i in range(n):
        cov += np.outer((X[i] - mean), (X[i] - mean))
    cov /= (n - 1)
    return mean.reshape(1, d), cov

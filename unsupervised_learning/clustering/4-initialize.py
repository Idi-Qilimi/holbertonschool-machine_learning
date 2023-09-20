#!/usr/bin/env python3
"""GMM function """
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    initializes variables in a Gaussian Mixture Model
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(k) is not int or k <= 0:
        return None, None, None

    n, d = X.shape
    phi = np.ones(k)/k
    m, _ = kmeans(X, k)
    S = np.tile(np.identity(d), (k, 1)).reshape(k, d, d)
    return phi, m, S

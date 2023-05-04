#!/usr/bin/env python3
"""Shuffle data"""


import numpy as np
"""Shuffle data"""


def shuffle_data(X, Y):
    """Shuffle data"""
    m = X.shape[0]
    permutation = np.random.permutation(m)
    X_shuffled = X[permutation]
    Y_shuffled = Y[permutation]
    return X_shuffled, Y_shuffled

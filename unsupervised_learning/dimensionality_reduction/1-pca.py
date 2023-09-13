#!/usr/bin/env python3
"""A function that performs PCA on a dataset"""
import numpy as np


def pca(X, ndim):
    """A function that performs PCA on a dataset"""
    X_mean = X - X.mean(axis=0)
    u, s, vh = np.linalg.svd(X_mean)
    W = vh.T
    Wr = W[:, 0:ndim]
    T = X_mean @ Wr
    return T

#!/usr/bin/env python3
"""Perform Principal Component Analysis (PCA) on a dataset."""
import numpy as np


def pca(X, var=0.95):
    """Perform Principal Component Analysis (PCA) on a dataset."""
    u, s, vh = np.linalg.svd(X)
    cum = np.cumsum(s)
    thresh = cum[len(cum) - 1] * var
    mask = np.where(thresh > cum)
    var = cum[mask]
    idx = len(var) + 1
    W = vh.T
    Wr = W[:, 0:idx]
    return Wr

#!/usr/bin/env python3
"""Multivariate Normal distribution"""


import numpy as np
"""Multivariate Normal distribution"""


class MultiNormal:
    """Multivariate Normal distribution"""
    def __init__(self, data):
         """Multivariate Normal distribution"""
         if not isinstance(data, np.ndarray) or len(data.shape) != 2:
             raise TypeError("data must be a 2D numpy.ndarray")
         n, d = data.shape
         if n < 2:
             raise ValueError("data must contain multiple data points")
         self.mean, self.cov = mean_cov(data.T)
         self.mean = self.mean.reshape(-1, 1)

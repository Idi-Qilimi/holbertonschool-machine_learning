#!/usr/bin/env python3
"""Perform binary classification"""


import numpy as np
"""Perform binary classification"""


class Neuron:
    """Perform binary classification"""
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError("nx must be integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0

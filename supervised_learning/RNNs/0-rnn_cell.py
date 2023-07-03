#!/usr/bin/env python3
"""initialization"""
import numpy as np


class RNNCell:
    """initialization"""
    def __init__(self, i, h, o):
        """constructor"""
        self.Wh = np.random.randn(h + i, h)
        self.Wy = np.random.randn(h, o)
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """forward prop"""
        concat = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(concat @ self.Wh + self.bh)
        y = h_next @ self.Wy + self.by
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)
        return h_next, y

#!/usr/bin/env python3
"""Update Bidirectional cell"""
import numpy as np


class BidirectionalCell:
    """Bidirectional Cell"""
    def __init__(self, i, h, o):
        self.Whf = np.random.normal(size=(i + h, h))
        self.Whb = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(2 * h, o))
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """Forward prop bidirectional"""
        xh_f = np.concatenate((h_prev, x_t), axis=1)
        h_next_f = np.tanh(np.dot(xh_f, self.Whf) + self.bhf)
        return h_next_f

    def backward(self, h_next, x_t):
        """Backward direction one step"""
        xh_b = np.concatenate((h_next, x_t), axis=1)
        h_prev_b = np.tanh(np.dot(xh_b, self.Whb) + self.bhb)
        return h_prev_b

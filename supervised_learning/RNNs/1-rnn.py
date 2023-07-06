#!/usr/bin/env python3
"""RNN cell"""
import numpy as np


def rnn(rnn_cell, X, h_0):
    """RNN cell"""
    t, m, i = X.shape
    h = h_0.shape[1]
    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, rnn_cell.by.shape[1]))
    H[0] = h_0
    for step in range(t):
        h_prev = H[step]
        x_step = X[step]
        H[step+1], Y[step] = rnn_cell.forward(h_prev, x_step)
    return H, Y

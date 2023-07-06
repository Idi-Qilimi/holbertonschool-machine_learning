#!/usr/bin/env python3
"""Forward prop bidirectional"""
import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """Forward prop bidirectional"""
    t, m, i = X.shape
    h = h_0.shape[1]
    H = np.zeros((t, m, 2 * h))
    Y = np.zeros((t, m, bi_cell.by.shape[1]))
    h_forward = h_0
    h_backward = h_t
    for step in range(t):
        x_t = X[step]
        h_forward = bi_cell.forward(h_forward, x_t)
        h_backward = bi_cell.backward(h_backward, x_t)
        H[step] = np.concatenate((h_forward, h_backward), axis=1)
        Y[step] = bi_cell.output(H[step])
    return H, Y

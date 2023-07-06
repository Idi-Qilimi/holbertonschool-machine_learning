#!/usr/bin/env python3
"""Deep RNN"""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Deep RNN"""
    t, m, i = X.shape
    l = len(rnn_cells)
    h = h_0.shape[2]
    H = np.zeros((t + 1, l, m, h))
    Y = np.zeros((t, m, rnn_cells[-1].by.shape[1]))
    H[0] = h_0
    for step in range(t):
        for layer in range(l):
            if layer == 0:
                h_prev = H[step, layer]
                h_next, y = rnn_cells[layer].forward(h_prev, X[step])
            else:
                h_prev = H[step, layer]
                h_next, y = rnn_cells[layer].forward(h_prev, H[step, layer - 1])
            H[step + 1, layer] = h_next
            Y[step] = y
    return H[1:], Y

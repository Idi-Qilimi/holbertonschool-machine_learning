#!/usr/bin/env python3
"""GRU cell"""
import numpy as np


class GRUCell:
    """GRU cell"""
    def __init__(self, i, h, o):
        self.Wz = np.random.normal(size=(i + h, h))
        self.Wr = np.random.normal(size=(i + h, h))
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """forward prop"""
        xh = np.concatenate((h_prev, x_t), axis=1)
        z = self.sigmoid(np.dot(xh, self.Wz) + self.bz)
        r = self.sigmoid(np.dot(xh, self.Wr) + self.br)
        xrh = np.concatenate((r * h_prev, x_t), axis=1)
        h_inter = np.tanh(np.dot(xrh, self.Wh) + self.bh)
        h_next = (1 - z) * h_prev + z * h_inter
        y = self.softmax(np.dot(h_next, self.Wy) + self.by)
        return h_next, y

    def sigmoid(self, x):
        """Sigmoid"""
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        """Softmax"""
        exps = np.exp(x)
        return exps / np.sum(exps, axis=1, keepdims=True)

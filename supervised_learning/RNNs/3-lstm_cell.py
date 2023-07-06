#!/usr/bin/env python3
"""LSTM cell"""
import numpy as np


class LSTMCell:
    """LSTM cell"""
    def __init__(self, i, h, o):
        self.Wf = np.random.normal(size=(i + h, h))
        self.Wu = np.random.normal(size=(i + h, h))
        self.Wc = np.random.normal(size=(i + h, h))
        self.Wo = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bf = np.zeros((1, h))
        self.bu = np.zeros((1, h))
        self.bc = np.zeros((1, h))
        self.bo = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, c_prev, x_t):
        """forward prop"""
        xh = np.concatenate((h_prev, x_t), axis=1)
        ft = self.sigmoid(np.dot(xh, self.Wf) + self.bf)
        ut = self.sigmoid(np.dot(xh, self.Wu) + self.bu)
        ct_inter = np.tanh(np.dot(xh, self.Wc) + self.bc)
        c_next = ft * c_prev + ut * ct_inter
        ot = self.sigmoid(np.dot(xh, self.Wo) + self.bo)
        h_next = ot * np.tanh(c_next)
        y = self.softmax(np.dot(h_next, self.Wy) + self.by)
        return h_next, c_next, y

    def sigmoid(self, x):
        """Sigmoid"""
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        """Softmax"""
        exps = np.exp(x)
        return exps / np.sum(exps, axis=1, keepdims=True)

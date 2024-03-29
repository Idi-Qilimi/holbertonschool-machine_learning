#!/usr/bin/env python3
"""Forward prop with dropout"""


import numpy as np
"""Forward prop with dropout"""


def dropout_forward_prop(X, weights, L, keep_prob):
    """Forward prop with dropout"""
    outputs = {}
    outputs["A0"] = X
    for index in range(L):
        weight = weights["W{}".format(index + 1)]
        bias = weights["b{}".format(index + 1)]
        z = np.matmul(weight, outputs["A{}".format(index)]) + bias
        dropout = np.random.binomial(1, keep_prob, size=z.shape)
        if index != (L - 1):
            A = np.tanh(z)
            A *= dropout
            A /= keep_prob
            outputs["D{}".format(index + 1)] = dropout
        else:
            A = np.exp(z)
            A /= np.sum(A, axis=0, keepdims=True)
        outputs["A{}".format(index + 1)] = A
    return outputs

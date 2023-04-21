#!/usr/bin/env python3
"""deep neural network"""


import numpy as np
"""deep neural network"""


class DeepNeuralNetwork:
    """class that represents a deep neural network"""
    def __init__(self, nx, layers):
        if type(nx) is not int:
            raise TypeError("...")
        if nx < 1:
            raise ValueError("...")
        if type(layers) is not list or len(layers) < 1:
            raise TyperError("...")
        weights = {}
        previous = nx
        for index, layer in enumerate(layers, 1):
            if type(layer) is not int or layer < 0:
                raise TypeError("list of positive integers")
            weights["b{}".format(index)] = np.zeros((layer, 1))
            weights["W{}".format(index)] = np.random.randn(layer, previous) *
                np.sqrt(2 / previous)
        self.L = len(layers)
        self.cache = {}
        self.weights = weights

#!/usr/bin/env python3
"""neural network"""


import numpy as np
"""calculate"""


class NeuralNetwork:
    """class neural"""
    def __init__(self, nx, nodes):
        """Initialisation"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return (self.__W1)

    @property
    def b1(self):
        return (self.__b1)

    @property
    def A1(self):
        return (self.__A1)

    @property
    def W2(self):
        return (self.__W2)

    @property
    def b2(self):
        return (self.__b2)

    @property
    def A2(self):
        return (self.__A2)

    def forward_prop(self, X):
        """forward prop"""
        z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + (np.exp(-z1)))
        z2 = np.matmul(self.W2, self.__A1)+self.b2
        self.__A2 = 1 / (1 + (np.exp(-z2)))
        return (self.__A1, self.__A2)

    def cost(self, Y, A):
        """neural cost"""
        m = Y.shape[1]
        m_loss = np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
        cost = (1 / m) * (-(m_loss))
        return cost

    def evaluate(self, X, Y):
        """evaluate network"""
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        prediction = np.where(A2 >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """gradient descent"""
        m = Y.shape[1]
        dz2 = (A2 - Y)
        d__W2 = (1 / m) * (np.matmul(dz2, A1.transpose()))
        d__b2 = (1 / m) * (np.sum(dz2, axis=1, keepdims=True))
        dz1 = (np.matmul(self.W2.transpose(), dz2)) * (A1 * (1 - A1))
        d__W1 = (1 / m) * (np.matmul(dz1, X.transpose()))
        d__b1 = (1 / m) * (np.sum(dz1, axis=1, keepdims=True))
        self.__W2 = self.W2 - (alpha * d__W2)
        self.__b2 = self.b2 - (alpha * d__b2)
        self.__W1 = self.W1 - (alpha * d__W1)
        self.__b1 = self.b1 - (alpha * d__b1)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        for itr in range(iterations):
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)
        return(self.evaluate(X, Y))

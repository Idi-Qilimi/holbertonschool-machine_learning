#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """


class Normal:
    """class that represents normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """class constructor"""
        self.mean = float(mean)
        self.stddev = float(stddev)
        if (self.stddev <= 0):
            raise ValueError("stddev must be a positive value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple value")

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        mean = self.mean
        stddev = self.stddev
        z = x - mean / sigma
        return z

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        mean = self.mean
        stddev = self.stddev
        x = z * stddev - mean
        return x

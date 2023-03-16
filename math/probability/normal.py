#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """


class Normal:
    """class that represents normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """class constructor"""
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple value")
            else:
                mean = float(sum(data) / len(data)
                self.mean = mean
                summation = 0
                for x in data:
                    summation += (summation / len(data)) ** (1 / 2)
                stddev = (summation / len(data)) ** (1 / 2)
                self.stddev = stddev

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        mean = self.mean
        stddev = self.stddev
        z = (x - mean) / stddev
        return z

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        mean = self.mean
        stddev = self.stddev
        x = (z * stddev) - mean
        return x

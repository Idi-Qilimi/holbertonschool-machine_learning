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
            if len(data) <= 3:
                raise ValueError("data must contain multiple value")

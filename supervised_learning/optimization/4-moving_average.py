#!/usr/bin/env python3
"""Moving average"""


import numpy as np
"""Moving average"""


def moving_average(data, beta):
    """Moving average"""
    v = 0
    EMA = []
    for i in range(len(data)):
        v = ((v * beta) + ((1 - beta) * data[i]))
        EMA.append(v / (1 - (beta ** (i + 1))))
    return EMA

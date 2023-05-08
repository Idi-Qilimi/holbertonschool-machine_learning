#!/usr/bin/env python3
"""F1 score"""


import numpy as np
"""F1 score"""


def f1_score(confusion):
    """F1 score"""
    p = precision(confusion)
    r = sensitivity(confusion)
    f1 = 2 * r * p / (r + p)
    return f1

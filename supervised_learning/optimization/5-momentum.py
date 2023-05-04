#!/usr/bin/env python3
"""Variable Momentum"""


import numpy as np
"""Variable Momentum"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """Variable Momentum"""
    dW_prev = (beta1 * v) + ((1 - beta1) * grad)
    var -= (alpha * dW_prev)
    return var, dW_prev

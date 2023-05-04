#!/usr/bin/env python3
"""Normalize X"""


import numpy as np
"""Normalize X"""


def normalize(X, m, s):
    """Normalize X"""
    X_norm = (X - m) / s
    return X_norm

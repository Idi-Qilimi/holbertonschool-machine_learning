#!/usr/bin/env python3
"""Concat matrix"""


import numpy as np
"""Concat matrix"""


def np_cat(mat1, mat2, axis=0):
    """Concat matrix"""
    a = np.array(mat1)
    b = np.array(mat2)
    new_matrix = []
    new_matrix = np.concatenate((a, b), axis)
    return new_matrix

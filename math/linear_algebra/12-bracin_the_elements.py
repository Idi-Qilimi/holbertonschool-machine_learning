#!/usr/bin/env python3
"""Element-wise math"""


def np_elementwise(mat1, mat2):
    """Element-wise math"""
    result = []
    result = mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
    return result

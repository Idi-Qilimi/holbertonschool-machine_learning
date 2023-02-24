#!/usr/bin/env python3
"""Element-wise math"""

def np_elementwise(mat1, mat2):
    """Element-wise math"""
    result = []
    result = np.add(mat1, mat2), np.subtract(mat1, mat2), np.multiply(mat1, mat2), np.divide(mat1, mat2)
    return result

#!/usr/bin/env python3
"""Shape of matrix"""


def matrix_shape(matrix):
    """Shape of matrix"""
    matrix_shape = []
    while (type(matrix) is list):
        matrix_shape.append(len(matrix))
        matrix = matrix[0]
    return matrix_shape

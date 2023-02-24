#!/usr/bin/env python3
"""Concatenate matrices along axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate matrices along axis"""
    new_matrix = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        new_matrix = mat1 + mat2
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        new_matrix = [mat1[i]+ mat2[i] for i in range(len(mat1))]
    return new_matrix

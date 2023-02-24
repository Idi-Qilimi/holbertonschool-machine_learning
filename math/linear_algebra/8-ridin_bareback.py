#!/usr/bin/env python3
"""Mat multiplication"""


def mat_mul(mat1, mat2):
    """Mat multiplication"""
    m1_rows, m1_cols = len(mat1), len(mat1[0])
    m2_rows, m2_cols = len(mat2), len(mat2[0])
    if m1_cols != m2_rows:
        return None
    result = [[0 for _ in range(m2_cols)] for _ in range(m1_rows)]
    for i in range(m1_rows):
        for j in range(m2_cols):
            for k in range(m1_cols):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

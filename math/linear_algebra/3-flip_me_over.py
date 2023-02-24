#!/usr/bin/env python3
"""Transpose matrix"""


def matrix_transpose(matrix):
    """Transpose matrix"""
    matrix_tran = []
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        matrix_tran.append(row)
    return matrix_tran

#!/usr/bin/env python3

matrix_shape = __import__('2-size_me_please').matrix_shape
def matrix_shape(matrix):
    matrix_shape=[]
    while (type(matrix) is list):
        matrix_shape.append(len(matrix))
        matrix = matrix[0]
    return matrix_shape

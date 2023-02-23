#!/usr/bin/env python3

matrix_shape = __import__('2-size_me_please').matrix_shape
def matrix_shape(matrix):
     mat = []
     while (type(matrix) is list):
         mat.append(len(matrix))
         mat = matrix[0]
    return matrix

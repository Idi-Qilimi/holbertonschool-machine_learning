#!/usr/bin/env python3
"""Derivative of polynomial"""


def poly_derivative(poly):
    """Derivative of polynomial"""
    if type(poly) is not list or poly == []:
        return None
    elif len(poly) < 2:
        return[0]
    else:
        derivative = poly.copy()
        exponent = 1
        derivative.pop(0)
        for i in range(len(derivative)):
            derivative[i] = derivative[i] * exponent
            exponent += 1
        return derivative

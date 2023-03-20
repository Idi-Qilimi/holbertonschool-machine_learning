#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images"""


import numpy as np
"""Performs a valid convolution on grayscale images"""


def convolve_grayscale_valid(images, kernel):
    """Performs a valid convolution on grayscale images"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    convoluted = np.zeros((m, height - kh + 1, width - kw + 1))
    for h in range(height - kh + 1):
        for w in range(width - kw):
            output_conv = np.sum(images[:, h: h + kh, w + kw] * kernel, axis = 1).sum(axis = 1)
        convoluted[:, h, w] = output_conv
    return convoluted

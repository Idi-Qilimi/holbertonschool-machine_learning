#!/usr/bin/env python3
"""Performs a same convolution on grayscale images"""


import numpy as np
"""Performs a same convolution on grayscale images"""


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    for z in range(height, width):
        convoluted_same = np.zeros((m, (height + 1) - kh + 1, (width + 1) - kw + 1))
    for h in range((height + 1) - kh + 1):
        for w in range((width + 1) - kw + 1):
            output_conv = np.sum(images[:, h: h + kh, w:w + kw] * kernel, axis = 1).sum(axis = 1)
            convoluted_same[:, h, w] = output_conv
    return convoluted

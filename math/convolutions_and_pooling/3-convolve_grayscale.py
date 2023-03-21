#!/usr/bin/env python3
"""Convolution Grayscale"""


import numpy as np
"""Convolution Grayscale"""


def convolve_grayscale_padding(images, kernel, padding):
    """Convolution Grayscale"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    ph, pw = padding
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)))
    ch = height + 2*ph - kh + 1
    cw = width + 2*pw - kw + 1
    convoluted = np.zeros(m, ch, cw)
    for h in range(ch):
        for w in range(cw):
            out = np.sum(images[:, h: h+kh, w+kw]*kernel,
                         axis=1).sum(axis=1)
            convoluted[:, h, w] = out
    return convoluted

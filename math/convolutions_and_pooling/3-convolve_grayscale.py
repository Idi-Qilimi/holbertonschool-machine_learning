#!/usr/bin/env python3
"""Convolution Grayscale"""


import numpy as np
"""Convolution Grayscale"""


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Convolution Grayscale"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    if padding == "same":
        if (kh % 2) == 1 and (kw % 2) == 1:
            ph = ((height - 1) * sh + kh - height) // 2 + 1
            pw = ((width - 1) * sw + kw - width) // 2 + 1
        else:
            ph = kh // 2
            pw = kw // 2
    elif padding == "valid":
        ph = 0
        pw = 0
    else:
        ph, pw = padding
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)))
    ch = ((height + (2*ph) - kh) // sh) + 1
    cw = ((width + (2*pw) - kw) // sw) + 1
    convoluted = np.zeros((m, ch, cw))
    i = 0
    for h in range(0, height + (2*ph) - kh + 1, sh):
        j = 0
        for w in range(0, width + (2 * pw) - kh + 1, sw):
            output_conv = np.sum(images[:, h:h+kh, w:w+kw]
                                 * kernel, axis=1).sum(axis=1)
            convoluted[:, i, j] = output_conv
            j += 1
        i += 1
        return convoluted

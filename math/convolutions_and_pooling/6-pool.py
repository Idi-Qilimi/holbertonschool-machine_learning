#!/usr/bin/env python3
"""pooling on images"""


import numpy as np
"""pooling on images"""


def pool(images, kernel_shape, stride, mode='max'):
    """pooling on images"""
    m, height, width, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride
    ph = ((height - kh) // sh) + 1
    pw = ((width - kw) // sw) + 1
    pooled = np.zeros((m, ph, pw, c))
    i = 0
    for h in range(0, height - kh + 1, sh):
        j = 0
        for w in range(0, width - kw + 1, sw):
            if mode == "max":
                out = np.max(images[:, h: h + kh,
                                       width: width + kw, :], axis=(1, 2, 3))
            if mode == "average":
                out = np.average(images[:, h: h + kh,
                                           width: width + kw, :], axis=(1, 2, 3))
            pooled[:, i, j] = out
            j += 1
        i += 1
    return pooled

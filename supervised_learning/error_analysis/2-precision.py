#!/usr/bin/env python3
"""Precision"""


import numpy as np
"""Precision"""


def precision(confusion):
    """Precision"""
    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    precision = tp / (tp + fp) 
    return precision

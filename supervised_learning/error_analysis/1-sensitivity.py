#!/usr/bin/env python3
"""Sensitivity"""


import numpy as np
"""Sensitivity"""


def sensitivity(confusion):
    """Sensitivity"""
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1) - tp
    tpr = tp / (tp + fn)
    return tpr

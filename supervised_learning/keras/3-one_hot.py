#!/usr/bin/env python3
"""Label vector into one-hot matrix"""


import tensorflow.keras as K
"""Label vector into one-hot matrix"""


def one_hot(labels, classes=None):
    """Label vector into one-hot matrix"""
    one_hot = K.utils.to_categorical(labels, num_classes=classes)
    return one_hot

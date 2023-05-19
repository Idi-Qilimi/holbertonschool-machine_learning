#!/usr/bin/env python3
"""Save and load a model"""


import tensorflow.keras as K
"""Save and load a model"""


def save_model(network, filename):
    """Save and load a model"""
    network.save(filename)
    return None


def load_model(filename):
    """Save and load a model"""
    model = K.models.load_model(filename)
    return model

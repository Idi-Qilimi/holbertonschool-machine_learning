#!/usr/bin/env python3
"""Validation data"""


import tensorflow.keras as K
"""Validation data"""


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, verbose=True, shuffle=False):
    """Validation data"""
    history = network.fit(x=data, y=labels,
                          batch_size=batch_size,
                          epochs=epochs,
                          validation_data=validation_data,
                          verbose=verbose,
                          shuffle=shuffle)
    return history

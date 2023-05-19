#!/usr/bin/env python3
"""Mini batch gradient descent"""


import tensorflow.keras as K
"""Mini batch gradient descent"""


def train_model(network, data, labels, batch_size, epochs,
                verbose=True, shuffle=False):
    """Mini batch gradient descent"""
    history = network.fit(x=data, y=labels,
                          batch_size=batch_size,
                          epochs=epochs,
                          verbose=verbose,
                          shuffle=shuffle)
    return history

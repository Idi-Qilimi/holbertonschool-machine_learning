#!/usr/bin/env python3
"""Early stopping"""


import tensorflow.keras as K
"""Early stopping"""


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """Early stopping"""
    if early_stopping and validation_data:
        callback = []
        callback.append(
            K.callbacks.EarlyStopping(monitor='loss', patience=patience))
    else:
        callback = None
    history = network.fit(x=data, y=labels,
                          batch_size=batch_size,
                          epochs=epochs,
                          validation_data=validation_data,
                          callbacks=callback,
                          verbose=verbose,
                          shuffle=shuffle)
    return history

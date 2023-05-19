#!/usr/bin/env python3
"""Prediction with nn"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """Prediction with nn"""
    prediction = network.predict(x=data,
                                 verbose=verbose)
    return prediction

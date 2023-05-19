#!/usr/bin/env python3
"""Save and load config"""
import tensorflow.keras as K


def save_config(network, filename):
    """Save and load config"""
    json = network.to_json()
    with open(filename, 'w+') as f:
        f.write(json)
    return None


def load_config(filename):
    """Save and load config"""
    with open(filename, 'r') as f:
        json_string = f.read()
    model = K.models.model_from_json(json_string)
    return model

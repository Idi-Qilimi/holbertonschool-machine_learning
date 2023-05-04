#!/usr/bin/env python3
"""Upgrade Adam"""


import tensorflow as tf
"""Upgrade Adam"""


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """Upgrade Adam"""
    optimizer = tf.keras.optimizers.Adam(
        learning_rate=alpha, 
        beta_1=beta1, 
        beta_2=beta2, 
        epsilon=epsilon)
    return optimizer.minimize(loss)

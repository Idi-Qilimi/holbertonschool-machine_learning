#!/usr/bin/env python3
"""Upgrade RMSProp"""


import tensorflow as tf
"""Upgrade RMSProp"""


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """Upgrade RMSProp"""
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                decay=beta2, epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op

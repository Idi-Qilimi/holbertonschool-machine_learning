#!/usr/bin/env python3
"""Momentum Upgrade"""


import tensorflow as tf
"""Momentum Upgrade"""


def create_momentum_op(loss, alpha, beta1):
    """Momentum Upgrade"""
    optimizer = tf.train.MomentumOptimizer(alpha, momentum=beta1)
    train_op = optimizer.minimize(loss)
    return train_op

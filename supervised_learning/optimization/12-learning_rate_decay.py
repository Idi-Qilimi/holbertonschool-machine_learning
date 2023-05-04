#!/usr/bin/env python3
"""Learning rate upgrade"""


import tensorflow as tf
"""Learning rate upgrade"""


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """Learning rate upgrade"""
    alpha_new = tf.divide(alpha, tf.pow(1 + decay_rate *
                    tf.floor_div(global_step, decay_step), 1))
    return alpha_new

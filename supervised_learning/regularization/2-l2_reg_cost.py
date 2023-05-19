#!/usr/bin/env python3
"""Regularization Cost"""


import tensorflow as tf
"""Regularization Cost"""


def l2_reg_cost(cost, lam):
    """Regularization Cost"""
    l2_reg_cost = tf.losses.get_regularization_losses()
        return (cost + l2_reg_cost)

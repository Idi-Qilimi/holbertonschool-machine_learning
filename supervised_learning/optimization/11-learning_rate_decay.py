#!/usr/bin/env python3
"""Learning rate"""


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """Learning rate"""
    updated_alpha = alpha / (1 + decay_rate * (global_step // decay_step))
    return updated_alpha

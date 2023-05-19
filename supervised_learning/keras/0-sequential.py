#!/usr/bin/env python3
"""NN with Keras"""


import tensorflow.keras as K
"""NN with Keras"""


def build_model(nx, layers, activations, lambtha, keep_prob):
    """NN with Keras"""
    sequential = []
    shape = (nx,)
    reg_l2 = K.regularizers.l2(lambtha)
    for i in range(len(layers)):
        if i == 0:
            sequential.append(K.layers.Dense(layers[i],
                                             activation=activations[i],
                                             kernel_regularizer=reg_l2,
                                             input_shape=shape))
        else:
            sequential.append(K.layers.Dropout(1 - keep_prob))
            sequential.append(K.layers.Dense(layers[i],
                                             activation=activations[i],
                                             kernel_regularizer=reg_l2))
    model = K.Sequential(sequential)
    return model

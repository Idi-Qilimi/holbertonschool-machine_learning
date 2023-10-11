#!/usr/bin/env python3
"""
Defines function that creates a variational autoencoder
"""
import tensorflow as tf
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense, Lambda
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras.optimizers import Adam


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    Defines function that creates a variational autoencoder
    """
    inputs = Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = Dense(nodes, activation='relu')(x)
    z_mean = Dense(latent_dims)(x)
    z_log_var = Dense(latent_dims)(x)
    def sampling(args):
        z_mean, z_log_var = args
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]
        epsilon = tf.keras.backend.random_normal(shape=(batch, dim))
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon
    z = Lambda(sampling)([z_mean, z_log_var])
    encoder = Model(inputs, [z, z_mean, z_log_var])
    latent_inputs = Input(shape=(latent_dims,))
    x = latent_inputs
    for nodes in hidden_layers[::-1]:
        x = Dense(nodes, activation='relu')(x)
    outputs = Dense(input_dims, activation='sigmoid')(x)
    decoder = Model(latent_inputs, outputs)
    outputs = decoder(encoder(inputs)[0])
    auto = Model(inputs, outputs)
    def vae_loss(x, x_decoded_mean):
        xent_loss = binary_crossentropy(x, x_decoded_mean)
        kl_loss = - 0.5 * tf.reduce_sum(1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var), axis=-1)
        return tf.reduce_mean(xent_loss + kl_loss)
    auto.compile(optimizer=Adam(), loss=vae_loss)
    return encoder, decoder, auto

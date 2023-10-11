#!/usr/bin/env python3
"""Variational Autoencoder"""
import tensorflow as tf
from tensorflow.keras import layers, models


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Variational Autoencoder"""
    encoder_inputs = tf.keras.Input(shape=(input_dims,))
    x = encoder_inputs
    for units in hidden_layers:
        x = layers.Dense(units, activation='relu')(x)
    z_mean = layers.Dense(latent_dims, activation=None)(x)
    z_log_var = layers.Dense(latent_dims, activation=None)(x)
    batch = tf.shape(z_mean)[0]
    dim = tf.shape(z_mean)[1]
    epsilon = tf.keras.backend.random_normal(shape=(batch, dim))
    z = z_mean + tf.exp(0.5 * z_log_var) * epsilon
    encoder = models.Model(
              encoder_inputs, [z, z_mean, z_log_var], name='encoder')
    latent_inputs = tf.keras.Input(shape=(latent_dims,))
    x = latent_inputs
    for units in reversed(hidden_layers):
        x = layers.Dense(units, activation='relu')(x)
    decoder_outputs = layers.Dense(input_dims, activation='sigmoid')(x)
    decoder = models.Model(latent_inputs, decoder_outputs, name='decoder')
    auto_outputs = decoder(encoder(encoder_inputs)[0])
    auto = models.Model(encoder_inputs, auto_outputs, name='vae')
    xent_loss = input_dims * tf.keras.losses.binary_crossentropy(
                encoder_inputs, auto_outputs)
    kl_loss = -0.5 * tf.reduce_sum(1 + z_log_var - tf.square(z_mean)
                                   - tf.exp(z_log_var), axis=-1)
    vae_loss = tf.reduce_mean(xent_loss + kl_loss)
    auto.add_loss(vae_loss)
    auto.compile(optimizer='adam', loss=None)
    return encoder, decoder, auto

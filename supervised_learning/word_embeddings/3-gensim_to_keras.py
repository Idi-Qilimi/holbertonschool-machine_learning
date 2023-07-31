#!/usr/bin/env python3
"""Gensim to Keras"""
from keras.layers import Embedding
from keras.initializers import Constant


def gensim_to_keras(model):
    """Converts a gensim word2vec model to a Keras Embedding layer."""
    vocab_size = len(model.wv.index_to_key)
    embedding_dim = model.wv.vector_size
    embedding_matrix = model.wv.get_normed_vectors()
    return Embedding(
        input_dim=vocab_size,
        output_dim=embedding_dim,
        embeddings_initializer=Constant(embedding_matrix),
        trainable=False)

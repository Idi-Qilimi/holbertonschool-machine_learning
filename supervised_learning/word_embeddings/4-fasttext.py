#!/usr/bin/env python3
"""Gensim fastText"""
from gensim.models import FastText

def fasttext_model(sentences, vector_size=100, min_count=5, negative=5, window=5, cbow=True, epochs=5, seed=0, workers=1):
    """Creates and trains a gensim fastText model"""
    model = FastText(sentences, vector_size=vector_size, min_count=min_count, negative=negative, window=window,
                     sg=(not cbow), epochs=epochs, seed=seed, workers=workers)
    return model

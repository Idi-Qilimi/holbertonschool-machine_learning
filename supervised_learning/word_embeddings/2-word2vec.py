#!/usr/bin/env python3
"""Gensim word2vec model"""
from gensim.models import Word2Vec


def word2vec_model(sentences, size=100, min_count=5, window=5, negative=5, cbow=True, iterations=5, seed=0, workers=1):
    """Gensim word2vec model"""
    sg = 0 if cbow else 1
    model = Word2Vec(sentences=sentences,
                     size=size,
                     min_count=min_count,
                     window=window,
                     negative=negative,
                     sg=sg,
                     iter=iterations,
                     seed=seed,
                     workers=workers)
    return model

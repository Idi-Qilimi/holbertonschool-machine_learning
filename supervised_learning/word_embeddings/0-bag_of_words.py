#!/usr/bin/env python3
"""Bag of words"""
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re


def bag_of_words(sentences, vocab=None):
    """Bag of Words"""
    if vocab is None:
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(sentences)
        vocab = vectorizer.get_feature_names_out()
    vocab = list(set(vocab))
    embeddings = np.zeros((len(sentences), len(vocab)), dtype=int)
    for i, sentence in enumerate(sentences):
        processed_sentence = re.sub(r'[^\w\s]', '', sentence.lower())
        words = processed_sentence.split()
        for word in words:
            try:
                idx = vocab.index(word)
                embeddings[i, idx] += 1
            except ValueError:
                pass
    features = vocab
    return embeddings, features

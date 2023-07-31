#!/usr/bin/env python3
"""TF-IDF"""
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def tf_idf(sentences, vocab=None):
    """TF-IDF """
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    embeddings = vectorizer.fit_transform(sentences)
    features = vectorizer.get_feature_names()
    return embeddings.toarray(), features

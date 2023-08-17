#!/usr/bin/env python3
"""N-gram BLEU score"""
import numpy as np


def ngram_bleu(references, sentence, n):
    """
    Calculate the n-gram BLEU score for a sentence
    :param references: list of reference translations
    :param sentence: list containing the model proposed sentence
    :param n: size of the n-gram to use for evaluation
    :return: the n-gram BLEU score
    """
    def get_ngrams(text, n):
        """
        Get ngrams for text
        :param text: list of tokens
        :param n: size of the n-gram
        :return: dictionary of ngrams and their counts
        """
        ngrams = {}
        for i in range(len(text)-n+1):
            ngram = tuple(text[i:i+n])
            if ngram in ngrams:
                ngrams[ngram] += 1
            else:
                ngrams[ngram] = 1
        return ngrams
    # Calculate clipped precision for each reference
    clipped_precision = []
    candidate_ngrams = get_ngrams(sentence, n)
    for reference in references:
        reference_ngrams = get_ngrams(reference, n)
        clipped_count = 0
        for ngram in candidate_ngrams:
            if ngram in reference_ngrams:
                clipped_count += min(candidate_ngrams[ngram], reference_ngrams[ngram])
        clipped_precision.append(clipped_count)
    # Calculate precision
    precision = max(clipped_precision) / sum(candidate_ngrams.values())
    return precision

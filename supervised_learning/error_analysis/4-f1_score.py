def f1_score(confusion):
    p = precision(confusion)
    r = sensitivity(confusion)
    f1 = 2 * r * p / (r + p)
    return f1

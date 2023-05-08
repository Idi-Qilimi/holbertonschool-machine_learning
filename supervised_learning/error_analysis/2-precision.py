def precision(confusion):
    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    precision = tp / (tp + fp) 
    return precision

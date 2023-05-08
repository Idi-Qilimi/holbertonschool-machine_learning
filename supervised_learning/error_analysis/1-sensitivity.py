def sensitivity(confusion):
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1) - tp
    tpr = tp / (tp + fn) 
    return tpr

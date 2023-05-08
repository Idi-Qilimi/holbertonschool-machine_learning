def specificity(confusion):
    tp = np.diag(confusion)
    fp = confusion.sum(axis=0) - tp
    fn = confusion.sum(axis=1) - tp
    tn = confusion.sum() - (fp + fn + tp)
    spec = tn / (tn + fp)
    return spec

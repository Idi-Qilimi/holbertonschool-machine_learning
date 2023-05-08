 def create_confusion_matrix(labels, logits):
        return np.matmul(labels.transpose(), logits)

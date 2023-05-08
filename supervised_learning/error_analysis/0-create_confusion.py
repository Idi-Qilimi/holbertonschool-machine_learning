 #!/usr/bin/env python3
"""confusion matrix"""


import numpy as np
"""confusion matrix"""


 def create_confusion_matrix(labels, logits):
        """confusion matrix"""
        return np.matmul(labels.transpose(), logits)

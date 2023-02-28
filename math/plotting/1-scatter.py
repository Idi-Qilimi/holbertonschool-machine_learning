#!/usr/bin/env python3
"""Scatter plot"""


import numpy as np
"""Scatter plot"""


import matplotlib.pyplot as plt
"""Scatter plot"""


mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.scatter(x, y, c='m')
plt.title("Men's Height vs Weight")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")

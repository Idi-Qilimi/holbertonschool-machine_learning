#!/usr/bin/env python3
"""Stack Bar Chart"""


import numpy as np
"""Stack Bar Chart"""


import matplotlib.pyplot as plt
"""Stack Bar Chart"""


np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
y1 = np.array([4, 15, 16])
y2 = np.array([5, 15, 8])
y3 = np.array([8, 4, 7])
y4 = np.array([16, 15, 7])


categories = ['Farrah', 'Fred', 'Felicia']


plt.bar(categories, y1, width=0.5, color='r')
plt.bar(categories, y2, width=0.5, bottom=y1, color='yellow')
plt.bar(categories, y3, width=0.5, bottom=y1+y2, color='#ff8000')
plt.bar(categories, y4, width=0.5, bottom=y1+y2+y3, color='#ffe5b4')
plt.ylim(0, 80)
plt.legend(["apples", "bananas", "oranges", "peaches"])

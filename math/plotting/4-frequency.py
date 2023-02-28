#!/usr/bin/env python3
"""Histogram plot"""


import numpy as np
"""Histogram plot"""


import matplotlib.pyplot as plt
"""Histogram plot"""


np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.hist(student_grades, bins=10, edgecolor='black')
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xlabel("Grades")
plt.ylabel("Number of students")
plt.title("Project A")

#!/usr/bin/env python3
"""All in One"""


import numpy as np
"""All in One"""


import matplotlib.pyplot as plt
"""All in One"""


y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure()
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[2, :])

fig.suptitle("All in One")
ax1.plot(y, 'r')

ax3.plot(x2, y2)
ax3.set_title("Exponential Decay of C-14")
ax3.set_xlabel("Time(years)")
ax3.set_ylabel("Fraction Remaining")
ax3.set_xlim(0, 28500)
ax3.set_yscale("log")

ax2.scatter(x1, y1, c='m')
ax2.set_title("Men's Height vs Weight")
ax2.set_xlabel("Height(in)")
ax2.set_ylabel("Weight(lbs)")

ax4.plot(x3, y31, 'r--')
ax4.plot(x3, y32, 'g')
ax4.set_title("Exponential Decay of Radioactive Elements", fontsize=9)
ax4.set_xlabel("Time(years)")
ax4.set_ylabel("Fraction Remaining", fontsize=7)
ax4.legend(["C-14", "Ra-226"], fontsize=7)

ax5.hist(student_grades, bins=10, edgecolor='black')
ax5.set_title("Project A")
ax5.set_xlabel("Grades")
ax5.set_ylabel("Number of Students", fontsize=9)
ax5.set_ylim(0, 30)
ax5.set_xlim(0, 100)

plt.tight_layout()

# 1) Combining a one and a two-dimensional NumPy Array

import numpy as np

a = np.array([1, 2, 3])  # 1-D array

b = np.array([           # 2-D array
    [4, 5, 6],
    [7, 8, 9]
])

c = np.concatenate(([a], b), axis=0)
print(c)

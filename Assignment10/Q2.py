#  2) Flatten a 2d numpy array into 1d array 

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = a.flatten()     # flatten function is used to convert 2-D array into 1-D array
print(b)
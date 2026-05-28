# 4) Replace negative value with zero in numpy array using replace

import numpy as np

arr = np.array([1, -2, 3, -4, 5, -6])
print(arr)

arr[arr < 0] = 0        # here negative values replace with 0

print("\nArray after replacing negative values:")
print(arr)
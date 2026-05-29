#  6) Study the following program import numpy as np
# create a numpy 1d-arrays arr1 = np.array([3, 4]) arr2 = np.array([1, 0])
# find average of NumPy arrays avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg)
#  -> Calculate average mean median mode values of two NumPy 2d-arrays

import numpy as np
from statistics import mode

# for 2-D array
a = np.array([
    [10, 20],
    [30, 40]
])

b = np.array([
    [50, 60],
    [70, 80]
])

avg = (a + b) / 2
print("\nAverage od 2-D array:\n", avg)

print("\nMean:", np.mean(avg))
print('\nMedian:', np.median(avg))
print("\nMode:", mode(avg.flatten()))

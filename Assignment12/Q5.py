# 5) Study the following program import numpy as np 
# create a numpy 1d-arrays arr1 = np.array([3, 4]) arr2 = np.array([1, 0])
# find average of NumPy arrays avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg) 
# -> Calculate average mean median mode values of two NumPy 2d-arrays

# 2-D arrays

import numpy as np
from statistics import mode

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print('\nAverage of arrays:')
avg = (a + b)/2
print(avg)

print('\nMean:')
mean = np.mean(avg)
print(mean)

print('\nMedian:')
median = np.median(avg)
print(median)

print('\nMode:')
m = mode(avg.flatten())
print(m)
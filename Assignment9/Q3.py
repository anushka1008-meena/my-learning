# 3) Replace NaN values with average of columns 

import numpy as np

arr = np.array([
    [1, 2, np.nan],
    [4, np.nan, 6],
    [7, 8, 9]
])

print("Original Array:")
print(arr)

col_mean = np.nanmean(arr, axis=0)            # average of columns


replace = np.where(np.isnan(arr))             # here we replace NaN values with columns mean
arr[replace] = np.take(col_mean, replace[1])

print("\nArray after replacing NaN values:")
print(arr)
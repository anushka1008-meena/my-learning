#1) Replace Nan with 0 and Interchange rows and columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] 

import numpy as np

arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

arr = np.nan_to_num(arr, nan=0)        # here nan replace with 0

print("Array after replacing NaN:")
print(arr)

# now interchange rows and columns
arr2 = arr.T                          # arr.T means it transpose the rows into columns

print("\nAfter interchanging rows and columns:")
print(arr2)


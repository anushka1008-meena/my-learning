# 1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] 

import numpy as np

a = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])
print(a)

print('\nAfter replacing nan values with 0')
b = np.nan_to_num(a , nan = 0)     # it replaces nan values with zero
print(b)

print('\n Interchange rows & columns')
res = np.transpose(a)
print(res)


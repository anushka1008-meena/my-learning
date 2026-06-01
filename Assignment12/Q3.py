#  3) Replace NaN values with average of columns 

import numpy as np

a = np.array([
    [1, np.nan, 3],
    [4, 5, np.nan],
    [7, 8, 9]
])

avg = np.nanmean(a, axis=0)     # axis = 0 calculates average of columns

inds = np.where(np.isnan(a))
a[inds] = avg[inds[1]]

print(a)
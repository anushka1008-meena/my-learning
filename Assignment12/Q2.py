# 2) Move axes of 3D array to new positions

import numpy as np

a = np.arange(24).reshape(2,3,4)
print(a)

res = np.moveaxis(a, 0, 1)
print()
print(res.shape)      # it is used to check weather axes moved correctly or not
print()
print(res)
# 4) Replace negative value with zero in numpy array using replace 

import numpy as np

a = np.array([1,2,-3,-4,5])

np.place(a, a<0, 0)    # numpy does not have a function replace() so we use np.place() function here
print(a)
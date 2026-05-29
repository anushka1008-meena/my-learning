#  5) Iterate 3D array using for loop and nditer

import numpy as np

a = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Using for loop:")
for i in a:
    for j in i:
        for k in j:
            print(k)



print("\nUsing nditer:")
for i in np.nditer(a):    # nditer = automatically iterate on each element of 
    print(i)
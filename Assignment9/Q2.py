# 2) Move axes of 3D array to new positions 

import numpy as np

# 3D array
arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print("Original array:\n")
print(arr)

arr2 = np.moveaxis(arr, 0, 2)         # move axes

print("\nArray after moving axes:")  
print(arr2)

print(''' \nExplanation
    original array = [1,2],[3,4]
                     [5,6],[7,8]
    so we move axes 0 to 2  -> so corresponding elements are grouped together 
    i.e = (1 is written with 5),(2 with 6) , (3 with 7) , (4 with 8)
''')
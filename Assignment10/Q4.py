# 4) Practice operations like Get the maximum value from given array Get the minimum value from given array 
# Find the number of rows and columns of a given array 
# using NumPy Select the elements from a given array (each element and specific element)
# Find the sum of values in a 2D array using for loop Adding, Subtracting, multiplying, dividing arrays in Numpy

import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60]
])

# (i) Practice operations like Get the maximum value from given array Get the minimum value from given array
print('\nmaximum value from array is:')
print(a.max())

print('\nminimum value from array is:')
print(a.min())
 

# (ii) Find the number of rows and columns of a given array 
rows = a.shape[0]
column = a.shape[1]
print('\nRows:', rows)
print('Columns:', column)


# (iii) using NumPy Select the elements from a given array (each element and specific element)
print()
print(a[0][1])     # 0 = row no.  &   1 = 1st index element of 0th row
print(a[1])        # it prints complete row


# (iv) Find the sum of values in a 2D array using for loop

sum = 0

for i in a:
    for j in i:
        sum = sum + j

print("\nSum is:", sum)


# Adding, Subtracting, multiplying, dividing arrays in Numpy
print('\naddition:')
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)

print('\nsubtraction:')
print(x - y)

print('\nmultiplication:')
print(x * y)

print('\ndivision:')
print(y / x)


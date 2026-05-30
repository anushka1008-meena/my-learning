# 1) Create numpy array and perform following operation :


#  > Convert 1D array to 2D 
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)

print(b)





# > Print Array Attributes(Like shape, dimenssion, data type, itemsize)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print()
print("Shape =", arr.shape)
print("Dimension =", arr.ndim)     # it shows dimension 1-D/2-D
print("Data type =", arr.dtype)    # it showa data type
print("Item size =", arr.itemsize)




#  > Create a 3×3 NumPy array of all 9 
print()
arr = np.full((3, 3), 9)
print(arr)



# > Create a 1D array of 10 evenly spaced values between 25 and 125 
arr = np.linspace(25, 125, 10)
print()
print(arr)





# > Convert a Python list into a NumPy array
l1 = [10,20,30,40,50]
arr = np.array(l1)

print()
print(arr)




#  > Reverse a 1D NumPy array 
arr = np.array([1,2,3,4,5])
res = arr[::-1]

print()
print(res)




# > Create a 4×4×3 array and extract value at its second set, first row and last column
print()
arr = np.arange(48).reshape(4, 4, 3)
print(arr)

print("\nRequired value =", arr[1, 0, 2])     # arr[set, row, column]






#  > Create a 4×4 and Extract Odd Rows and Even Columns 
arr = np.arange(1, 17).reshape(4, 4)
print(arr)

print()
print("\nOdd rows and even columns:")
print(arr[::2, 1::2])




# > Slice the first two rows and first two columns of econd set from a 4×4×3 array
arr = np.arange(48).reshape(4, 4, 3)
res = arr[1, :2, :2]

print()
print(res) 
 



# > Replace all odd numbers in a NumPy array with -1 by itterating using for loop [[23, 56, 78, 93], [71, 82,13, 24]]
arr = np.array([
    [23, 56, 78, 93],
    [71, 82, 13, 24]
])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i][j] % 2 != 0:
            arr[i][j] = -1

print()
print(arr) 
 




# > Get the indices of non-zero elements in an array [1, 0, 2, 0, 3, 0, 4] 
arr = np.array([1,0,2,0,3,0,4])

print()
index = np.nonzero(arr)
print(index)






# > Perform arithmetic operations on two NumPy arrays element-wise Add two NumPy arrays element by element. Multiply two NumPy arrays element by element.
arr1 = np.array([5,6,7,8])
arr2 = np.array([1,2,3,4])

a = arr1 + arr2
b = arr1 * arr2

print()
print("Addition =", a)
print("Multiplication =", b)





#  > Write a code to compute the dot product of two NumPy arrays arr1 = [15, 20, 25] arr2 = [10,40,37]
a = np.array([15, 20, 25])
b = np.array([10, 40, 37])

dot = np.dot(a,b)

print()
print("Dot product =", dot)
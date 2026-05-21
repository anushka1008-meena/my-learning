# Write a Python function to multiply all the numbers in a list.

def l1(value):
    result = 1

    for i in value:
        result = result * i
    
    print('Multiplication of numbers in list is:',result)

l1([1,2,3])
  
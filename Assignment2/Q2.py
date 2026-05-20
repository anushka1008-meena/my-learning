# function to perform basic math operations

a = int(input('enter a:'))
b = int(input('enter b:'))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print('Addition =',add(a,b))
print('subtraction =',subtract(a,b))
print('multiplication =',multiply(a,b))
print('division =',divide(a,b))

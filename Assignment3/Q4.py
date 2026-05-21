# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if n<0:
        print('Negative integer not allowed')
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
        print('Factorial is:',fact)

factorial(4)



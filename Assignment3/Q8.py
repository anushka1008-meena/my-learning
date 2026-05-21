# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def prime(n):        
    for i in range(2,n):
        if(n%i) == 0:
            print('Not a prime no')
            break

    else:
        print('It is a prime no')

prime(7)
# Write a Python function to Print Even Numbers from a Given List

def even(num):
    for i in num:
        if(i%2 == 0):
            print(i)

print('Even numbers from list are:')
    
even([1,2,3,4])
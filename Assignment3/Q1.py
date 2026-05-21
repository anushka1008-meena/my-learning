# Write a Python function to find the maximum of three numbers.

def info(a,b,c):
    num = [a,b,c]
    max = num[0]

    for i in num:
        if(i > max):
            max = i

    print('Maximun no. is:',max)

info(2,7,4)
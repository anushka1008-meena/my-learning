# Write a Python function that accepts a string and counts the number of upper and lower case letters. 

def str(name):
    upper = 0
    lower = 0

    for i in name:
        if(i.isupper()):
            upper += 1

        elif(i.islower()):         # bcoz we need to check codition.....that's why we use elif here indteaf of else
            lower += 1

    print('upper case letters are:',upper)
    print('lower case letters are:',lower)

str('AnusHKA')
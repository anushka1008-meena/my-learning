# Practise reading, writting, appending data in a file

# write file
f = open('new.txt','w')

f.write('Hello Python\n')
f.write('Today is thursday')
f.close()

#-------------------------------------------------------
# read file
f = open('new.txt','r')

data = f.read()
print(data)
f.close()

print()        # it is used for giving space to see the o/p properly
print()
print()

# read file using readline
f = open('new.txt','r')

print(f.readline())        # gives extra spacing b/w output
print(f.readline())
f.close()


# read file using readlines
f = open('new.txt','r')

data = f.readlines()    #it makes the line in the form of list
print(data)
f.close()

# -------------------------------------------------

# append file
f = open('new.txt','a')

f.write('\n\nThis line is added in file')
f.close()
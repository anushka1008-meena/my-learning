
l = []
while(True):
    print('''
        1. Add element
        2. Remove element
        3. Display first 3 elements
        4. Display last 3 elements
        5. Print
        6. Exit ''')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        e = input('Enter an element to add:')
        l.append(e)   # bcoz FIFO that's why we use append

    elif ch == 2:
        if len(l) == 0:
            print('List is empty')
        else:
            l.pop(0)

    elif ch == 3:
        print(l[:3])

    elif ch == 4:
        print(l[-4:])

    elif ch == 5:
        print(l)

    elif ch == 6:
        break
    
    else:
        print('Invalid choice')
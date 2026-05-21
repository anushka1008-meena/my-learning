# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def l1(values):
    l2 = []

    for i in values:
        if i not in l2:      # if element of l1 are not present in l2 -> then we append the element
            l2.append(i)
    return l2

print(l1([1,2,3,4,3,4,7,8,2]))
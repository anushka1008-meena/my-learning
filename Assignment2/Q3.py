# check palindrome no.

n = int(input("Enter a no.: "))

num = n 
rev = 0

# reverse 
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

# comparision b/w original & reverse no.
if num == rev:
    print("palindrome number")
else:
    print("Not a palindrome number")
# Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.

import csv

data = [
       ['name','address','mobile','email']
]

# now we insert 2-3 data entered by user
for i in range(3):
    name    = input('enter name: ')
    address = input('enter address: ')
    mobile  = input('enter mobile: ')
    email   = input('enter email: ')

    data.append([name,address,mobile,email])


# now we write into csv file
with open('address_book.csv','w',newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)

print('Data inserted successfully!!')  # data added into address_csv file
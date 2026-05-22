# Practice DATABASE  
# 1) Create Database
# 2) Create 2-3 tables
# 3) Insert some records
# 4) Perform diffrent select operations
# 5) Update some data
# 6) Delete some data

# Practice DATABASE
# 1) Create Database
# 2) Create 3 tables
# 3) Insert records
# 4) Select operations
# 5) Update data
# 6) Delete data

import sqlite3

# 1) create database
conn = sqlite3.connect('new.db')

# -------------------------------------------
# 2) create student table

# conn.execute('''
# create table if not exists students(
#     s_id integer primary key autoincrement,
#     s_name varchar(20),
#     s_field varchar(20)
# )
# ''')

# create course table

# conn.execute('''
# create table if not exists courses(
#     c_id integer primary key autoincrement,
#     c_name varchar(20)
# )
# ''')

# create marks table

# conn.execute('''
# create table if not exists marks(
#     m_id integer primary key autoincrement,
#     s_id integer,
#     c_id integer,
#     marks integer
# )
# ''')
# print("Tables created successfully")

# -----------------------------------------------------------
# 3) insert records

# conn.execute("insert into students(s_name,s_field) values('anushka','B.tech')")

# conn.execute("insert into students(s_name,s_field) values('disha','Bsc')")

# conn.execute("insert into courses(c_name) values('Python')")

# conn.execute("insert into courses(c_name) values('Java')")

# conn.execute("insert into marks(s_id,c_id,marks) values(1,1,90)")

# conn.execute("insert into marks(s_id,c_id,marks) values(2,2,85)")

# conn.commit()

# print("Records inserted successfully")

# -----------------------------------------
# 4) select operations

# print("\nStudents Table")

# res = conn.execute("select * from students")

# for row in res:
#     print(row)

# print("\nCourses Table")

# res = conn.execute("select * from courses")

# for row in res:
#     print(row)

# print("\nMarks Table")

# res = conn.execute("select * from marks")

# for row in res:
#     print(row)

#  ---------------------------------------------------
# 5) update data

# conn.execute("update students set s_field='M.tech' where s_id=1")

# conn.commit()

# print("\nData updated successfully")

# res = conn.execute("select * from students")
# for row in res:
#     print(row)

# ---------------------------------------------------
# 6) delete data

conn.execute("delete from students where s_id=2")

conn.commit()

print("\nData deleted successfully")

res = conn.execute("select * from students")

for row in res:
    print(row)

conn.close()
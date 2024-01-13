import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to inset record,create table

cursor = connection.cursor()

## create the table
table_info="""
create table Student(
    Name varchar(50),
    Class varchar(25),
    Section varchar(25),
    Mark int
    );
"""
cursor.execute(table_info)

## insert some records

cursor.execute('''insert into Student values('Test1','DS','A',99)''')
cursor.execute('''insert into Student values('Test2','DS','B',95)''')
cursor.execute('''insert into Student values('Test3','DS','C',90)''')
cursor.execute('''insert into Student values('Test4','DO','A',80)''')
cursor.execute('''insert into Student values('Test5','DO','B',85)''')

## Display all the records

print("The inserted records are")
data = cursor.execute('''Select * from Student''')
for row in data:
    print(row)
connection.commit()
connection.close()
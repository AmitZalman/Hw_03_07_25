
import os
if os.path.exists('students.db'):
    os.remove('students.db')

import sqlite3
conn = sqlite3.connect('students.db')  # מתחבר (או יוצר אם לא קיים) קובץ DB בשם students.db
conn.row_factory = sqlite3.Row         # מגדיר שהתוצאות של fetch יחזירו sqlite3.Row
cursor = conn.cursor()                 # יוצר cursor כדי להריץ פקודות SQL

cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENTS (
    ID INTEGER PRIMARY KEY ,
    NAME TEXT NOT NULL , 
    GRADE INTEGER NOT NULL , 
    BIRTHYEAR INTEGER);
''')

data = [
  (1, 'Noa', 85, 2010),
  (2, 'Lior', 90, 2011),
  (3, 'Dana', 78, 2009)
]



cursor.executemany('''
    INSERT INTO STUDENTS (ID , NAME , GRADE, BIRTHYEAR) 
    VALUES (?, ?, ?, ?);
    ''', data)

#Ex 5 update dana's grade to 88

Change = [88 ,'Dana']
cursor.execute('''
    UPDATE STUDENTS SET GRADE = ? WHERE Name = (?)
     ''',Change)

#Ex 6 Delete student ID 2 From Students
cursor.execute('''
DELETE FROM STUDENTS WHERE ID = 2;''')


#Ex 7 Print all Students
cursor.execute('''SELECT * FROM STUDENTS;''')
students = cursor.fetchall()
for student in students:
    print(dict(student))

#Ex 8 Input from User

while True:
    try:
        ID = int(input("please enter the Id: "))
        NAME = input("please enter Student Name: ")
        GRADE = float(input("please enter the student Grade: "))
        BIRTHYEAR = int(input("Please enter the Students Birthyear: "))
    except ValueError:
        print("please enter the corrct Value!!! ")
        continue


    data = [(ID , NAME , GRADE, BIRTHYEAR)]
    try:
        cursor.executemany('''
        INSERT INTO STUDENTS (ID , NAME , GRADE , BIRTHYEAR)
        VALUES (? , ? , ? , ?);
        ''',data)

    except  sqlite3.IntegrityError as E:
        print(f"Invalid value: {E}. Please insert another one!")
        continue

    choice = input("To enter another student press  Enter, to quit press (q): ").lower().strip()
    if choice == 'q':
        break






conn.commit()
conn.close()
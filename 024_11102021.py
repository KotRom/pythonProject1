#pip install mysql-connector-pyton

#c:\users\37255\appdata\local\programs\python\python39new\python.exe -m pip install --upgrade pip

import mysql.connector
import  pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='test_db',
)
mycursor = mydb.cursor()
mycursor.execute(f'SELECT * FROM students')
for student in mycursor:
    print(student)

#mycursor.execute("CREATE TABLE student (name VARCHAR(255), age INT(10))")

#sqlFormula = "INSERT INTO students (name, age) VALUES ('Roman', '33')"
#mycursor.execute(sqlFormula)
#mydb.commit()

#mycursor.execute('CREATE DATABASE test_db')
#mycursor.execute('SHOW DATABASES')
#for db in mycursor:
#    print(db)


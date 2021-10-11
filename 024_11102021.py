#pip install mysql-connector-pyton

#c:\users\37255\appdata\local\programs\python\python39new\python.exe -m pip install --upgrade pip

import mysql_connector
mydb = mysql_connector.connect(
    host='localhost',
    user='root',
    password='1234'
)

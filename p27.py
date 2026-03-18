import mysql.connector

a = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

mycursor = a.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

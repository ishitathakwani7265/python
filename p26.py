import mysql.connecter

mydb = mysql.connecter.connect(
    host="localhost",
    user="root",
    password="",
    database="collage"
)

a=mydb.cursor()

a.execute("CREATE TABLE customers (name VARCHAR(255),ADDRESS VARCHAR(255)")

if a:
    print("table created")

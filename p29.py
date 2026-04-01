import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="college"
)

mycursor = mydb.cursor()

sql = "SELECT name, address FROM customers"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

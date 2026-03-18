import mysql.connecter

mydb = mysql.connecter.connect(
    host="localhost",
    user="root",
    password=""
)

a=mydb.cursor()

#a.execute("create database collage")
    
a.execute("SHOW DATNABASE")

for x in a:
    print(x)

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Hellog@1994'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE  elderco")
print("All Done!")
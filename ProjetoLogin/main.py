import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "usuarios"
)
print(banco)


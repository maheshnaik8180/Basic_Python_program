import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin"
)
print(db_connection)
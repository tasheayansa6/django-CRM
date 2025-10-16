import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password123',
)
print("ALL Done!!")

connection.close()

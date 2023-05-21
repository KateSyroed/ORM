import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='danilova1988',
    host='127.0.0.1',
    port='5432',
    database='MyDB'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM orders;")

result = cursor.fetchall()
# print(result)

for user in result:
    print(user)

cursor.close()
connection.close()
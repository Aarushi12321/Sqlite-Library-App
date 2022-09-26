import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers ORDER BY first_name ASC")
items = c.fetchall()

for item in items:
	print(item)

conn.commit()
conn.close()
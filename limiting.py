import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers ORDER BY first_name ASC LIMIT 4")
items = c.fetchall()

for item in items:
	print(item)

print("Data has been successfully limited and fetched.")
conn.commit()
conn.close()
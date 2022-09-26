import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# c.execute("SELECT , * FROM customers")
# here rowid is primary key
#c.execute("SELECT rowid, * FROM customers WHERE last_name='Doe'")
c.execute("""
			SELECT rowid, * 
			FROM customers 
			WHERE email LIKE '%@hogwards.com'
			OR first_name LIKE 'M%'
			""")

#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()
for item in items:
	print(item)

print("Data from the table has been fetched successfully.")

conn.commit()
conn.close()
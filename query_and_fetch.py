import sqlite3


# c.execute("SELECT , * FROM customers")
# here rowid is primary key

def show_all(fetch_many=None):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("SELECT rowid, * FROM customers")

	if fetch_many is not None:
		items = c.fetchmany(fetch_many)
	else:
		items = c.fetchall()

	for item in items:
		print(item)

	print("Data from the table has been fetched successfully.")
	conn.commit()
	conn.close()
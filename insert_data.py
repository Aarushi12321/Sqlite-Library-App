import sqlite3

def insert_one(first_name, last_name, phone_number, email):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("""
		INSERT INTO customers VALUES (?,?,?,?)
		""", (first_name, last_name, phone_number, email))

	print(first_name, last_name, phone_number, email, 'added to the table: customers.')

	conn.commit()
	conn.close()

	return
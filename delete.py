import sqlite3

def delete_one(row_id):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("DELETE FROM customers WHERE rowid="+str(row_id))

	print("Required from the table has been deleted successfully.")

	conn.commit()
	conn.close()

	return
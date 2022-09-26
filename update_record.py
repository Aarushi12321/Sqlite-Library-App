import sqlite3

def update_record(new_field,new_value, old_field, old_value):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("UPDATE customers SET "+new_field+" = "+new_value+" WHERE "+old_field+" = "+old_value)

	print("Data from the table has been updated successfully.")

	conn.commit()
	conn.close()

	return
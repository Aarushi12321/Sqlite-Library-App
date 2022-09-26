import sqlite3

# create a connection and pass the name of the database that you want to connect to
conn = sqlite3.connect('customer.db')
# Enter tehe directory on bash and then python (filename) to run this file

# create a cursor to access other things in database
c = conn.cursor()

# create a table using cursor
# multiple lines, use doc strings. Single line, use simple ""
# sqlite3 is case sensitive

# sqlite has only 5 datatypes - NULL, INTEGER, REAL, TEXT, BLOB
try:
	c.execute("""
	CREATE TABLE customers(
	first_name TEXT,
	last_name TEXT,
	phone_number INT,
	email TEXT
	)
	""")
	print('Table name: customers added to db: customer.')
except:
	print('This table already exists in the database.')
# Commit our command to the database
conn.commit()
# close our connection
conn.close()
import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

customer_list = [('Harry', 'Potter', '12002100', 'harrypotter@hogwards.com'),
				('Ron', 'Weasley', '12002101', 'ronweasley@hogwards.com'),
				('Hermoine', 'Granger', '12002102', 'hermionegranger@hogwards.com'),
				('Draco', 'Malfoy', '12002103', 'dracomalfoy@hogwards.com')]

c.executemany("""
	INSERT INTO customers VALUES (?,?,?,?)
	""", customer_list)
print('Multiple values added to customer table.')

conn.commit()
conn.close()
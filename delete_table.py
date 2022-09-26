import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("DROP TABLE customers")

print("Table has been successfully deleted.")
conn.commit()
conn.close()
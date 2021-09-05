import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()




for row in c.execute('SELECT * FROM stocks ORDER BY price'):
	print(row)

'''
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

c.execute('SELECT * FROM stocks ORDER BY price')
print (c.fetchall())
'''

conn.close()
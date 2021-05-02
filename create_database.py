import sqlite3

conn = sqlite3.connect('database/database.db')
cur = conn.cursor()

cur.execute('CREATE TABLE status (id integer primary key, status integer);')
cur.execute('INSERT INTO status VALUES(1,0)')

conn.commit()

conn.close()
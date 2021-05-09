import sqlite3

conn = sqlite3.connect('database/database.db')
cur = conn.cursor()

cur.execute('CREATE TABLE status (id integer primary key, status integer);')
cur.execute('INSERT INTO status VALUES(1,0)')

cur.execute('CREATE TABLE stream (id integer primary key, stream BLOB);')
cur.execute('INSERT INTO stream VALUES(1,"")')

conn.commit()

conn.close()
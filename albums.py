# https://docs.python.org/3/library/sqlite3.html
# https://youtu.be/cZTxadhqahQ?si=X3YriXeR90gtDDl7
import sqlite3

conn = sqlite3.connect('albums.db')
conn.execute("PRAGMA foreign_keys = 1")
# Create Cursor
cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists band (
    band_id INTEGER  NOT NULL PRIMARY KEY,
    name TEXT, 
    year INTEGER,
    comment TEXT
    )""")

cur.execute("""CREATE TABLE if not exists album (
	album_id INTEGER  NOT NULL PRIMARY KEY,
	name TEXT,
	band_id INTEGER,
	year INTEGER,
	FOREIGH KEY band_id REFERENCES band(band_id)
    )""")



cur.execute("INSERT INTO band VALUES (1,'The Beatles', 1957, 'UK')")
cur.execute("INSERT INTO band VALUES (2,'Metallica', 1981, 'USA')")
cur.execute("INSERT INTO band VALUES (3,'Queen', 1970, 'UK')")

cur.execute("INSERT INTO album VALUES (1,'Master of Puppets', 2, 1986,2)")
cur.execute("INSERT INTO album VALUES (2,'The Black Album', 2, 1991,2)")
cur.execute("INSERT INTO album VALUES (3,'Ride the Lightning', 2, 1984,2)")
cur.execute("INSERT INTO album VALUES (4, 'A Night at the Opera', 3, 1975,3 )")
cur.execute("INSERT INTO album VALUES (5, 'News of the World', 3, 1976,3 )")

conn.commit()
cur.close()
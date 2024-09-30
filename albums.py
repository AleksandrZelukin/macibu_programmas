import sqlite3

conn = sqlite3.connect("albums.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists band (
            band_id INTEGER NOT NULL PRIMARY KEY,
            nosaukums TEXT)""")

cur.execute("""CREATE TABLE if not exists albums (
            albums_id INTEGER,
            nosaukums TEXT,
            band_id)""")
band_id = int(input("band ID: "))
nosaukums = input("Nosaukums: ")
band = [band_id, nosaukums]
cur.execute("INSERT INTO band VALUES(?,?)",band)

#cur.execute("INSERT INTO band VALUES(1,'The Beatles')")
#cur.execute("INSERT INTO band VALUES(2,'Pink Floyd')")
#cur.execute("INSERT INTO band VALUES(3,'Deep Purple')")

#cur.execute("INSERT INTO albums VALUES(1,'Sgt. Peppers Lonely Hearts Club Band',1)")
#cur.execute("INSERT INTO albums VALUES(2,'Yellow Submarine',1)")
#cur.execute("INSERT INTO albums VALUES(3,'Revolver',1)")
#cur.execute("INSERT INTO albums VALUES(4,'The Wall',2)")

conn.commit()
cur.close()

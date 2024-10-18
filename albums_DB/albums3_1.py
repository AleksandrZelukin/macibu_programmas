import sqlite3
from albums3_1_saraksts import grupas

conn = sqlite3.connect("albums3_1.db")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS band")
cur.execute("DROP TABLE IF EXISTS albums")

conn.execute("PRAGMA foreign_keys = 1")

cur.execute("""CREATE TABLE if not exists band (
            band_id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_nosaukums TEXT)""")

cur.execute("""CREATE TABLE if not exists albums (
            albums_id INTEGER PRIMARY KEY AUTOINCREMENT,
            album_nosaukums TEXT,
            band_id INTEGER,
            FOREIGN KEY (band_id) REFERENCES band(band_id))""")

cur.executemany("INSERT INTO band VALUES (?,?)",(grupas))

conn.commit()

# cur.execute("INSERT INTO band (band_nosaukums) VALUES('The Beatles')")
# cur.execute("INSERT INTO band (band_nosaukums) VALUES('Pink Floyd')")
# cur.execute("INSERT INTO band (band_nosaukums) VALUES('Deep Purple')")

# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Sgt. Peppers Lonely Hearts Club Band',1)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Yellow Submarine',1)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Revolver',1)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('The Wall',2)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Machine Head',3)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Perfect Strangers',3)")
# cur.execute("INSERT INTO albums (album_nosaukums, band_id) VALUES('Wish You Were Here',2)")

cur.execute('SELECT band_nosaukums FROM band')
all_band = cur.fetchall()
print("Gruppas")
for band in all_band:
  print(band)

cur.execute('SELECT album_nosaukums FROM albums')
all_albums = cur.fetchall()
print("Albums")
for albums in all_albums:
  print(albums)

print("visi kopa")
cur.execute("""SELECT band.band_nosaukums, albums.album_nosaukums 
            FROM band, albums 
            WHERE band.band_id = albums.band_id """)
kopa = cur.fetchall()
for visi_kopa in kopa:
  print(visi_kopa)

conn.commit()
cur.close()

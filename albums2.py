import sqlite3

conn = sqlite3.connect("albums2.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists band (
            band_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT)""")

cur.execute("""CREATE TABLE if not exists albums (
            albums_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT,
            band_id,
            FOREIGN KEY (band_id) REFERENCES band(band_id))""")

cur.execute("INSERT INTO band (nosaukums) VALUES('The Beatles')")
cur.execute("INSERT INTO band (nosaukums) VALUES('Pink Floyd')")
cur.execute("INSERT INTO band (nosaukums) VALUES('Deep Purple')")

cur.execute("INSERT INTO albums (nosaukums, band_id) VALUES('Sgt. Peppers Lonely Hearts Club Band',1)")
cur.execute("INSERT INTO albums (nosaukums, band_id) VALUES('Yellow Submarine',1)")
cur.execute("INSERT INTO albums (nosaukums, band_id) VALUES('Revolver',1)")
cur.execute("INSERT INTO albums (nosaukums, band_id) VALUES('The Wall',2)")


cur.execute('SELECT * FROM band')
all_band = cur.fetchall()
print("Gruppas")
for band in all_band:
  print(band)

cur.execute('SELECT * FROM albums')
all_albums = cur.fetchall()
print("Albums")
for albums in all_albums:
  print(albums)
cur.execute("SELECT * FROM band JOIN albums ON albums.band_id = band.band_id ")
conn.commit()
cur.close()

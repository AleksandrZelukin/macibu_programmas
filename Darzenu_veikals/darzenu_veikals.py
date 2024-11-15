import sqlite3

conn = sqlite3.connect("darzenu_veikals.db")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS band")
cur.execute("DROP TABLE IF EXISTS albums")

conn.execute("PRAGMA foreign_keys = 1")

cur.execute("""CREATE TABLE if not exists pirceji (
            pircejs_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pirceja_vards TEXT,
            pirceja_talrunis TEXT,
            pirceja_epasts TEXT)""")

cur.execute("""CREATE TABLE if not exists preces (
            preces_id INTEGER PRIMARY KEY AUTOINCREMENT,
            preces_nosaukums TEXT,
            preces_vienibas TEXT,
            preces_cena REAL
            )""")

cur.execute("""CREATE TABLE if not exists pirkumi (
            pirkuma_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pirkuma_pircejs INTEGER,
            pirkuma_nosaukums INTEGER,
            pirkuma_daudzums REAL,
            FOREIGN KEY (pirkuma_pircejs) REFERENCES pirceji(pircejs_id),
            FOREIGN KEY (pirkuma_nosaukums) REFERENCES preces(preces_id)
            )""")


conn.commit()

# cur.execute("INSERT INTO pirceji (pirceja_vards, pirceja_talrunis, pirceja_epasts) VALUES('Valdis','23782489','valdis@pasts.lv')")
# cur.execute("INSERT INTO preces (preces_nosaukums, preces_vienibas, preces_nosaukums) VALUES('Krējums', 'kg.', 6.8)")
# cur.execute("INSERT INTO pirkumi (pirkuma_pircejs, pirkuma_nosaukums, pirkuma_daudzums) VALUES(1,1,2)")



# cur.execute('SELECT band_nosaukums FROM band')
# all_band = cur.fetchall()
# print("Gruppas")
# for band in all_band:
#   print(band)

# cur.execute('SELECT album_nosaukums FROM albums')
# all_albums = cur.fetchall()
# print("Albums")
# for albums in all_albums:
#   print(albums)

# print("visi kopa")
# cur.execute("""SELECT band.band_nosaukums, albums.album_nosaukums 
#             FROM band, albums 
#             WHERE band.band_id = albums.band_id """)
# kopa = cur.fetchall()
# for visi_kopa in kopa:
#   print(visi_kopa)

conn.commit()
cur.close()

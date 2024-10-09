import sqlite3

conn = sqlite3.connect("autoserviss.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE if not exists klients(
    klients_id INTEGER PRIMARY KEY,
    vards TEXT,
    uzvards TEXT,
    talrunis TEXT)""")

cur.execute("""CREATE TABLE if not exists auto(
    auto_id TEXT PRIMARY KEY,
    marka TEXT,
    modelis TEXT,
    klients_id INTEGER,
    FOREIGN KEY (klients_id) REFERENCES klients(klients_id))""")

cur.execute("""CREATE TABLE if not exists serviss(
    serviss_id INTEGER PRIMARY KEY,
    oil TEXT,
    riepas TEXT,
    bremzes TEXT,
    auto_id INTEGER,
    FOREIGN KEY (auto_id) REFERENCES auto(auto_id))""")

cur.execute("INSERT INTO klients VALUES(2,'Aigars','Ozols','12124567')")
cur.execute("INSERT INTO auto VALUES('GD1234','BMW','740D',2)")
cur.execute("INSERT INTO serviss VALUES(1,'YES','NO','NO','GD1234')")

conn.commit()
cur.close()
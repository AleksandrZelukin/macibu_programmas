import sqlite3

db= sqlite3.connect('noma.db')

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS nomnieks (
    id_nomnieks INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    talrunis TEXT
 )""")

cur.execute("""CREATE TABLE IF NOT EXISTS instrumenti (
    id_instruments INTEGER PRIMARY KEY AUTOINCREMENT,
    instruments TEXT NOT NULL,
    data TEXT NOT NULL,
    cena INTEGER
 )""")


cur.execute("""CREATE TABLE IF NOT EXISTS noma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_nomnieks INTEGER NOT NULL,
    id_instruments INTEGER NOT NULL,
    FOREIGN KEY("id_instruments") REFERENCES "Instrumenti"("id_instruments"),
    FOREIGN KEY("id_nomnieks") REFERENCES "Nomnieks"("id_nomnieks")
 )""")

# cur.execute("INSERT INTO nomnieks VALUES ('1','Aigars','Ozols','23234556')")
# cur.execute("INSERT INTO nomnieks VALUES ('2','Olga','Piraga','23234556')")
# cur.execute("INSERT INTO nomnieks VALUES ('3','Velta','Pludmale','23234556')")
# cur.execute("INSERT INTO nomnieks VALUES ('4','Selga','Valnere','23234556')")
cur.execute("INSERT INTO nomnieks VALUES ('Selga','Valnere','23234556')")

# cur.execute("INSERT INTO instrumenti VALUES ('1','Urbis','02.12.2022',25)")
# cur.execute("INSERT INTO instrumenti VALUES ('2','Urbis','14.12.2022',30)")
# cur.execute("INSERT INTO instrumenti VALUES ('3','Knaibles','02.12.2022',12)")

# cur.execute("INSERT INTO noma VALUES('1','1','3')")
# cur.execute("INSERT INTO noma VALUES('2','3','3')")
# cur.execute("INSERT INTO noma VALUES('3','4','3')")

# cur.execute("""SELECT * FROM noma 
#   JOIN nomnieks ON nomnieks.id_nomnieks = noma.id_nomnieks 
#   JOIN instrumenti ON instrumenti.id_instruments = noma.id_instruments""")

cur.execute("""SELECT vards, uzvards, instruments FROM noma 
  JOIN nomnieks ON nomnieks.id_nomnieks = noma.id_nomnieks 
  JOIN instrumenti ON instrumenti.id_instruments = noma.id_instruments""")

# cur.execute("SELECT * FROM nomnieks, noma")

db.commit()
items = cur.fetchall()
print(items)

# for el in items:
#     print(el[1] + "\n" + el[3])



db.close()
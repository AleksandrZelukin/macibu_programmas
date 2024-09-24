# https://docs.python.org/3/library/sqlite3.html
import sqlite3

db = sqlite3.connect('kafejnicas_tikls.db')
db.execute("PRAGMA foreign_keys = 1")
# Create Cursor
c = db.cursor()

c.execute("""CREATE TABLE if not exists kafejnicas (
    "ID_kafejnica" INTEGER  NOT NULL PRIMARY KEY,
    "nosaukums" TEXT, 
    "adresi" TEXT,
    "darbinieks" INTEGER
    )""")

# Tabulu izveidošana
c.execute("""CREATE TABLE if not exists darbinieks (
	"ID_darbinieks"	INTEGER  NOT NULL PRIMARY KEY,
	"vards"	TEXT,
	"uzvards"	TEXT,
	"talrunis"	TEXT,
	"amats"	TEXT,
	"atvalinajums"	TEXT,
    "pasutijums" INTEGER,
	FOREIGH KEY "id_darbinieks" REFERENCES kafeinicas("darbinieks")
    )""")


c.execute("""CREATE TABLE if not exists pasutijums (
	"ID_pasutijums"	INTEGER  NOT NULL PRIMARY KEY,
	"datums"	TEXT,
	"apraksts"	TEXT,
    "darbinieks" INTEGER,
    FOREIGH KEY "ID_pasutijums" REFERENCES darbinieks ("pasutijums")
    )""")



#db.commit()
#db.close()


# tabulas aizpildišana
c.execute("INSERT INTO darbinieks VALUES (1,'Valdis', 'Ozols', '+371 24564567','Pavars',1,'atvalinajuma')")

c.execute("INSERT INTO kafejnicas VALUES (1,'Allegro', 'Kaleju 12')")

c.execute("INSERT INTO pasutijums VALUES (1,'09.11.2023', 'Cepumi', 1)")


# Удаление данных
c.execute("DELETE FROM articles WHERE avtor = 'Admin'")

# Изменение данных
c.execute("UPDATE articles SET avtor = 'Admin', views = 1 WHERE title = 'Amazon is cool!'")

# Выборка данных
c.execute("SELECT rowid, * FROM darbinieks WHERE rowid < 5 ORDER BY views")
items = c.fetchall()
print(items)
print(c.fetchmany(1))
# print(c.fetchone()[1])

for el in items:
    print(el[1] + "\n" + el[4])

db.commit()

db.close()


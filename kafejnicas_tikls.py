# https://docs.python.org/3/library/sqlite3.html
import sqlite3

db = sqlite3.connect('kafejnicas_tikls.db')
db.execute("PRAGMA foreign_keys = 1")
# Create Cursor
c = db.cursor()

# Tabulu izveidošana
c.execute("""CREATE TABLE if not exists darbinieks (
	"ID_darbinieks"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"vards"	TEXT,
	"uzvards"	TEXT,
	"talrunis"	TEXT,
	"amats"	TEXT,
	"kafejnica"	INTEGER,
	"atvalinajums"	TEXT)
""")


c.execute("""CREATE TABLE if not exists pasutijums (
	"ID_pasutijums"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"datums"	TEXT,
	"apraksts"	TEXT,
    "darbinieks" INTEGER)
""")

c.execute("""CREATE TABLE if not exists kafejnicas (
	"ID_kafejnica"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"nosaukums"	TEXT,
	"adresi"	TEXT,
	FOREIGN KEY ("ID_kafejnica") REFERENCES darbinieks ("kafejnica")
)""")

#db.commit()
#db.close()


# tabulas aizpildišana
c.execute("INSERT INTO darbinieks VALUES ('3', 'Valdis', 'Ozols', '+371 24564567','Pavars',1,'atvalinajuma')")

c.execute("INSERT INTO kafejnicas VALUES ('3', 'Allegro', 'Kaleju 12')")

c.execute("INSERT INTO pasutijums VALUES ('2', '09.11.2023', 'Cepumi', 1)")


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


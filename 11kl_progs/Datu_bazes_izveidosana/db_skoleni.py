import sqlite3
con = sqlite3.connect("11klase_datu_baze.db")

cur = con.cursor()

cur.execute("""CREATE TABLE  if not exists dalibnieki(
            numurs integer,
            vards text,
            uzvards text,
            talrunis text)""")
cur.execute("""CREATE TABLE if not exists prieksmeti(
            numurs integer,
            nosaukums text)""")

cur.execute("INSERT INTO dalibnieki VALUES (1, 'Aigars','Ozols' ,'12345678')")
cur.execute("INSERT INTO dalibnieki VALUES (2, 'Olga','Piraga' ,'87654321')")
cur.execute("INSERT INTO prieksmeti VALUES (1,'Matematika')")

ieraksti = cur.execute("SELECT numurs, vards, uzvards, talrunis FROM dalibnieki").fetchall()
print(ieraksti)
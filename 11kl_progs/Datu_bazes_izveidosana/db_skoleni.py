import sqlite3
con = sqlite3.connect("11klase_datu_baze.db")

cur = con.cursor()

cur.execute("""CREATE TABLE  if not exists dalibnieki(
            numurs INTEGER PRIMARY KEY,
            vards text,
            uzvards text,
            talrunis text)""")
cur.execute("""CREATE TABLE if not exists prieksmeti(
            group_id INTEGER,
            nosaukums text PRIMARY KEY,
            FOREIGN KEY (group_id)
            REFERENCES dalibnieki (group_id) )""")

cur.execute("INSERT INTO dalibnieki VALUES (1, 'Aigars','Ozols' ,'12345678')")
cur.execute("INSERT INTO dalibnieki VALUES (2, 'Olga','Piraga' ,'87654321')")
cur.execute("INSERT INTO prieksmeti VALUES (1,'Matematika')")
cur.execute("INSERT INTO prieksmeti VALUES (2,'Datorika')")
cur.execute("INSERT INTO prieksmeti VALUES (3,'Sports')")
cur.execute("INSERT INTO prieksmeti VALUES (4,'Fizika')")

dalibnieki = cur.execute("SELECT numurs, vards, uzvards, talrunis FROM dalibnieki").fetchall()
prieksmeti = cur.execute("SELECT group_id, nosaukums FROM prieksmeti").fetchall()

con.commit()
print("DALIBNIEKI")
for i in dalibnieki:
    print(i)
print("PRIEKSMETI")
for m in prieksmeti:
    print(m)
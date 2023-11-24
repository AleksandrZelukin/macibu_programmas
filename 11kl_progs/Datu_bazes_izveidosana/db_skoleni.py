import sqlite3
con = sqlite3.connect("db_skoleni.db")

cur = con.cursor()

cur.execute("""CREATE TABLE  if not exists dalibnieki(
            numurs INTEGER PRIMARY KEY,
            vards text,
            uzvards text,
            talrunis text)""")


num = int(input("Dalibnieka numurs: "))
var = input("Dalibnieka vārds: ")
uzv = input("Dalibnieka uzvārds: ")
talr = input("kontakta talruņa numurs: ")


ieraksts_dalibnieks=(num,var,uzv,talr)

cur.execute("INSERT INTO dalibnieki VALUES (?,?,?,?)",ieraksts_dalibnieks)

dalibnieki = cur.execute("SELECT numurs, vards, uzvards, talrunis FROM dalibnieki").fetchall()

con.commit()

print("DALIBNIEKI")
for i in dalibnieki:
    print(i)

    
con.close()
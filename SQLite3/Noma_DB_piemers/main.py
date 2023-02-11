from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect('noma.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS nomnieks(
    id_nomnieks TEXT PRIMARY KEY,
    "vards" TEXT, 
    "uzvards" TEXT, 
    "talrunis" TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS instrumenti (
    id_instruments TEXT PRIMARY KEY,
    instruments TEXT,
    data TEXT,
    cena TEXT
 )""")


sql.execute("""CREATE TABLE IF NOT EXISTS noma (
    id TEXT PRIMARY KEY,
    id_nomnieks TEXT NOT NULL,
    id_instruments TEXT NOT NULL,
    FOREIGN KEY("id_instruments") REFERENCES "Instrumenti"("id_instruments"),
    FOREIGN KEY("id_nomnieks") REFERENCES "Nomnieks"("id_nomnieks")
 )""")


db.commit()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def nomnieki():
    if request.method == "POST":
        id_nomnieks = request.form["id_nomnieks"]
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        talrunis = request.form["talrunis"]
        rez = [id_nomnieks,vards,uzvards,talrunis]
        db = sqlite3.connect('noma.db')
        sql = db.cursor()
        sql.execute("INSERT INTO nomnieks VALUES(?,?,?,?)",rez)
        db.commit()
        db.close()
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def instrumenti():
    if request.method == "POST":
        id_instruments = request.form["id_instruments"]
        instruments = request.form["instruments"]
        data = request.form["data"]
        cena = request.form["cena"]
        rez = [id_instruments,instruments,data,cena]
        db = sqlite3.connect('noma.db')
        sql = db.cursor()
        sql.execute("INSERT INTO nomnieks VALUES(?,?,?,?)",rez)
        db.commit()
        db.close()
    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=True)
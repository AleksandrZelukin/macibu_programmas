from flask import Flask, render_template, url_for, request, redirect
import sqlite3


app = Flask(__name__)


con= sqlite3.connect('noma.db')

cur = con.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS nomnieks (
#     id_nomnieks INTEGER PRIMARY KEY AUTOINCREMENT,
#     vards TEXT NOT NULL,
#     uzvards TEXT NOT NULL,
#     talrunis TEXT
#  )""")

 cur.execute("""CREATE TABLE IF NOT EXISTS nomnieks (
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


def user_to_db():
    con = sqlite3.connect('noma.db')
    cur = con.cursor()
    cur.execute('INSERT INTO nomnieks(vards,uzvards,talrunis) VALUES (?,?,?)')
    con.commit()
    con.close()



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        talrunis = request.form["talrunis"]

        user_to_db(vards,uzvards,talrunis)
        

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
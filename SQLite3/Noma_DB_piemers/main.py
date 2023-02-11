from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

con = sqlite3.connect('noma.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS nomnieks (
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    talrunis TEXT
 )""")
con.close()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def nomnieks():
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        talrunis = request.form["talrunis"]
        cur = con.cursor()
        cur.execute('INSERT INTO nomnieks VALUES (?,?,?)')

con.commit()
cur.close()
if __name__ == "__main__":
    app.run(debug=True)
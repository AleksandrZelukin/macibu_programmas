from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect('noma.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS nomnieks (
    vards TEXT,
    uzvards TEXT,
    talrunis TEXT
 )""")
db.commit()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def nomnieks():
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        talrunis = request.form["talrunis"]
        cur.execute('INSERT INTO nomnieks VALUES (?,?,?)')

db.commit()
cur.close()


if __name__ == "__main__":
    app.run(debug=True)
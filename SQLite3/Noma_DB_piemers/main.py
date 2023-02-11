from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


def user_to_db(vards,uzvards,talrunis):
    con = sqlite3.connect('noma.db')
    cur = con.cursor()
    cur.execute('INSERT INTO nomnieks VALUES (?,?,?)')
    con.commit()
    con.close()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
if request.method == "POST":
    vards = request.form["vards"]
    uzvards = request.form["uzvards"]
    talrunis = request.form["talrunis"]
        
    user_to_db(vards,uzvards,talrunis)


if __name__ == "__main__":
    app.run(debug=True)
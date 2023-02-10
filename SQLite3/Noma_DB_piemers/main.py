from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


def user_to_db(id_nomnieks,vards,uzvards,talrunis):
    con = sqlite3.connect('noma.db')
    cur = con.cursor()
    cur.execute('INSERT INTO nomnieks VALUES (?,?,?,?)')
    con.commit()
    con.close()



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        talrunis = request.form["talrunis"]
        rez=(vards,uzvards,talrunis)
        user_to_db(vards,uzvards,talrunis)
        

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
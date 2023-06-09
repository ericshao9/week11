from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/update',methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        try:
            EmpID = request.form['EmpID']
            EmpName = request.form['EmpName']
            EmpGender = request.form['EmpGender']
            EmpPhone = request.form['EmpPhone']
            EmpBdate = request.form['EmpBdate']

            with sql.connect(host="localhost", \
                    user="flask", \
                    password="ubuntu", \
                    database="flask_db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Employee (EmpID,EmpName,EmpGender,EmpPhone,EmpBdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(EmpID,EmpName,EmpGender,EmpPhone,EmpBdate))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg = msg)
            con.close()
    
@app.route('/information')
def information():
    with sql.connect(host="localhost", \
                    user="flask", \
                    password="ubuntu", \
                    database="flask_db") as con:
        
        cur = con.cursor()
        cur.execute("Select * from Employee")
        rows = cur.fetchall()
    return render_template("information.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)


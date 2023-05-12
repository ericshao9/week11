import mysql.connector as sql
conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db")
cur = conn.cursor()

cmd = "CREATE TABLE Employee (\
sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
EmpID VARCHAR(30) NOT NULL,\
EmpName VARCHAR(30), \
EmpGender VARCHAR(30), \
EmpPhone VARCHAR(30), \
EmpBDate VARCHAR(30))"

cur.execute(cmd)
conn.close()


import sqlite3

table = sqlite3.connect("database.db")

table.execute("CREATE TABLE Employee (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate TEXT)")
table.close()
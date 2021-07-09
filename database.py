import sqlite3  
con = sqlite3.connect("Student.db")  
print("Database opened successfully")  
con.execute("create table Student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
print("Table created successfully")  
con.close()


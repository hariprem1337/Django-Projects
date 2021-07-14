import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()

curs.execute("create table if not exists Employee(id_number integer unique, name text, contact integer unique, email text unique, salary real, experience real)")

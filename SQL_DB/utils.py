import sqlite3 as sql

def getCursor():
    conn = sql.connect("sathya.sqlite")
    curs = conn.cursor()
    return conn, curs

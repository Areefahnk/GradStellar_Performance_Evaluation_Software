import sqlite3

conn = sqlite3.connect('gradstellar_database.db')


def update(id,name_new):
    conn.execute("")
    conn.commit()
    print("Successully updated")

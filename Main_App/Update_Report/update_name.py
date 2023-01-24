import sqlite3

conn = sqlite3.connect('gradstellar_database.db')


def update(id,name_new):
    conn.execute("update performance set name='" +name_new+ "' where G_id='"+str(id)+"'")
    conn.commit()
    print("Successully updated")
import sqlite3

conn = sqlite3.connect('gradstellar_database.db')


def update(id,name_new):
    conn.execute("update Partcipants set name='"+name+" 'where g_id='"+str(g_id)+"'")
    conn.commit()
    print("Successully updated")
 

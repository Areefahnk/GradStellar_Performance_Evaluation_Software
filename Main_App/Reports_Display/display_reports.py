import  sqlite3
conn  =  sqlite3.connect ('gradstellar_database.db')
def display():
    records=conn.execute("select *from performance")
    for i in records:
        print(i)
    
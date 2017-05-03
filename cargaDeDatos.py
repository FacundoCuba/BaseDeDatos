import sqlite3

def carga():
    base = sqlite3.connect('D:\pi.db')
    c = base.cursor()
    c.execute('SELECT * FROM ARTICULOS')
    a = c.fetchall()
    print(a)
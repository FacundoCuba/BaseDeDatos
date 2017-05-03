import sqlite3
import inicio

base = sqlite3.connect('D:\pi.db')
c = base.cursor()
c.execute('SELECT * FROM ARTICULOS')
a = c.fetchall()
inicio.menuInicio()

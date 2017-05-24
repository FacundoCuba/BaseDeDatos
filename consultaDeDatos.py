import sqlite3
import inicio

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def consulta():
    print("Ingrese una opcion para continuar...")
    print("1 para ver la lista de Fabricantes")
    print("2 para ver la lista de Articulos")
    print("3 para ver la lista completa")
    print("4 para el Menu de Inicio")
    inputDeConsulta = input()
    if inputDeConsulta == "1":
        c.execute('SELECT * FROM FABRICANTES')
        a = c.fetchall()
        print("ID NOMBRE")
        for i in a:
            print(i[0], i[1])
    elif inputDeConsulta == "2":
        c.execute('SELECT * FROM ARTICULOS')
        a = c.fetchall()
        print("ID NOMBRE PRECIO ID_FAB")
        for i in a:
            print(i[0], i[1], i[2], i[3])
    elif inputDeConsulta == "3":
        c.execute('SELECT ARTICULOS.ID, ARTICULOS.NOMBRE, ARTICULOS.PRECIO, FABRICANTES.NOMBRE FROM ARTICULOS INNER JOIN FABRICANTES ON ARTICULOS.FAB = FABRICANTES.ID')
        a = c.fetchall()
        print("ID NOMBRE PRECIO FABRICANTE")
        for i in a:
            print(i[0], i[1], i[2], i[3])
    elif inputDeConsulta == "4":
        inicio.menuInicio()
    else:
        print("Ingrese una opcion valida!")
        consulta()

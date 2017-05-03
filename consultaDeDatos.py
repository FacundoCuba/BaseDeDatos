import sqlite3

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def consulta():
    print("Ingrese una opcion para continuar...")
    print("1 para ver la lista de Fabricantes")
    print("2 para ver la lista de Articulos")
    print("3 para Salir")
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
        print("Saliendo...")
        print("")
        exit()
    else:
        print("Ingrese una opcion valida!")
        consulta()

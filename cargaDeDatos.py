import sqlite3

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def carga():
    print("Ingrese una opcion para continuar...")
    print("1 para Cargar Fabricantes")
    print("2 para Cargar Articulos")
    print("3 para Salir")
    inputDeCarga = input()
    if inputDeCarga == "1":
        nombre = input("Ingrese Nombre: ")
        c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(nombre))
        a = c.fetchall()
        carga()
    elif inputDeCarga == "2":
        c.execute('SELECT * FROM ARTICULOS')
        a = c.fetchall()
        carga()
    elif inputDeCarga == "3":
        print("Saliendo...")
        print("")
        exit()

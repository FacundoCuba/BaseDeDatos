import sqlite3

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def menuInicio():
    print("Base de Datos de Productos Informaticos")
    print("Ingrese una opcion para continuar...")
    print("1 para Realizar Consultas")
    print("2 para Cargar Datos")
    print("3 para Salir")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        consulta()
    elif inputDelUser == "2":
        carga()
    elif inputDelUser == "3":
        print("Saliendo...")
        print("")
        exit()
    else:
        print("Ingrese una opcion valida!")
        print("")
        menuInicio()

###################CONSULTA################################
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
        menuInicio()
    else:
        print("Ingrese una opcion valida!")
        consulta()

###################CARGA################################
def carga():
    print("Ingrese una opcion para continuar...")
    print("1 para Cargar Fabricantes")
    print("2 para Cargar Articulos")
    print("3 para Menu de Inicio")
    inputDeCarga = input()
    if inputDeCarga == "1":
        nombreFabricante = input("Ingrese Nombre del Fabricante: ").upper()
        c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(nombreFabricante))
        base.commit()
        carga()
    elif inputDeCarga == "2":
        nombreArticulo = input("Ingrese Nombre del Articulo: ").upper()
        precio = input("Ingrese el Precio: ").upper()
        fabricante = input("Ingrese Nombre del Fabricante: ").upper()
        listaDeFabricantes = []
        c.execute('SElECT NOMBRE FROM FABRICANTES')
        a = c.fetchall()
        for i in a:
            listaDeFabricantes.append(a)
        if fabricante in listaDeFabricantes:
            c.execute('INSERT INTO ARTICULOS(NOMBRE,PRECIO,FAB) VALUES ("{}",{},(SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")));'.format(nombreArticulo, precio, fabricante))
            base.commit()
        else:
            c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(fabricante))
            c.execute('INSERT INTO ARTICULOS(NOMBRE,PRECIO,FAB) VALUES ("{}",{},(SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")));'.format(nombreArticulo, precio, fabricante))
            base.commit()
        carga()
    elif inputDeCarga == "3":
        menuInicio()
    else:
        print("Ingrese una opcion valida!")
        carga()


menuInicio()
carga()
consulta()
import sqlite3
import inicio

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def carga():
    print("Ingrese una opcion para continuar...")
    print("1 para Cargar Fabricantes")
    print("2 para Cargar Articulos")
    print("3 para Menu de Inicio")
    inputDeCarga = input()
    if inputDeCarga == "1":
        nombreFabricante = input("Ingrese Nombre del Fabricante: ")
        c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(nombreFabricante))
        a = c.fetchall()
        carga()
    elif inputDeCarga == "2":
        nombreArticulo = input("Ingrese Nombre del Articulo: ")
        precio = input("Ingrese el Precio: ")
        fabricante = input("Ingrese Nombre del Fabricante: ")
        try:
            c.execute('SELECT "{}" FROM FABRICANTES;'.format(fabricante))
            a = c.fetchall()
            if not a:
                c.execute('INSERT INTO FABRICACANTES(NOMBRE) VALUES ("{}");'.format(fabricante))
                b = c.fetchall()
        c.execute('INSERT INTO ARTICULOS(NOMBRE,PRECIO,FAB) VALUES ("{}",{},(SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")));'.format(nombreArticulo, precio, fabricante))
        d = c.fetchall()
        carga()
    elif inputDeCarga == "3":
        inicio.menuInicio()
    else:
        print("Ingrese una opcion valida!")
        carga()

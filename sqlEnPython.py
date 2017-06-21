import sqlite3

base = sqlite3.connect('D:\pi.db')
c = base.cursor()

def menuInicio():
    print("Base de Datos de Productos Informaticos")
    print("Ingrese una opcion para continuar...")
    print("1 para Realizar Consultas")
    print("2 para Cargar Datos")
    print("3 para Facturacion")
    print("4 para Salir")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        consulta()
    elif inputDelUser == "2":
        carga()
    elif inputDelUser == "3":
        facturacion()
    elif inputDelUser == "4":
        print("Saliendo...")
        print("")
        exit()
    #SECUENCIA#SQL#POR#CONSOLA#DE#PYTHON#
    elif inputDelUser == "5":
        c.execute(input())
        a = c.fetchall()
        print(a)
        menuInicio()
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
    print("3 para Cargar Clientes")
    print("4 para Cargar Facturas")
    print("5 para Menu de Inicio")
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
            listaDeFabricantes.append(i[0])
        if fabricante in listaDeFabricantes:
            c.execute('INSERT INTO ARTICULOS(NOMBRE,PRECIO,FAB) VALUES ("{}",{},(SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")));'.format(nombreArticulo, precio, fabricante))
            base.commit()
        else:
            c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(fabricante))
            c.execute('INSERT INTO ARTICULOS(NOMBRE,PRECIO,FAB) VALUES ("{}",{},(SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")));'.format(nombreArticulo, precio, fabricante))
            base.commit()
        carga()
    elif inputDeCarga == "3":
        nombreCliente = input("Ingrese Nombre del Cliente: ").upper()
        apellidoCliente = input("Ingrese Apellido del Cliente: ").upper()
        cuilCuit = int(input("Ingrese CUIL/CUIT del Cliente: "))
        c.execute('INSERT INTO CLIENTES(NOMBRE,APELLIDO,CUIL_CUIT) VALUES ("{}","{}",{});'.format(nombreCliente,apellidoCliente,cuilCuit))
        base.commit()
        carga()
    elif inputDeCarga == "4":
        fecha = int(input("Ingrese la fecha (ddmmaaaa): "))
        cuilCuit = int(input("Ingrese CUIL/CUIT del Cliente: "))
        listaDeCuilCuit = []
        c.execute('SElECT CUIL_CUIT FROM CLIENTES')
        a = c.fetchall()
        for i in a:
            listaDeCuilCuit.append(i[0])
        if cuilCuit in listaDeCuilCuit:
            c.execute('INSERT INTO FACTURAS(FECHA,ID_CLI) VALUES ({},(SELECT ID FROM CLIENTES WHERE (CUIL_CUIT = {})));'.format(fecha,cuilCuit))
            base.commit()
        else:
            nombreCliente = input("Ingrese Nombre del Cliente: ").upper()
            apellidoCliente = input("Ingrese Apellido del Cliente: ").upper()
            c.execute('INSERT INTO CLIENTES(NOMBRE,APELLIDO,CUIL_CUIT) VALUES ("{}","{}",{});'.format(nombreCliente,apellidoCliente,cuilCuit))
            c.execute('INSERT INTO FACTURAS(FECHA,ID_CLI) VALUES ({},(SELECT ID FROM CLIENTES WHERE (CUIL_CUIT = {})));'.format(fecha,cuilCuit))
            base.commit()
        carga()
    elif inputDeCarga == "5":
        menuInicio()
    else:
        print("Ingrese una opcion valida!")
        carga()

##########FACTURACION#########
'''def facturacion():
    articulo = input("Ingrese Nombre del Articulo: ").upper()
    fabricante = input("Ingrese el Nombre del Articulo").upper()
    cliente = input("Ingrese CUIL/CUIT del Cliente: ").upper()
    cantidad = int(input("Ingrese la cantidad: "))
    precio = c.execute('SELECT ARTICULOS.PRECIO FROM ARTICULOS WHERE (ARTICULOS.NOMBRE = "{}" AND FABRICANTES.NOMBRE = "{}");'.format(articulo,fabricante))
    c.execute('INSERT INTO ART_FAC(CANTIDAD,PRECIO) VALUES ({},{},{},{});'.format(cantidad,precio))
    base.commit()
'''


#TODO juntar encabezado y detalle, e imprimirlos.

menuInicio()
carga()
consulta()
#facturacion()
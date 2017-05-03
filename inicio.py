import cargaDeDatos
import consultaDeDatos

def menuInicio():
    print("Base de Datos de Productos Informaticos")
    print("Ingrese un opcion para continuar...")
    print("1 para Cargar Datos")
    print("2 para Realizar Consultas")
    print("3 para Salir")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        cargaDeDatos
    elif inputDelUser == "2":
        consultaDeDatos
    elif inputDelUser == "3":
        print("Saliendo...")
        print("")
        exit()
    else:
        print("Ingrese una opcion valida!")
        print("")
        menuInicio()
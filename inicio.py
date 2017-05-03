import cargaDeDatos
import consultaDeDatos

def menuInicio():
    print("Base de Datos de Productos Informaticos")
    print("Ingrese una opcion para continuar...")
    print("1 para Cargar Datos")
    print("2 para Realizar Consultas")
    print("3 para Salir")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        print("Ingrese una opcion para continuar...")
        print("1 para Cargar Fabricantes")
        print("2 para Cargar Articulos")
        print("3 para Salir")
        inputDeCarga = input()
        if inputDeCarga == "1":
            cargaDeDatos.carga()
        elif inputDeCarga == "2":
            cargaDeDatos.carga()
        elif inputDeCarga == "3":
            print("Saliendo...")
            print("")
            exit()
        else:
            print("Ingrese una opcion valida!")
            print("")
            menuInicio()
    elif inputDelUser == "2":
        consultaDeDatos.consulta()
    elif inputDelUser == "3":
        print("Saliendo...")
        print("")
        exit()
    else:
        print("Ingrese una opcion valida!")
        print("")
        menuInicio()
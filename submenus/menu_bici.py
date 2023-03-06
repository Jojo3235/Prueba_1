import sys
sys.path.insert(0, "")


import primera_parte.bicicleta as bcl
import helpers

def menu_bici():
    while True:
        helpers.menu_vehiculo_especifico("bicicleta")
        opcion_3 = input("> ")
        helpers.limpiar_pantalla()

        if opcion_3 == "1":
            print("Listado de coches...\n")
            for bici in bcl.Bicicletas.lista:
                print(bici)

        elif opcion_3 == "2":
            print("Buscando bicicleta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la bicicleta. ")
            bici = bcl.Bicicletas.buscar(id)
            print(bici) if bici else print("No se ha encontrado la bicicleta.")
            
        elif opcion_3 == "3":
            print("Añadiendo una bicicleta...\n")
            color = helpers.leer_texto(1, 100, "Introduzca el color de la bici").capitalize()
            tipo = helpers.introducir_numero("Introduzca el tipo de bici (urbana, deportiva): ").capitalize()
            bcl.Bicicletas.nuevo(color, tipo)
            print("Bicicleta añadida con éxito.")

        elif opcion_3 == "4":
            print("Modificar bicicleta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la bicicleta")
            bici = bcl.Bicicletas.buscar(id)
            if bici:
                color = helpers.leer_texto(1, 100, "Introduzca el color de la bicicleta").capitalize()
                tipo = helpers.introducir_numero("Introduzca el tipo de bicicleta (urbana, deportiva): ").capitalize()
                while True:
                    if tipo in ["urbana","deportiva"]:
                        bcl.Bicicletas.modificar(id, color, tipo)
                        print("Bicicleta modificada con éxito.")
                        break
                    else:
                        print("El tipo de bici no es válido.")

        elif opcion_3 == "5":
            print("Borrar una bicicleta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la bicicleta")
            print("Bicicleta borrada con éxito.") if bcl.Bicicletas.borrar(id) else print("No se ha encontrado la bicicleta.")

        elif opcion_3 == "6":
            print("Saliendo...\n")
            break

        input("\nPresione ENTER para continuar...")
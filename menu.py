import os 
import helpers as helpers
import primera_parte.coche as ch
import primera_parte.bicicleta as bcl
import primera_parte.subparte_primera.camioneta as cmt
import primera_parte.subparte_primera.formula1 as f1
import primera_parte.subparte_segunda.Motocicleta as mtcl
import primera_parte.cosa_rara.quad as qd


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("============================")
        print("    Bienvenido al Gestor    ")
        print("============================")
        print("[1] Listar las categorías   ")
        print("[2] Acceder a coches        ")
        print("[3] Acceder a bicicletas    ")
        print("[4] Acceder a camionetas    ")
        print("[5] Acceder a formula1      ")
        print("[6] Acceder a quads         ")
        print("[7] Acceeder a motocicletas ")
        print("============================")

        opcion_1 = input("> ")
        helpers.limpiar_pantalla()

        if opcion_1 == "1":
            print("[1] Coches      ")
            print("[2] Bicicletas  ")
            print("[3] Camionetas  ")
            print("[4] Formula1    ")
            print("[5] Quads       ")
            print("[6] Motocicletas")

        elif opcion_1 == "2":
            helpers.menu_vehiculo_especifico("coche")
            opcion_2 = input("> ")
            helpers.limpiar_pantalla()

            if opcion_2 == "1":
                print("Listado de coches...\n")
                for coche in ch.Coches.lista:
                    print(coche)

            elif opcion_2 == "2":
                print("Buscando coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                coche = ch.Coches.buscar(id)
                print(coche) if coche else print("No se ha encontrado el coche.")
            
            elif opcion_2 == "3":
                print("Añadiendo un coche...\n")
                color = helpers.leer_texto(1, 100, "Introduzca el color del coche").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del coche").capitalize()
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada del coche").capitalize()
                ch.Coches.crear(color, velocidad, cilindrada)

            elif opcion_2 == "4":
                print("Modificar un coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                coche = ch.Coches.buscar(id)
                if coche:
                    color = helpers.leer_texto(1, 100, "Introduzca el color del coche").capitalize()
                    velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del coche").capitalize()
                    cilindrada = helpers.introducir_numero("Introduzca la cilindrada del coche").capitalize()
                    ch.Coches.modificar(coche.id, color, velocidad, cilindrada)
                    print("Coche modificado con éxito.")
                else:
                    print("No se ha encontrado el coche.")

            elif opcion_2 == "5":
                print("Borrar un coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                print("Coche borrado con éxito.") if ch.Coches.borrar(id) else print("No se ha encontrado el coche.")

            elif opcion_2 == "6":
                print("Saliendo...\n")
                break

            input("\nPresione ENTER para continuar...")

        elif opcion_1 == "3":
            helpers.menu_vehiculo_especifico("bicicleta")
            opcion_3 = input("> ")
            helpers.limpiar_pantalla()

            if opcion_3 == "1":
                print("Listado de coches...\n")
                for bici in bcl.Bicicletas.lista:
                    print(bici)

            elif opcion_3 == "2":
                print("Buscando bicicleta...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                coche = ch.Coches.buscar(id)
                print(coche) if coche else print("No se ha encontrado el coche.")
            
            elif opcion_2 == "3":
                print("Añadiendo un coche...\n")
                color = helpers.leer_texto(1, 100, "Introduzca el color del coche").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del coche").capitalize()
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada del coche").capitalize()
                ch.Coches.crear(color, velocidad, cilindrada)

            elif opcion_2 == "4":
                print("Modificar un coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                coche = ch.Coches.buscar(id)
                if coche:
                    color = helpers.leer_texto(1, 100, "Introduzca el color del coche").capitalize()
                    velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del coche").capitalize()
                    cilindrada = helpers.introducir_numero("Introduzca la cilindrada del coche").capitalize()
                    ch.Coches.modificar(coche.id, color, velocidad, cilindrada)
                    print("Coche modificado con éxito.")
                else:
                    print("No se ha encontrado el coche.")

            elif opcion_2 == "5":
                print("Borrar un coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                print("Coche borrado con éxito.") if ch.Coches.borrar(id) else print("No se ha encontrado el coche.")

            elif opcion_2 == "6":
                print("Saliendo...\n")
                break

            input("\nPresione ENTER para continuar...")
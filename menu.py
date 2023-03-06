import os 
import helpers as helpers
import primera_parte.coche as ch
import primera_parte.bicicleta as bcl
import primera_parte.subparte_primera.camioneta as cmt
import primera_parte.subparte_primera.formula1 as f1
import primera_parte.subparte_segunda.motocicleta as mtcl
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
                ch.Coches.nuevo(color, velocidad, cilindrada)

            elif opcion_2 == "4":
                print("Modificar coche...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID del coche")
                coche = ch.Coches.buscar(id)
                if coche:
                    color = helpers.leer_texto(1, 100, "Introduzca el color del coche").capitalize()
                    velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del coche").capitalize()
                    cilindrada = helpers.introducir_numero("Introduzca la cilindrada del coche").capitalize()
                    ch.Coches.modificar(id, color, velocidad, cilindrada)
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
                id = helpers.leer_texto(1, 100, "Introduzca la ID de la bicicleta. ")
                bici = bcl.Bicicletas.buscar(id)
                print(bici) if bici else print("No se ha encontrado la bicicleta.")
            
            elif opcion_3 == "3":
                print("Añadiendo una bicicleta...\n")
                color = helpers.leer_texto(1, 100, "Introduzca el color de la bici").capitalize()
                while True:
                    tipo = helpers.introducir_numero("Introduzca el tipo de bici (urbana, deportiva): ").capitalize()
                    try:
                        tipo.lower() in ["urbana","deportiva"]
                        break
                    except:
                        print("El tipo de bici no es válido.")
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
            
        elif opcion_1 == "7":
            helpers.menu_vehiculo_especifico("motocicleta")
            opcion_7 = input("> ")
            helpers.limpiar_pantalla()

            if opcion_7 == "1":
                print("Listado de coches...\n")
                for moto in mtcl.Motocicletas.lista:
                    print(moto)

            elif opcion_7 == "2":
                print("Buscando motocicleta...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID de la motocicleta. ")
                moto = mtcl.Motocicletas.buscar(id)
                print(moto) if moto else print("No se ha encontrado la motocicleta.")

            elif opcion_7 == "3":
                print("Añadiendo una motocicleta...\n")
                color = helpers.leer_texto(1, 100, "Introduzca el color de la bici").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima de la motocicleta").capitalize()
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada de la motocicleta").capitalize()
                while True:
                    tipo = helpers.introducir_numero("Introduzca el tipo de bici (urbana, deportiva): ").capitalize()
                    try:
                        tipo.lower() in ["urbana","deportiva"]
                        break
                    except:
                        print("El tipo de bici no es válido.")
                mtcl.Motocicletas.nuevo(color, tipo, velocidad, cilindrada)
                print("motocicleta añadida con éxito.")

            elif opcion_7 == "4":
                print("Modificar motocicleta...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID de la motocicleta")
                moto = mtcl.Motocicletas.buscar(id)
                if moto:
                    color = helpers.leer_texto(1, 100, "Introduzca el color de la motocicleta").capitalize()
                    tipo = helpers.introducir_numero("Introduzca el tipo de motocicleta (urbana, deportiva): ")
                    velocidad = helpers.introducir_numero("Introduzca la velocidad de la motocicleta: ")
                    cilindrada = helpers.introducir_numero("Introduzca la cilindrada de la motocicleta: ")
                    while True:
                        if tipo in ["urbana","deportiva"]:
                            mtcl.Motocicletas.modificar(id, color, tipo, velocidad, cilindrada)
                            print("motocicleta modificada con éxito.")
                            break
                        else:
                            print("El tipo de bici no es válido.")

            elif opcion_7 == "5":
                print("Borrar una motocicleta...\n")
                id = helpers.leer_texto(1, 100, "Introduzca la ID de la motocicleta")
                print("motocicleta borrada con éxito.") if mtcl.Motocicletas.borrar(id) else print("No se ha encontrado la motocicleta.")

            elif opcion_7 == "6":
                print("Saliendo...\n")
                break

            input("\nPresione ENTER para continuar...")
import helpers
import primera_parte.subparte_segunda.motocicleta as mtcl


def menu_moto():
    while True:
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
            velocidad = helpers.introducir_numero("Introduzca la velocidad máxima de la motocicleta")
            cilindrada = helpers.introducir_numero("Introduzca la cilindrada de la motocicleta")
            tipo = helpers.leer_texto("Introduzca el tipo de bici (urbana, deportiva): ")
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
                mtcl.Motocicletas.modificar(id, color, tipo, velocidad, cilindrada)
                print("Motocicleta modificada con éxito.")
            else:
                print("Motocicleta no encontrada.")

        elif opcion_7 == "5":
            print("Borrar una motocicleta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la motocicleta")
            print("motocicleta borrada con éxito.") if mtcl.Motocicletas.borrar(id) else print("No se ha encontrado la motocicleta.")

        elif opcion_7 == "6":
            print("Saliendo...\n")
            break

        input("\nPresione ENTER para continuar...")
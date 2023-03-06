import sys
sys.path.insert(0, "")

import helpers
import primera_parte.cosa_rara.quad as qd


def menu_quad():
    while True:
        helpers.menu_vehiculo_especifico("quad")
        opcion_4 = input("> ")
        helpers.limpiar_pantalla()
        
        if opcion_4 == "1":
            print("Listado de quads...\n")
            for quad in qd.Quads.lista:
                print(quad)
        
        elif opcion_4 == "2":
            print("Buscando quad...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del quad")
            quad = qd.Quads.buscar(id)
            print(quad) if quad else print("No se ha encontrado el quad.")
        
        elif opcion_4 == "3":
            print("Añadiendo una quad...\n")
            color = helpers.leer_texto(1, 100, "Introduzca el color del quad").capitalize()
            velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del quad")
            cilindrada = helpers.introducir_numero("Introduzca la cilindrada del quad")
            carga = helpers.introducir_numero("Introduzca la carga del quad")
            tipo = helpers.leer_texto("Introduzca el tipo de quad: ")
            modelo = helpers.leer_texto("Introduzca el modelo del quad: ")
            qd.Quads.nuevo(color, velocidad, cilindrada, tipo, carga, modelo)
            print("Quad añadido con éxito.")

        elif opcion_4 == "4":
            print("Modificar camioneta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la camioneta")
            quad = qd.Quads.buscar(id)
            if quad:
                color = helpers.leer_texto(1, 100, "Introduzca el color del quad").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del quad")
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada del quad")
                carga = helpers.introducir_numero("Introduzca la carga del quad")
                tipo = helpers.leer_texto("Introduzca el tipo de quad: ")
                modelo = helpers.leer_texto("Introduzca el modelo del quad: ")
                qd.Quads.modificar(id, color, velocidad, cilindrada, tipo, carga, modelo)
                print("Quad modificado con éxito.")
            else:
                print("No se ha encontrado el quad.")
        
        elif opcion_4 == "5":
            print("Borrar un quad...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del quadd")
            print("Camioneta borrada con éxito.") if qd.Quads.borrar(id) else print("No se ha encontrado la camioneta.")
        
        elif opcion_4 == "6":
            print("Saliendo...\n")
            break
        
        input("\nPresione ENTER para continuar...")
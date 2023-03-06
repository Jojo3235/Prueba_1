import sys
sys.path.insert(0, "")

import helpers
import primera_parte.subparte_primera.formula1 as f1

def menu_formula1():
    while True:
        helpers.menu_vehiculo_especifico("Formula1")
        opcion_5 = input("> ")
        helpers.limpiar_pantalla()
        
        if opcion_5 == "1":
            print("Listado de camionetas...\n")
            for formula1 in f1.Formula1s.lista:
                print(formula1)
        
        elif opcion_5 == "2":
            print("Buscando formula1...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del formula1")
            formula1 = f1.Formula1s.buscar(id)
            print(formula1) if formula1 else print("No se ha encontrado el formula1.")
        
        elif opcion_5 == "3":
            print("Añadiendo un formula1...\n")
            color = helpers.leer_texto(1, 100, "Introduzca el color del formula1").capitalize()
            velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del formula1")
            cilindrada = helpers.introducir_numero("Introduzca la cilindrada del formula1")
            escuderia = helpers.leer_texto(1, 100, "Introduzca la escuderia del formula1")
            f1.Formula1s.nuevo(color, velocidad, cilindrada, escuderia)
            print("Formula1 añadido con éxito.")

        elif opcion_5 == "4":
            print("Modificar formula1...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del formula1")
            formula1 = f1.Formula1s.buscar(id)
            if formula1:
                color = helpers.leer_texto(1, 100, "Introduzca el color del formula1").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima del formula1")
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada del formula1")
                escuderia = helpers.leer_texto(1, 100, "Introduzca la escuderia del formula1")
                f1.Formula1s.modificar(id, color, velocidad, cilindrada, escuderia)
                print("Formula1 modificado con éxito.")
            else:
                print("No se ha encontrado el formula1.")
        
        elif opcion_5 == "5":
            print("Borrar un formula1...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del formula1")
            print("Camioneta borrada con éxito.") if f1.Formula1s.borrar(id) else print("No se ha encontrado el formula1.")
        
        elif opcion_5 == "6":
            print("Saliendo...\n")
            break
        
        input("\nPresione ENTER para continuar...")
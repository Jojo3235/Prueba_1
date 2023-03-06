import helpers
import primera_parte.coche as ch

def menu_coche():
    while True:
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
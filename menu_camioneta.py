import helpers
import primera_parte.subparte_primera.camioneta as cm

def menu_camioneta():
    while True:
        helpers.menu_vehiculo_especifico("camioneta")
        opcion_4 = input("> ")
        helpers.limpiar_pantalla()
        
        if opcion_4 == "1":
            print("Listado de camionetas...\n")
            for camioneta in cm.Camionetas.lista:
                print(camioneta)
        
        elif opcion_4 == "2":
            print("Buscando coche...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la camioneta")
            camioneta = cm.Camionetas.buscar(id)
            print(camioneta) if camioneta else print("No se ha encontrado la camioneta.")
        
        elif opcion_4 == "3":
            print("Añadiendo una camioneta...\n")
            color = helpers.leer_texto(1, 100, "Introduzca el color de la camioneta").capitalize()
            velocidad = helpers.introducir_numero("Introduzca la velocidad máxima de la camioneta")
            cilindrada = helpers.introducir_numero("Introduzca la cilindrada de la camioneta")
            carga = helpers.introducir_numero("Introduzca la carga de la camioneta")
            cm.Camionetas.nuevo(color, velocidad, cilindrada, carga)
            print("Camioneta añadida con éxito.")

        elif opcion_4 == "4":
            print("Modificar camioneta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID de la camioneta")
            camioneta = cm.Camionetas.buscar(id)
            if camioneta:
                color = helpers.leer_texto(1, 100, "Introduzca el color de la camioneta").capitalize()
                velocidad = helpers.introducir_numero("Introduzca la velocidad máxima de la camioneta")
                cilindrada = helpers.introducir_numero("Introduzca la cilindrada de la camioneta")
                carga = helpers.introducir_numero("Introduzca la carga de la camioneta")
                cm.Camionetas.modificar(id, color, velocidad, cilindrada, carga)
                print("Camioneta modificada con éxito.")
            else:
                print("No se ha encontrado la camioneta.")
        
        elif opcion_4 == "5":
            print("Borrar una camioneta...\n")
            id = helpers.leer_texto(1, 100, "Introduzca la ID del camioneta")
            print("Camioneta borrada con éxito.") if cm.Camionetas.borrar(id) else print("No se ha encontrado el camioneta.")
        
        elif opcion_4 == "6":
            print("Saliendo...\n")
            break
        
        input("\nPresione ENTER para continuar...")
import os
import helpers2
import vehiculos2 as vh
import platform


def iniciar():
    while True:
        helpers2.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los vehiculos ")
        print("[2] Buscar un vehiculo   ")
        print("[3] Añadir un vehiculo  ")
        print("[4] Modificar un vehiculo")
        print("[5] Borrar un vehiculo  ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers2.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehiculos...\n")
            for vehiculo in vh.Vehiculos.lista:
                print(vehiculo)

        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            id = helpers2.leer_texto(1, 100, "Introduzca la id del vehiculo")
            vehiculo = vh.Vehiculos.buscar(id)
            print(vehiculo) if vehiculo else print("Vehiculo no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehiculo...\n")
            color = helpers2.leer_texto(2, 30, "Color del vehiculo: ")
            ruedas = helpers2.introducir_numero("Ruedas del vehiculo: ")
            vh.Vehiculos.crear(color, ruedas)
            print("Vehiculo añadido correctamente.")

        elif opcion == '4':
            print("Modificando un cliente...\n")
            id = helpers2.leer_texto(1, 100, "Introduzca la id del vehiculo")
            vehiculo = vh.Vehiculos.buscar(id)
            if vehiculo:
                color = helpers2.leer_texto(1,100, "Introduzca el color del vehiculo")
                ruedas = helpers2.introducir_numero("Introduzca el numero de ruedas del vehiculo")
                vh.Vehiculos.modificar(vehiculo.id, color, ruedas)
                print("Vehiculo modificado correctamente.")
            else:
                print("Vehiculo no encontrado.")

        elif opcion == '5':
            print("Borrando un vehiculo...\n")
            id = helpers2.leer_texto(1, 100, "Introduzca la id del vehiculo")
            print("Vehiculo borrado correctamente.") if vh.Vehiculos.borrar(id) else print("Vehiculo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")

if __name__ == '__main__':
    iniciar()
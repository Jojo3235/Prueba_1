import os 
import helpers as helpers
import vehiculos as vh


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los vehículos ")
        print("[2] Buscar un vehículo   ")
        print("[3] Añadir un vehículo   ")
        print("[4] Modificar un vehículo")
        print("[5] Borrar un vehículo   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

import os 
import helpers as helpers
import submenus.menu_bici as menu_bici
import submenus.menu_camioneta as menu_camioneta
import submenus.menu_coche as menu_coche
import submenus.menu_f1 as menu_f1
import submenus.menu_moto as menu_moto
import submenus.menu_quad as menu_quad


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
        print("[8] Salir del Gestor        ")
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
            menu_coche.menu_coche()

        elif opcion_1 == "3":
            menu_bici.menu_bici()

        elif opcion_1 == "4":
            menu_camioneta.menu_camioneta()

        elif opcion_1 == "5":
            menu_f1.menu_f1()

        elif opcion_1 == "6":
            menu_quad.menu_quad()

        elif opcion_1 == "7":
            menu_moto.menu_moto()

        elif opcion_1 == "8":
            print("Saliendo...\n")
            break

        input("\nPresione ENTER para continuar...")
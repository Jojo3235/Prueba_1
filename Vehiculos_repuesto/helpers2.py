import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def introducir_numero(mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        try:
            numero = int(input("> "))
            return numero
        except ValueError:
            print("Debe introducir un número.")

def id_valida(id, lista):
    if not re.match('^[0-9]+$', id):
        print("ID inválida, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.id == id:
            print("ID utilizada por otro cliente.")
            return False
    return True

def menu_vehiculo_especifico(tipo):
    print("========================")
    print("  Bienvenido al Gestor de {}s".format(tipo))
    print("========================")
    print("[1] Listar los {}s".format(tipo))
    print("[2] Buscar un {}".format(tipo))
    print("[3] Añadir un {}".format(tipo))
    print("[4] Modificar un {}".format(tipo))
    print("[5] Borrar un {}".format(tipo))
    print("[6] Cerrar el Gestor    ")
    print("========================")
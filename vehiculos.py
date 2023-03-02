import config
import csv


class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas}
    

class Vehiculos:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for color, ruedas in reader:
            vehiculo = Vehiculo(color, ruedas)
            lista.append(vehiculo)
    
    @staticmethod
    def buscar(id):
        for vehiculo in Vehiculos.lista:
            if vehiculo.id == id:
                return vehiculo

    @staticmethod
    def eliminar(id):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def modificar(id, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for vehiculo in Vehiculos.lista:
                writer.writerow((vehiculo.ruedas, vehiculo.color))
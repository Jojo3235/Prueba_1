import sys
sys.path.insert(0, "")

from vehiculos import Vehiculo
import config
import csv


permitidas = ["urbana", "deportiva"]

class Bicicleta(Vehiculo):

    def __init__(self, color, tipo):
        Vehiculo.__init__(self, color, 2)
        if tipo.lower() in permitidas:
            self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.tipo)
    
    def to_dict(self):
        diccionario = Vehiculo.to_dict(self)
        diccionario.update({"tipo":self.tipo})
        return diccionario

class Bicicletas():
    
    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, tipo in reader:
            if ruedas == "2":
                bicicleta = Bicicleta(color, tipo)
                lista.append(bicicleta)

    @staticmethod
    def nuevo(color, tipo):
        bicicleta = Bicicleta(color, tipo)
        Bicicletas.lista.append(bicicleta)
        Bicicletas.guardar()
        return bicicleta

    @staticmethod
    def buscar(id):
        for bicicleta in Bicicletas.lista:
            if bicicleta.id == id:
                return bicicleta

    @staticmethod
    def modificar(id, color, tipo):
        for indice, bicicleta in enumerate(Bicicletas.lista):
            if bicicleta.id == id:
                Bicicletas.lista[indice].color = color
                Bicicletas.lista[indice].tipo = tipo
                Bicicletas.guardar()
                return Bicicletas.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, bicicleta in enumerate(Bicicletas.lista):
            if bicicleta.id == id:
                bicicleta = Bicicletas.lista.pop(indice)
                Bicicletas.guardar()
                return bicicleta
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for bicicleta in Bicicletas.lista:
                writer.writerow([bicicleta.id, bicicleta.color, bicicleta.ruedas, bicicleta.tipo])
        
        Bicicletas.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            Bicicletas.lista.clear()
            for id, color, ruedas, tipo in reader:
                if ruedas == "2":
                    bicicleta = Bicicleta(color, tipo)
                    bicicleta.id = id
                    Bicicletas.lista.append(bicicleta)

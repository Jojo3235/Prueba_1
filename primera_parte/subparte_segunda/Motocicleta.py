import sys
sys.path.insert(0, "primera_parte")

from bicicleta import Bicicleta
import config
import csv


class Motocicleta(Bicicleta):

    def __init__(self, color, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + ", velocidad máxima {}km/h, cilindrada: {}".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        diccionario = Bicicleta.to_dict(self)
        diccionario.update({"cilindrada":self.cilindrada, "velocidad":self.velocidad})
        return diccionario

class Motocicletas:

    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, tipo, velocidad, cilindrada in reader:
            motocicleta = Motocicleta(color, tipo, velocidad, cilindrada)
            lista.append(motocicleta)

    @staticmethod
    def nuevo(color, tipo, velocidad, cilindrada):
        motocicleta = Motocicleta(color, tipo, velocidad, cilindrada)
        Motocicletas.lista.append(motocicleta)
        Motocicletas.guardar()
        return motocicleta

    @staticmethod
    def buscar(id):
        for motocicleta in Motocicletas.lista:
            if motocicleta.id == id:
                return motocicleta

    @staticmethod
    def modificar(id, color, tipo, velocidad, cilindrada):
        for indice, motocicleta in enumerate(Motocicletas.lista):
            if motocicleta.id == id:
                Motocicletas.lista[indice].color = color
                Motocicletas.lista[indice].tipo = tipo
                Motocicletas.lista[indice].velocidad = velocidad
                Motocicletas.lista[indice].cilindrada = cilindrada
                Motocicletas.guardar()
                return Motocicletas.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, motocicleta in enumerate(Motocicletas.lista):
            if motocicleta.id == id:
                motocicleta = Motocicletas.lista.pop(indice)
                Motocicletas.guardar()
                return motocicleta
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for motocicleta in Motocicletas.lista:
                writer.writerow([motocicleta.id, motocicleta.color, motocicleta.ruedas, motocicleta.tipo])
        
        Motocicletas.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            Motocicletas.lista.clear()
            for id, color, ruedas, tipo in reader:
                if ruedas == "2":
                    motocicleta = Motocicleta(color, tipo)
                    motocicleta.id = id
                    Motocicletas.lista.append(motocicleta)

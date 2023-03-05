import sys
sys.path.insert(0, "1")

from coche import Coche
import config
import csv

class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", carga máxima: {}kg".format(self.carga)
    
    def to_dict(self):
        diccionario = Coche.to_dict(self)
        diccionario.update({"carga":self.carga})
        return diccionario
    
class Camionetas():
    
    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, velocidad, cilindrada in reader:
            if ruedas == "4":
                camioneta = Camioneta(color, velocidad, cilindrada)
                lista.append(camioneta)

    @staticmethod
    def nuevo(color, velocidad, cilindrada):
        coche = Coche(color, velocidad, cilindrada)
        Camionetas.lista.append(coche)
        Camionetas.guardar()
        return coche

    @staticmethod
    def buscar(id):
        for coche in Camionetas.lista:
            if coche.id == id:
                return coche

    @staticmethod
    def modificar(id, color, velocidad, cilindrada):
        for indice, coche in enumerate(Camionetas.lista):
            if coche.id == id:
                Camionetas.lista[indice].color = color
                Camionetas.lista[indice].velocidad = velocidad
                Camionetas.lista[indice].cilindrada = cilindrada
                Camionetas.guardar()
                return Camionetas.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, coche in enumerate(Camionetas.lista):
            if coche.id == id:
                coche = Camionetas.lista.pop(indice)
                Camionetas.guardar()
                return coche
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for coche in Camionetas.lista:
                writer.writerow([coche.id, coche.color, coche.ruedas, coche.velocidad, coche.cilindrada])
        
        Camionetas.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for id, color, ruedas, velocidad, cilindrada in reader:
                if ruedas == "4":
                    coche = Coche(color, velocidad, cilindrada)
                    coche.id = id
                    Camionetas.lista.append(coche)
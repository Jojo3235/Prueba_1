import sys
sys.path.insert(0, "")

from vehiculos import Vehiculo
import csv
import config

class Coche(Vehiculo):

    def __init__(self, color, velocidad, cilindrada):
        Vehiculo.__init__(self, color, 4)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", llega hasta {} km/h, tiene {}cc de potencia".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        diccionario = Vehiculo.to_dict(self)
        diccionario.update({"velocidad":self.velocidad, "cilindrada":self.cilindrada})
        return diccionario
    
class Coches():
    
    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, velocidad, cilindrada in reader:
            if ruedas == "4":
                coche = Coche(color, velocidad, cilindrada)
                lista.append(coche)

    @staticmethod
    def nuevo(color, velocidad, cilindrada):
        coche = Coche(color, velocidad, cilindrada)
        Coches.lista.append(coche)
        Coches.guardar()
        return coche

    @staticmethod
    def buscar(id):
        for coche in Coches.lista:
            if coche.id == id:
                return coche

    @staticmethod
    def modificar(id, color, velocidad, cilindrada):
        for indice, coche in enumerate(Coches.lista):
            if coche.id == id:
                Coches.lista[indice].color = color
                Coches.lista[indice].velocidad = velocidad
                Coches.lista[indice].cilindrada = cilindrada
                Coches.guardar()
                return Coches.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, coche in enumerate(Coches.lista):
            if coche.id == id:
                coche = Coches.lista.pop(indice)
                Coches.guardar()
                return coche
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for coche in Coches.lista:
                writer.writerow([coche.id, coche.color, coche.ruedas, coche.velocidad, coche.cilindrada])
        
        Coches.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for id, color, ruedas, velocidad, cilindrada in reader:
                if ruedas == "4":
                    coche = Coche(color, velocidad, cilindrada)
                    coche.id = id
                    Coches.lista.append(coche)

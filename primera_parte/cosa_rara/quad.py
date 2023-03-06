import sys
sys.path.insert(0, "primera_parte")

from coche import Coche
import csv
import config


permitidos = ["urbano", "deportivo"]

class Quad(Coche):

    def __init__(self, color, velocidad, cilindrada, tipo, carga, modelo):
        Coche.__init__(self, color, 4, velocidad, cilindrada)
        if tipo in permitidos:
            self.tipo = tipo
        else:
            raise ValueError("El tipo no está permitido (urbano, deportivo)")
        self.carga = carga
        self.modelo = modelo

    def __str__(self):
        return Coche.__str__(self) + "tipo: {}, carga {} kg, modelo {}".format(self.tipo, self.carga, self.modelo)
    
    def to_dict(self):
        diccionario = Coche.to_dict(self)
        diccionario.update({"tipo": self.tipo, "carga":self.carga, "modelo":self.modelo})
        return diccionario
    
  
class Quads():
    
    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, velocidad, cilindrada, tipo, carga, modelo in reader:
            if ruedas == "4":
                quad = Quad(color, velocidad, cilindrada, tipo, carga, modelo)
                lista.append(quad)

    @staticmethod
    def nuevo(color, velocidad, cilindrada, tipo, carga, modelo):
        quad = Quad(color, velocidad, cilindrada, tipo, carga, modelo)
        Quads.lista.append(quad)
        Quads.guardar()
        return quad

    @staticmethod
    def buscar(id):
        for quad in Quads.lista:
            if quad.id == id:
                return quad

    @staticmethod
    def modificar(id, color, velocidad, cilindrada, tipo, carga, modelo):
        for indice, quad in enumerate(Quads.lista):
            if quad.id == id:
                Quads.lista[indice].color = color
                Quads.lista[indice].velocidad = velocidad
                Quads.lista[indice].cilindrada = cilindrada
                Quads.lista[indice].tipo = tipo
                Quads.lista[indice].carga = carga
                Quads.lista[indice].modelo = modelo
                Quads.guardar()
                return Quads.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, quad in enumerate(Quads.lista):
            if quad.id == id:
                quad = Quads.lista.pop(indice)
                Quads.guardar()
                return quad
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for quad in Quads.lista:
                writer.writerow([quad.id, quad.color, quad.ruedas, quad.velocidad, quad.cilindrada, quad.tipo, quad.carga, quad.modelo])
        
        Quads.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for id, color, ruedas, velocidad, cilindrada, tipo, carga, modelo in reader:
                if ruedas == "4":
                    quad = Quad(color, velocidad, cilindrada, tipo, carga, modelo)
                    quad.id = id
                    Quads.lista.append(quad)
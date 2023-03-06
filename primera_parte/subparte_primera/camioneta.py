import sys
sys.path.insert(0, "primera_parte")

from coche import Coche
import config
import csv

class Camioneta(Coche):
    
    def __init__(self, color, velocidad, cilindrada, carga):
        Coche.__init__(self, color, velocidad, cilindrada)
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
        for id, color, ruedas, velocidad, cilindrada, carga in reader:
            if ruedas == "4":
                camioneta = Camioneta(color, velocidad, cilindrada, carga)
                lista.append(camioneta)

    @staticmethod
    def nuevo(color, velocidad, cilindrada, carga):
        camioneta = Camioneta(color, velocidad, cilindrada, carga)
        Camionetas.lista.append(camioneta)
        Camionetas.guardar()
        return camioneta

    @staticmethod
    def buscar(id):
        for camioneta in Camionetas.lista:
            if camioneta.id == id:
                return camioneta

    @staticmethod
    def modificar(id, color, velocidad, cilindrada, carga):
        for indice, camioneta in enumerate(Camionetas.lista):
            if camioneta.id == id:
                Camionetas.lista[indice].color = color
                Camionetas.lista[indice].velocidad = velocidad
                Camionetas.lista[indice].cilindrada = cilindrada
                Camionetas.lista[indice].carga = carga
                Camionetas.guardar()
                return Camionetas.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, camioneta in enumerate(Camionetas.lista):
            if camioneta.id == id:
                camioneta = Camionetas.lista.pop(indice)
                Camionetas.guardar()
                return camioneta
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for camioneta in Camionetas.lista:
                writer.writerow([camioneta.id, camioneta.color, camioneta.ruedas, camioneta.velocidad, camioneta.cilindrada, camioneta.carga])
        
        Camionetas.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            Camionetas.lista.clear()
            for id, color, ruedas, velocidad, cilindrada, carga in reader:
                if ruedas == "4":
                    camioneta = Camioneta(color, velocidad, cilindrada, carga)
                    camioneta.id = id
                    Camionetas.lista.append(camioneta)

#Esto funciona
def main():
    # Creamos algunas instancias de Camionetas
    camionetas_1 = Camioneta("rojo", 300, 600, 243)
    camionetas_2 = Camioneta("azul", 350, 700, 23)
    camionetas_3 = Camioneta("verde", 320, 650, 200)
  
    # Las guardamos en la base de datos
    Camionetas.nuevo(camionetas_1.color, camionetas_1.velocidad, camionetas_1.cilindrada, camionetas_1.carga)
    Camionetas.nuevo(camionetas_2.color, camionetas_2.velocidad, camionetas_2.cilindrada, camionetas_2.carga)
    Camionetas.nuevo(camionetas_3.color, camionetas_3.velocidad, camionetas_3.cilindrada, camionetas_3.carga)
  
if __name__ == '__main__':
    main()
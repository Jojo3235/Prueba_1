import sys
sys.path.insert(0, "primera_parte")

from coche import Coche
import config
import csv


class Formula1(Coche):

    def __init__(self, color, velocidad, cilindrada, escuderia):
        Coche.__init__(self, color, velocidad, cilindrada)
        self.escuderia = escuderia

    def __str__(self):
        return Coche.__str__(self) + ", escuderia: {}".format(self.escuderia)
    
    def to_dict(self):
        diccionario = Coche.to_dict(self)
        diccionario.update({"escuderia":self.escuderia})
        return diccionario
    
class Formula1s():
    
    lista = []
    with open(config.DATABASE_PATH, newline='') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas, velocidad, cilindrada, escuderia in reader:
            if ruedas == "4":
                formula1 = Formula1(color, velocidad, cilindrada, escuderia)
                lista.append(formula1)

    @staticmethod
    def nuevo(color, velocidad, cilindrada, escuderia):
        formula1 = Formula1(color, velocidad, cilindrada, escuderia)
        Formula1s.lista.append(formula1)
        Formula1s.guardar()
        return formula1

    @staticmethod
    def buscar(id):
        for formula1 in Formula1s.lista:
            if formula1.id == id:
                return formula1

    @staticmethod
    def modificar(id, color, velocidad, cilindrada, escuderia):
        for indice, formula1 in enumerate(Formula1s.lista):
            if formula1.id == id:
                Formula1s.lista[indice].color = color
                Formula1s.lista[indice].velocidad = velocidad
                Formula1s.lista[indice].cilindrada = cilindrada
                Formula1s.lista[indice].escuderia = escuderia
                Formula1s.guardar()
                return Formula1s.lista[indice]

    @staticmethod
    def borrar(id):
        for indice, formula1 in enumerate(Formula1s.lista):
            if formula1.id == id:
                formula1 = Formula1s.lista.pop(indice)
                Formula1s.guardar()
                return formula1
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for formula1 in Formula1s.lista:
                writer.writerow([formula1.id, formula1.color, formula1.ruedas, formula1.velocidad, formula1.cilindrada, formula1.escuderia])
        
        Formula1s.lista.clear()
        with open(config.DATABASE_PATH, newline='') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for id, color, ruedas, velocidad, cilindrada, escuderia in reader:
                if ruedas == "4":
                    formula1 = Formula1(color, velocidad, cilindrada, escuderia)
                    formula1.id = id
                    Formula1s.lista.append(formula1)

def main():
    # Creamos algunas instancias de Formula1
    formula1_1 = Formula1("rojo", 300, 600, "Ferrari")
    formula1_2 = Formula1("azul", 350, 700, "Mercedes")
    formula1_3 = Formula1("verde", 320, 650, "Red Bull")
    
    # Las guardamos en la base de datos
    Formula1s.nuevo(formula1_1.color, formula1_1.velocidad, formula1_1.cilindrada, formula1_1.escuderia)
    Formula1s.nuevo(formula1_2.color, formula1_2.velocidad, formula1_2.cilindrada, formula1_2.escuderia)
    Formula1s.nuevo(formula1_3.color, formula1_3.velocidad, formula1_3.cilindrada, formula1_3.escuderia)
    
if __name__ == '__main__':
    main()
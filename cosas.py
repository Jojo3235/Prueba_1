import csv 
import config

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def numero_ruedas(self):
        return self.ruedas        

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas, "velocidad":self.velocidad, "cilindrada":self.cilindrada}


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", carga máxima: {}kg".format(self.carga)
    
    def to_dict(self):
        return {Vehiculos.to_dict(self)} #añadir las otras cosas

class Bicicleta(Vehiculo):

    def __init__(self,color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ",tipo de bicicleta: {}".format(self.tipo)

    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas, "tipo":self.tipo}

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas, "tipo":self.tipo, "velocidad":self.velocidad, "cilindrada":self.cilindrada}


class Vehiculos():
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader()

    @staticmethod
    def catalogar(lista, numero_ruedas):
        
        return "se han encontrado {} vehículos con {} ruedas".format()
        pass

    
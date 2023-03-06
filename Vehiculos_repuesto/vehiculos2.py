import config2
import csv

class Vehiculo():
    
    id = 0

    def __init__(self, color, ruedas):
        self.id = Vehiculo.id
        Vehiculo.id += 1
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "id: {}, color {}, {} ruedas".format(self.id, self.color, self.ruedas)

    def to_dict(self):
        return {"id": self.id, "color":self.color, "ruedas":self.ruedas}
    
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
    
permitidas = ["urbana", "deportiva"]

class Bicicleta(Vehiculo):

    def __init__(self, color, tipo):
        Vehiculo.__init__(self, color, 2)
        if tipo.lower() in permitidas:
            self.tipo = tipo
        else:
            raise ValueError("El tipo no está permitido (urbana, deportiva)")
        
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.tipo)
    
    def to_dict(self):
        diccionario = Vehiculo.to_dict(self)
        diccionario.update({"tipo":self.tipo})
        return diccionario

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
    

class Quad(Coche):

    def __init__(self, color, velocidad, cilindrada, tipo, carga, modelo):
        Coche.__init__(self, color, 4, velocidad, cilindrada)
        if tipo in permitidas:
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
    
class Vehiculos():

    lista = []
    with open(config2.DATABASE_PATH, newline='n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, color, ruedas in reader:
            vehiculo = Vehiculo(color, ruedas)
            lista.append(vehiculo)

    @staticmethod
    def buscar(id):
        for vehiculo in Vehiculos.lista:
            if vehiculo.id == id:
                return vehiculo
            
    @staticmethod
    def crear(color, ruedas):
        vehiculo = Vehiculo(color, ruedas)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def modificar(id, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                Vehiculo.lista[indice].color = color
                Vehiculo.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
    
    @staticmethod
    def borrar(id):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                del Vehiculos.lista[indice]
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def listar():
        return Vehiculos.lista
    
    @staticmethod
    def guardar(vehiculo):
        with open(config2.DATABASE_PATH, 'w', newline='n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow([vehiculo.id, vehiculo.color, vehiculo.ruedas])
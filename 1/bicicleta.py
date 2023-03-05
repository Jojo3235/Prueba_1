import sys
sys.path.insert(0, "")

from vehiculos import Vehiculo, Vehiculos


permitidas = ["urbana", "deportiva"]

class Bicicleta(Vehiculo):

    def __init__(self, color, tipo):
        Vehiculo.__init__(self, color, 2)
        if tipo.lower() in Bicicleta.permitidas:
            self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        diccionario = Vehiculo.to_dict(self)
        diccionario.update({"tipo":self.tipo})
        return diccionario
    

class Coches(Vehiculos):
    
    def __init__(self):
        Vehiculos.__init__(self)
        self.tipo_vehiculo = "bicicleta"

    @staticmethod
    def nuevo(self):
        color = input("Color: ")
        ruedas = 4
        velocidad = input("Velocidad: ")
        cilindrada = input("Cilindrada: ")
        self.vehiculos.append(Bicicleta(color, ruedas, velocidad, cilindrada))

    @staticmethod
    def listar(self):
        for bicicleta in self.vehiculos:
            print(bicicleta)

    @staticmethod
    def buscar(self):
        color = input("Color: ")
        for coche in self.vehiculos:
            if coche.color == color:
                print(coche)

    @staticmethod
    def modificar(self):
        color = input("Color: ")
        for bicicleta in self.vehiculos:
            if bicicleta.id == id:
                print(bicicleta)
                color = input("Nuevo color: ")
                ruedas = 2
                tipo = input("Nuevo tipo: ")
                bicicleta.color = color
                bicicleta.ruedas = ruedas
                if tipo.lower() in permitidas:
                    bicicleta.tipo = tipo

    @staticmethod
    def borrar(self):
        id = input("id: ")
        for coche in self.vehiculos:
            if coche.id == id:
                self.vehiculos.remove(coche)
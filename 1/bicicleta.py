import sys
sys.path.insert(0, "")

from vehiculos import Vehiculo #, Vehiculos


class Bicicleta(Vehiculo):

    permitidas = ["urbana", "deportiva"]

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
    
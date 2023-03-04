from vehiculos import Vehiculo, Vehiculos

class Bicicleta(Vehiculo):

    permitidas = ["urbana", "deportiva"]

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        if tipo in Bicicleta.permitidas:
            self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + ", tipo de bicicleta: {}".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        diccionario = Vehiculo.to_dict(self)
        diccionario.update({"tipo":self.tipo})
        return diccionario
    
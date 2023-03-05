import sys
sys.path.insert(0, "1")

from bicicleta import Bicicleta
from coche import Coche


class Quad(Coche, Bicicleta):
    def __init__(self, color, tipo, carga, modelo):
        Bicicleta.__init__(self, color, tipo)
        Coche.__init__(self, color, 4)
        self.carga = carga
        self.modelo = modelo

    def __str__(self):
        return Bicicleta.__str__(self) + ", carga {} kg, modelo {}".format(self.carga, self.modelo)
    
    def to_dict(self):
        diccionario = Bicicleta.to_dict(self)
        diccionario.update(Coche.to_dict(self))
        diccionario.update({"carga":self.carga, "modelo":self.modelo})
        return diccionario
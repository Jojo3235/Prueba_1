import sys
sys.path.insert(0, "1")

from coche import Coche


class Formula1(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, escuderia):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.escuderia = escuderia

    def __str__(self):
        return Coche.__str__(self) + ", escuderia: {}".format(self.escuderia)
    
    def to_dict(self):
        diccionario = Coche.to_dict(self)
        diccionario.update({"escuderia":self.escuderia})
        return diccionario
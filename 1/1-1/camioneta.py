from coche import Coche

class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", carga máxima: {}kg".format(self.carga)
    
    def to_dict(self):
        diccionario = Coche.to_dict(self)
        diccionario.update({"carga":self.carga})
        return diccionario
    

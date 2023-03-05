import sys
sys.path.insert(0, "1")

from bicicleta import Bicicleta

class Motocicleta(Bicicleta):

    def __init__(self, color, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
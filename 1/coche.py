from vehiculos import Vehiculo, Vehiculos

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas, "velocidad":self.velocidad, "cilindrada":self.cilindrada}

class Coches(Vehiculos):
    
    def __init__(self):
        Vehiculos.__init__(self)
        self.tipo = "coche"

    def nuevo(self):
        color = input("Color: ")
        ruedas = 4
        velocidad = input("Velocidad: ")
        cilindrada = input("Cilindrada: ")
        self.vehiculos.append(Coche(color, ruedas, velocidad, cilindrada))

    def listar(self):
        for coche in self.vehiculos:
            print(coche)

    def buscar(self):
        color = input("Color: ")
        for coche in self.vehiculos:
            if coche.color == color:
                print(coche)

    def modificar(self):
        color = input("Color: ")
        for coche in self.vehiculos:
            if coche.color == color:
                print(coche)
                color = input("Nuevo color: ")
                ruedas = input("Nuevas ruedas: ")
                velocidad = input("Nueva velocidad: ")
                cilindrada = input("Nueva cilindrada: ")
                coche.color = color
                coche.ruedas = ruedas
                coche.velocidad = velocidad
                coche.cilindrada = cilindrada

    def borrar(self):
        color = input("Color: ")
        for coche in self.vehiculos:
            if coche.color == color:
                self.vehiculos.remove(coche)
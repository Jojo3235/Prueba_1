class Vehiculo():
    
    id = 1

    def __init__(self, color, ruedas):
        self.id = Vehiculo.id
        Vehiculo.id += 1
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "El vehículo tiene la id {}, es de color {}, tiene {} ruedas".format(self.id, self.color, self.ruedas)

    def to_dict(self):
        return {"id": self.id, "color":self.color, "ruedas":self.ruedas}
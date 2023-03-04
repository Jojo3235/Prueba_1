import config
import csv

# Creacion de la clase de la que se heredaran cosas
# Acceso a base de datos
# Lectura de db
# Modificacion en la db 
# Busqueda en la db



class Vehiculo():
    
    id = 0

    def __init__(self, color, ruedas):
        self.id = Vehiculo.id
        Vehiculo.id += 1
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

    def to_dict(self):
        return {"color":self.color, "ruedas":self.ruedas}
    

class Vehiculos:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for color, ruedas in reader:
            vehiculo = Vehiculo(color, ruedas)
            lista.append(vehiculo)
    
    @staticmethod
    def buscar(id):
        for vehiculo in Vehiculos.lista:
            if vehiculo.id == id:
                return vehiculo
    @staticmethod
    def detectar_numero_ruedas(numero_ruedas):
        lista = []
        for vehiculo in Vehiculos.lista:
            if vehiculo.ruedas == numero_ruedas:
                lista.append(vehiculo)
        return lista
    
    @staticmethod
    def eliminar(id):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def modificar(id, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for vehiculo in Vehiculos.lista:
                writer.writerow((vehiculo.ruedas, vehiculo.color))
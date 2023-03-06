import unittest
import primera_parte.coche as ch
import primera_parte.bicicleta as bcl
import primera_parte.subparte_primera.camioneta as cmt
import primera_parte.subparte_primera.formula1 as f1
import primera_parte.subparte_segunda.motocicleta as mtcl
import primera_parte.cosa_rara.quad as qd

class TestVehiculos(unittest.TestCase):

    def test_coche(self):
        coche = ch.Coche("rojo", 200, 2000)
        assert coche.color == "rojo"
        assert coche.ruedas == 4
        assert coche.velocidad == 200
        assert coche.cilindrada == 2000
        assert str(coche) == "rojo, 4 ruedas, llega hasta 200 km/h, tiene 2000cc de potencia"
        assert coche.to_dict() == {"color":"rojo", "ruedas":4, "velocidad":200, "cilindrada":2000}
        coche2 = ch.Coche("verde", 300, 3000)
        assert coche2.color == "verde"
        assert coche2.ruedas == 4
        assert coche2.velocidad == 300
        assert coche2.cilindrada == 3000
        assert str(coche2) == "verde, 4 ruedas, llega hasta 300 km/h, tiene 3000cc de potencia"
        assert coche2.to_dict() == {"color":"verde", "ruedas":4, "velocidad":300, "cilindrada":3000}
        coche3 = ch.Coche("azul", 400, 4000)
        assert coche3.color == "azul"
        assert coche3.ruedas == 4
        assert coche3.velocidad == 400
        assert coche3.cilindrada == 4000
        assert str(coche3) == "azul, 4 ruedas, llega hasta 400 km/h, tiene 4000cc de potencia"
        assert coche3.to_dict() == {"color":"azul", "ruedas":4, "velocidad":400, "cilindrada":4000}
        coche4 = ch.Coche("amarillo", 500, 5000)
        assert coche4.color == "amarillo"
        assert coche4.ruedas == 4
        assert coche4.velocidad == 500
        assert coche4.cilindrada == 5000
        assert str(coche4) == "amarillo, 4 ruedas, llega hasta 500 km/h, tiene 5000cc de potencia"

    def test_bicicleta(self):

        bicicleta = bcl.Bicicleta("rojo", 2)
        assert bicicleta.color == "rojo"
        assert bicicleta.ruedas == 2
        assert str(bicicleta) == "rojo, 2 ruedas"
        assert bicicleta.to_dict() == {"color":"rojo", "ruedas":2}
        bicicleta2 = bcl.Bicicleta("verde", 2)
        assert bicicleta2.color == "verde"
        assert bicicleta2.ruedas == 2
        assert str(bicicleta2) == "verde, 2 ruedas"
        assert bicicleta2.to_dict() == {"color":"verde", "ruedas":2}
        bicicleta3 = bcl.Bicicleta("azul", 2)
        assert bicicleta3.color == "azul"
        assert bicicleta3.ruedas == 2
        assert str(bicicleta3) == "azul, 2 ruedas"
        assert bicicleta3.to_dict() == {"color":"azul", "ruedas":2}
        bicicleta4 = bcl.Bicicleta("amarillo", 2)
        assert bicicleta4.color == "amarillo"
        assert bicicleta4.ruedas == 2
        assert str(bicicleta4) == "amarillo, 2 ruedas"

    def test_camioneta(self):

        camioneta = cmt.Camioneta("rojo", 200, 2000, 20000)
        assert camioneta.color == "rojo"
        assert camioneta.ruedas == 4
        assert camioneta.velocidad == 200
        assert camioneta.cilindrada == 2000
        assert camioneta.carga == 20000
        assert str(camioneta) == "rojo, 4 ruedas, llega hasta 200 km/h, tiene 2000cc de potencia, carga hasta 20000kg"
        assert camioneta.to_dict() == {"color":"rojo", "ruedas":4, "velocidad":200, "cilindrada":2000, "carga":20000}
        camioneta2 = cmt.Camioneta("verde", 300, 3000, 30000)
        assert camioneta2.color == "verde"
        assert camioneta2.ruedas == 4
        assert camioneta2.velocidad == 300
        assert camioneta2.cilindrada == 3000
        assert camioneta2.carga == 30000
        assert str(camioneta2) == "verde, 4 ruedas, llega hasta 300 km/h, tiene 3000cc de potencia, carga hasta 30000kg"
        assert camioneta2.to_dict() == {"color":"verde", "ruedas":4, "velocidad":300, "cilindrada":3000, "carga":30000}
        camioneta3 = cmt.Camioneta("azul", 400, 4000, 40000)
        assert camioneta3.color == "azul"
        assert camioneta3.ruedas == 4
        assert camioneta3.velocidad == 400
        assert camioneta3.cilindrada == 4000
        assert camioneta3.carga == 40000
        assert str(camioneta3) == "azul, 4 ruedas, llega hasta 400 km/h, tiene 4000cc de potencia, carga hasta 40000kg"
        assert camioneta3.to_dict() == {"color":"azul", "ruedas":4, "velocidad":400, "cilindrada":4000, "carga":40000}
        
    def test_quad(self):

        quad = qd.Quad("rojo", 200, 2000)
        assert quad.color == "rojo"
        assert quad.ruedas == 4
        assert quad.velocidad == 200
        assert quad.cilindrada == 2000
        assert str(quad) == "rojo, 4 ruedas, llega hasta 200 km/h, tiene 2000cc de potencia"
        assert quad.to_dict() == {"color":"rojo", "ruedas":4, "velocidad":200, "cilindrada":2000}
        quad2 = qd.Quad("verde", 300, 3000)
        assert quad2.color == "verde"
        assert quad2.ruedas == 4
        assert quad2.velocidad == 300
        assert quad2.cilindrada == 3000
        assert str(quad2) == "verde, 4 ruedas, llega hasta 300 km/h, tiene 3000cc de potencia"
        assert quad2.to_dict() == {"color":"verde", "ruedas":4, "velocidad":300, "cilindrada":3000}
        quad3 = qd.Quad("azul", 400, 4000)
        assert quad3.color == "azul"
        assert quad3.ruedas == 4
        assert quad3.velocidad == 400
        assert quad3.cilindrada == 4000
        assert str(quad3) == "azul, 4 ruedas, llega hasta 400 km/h, tiene 4000cc de potencia"
        assert quad3.to_dict() == {"color":"azul", "ruedas":4, "velocidad":400, "cilindrada":4000}

    def test_moto(self):

        moto = mtcl.Motocicleta("rojo", 200, 2000)
        assert moto.color == "rojo"
        assert moto.ruedas == 2
        assert moto.velocidad == 200
        assert moto.cilindrada == 2000
        assert str(moto) == "rojo, 2 ruedas, llega hasta 200 km/h, tiene 2000cc de potencia"
        assert moto.to_dict() == {"color":"rojo", "ruedas":2, "velocidad":200, "cilindrada":2000}
        moto2 = mtcl.Motocicleta("verde", 300, 3000)
        assert moto2.color == "verde"
        assert moto2.ruedas == 2
        assert moto2.velocidad == 300
        assert moto2.cilindrada == 3000
        assert str(moto2) == "verde, 2 ruedas, llega hasta 300 km/h, tiene 3000cc de potencia"
        assert moto2.to_dict() == {"color":"verde", "ruedas":2, "velocidad":300, "cilindrada":3000}
        moto3 = mtcl.Motocicleta("azul", 400, 4000)
        assert moto3.color == "azul"
        assert moto3.ruedas == 2
        assert moto3.velocidad == 400
        assert moto3.cilindrada == 4000
        assert str(moto3) == "azul, 2 ruedas, llega hasta 400 km/h, tiene 4000cc de potencia"
        assert moto3.to_dict() == {"color":"azul", "ruedas":2, "velocidad":400, "cilindrada":4000}

    def test_f1(self):

        f1 = f1cl.F1("rojo", 200, 2000)
        assert f1.color == "rojo"
        assert f1.ruedas == 4
        assert f1.velocidad == 200
        assert f1.cilindrada == 2000
        assert str(f1) == "rojo, 4 ruedas, llega hasta 200 km/h, tiene 2000cc de potencia"
        assert f1.to_dict() == {"color":"rojo", "ruedas":4, "velocidad":200, "cilindrada":2000}
        f12 = f1cl.F1("verde", 300, 3000)
        assert f12.color == "verde"
        assert f12.ruedas == 4
        assert f12.velocidad == 300
        assert f12.cilindrada == 3000
        assert str(f12) == "verde, 4 ruedas, llega hasta 300 km/h, tiene 3000cc de potencia"
        assert f12.to_dict() == {"color":"verde", "ruedas":4, "velocidad":300, "cilindrada":3000}
        f13 = f1cl.F1("azul", 400, 4000)
        assert f13.color == "azul"
        assert f13.ruedas == 4
        assert f13.velocidad == 400
        assert f13.cilindrada == 4000
        assert str(f13) == "azul, 4 ruedas, llega hasta 400 km/h, tiene 4000cc de potencia"
        assert f13.to_dict() == {"color":"azul", "ruedas":4, "velocidad":400, "cilindrada":4000}


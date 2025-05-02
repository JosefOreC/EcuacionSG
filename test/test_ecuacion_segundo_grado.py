"""
    Codigo de pruebas y errores para la clase EcuacionSegundoGrado
"""

import unittest

from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado


class TestEcuacionSegundoGrado(unittest.TestCase):
    def test_EcuacionSG_raicesResultantes_Reales(self):
        # Forma ax^2+bx+c = 0
        a = 1
        b = -3
        c = 2
        ecua_seg = EcuacionSegundoGrado(a, b, c)
        resultado_e1 = 2.0
        resultado_e2 = 1.0

        self.assertEqual([resultado_e1, resultado_e2], ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_doble(self):
        a = 1
        b = -2
        c = 1
        ecua_seg = EcuacionSegundoGrado(a, b, c)
        resultado_e1 = resultado_e2 = 1.0

        self.assertEqual([resultado_e1, resultado_e2], ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_complejas(self):
        a = 1
        b = 2
        c = 2
        ecua_seg = EcuacionSegundoGrado(a, b, c)

        resultado_e1 = complex(-1, 1)
        resultado_e2 = complex(-1, -1)

        self.assertEqual([resultado_e1, resultado_e2], ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_noSegundoGrado(self):
        a = 0
        b = 2
        c = 1
        ecua_seg = EcuacionSegundoGrado(a, b, c)

        response = "Error! Datos no correspondientes a segundo grado."

        self.assertEqual(response, ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_datosNoNumericos(self):
        a = 'a'
        b = 2.0
        c = 1.0
        ecua_seg = EcuacionSegundoGrado(a, b, c)

        response = f"Error! Dato '{a}' no es numerico ni real."

        self.assertEqual(response, ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_raicesComplejas1(self):
        a = 1
        b = 1
        c = 1
        ecua_seg = EcuacionSegundoGrado(a, b, c)

        resultado_e1 = complex(-0.5, 0.866)
        resultado_e2 = complex(-0.5, -0.866)

        self.assertEqual([resultado_e1, resultado_e2], ecua_seg.calcular_raices())

    def test_EcuacionSG_raicesResultantes_raicesComplejas2(self):
        a = 1
        b = -5
        c = 10
        ecua_seg = EcuacionSegundoGrado(a, b, c)

        resultado_e1 = complex(2.5, 1.936)
        resultado_e2 = complex(2.5, -1.936)

        self.assertEqual([resultado_e1, resultado_e2], ecua_seg.calcular_raices())


if __name__ == "__main__":
    unittest.main()

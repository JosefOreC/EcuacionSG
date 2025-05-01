"""
    Codigo para la clase ecuación de segundo grado

"""

import math

class EcuacionSegundoGrado:
    def __init__(self,a=0,b=0,c=0):
        self.__a = a
        self.b = b
        self.c = c

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def set_all_data(self,a,b,c):
        self.set_c(c)
        self.set_b(b)
        self.set_a(a)
    
    def validar_dato(self, dato, lista=[]):
        if not type(dato) in [float, int]:
            lista.append(dato)
            return False
        return True
    def validar_datos_ecuacion(self):

        datos_no_validos = []
        is_data_valid = (self.validar_dato(self.__a, datos_no_validos)
                         and self.validar_dato(self.b, datos_no_validos)
                         and self.validar_dato(self.c, datos_no_validos))
        if len(datos_no_validos)>1:
            response1 = "s"
        else: response1 = ""

        if not is_data_valid:
            response = f"Error! Dato{response1} "
            for dato in datos_no_validos:
                response+= f"'{dato}'"
                if datos_no_validos.index(dato) > 0 and datos_no_validos.index(dato)<len(datos_no_validos)-1:
                    response+=', '
            response+= " no es numerico ni real."
        else: response = "Todo válido"
        return is_data_valid, response, None


    def calcular_raices(self):

        is_valid, response, _ = self.validar_datos_ecuacion()

        if not is_valid:
            return response

        if self.__a == 0:
            return "Error! Datos no correspondientes a segundo grado."

        discriminante = (self.b**2)-4*self.__a*self.c
        is_dis_negative = discriminante < 0
        calc_discriminante = abs(discriminante)
        calc_discriminante = math.sqrt(calc_discriminante)
        calc_discriminante /= 2*self.__a
        calc_b = (-self.b)/(2*self.__a)

        calc_b = round(calc_b, 3)
        calc_discriminante = round(calc_discriminante, 3)

        if is_dis_negative:

            return [complex(calc_b,calc_discriminante), complex(calc_b, -calc_discriminante)]

        raiz_1 = calc_b+calc_discriminante
        raiz_2 = calc_b - calc_discriminante

        return [raiz_1,raiz_2]


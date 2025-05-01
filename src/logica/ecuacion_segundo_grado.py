"""
    Codigo para la clase ecuación de segundo grado

"""

class EcuacionSegundoGrado:
    def __init__(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c

    def validar_dato(self, dato, lista=[]):
        if not type(dato) in [float, int]:
            lista.append(dato)
            return False
        return True
    def validar_datos_ecuacion(self):

        datos_no_validos = []
        is_data_valid = (self.validar_dato(self.a, datos_no_validos)
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

        if self.a == 0:
            return "Error! Datos no correspondientes a segundo grado."





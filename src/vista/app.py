"""
    Almacena la visualización con el usuario

"""
from dataclasses import is_dataclass
from idlelib.mainmenu import menudefs

from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado


class Vista:



    def __init__(self):

        """
            Inicar vista
        """
        self.__comands = {1: (self.calcular_raices), 2: (self.modo_programador), 3: exit}
        self.main()

    def main(self):
        while (response:=self.menu()):
            self.select_option(response)


    def val_input(self, message, inf=None, sup=None):
        dato = input(message)
        inf_mess = inf
        sup_mess = sup
        try:
            dato = float(dato)
            is_dato_in_range = True
            if sup != None:
                is_dato_in_range = (dato <= sup)
            else: sup_mess = 'infinite'
            if inf != None:
                is_dato_in_range = is_dato_in_range and (dato >= inf)
            else: inf_mess = 'infinite'
            if not is_dato_in_range:
                return self.val_input(message = f"Dato fuera del rango [{inf_mess};{sup_mess}]\nIntente de nuevo: ",
                                      inf=inf, sup=sup)
        except TypeError:
            print("El dato no es valido, intente de nuevo")
            return self.val_input(message)
        except ValueError:
            print("El dato no es valido, intente de nuevo")
            return self.val_input(message)

        return dato

    def select_option(self, option):
        (self.__comands.get(option))()

    def modo_programador(self):
        self.line()
        print("|\tSE HA INGRESADO AL MODO PROGRAMADOR ")
        self.line()
        while (comando:=input("modeDevelop>")) != 'exit':
            if comando == '?':
                self.line()
                print("exit -> Volver al menú")
                self.line()
                continue
            try:
                exec(comando)
            except Exception as E:
                print(E)

    def calcular_raices(self, var=False):
        print("Ingrese la ecuación ax^2 + bx + c = 0")
        a = self.val_input("a: ")
        b = self.val_input("b: ")
        c = self.val_input("c: ")

        ecuacion = EcuacionSegundoGrado(a, b, c)
        resultado = ecuacion.calcular_raices()
        if type(resultado) == list:
            print(f"Las raíces de la ecuación son: \n\tx1: {resultado[0]} \n\tx2: {resultado[1]}")
        else: print(resultado)
        if var:
            return resultado

    def line(self):
        for i in range(20): print("-", end="")
        print()

    def menu(self):
        self.line()
        print("\t\tMENU")
        self.line()
        print("\t1. Calcular ecuación segundo grado.")
        print("\t2. Entrar a modo programador")
        print("\t3. Salir")
        self.line()
        return self.val_input(message="Ingrese Opción: ", sup= 3, inf=1)

if __name__=='__main__':
    Vista()



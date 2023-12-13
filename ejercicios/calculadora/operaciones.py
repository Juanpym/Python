# para seguir los principios solid se crea clase operacion, para hacerla HIJA de otra (calculadora)
class Operacion:
    while True:
        def suma(self, num1, num2):
            try:
                num1 + num2
            except ValueError: print('Números inválidos.')
            True 

        def resta(self, num1, num2):
            return num1 - num2

        def multiplicacion(self, num1, num2):
            return num1 * num2

        def division(self, num1, num2):

            if num2 != 0:
                return num1 / num2
            else:
                return "No es posible realizar divisioness por 0"

print('aa')
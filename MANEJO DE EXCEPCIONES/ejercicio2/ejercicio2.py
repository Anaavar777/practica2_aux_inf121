class NumeroInvalidoException(Exception):
    pass

class ArithmeticException(Exception):
    pass

class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ArithmeticException("No se puede dividir entre cero")
        return a / b

    @staticmethod
    def convertir_a_entero(cadena):
        if cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit()):
            return int(cadena)
        raise NumeroInvalidoException(f"'{cadena}' no es un número válido")


def main():
    print("PRUEBAS DE LA CALCULADORA\n")

    print("Suma:", Calculadora.sumar(5, 3))
    print("Resta:", Calculadora.restar(10, 4))
    print("Multiplicación:", Calculadora.multiplicar(6, 7))

    try:
        print("División:", Calculadora.dividir(10, 2))
        print("División con error:", Calculadora.dividir(5, 0))
    except ArithmeticException as e:
        print("Error:", e)

    try:
        print("Convertir '123':", Calculadora.convertir_a_entero("123"))
        print("Convertir 'abc':", Calculadora.convertir_a_entero("abc"))
    except NumeroInvalidoException as e:
        print("Error:", e)


main()

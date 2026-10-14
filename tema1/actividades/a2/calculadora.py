class Calculadora:

    # Función para sumar 1 o más números
    def suma(self, *args):
        self.check_args(*args)
        resultado = 0
        
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("Alguno de los valores no es un numero")
            resultado += value

        return resultado

    # Función para restar dos números
    def resta(self, valor1, valor2):
        self.two_numbers_check(valor1, valor2)
        return valor1 - valor2
    
    # Función para multiplicar 1 o más números
    def multiplicacion(self, *args):
        self.check_args(*args)
        resultado = 1

        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("Alguno de los valores no es un numero")
            resultado *= value
    
        return resultado
    
    # Función para dividir dos numeros
    def division(self, valor1, valor2):
            self.two_numbers_check(valor1, valor2)

            if valor2 == 0:
                raise ValueError("No se puede dividir por 0")

            return valor1 / valor2

    # Comprueba si se ha introducido al menos un valor
    def check_args(self, *args):
        if len(args) < 1:
            raise TypeError("Debe introducir al menos 1 valor")
        
        if len(args) == 1:
            return args[0]
    
    # Comprueba si los dos valores son números (int o float)
    def two_numbers_check(self, valor1, valor2):
        if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
            raise TypeError("Alguno de los valores no es un numero")


# %%writefile
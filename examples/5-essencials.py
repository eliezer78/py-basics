class Matematica:
    # Atributo estático de clase: compartido por todas las instancias
    contador = 0
        
    # Método normal (de instancia): recibe self y puede usar atributos de la instancia
    def sumar(self, a, b):
        print("Método de instancia")
        return a + b

    # Método de clase: recibe cls y puede usar/modificar atributos de clase
    @classmethod
    def restar(cls, a, b):
        print("Método de clase")
        return a - b

    # Método estático: no recibe ni self ni cls, funciona como función normal dentro de la clase
    @staticmethod
    def multiplicar(a, b):
        print("Método estático")
        return a * b

# Demostración de uso
m = Matematica()

# Método de instancia: se accede desde una instancia, recibe self
print(m.sumar(3, 2))        # Salida: 5

# Método de clase: se puede acceder desde la clase o la instancia, recibe cls
print(Matematica.restar(5, 3))  # Salida: 2
print(m.restar(7, 2))           # Salida: 5

# Método estático: se puede acceder desde la clase o la instancia, sin self ni cls
print(Matematica.multiplicar(4, 6))  # Salida: 24
print(m.multiplicar(2, 8))           # Salida: 16
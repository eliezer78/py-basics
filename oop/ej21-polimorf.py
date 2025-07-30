### Ejercicio 21 : Polimorfismo - Clase Figuras Geométricas

# Crea un programa que permita calcular el área de diferentes figuras geométricas 
# utilizando polimorfismo.
#
# 1. Define una clase abstracta llamada 'Figura' con un método abstracto 'calcular_area()'.
# 2. Crea al menos dos clases que hereden de 'Figura': 'Circulo' y 'Rectangulo'.
#    - 'Circulo' debe tener un atributo 'radio'.
#    - 'Rectangulo' debe tener atributos 'base' y 'altura'.
# 3. Implementa el método 'calcular_area()' en cada subclase para calcular el área apropiada.
# 4. Escribe una función 'mostrar_areas(figuras)' que reciba una lista de figuras y, 
#    usando polimorfismo, imprima el área de cada una.


from abc import ABC, abstractmethod
import math

# Clase abstracta Figura
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de la figura"""
        pass

# Clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """Calcula el área de un círculo"""
        return math.pi * self.radio ** 2

# Clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área de un rectángulo"""
        return self.base * self.altura

figuras = [
        Circulo(5),           
        Rectangulo(4, 6),     
        Circulo(2.5),         
        Rectangulo(3, 8),
        Circulo(3)      
    ]

print("=== Áreas de las Figuras ===")
for figura in figuras:
        area = figura.calcular_area()  # Polimorfismo: cada objeto responde a su propia versión de calcular_area
        print(f"El área de la figura es: {area:.2f}")
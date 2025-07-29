### Ejercicio 22: Polimorfismo - Clases Vehículo, Auto y Motocicleta
#
# Imagina que estás desarrollando un sistema para una tienda de vehículos. 
# La tienda vende autos y motocicletas. Cada tipo de vehículo debe poder 
# mostrar su propia información y calcular el impuesto de venta de manera diferente.
# Utilizando el concepto de polimorfismo, crea un sistema que permita manejar
# diferentes tipos de vehículos de forma uniforme.
#
# 1. Crea una clase base llamada `Vehiculo` con los siguientes métodos:
#    - `mostrar_info()` (método abstracto): debe mostrar información general del vehículo.
#    - `calcular_impuesto()` (método abstracto): debe devolver el monto del impuesto de venta.
#
# 2. Crea dos clases derivadas:
#    - `Auto`: debe tener atributos como marca, modelo, precio y número de puertas.
#    - `Motocicleta`: debe tener atributos como marca, modelo, precio y tipo 
#      (deportiva, scooter, etc.).
#
# 3. Implementa los métodos `mostrar_info()` y `calcular_impuesto()` en cada clase derivada:
#    - Para `Auto`, el impuesto es el 10% del precio.
#    - Para `Motocicleta`, el impuesto es el 6% del precio.
#
# 4. Escribe una función llamada `imprimir_reporte(vehiculos: list)` que reciba una lista de 
#    vehículos y, utilizando polimorfismo, imprima la información y el impuesto de cada uno.

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase base abstracta para vehículos"""
    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def calcular_impuesto(self):
        pass

class Auto(Vehiculo):
    """Clase que representa un auto"""
    def __init__(self, marca, modelo, precio, puertas):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.puertas = puertas

    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo}, Precio: ${self.precio}, Puertas: {self.puertas}")

    def calcular_impuesto(self):
        return self.precio * 0.10

class Motocicleta(Vehiculo):
    """Clase que representa una motocicleta"""
    def __init__(self, marca, modelo, precio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Motocicleta: {self.marca} {self.modelo}, Precio: ${self.precio}, Tipo: {self.tipo}")

    def calcular_impuesto(self):
        return self.precio * 0.06

def imprimir_reporte(vehiculos):
    """Imprime el reporte de vehículos"""
    print("=== REPORTE DE VEHÍCULOS ===")
    for v in vehiculos:
        v.mostrar_info()
        impuesto = v.calcular_impuesto()
        print(f"Impuesto de venta: ${impuesto:.2f}\n")

vehiculos = [
    Auto("Toyota", "Corolla", 15000, 4),
    Motocicleta("Yamaha", "MT-03", 6000, "Deportiva"),
    Auto("Ford", "Fiesta", 12000, 5),
    Motocicleta("Honda", "PCX 150", 3500, "Scooter")
]

# vehiculo = Vehiculo()  # Esto es solo para ilustrar que Vehiculo es abstracta y no se puede instanciar
imprimir_reporte(vehiculos)
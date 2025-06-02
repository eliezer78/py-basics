### Ejercicio 17: Herencia - Clase Vehiculo
#
# Imagina que estás desarrollando un sistema para una empresa de transporte. 
# Debes modelar diferentes tipos de vehículos usando clases en Python.
#
# Crea una clase base llamada Vehiculo que tenga: marca y modelo,
# y un método informacion() que imprima la marca y el modelo.
# Crea una clase derivada llamada Auto que herede de Vehiculo y además tenga:
# num_puertas y un método informacion() que además de la marca y el modelo, 
# imprima el número de puertas.
# Crea otra clase derivada llamada Moto que herede de Vehiculo y además tenga:
# cilindrada y un método informacion() que además de la marca y el modelo, imprima la cilindrada.
# Crea un objeto de tipo Auto y otro de tipo Moto, y llama a su método informacion()

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

# Clase derivada
class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def informacion(self):
        super().informacion()
        print(f"Número de puertas: {self.num_puertas}")

# Otra clase derivada
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def informacion(self):
        super().informacion()
        print(f"Cilindrada: {self.cilindrada} cc")

# Crear objetos y probar
auto1 = Auto("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "MT-07", 689)

print("Información del auto:")
auto1.informacion()

print("\nInformación de la moto:")
moto1.informacion()
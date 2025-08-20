### Clases y Objetos

class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}", end=", ")

class Perro(Animal):
    def __init__(self, nombre, edad, especie, duenio):
        super().__init__(nombre, edad, especie)
        self.duenio = duenio
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Dueño: {self.duenio}")
    
    def hablar(self):
        print("Guau guau!")

class Leon(Animal):
    def __init__(self, nombre, edad, especie, reserva):
        super().__init__(nombre, edad, especie)
        self.reserva = reserva
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Reserva: {self.reserva}")
    
    def hablar(self):
        print("Hola a todos, yo soy el león!")

perro = Perro("Dogui",3,"Canino","Juan Carlos")
leon = Leon("Robert",8,"Felino","Sahara")

perro.mostrar_info()
perro.hablar()

leon.mostrar_info()
leon.hablar()

# print(Perro.__bases__)
# print(Leon.__mro__)

def suma(a,b):
    return a + b

calculo = suma(5,6) * 2
print(calculo)


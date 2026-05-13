### Clases y Objetos ----------------------------------------------------

class Animal: # Clase
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        
    def hablar(self):
        print("Hola!!!")
        
    def moverse(seff):
        print("Estoy moviendome!")
    
perro = Animal("dogui", 3, "perro")      # Instancias de la clase: objetos
gato = Animal("michifus", 4, "gato")
pajaro = Animal("caniggia", 56, "ave")

print(perro.nombre)   # Atributos
print(gato.edad)
print(pajaro.especie) 

perro.hablar() # Métodos
gato.moverse()
pajaro.moverse()

### Herencia ------------------------------------------------------

class Persona: # Clase
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad
    
    def hablar(self):
        print("Buenas tardes!")
        
    def presentarse(self):
        print(f"Hola me llamo {self.nombre}, tengo {self.edad} años")

class Alumno(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def mostrar_datos(self):
        print(f"Hola me llamo {self.nombre}, tengo {self.edad} años y curso la carrera {self.carrera}")

# class Docente

alumno = Alumno("Lionel", 38, "Ing. Sistemas")
alumno.mostrar_datos()















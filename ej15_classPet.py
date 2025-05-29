### Ejercicio 15: Clase Mascota
# 
# Crea una clase llamada Mascota que tenga los siguientes atributos:
# nombre (string)
# especie (string)
# edad (integer)
#
# La clase debe tener los siguientes métodos:
# __init__(self, nombre, especie, edad): Constructor que inicializa los atributos.
# cumplir_anios(self): Incrementa la edad de la mascota en 1.
# mostrar_informacion(self): Muestra la información de la mascota en el siguiente 
# formato: "Nombre: [nombre], Especie: [especie], Edad: [edad] años"
#
# Crea un programa principal que:
# 1. Solicite al usuario registrar una mascota ingresando su nombre, especie y 
# edad.
# Cree un objeto de la clase Mascota con los datos ingresados.
# Permita al usuario realizar acciones como:
# 2. Mostrar la información de la mascota.
# 3. Incrementar la edad de la mascota (es decir, "cumplir años").
# 4. Salir del programa.

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad 

    def cumplir_anios(self):
        self.edad += 1
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años")

# Programa principal
print("Sistema de Gestión de Mascotas")
nombre = input("Ingrese el nombre de la mascota: ")
especie = input("Ingrese la especie de la mascota: ")
edad = int(input("Ingrese la edad de la mascota: "))
    
# Crear un objeto de la clase Mascota
mascota = Mascota(nombre, especie, edad)

while True:
    print("\n1. Mostrar información de la mascota")
    print("2. Cumplir años (incrementar edad)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mascota.mostrar_informacion()
    elif opcion == "2":
        mascota.cumplir_anios()
        print(f"{mascota.nombre} ha cumplido un año más.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

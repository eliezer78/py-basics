### Ejercicio 16: Clase Estudiante

# Crear una clase llamada Estudiante que tenga los siguientes atributos:
# nombre (string)
# edad (integer)
# carrera (string)
# calificaciones (list)
#
# La clase debe tener los siguientes métodos:
# __init__(self, nombre, edad, carrera): Constructor que inicializa el nombre, 
#    edad y carrera del estudiante. Inicializa también calificaciones como 
#    una lista vacía.
# agregar_calificacion(self, calificacion): Agrega una nueva calificación 
#                                           al estudiante.
# calcular_promedio(self): Calcula y devuelve el promedio de las calificaciones. 
#                          Si no hay calificaciones, devuelve 0.
# mostrar_informacion(self): Muestra toda la información del estudiante, 
#                            incluyendo su promedio.
# 
# Solicite al usuario ingresar el nombre, edad y carrera de un estudiante.
# Cree un objeto de la clase Estudiante con los datos ingresados.
# Permita al usuario agregar calificaciones al estudiante.
# Muestre la información completa del estudiante al final.

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.calcular_promedio():.2f}")

# Programa principal
print("Sistema de Gestión de Estudiantes")
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
carrera = input("Ingrese la carrera del estudiante: ")

# Crear un objeto de la clase Estudiante
estudiante = Estudiante(nombre, edad, carrera)

while True:
    print("\n1. Agregar calificación")
    print("2. Mostrar información del estudiante")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        calificacion = float(input("Ingrese la calificación: "))
        estudiante.agregar_calificacion(calificacion)
    elif opcion == "2":
        estudiante.mostrar_informacion()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
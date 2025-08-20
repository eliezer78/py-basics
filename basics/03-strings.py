# Strings

# Formateo
nombre, apellido, edad = "Lionel", "Messi", 37

print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido,edad))

print("Mi nombre es %s %s y mi edad es %d" % (nombre, apellido, edad))

print("Mi nombre es " + nombre + " " + apellido + " y mi edad es " + str(edad))

print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

import random
numeros = range(1, 11)
posicion_aleatoria = 4
elemento_aleatorio = numeros[posicion_aleatoria]
print(f"El número aleatorio elegido es: {elemento_aleatorio}")
print(numeros[4])

# Solicitar al usuario que ingrese los números separados por comas
entrada = input("Ingresa los números separados por comas: ")

# Convertir la entrada en una lista de enteros
lista = [int(num) for num in entrada.split(",")]

# Crear un diccionario para contar las ocurrencias
diccio = {}
for i in lista:
    if i in diccio:
        diccio[i] += 1
    else:
        diccio[i] = 1

# Mostrar la lista y el diccionario en pantalla
print("Lista:", lista)
print("Diccionario de ocurrencias:", diccio)
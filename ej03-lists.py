import random

# Solicitar al usuario la cantidad de valores aleatorios
x = int(input("Ingresa la cantidad de valores aleatorios que deseas generar: "))

# Generar la lista con valores aleatorios entre 1 y 100
valores = [random.randint(1, 100) for _ in range(x)]
print("Lista generada:", valores)

# Obtener el mayor y el menor valor de la lista
mayor = max(valores)
menor = min(valores)
print("El mayor valor es:", mayor)
print("El menor valor es:", menor)

# Imprimir los valores en posiciones pares e impares
pares = [valores[i] for i in range(len(valores)) if i % 2 == 0]  # Posiciones pares
impares = [valores[i] for i in range(len(valores)) if i % 2 != 0]  # Posiciones impares
print("Valores en posiciones pares:", pares)
print("Valores en posiciones impares:", impares)

# Crear dos listas nuevas con valores pares e impares
valores_pares = [num for num in valores if num % 2 == 0]
valores_impares = [num for num in valores if num % 2 != 0]
print("Lista de valores pares:", valores_pares)
print("Lista de valores impares:", valores_impares)
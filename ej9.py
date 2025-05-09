# Cargar una matriz de números enteros y mostrarla en pantalla.
# Se debe permitir al usuario ingresar el número de filas y columnas de la matriz. 
# La matriz debe ser cargada por el usuario, quien ingresará los valores fila por fila.
# Finalmente, se debe imprimir la matriz de forma legible.

# Ingreso de medidas de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))    

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

print("Matriz:")
for fila in matriz:
    print(fila)
    

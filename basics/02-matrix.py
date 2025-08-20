def cargar_matriz():
    """
    Permite al usuario cargar los valores de una matriz.
    """
    # Solicitar el número de filas y columnas de la matriz
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))

    # Inicializar la matriz vacía
    matriz = []

    # Pedir al usuario que ingrese los valores fila por fila
    print("Introduce los valores de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)

    return matriz

def imprimir_matriz(matriz):
    """
    Imprime la matriz de forma legible.
    """
    print("Matriz:")
    for fila in matriz:
        print(fila)

# Programa principal
if __name__ == "__main__":
    matriz = cargar_matriz()
    imprimir_matriz(matriz)
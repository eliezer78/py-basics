def sumar_mat(matriz1, matriz2):
    """    Suma dos matrices del mismo tamaño."""

    # Verificar que las dimensiones sean iguales
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    # Sumar las matrices
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    
    return resultado

def imprimir_mat(matriz):
    """Imprime una matriz de forma legible."""
    for fila in matriz:
        print(fila)

# Programa principal
if __name__ == "__main__":
    # Ejemplo de matrices
    matriz1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    matriz2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

    print("Matriz 1:")
    imprimir_mat(matriz1)

    print("\nMatriz 2:")
    imprimir_mat(matriz2)

    # Sumar las matrices
    try:
        suma = sumar_mat(matriz1, matriz2)
        print("\nSuma de las matrices:")
        imprimir_mat(suma)
    except ValueError as e:
        print(e)


import numpy as np

# Crear una matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Acceder a elementos
print(matriz[0, 1])  # Accede al elemento en la posición (0,1): 2

# Modificar un elemento
matriz[1, 2] = 9
print(matriz)

# Operaciones con matrices
matriz2 = np.array([[7, 8, 9], [10, 11, 12]])
suma = matriz + matriz2
print(suma)  # [[ 8 10 12]
#  [14 16 18]]

# Transponer una matriz
transpuesta = matriz.T
print(transpuesta)
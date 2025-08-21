### PACKAGE MANAGER
### PyPI (Python Package Index) - PIP

# importar numpy
import numpy as np

# Crear un array a partir de una lista
a = np.array([1, 2, 3, 4, 5])
print("Array:", a)

# Crear una matriz 2D
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", b)

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)   # suma elemento a elemento
print(x * y)   # multiplicación elemento a elemento
print(x ** 2)  # potencia

data = np.array([10, 20, 30, 40, 50])

print("Media:", np.mean(data))
print("Mediana:", np.median(data))
print("Desviación estándar:", np.std(data))
print("Varianza:", np.var(data))

# Importar pandas
import pandas as pd

# Crear un DataFrame (tabla)
data = {
    "Nombre": ["Ana", "Luis", "Carla"],
    "Edad": [23, 34, 29],
    "Ciudad": ["Madrid", "Buenos Aires", "México DF"]
}

df = pd.DataFrame(data)
print(df)

# Seleccionar columna
print(df["Nombre"])

# Filtrar filas (edad mayor a 25)
print(df[df["Edad"] > 25])

# importar requests
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
print("Chiste:", data["value"])

# importar mi paquete
from mypackage import calculator

print(calculator.suma(1,2))
print(calculator.producto(5,3))

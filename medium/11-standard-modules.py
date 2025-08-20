### Python Standard Library

# math, datetime, random, textwrap, 
# array, sys, os, json, re, statistics

import math

print(math.sqrt(16))
print(math.pi)
print(math.sin(math.pi / 2))
print(math.log(100, 10))
print(math.factorial(5))
print(math.gcd(48, 180))

import datetime

now = datetime.datetime.now()
print("Fecha y hora actual:", now)
print("Año:", now.year)
print("Mes:", now.month)
print("Día:", now.day)
print("Dentro de 5 días:", now + datetime.timedelta(days=5))

import random

rdm = random.randint(1, 100)
print("Número aleatorio:", rdm)

import array

a = array.array('i', [1, 2, 3, 4, 5])
print(sum(a))
print(a[1:4])



"""
import numpy as np

array = np.array([1, 2, 3])

print(array * 2)

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
# print(df["Nombre"])

# Filtrar filas (edad mayor a 25)
# print(df[df["Edad"] > 25])

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
print("Chiste:", data["value"])


from mypackage import maths

sum_result = maths.sum_two_values(5, 7)
print("Suma:", sum_result)
"""
### PYTHON STANDARD LIBRARY

# math, datetime, random, textwrap, 
# array, sys, os, json, re, statistics

from math import sqrt, pi, sin, log, factorial, gcd

print(sqrt(16))
print(pi)
print(sin(pi / 2))
print(log(100, 10))
print(factorial(5))
print(gcd(48, 180, 456))

from datetime import datetime, timedelta

now = datetime.now()
print("Fecha y hora actual:", now)
print("Año:", now.year)
print("Mes:", now.month)
print("Día:", now.day)
print("Dentro de 5 días:", now + timedelta(days=5))

import random

rdm = random.randint(1, 100)
print("Número aleatorio:", rdm)


from array import array

a = array('i', [1, 2, 3, 4, 5])
m = array('u', ["a","b","c"])
print(sum(a))
print(a[1:2])

import textwrap

doc = "La Biblioteca Estándar de Python (Python Standard Library, o PSL) es una extensa colección de módulos y paquetes que vienen incluidos con la instalación de Python. Es una de las características más importantes del lenguaje, ya que provee una gran cantidad de funcionalidades listas para usar sin necesidad de instalar nada adicional."

print(textwrap.fill(doc, width=80))

import os

print("Directorio actual:", os.getcwd())
print("Archivos en el directorio:", os.listdir('.'))
print("Ruta absoluta del script:", os.path.abspath(__file__))
# Ejemplo de manejo de excepciones en Python
# Este programa solicita al usuario que ingrese un número y maneja la excepción

















"""
with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if not linea:
            continue
        print(linea.strip())
"""
"""
# while True:
try:
    num = float(input("Ingrese un número:"))
    print("El número ingresado es:", num)
    a = 2 / 0
    print("Fin del bloque try-except.")
    #break
except ValueError:
    print("Error: No se ingresó un número válido.")
except KeyboardInterrupt:
    print("\nError: Se interrumpió el programa.")
    #break
except Exception as e:
    print("Error inesperado:", e)
    #break
finally:
    print("Fin del bloque finally.")
"""     

# Ejemplo de manejo de excepciones en Python
# Este programa intenta abrir un archivo y leer un número entero de él.
# Si el archivo no existe o el contenido no es un número entero, 
# maneja la excepción.

import sys

try:
    f = open("notas.txt")
    s = f.readline()
    i = int(s.strip())
    print("El número es:", i)
except OSError as err:
    print("Error de sistema:", err) 
except ValueError:
    print("Error: No se pudo convertir a entero.")
except Exception as err:
    print("Error inesperado:", err)   



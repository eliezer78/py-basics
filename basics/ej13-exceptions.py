# Ejercicio Práctico: Lector de notas de alumnos desde archivo
#
# Escribe un programa en Python que lea un archivo de texto llamado `notas.txt`, 
# donde cada línea contiene el nombre de un estudiante y su nota separados por 
# una coma.
# El programa debe manejar las siguientes excepciones:
# - Si el archivo no existe, debe mostrar un mensaje de error: 
# "Error: El archivo no existe."
# - Si una línea no tiene el formato correcto (nombre, nota), 
# debe mostrar un mensaje de error:
#   "Error en línea: <línea>. Formato incorrecto."
# - Si la nota no es un número válido, debe mostrar un mensaje de error:
#   "Error: Nota inválida para el estudiante <nombre>."
#
# El programa debe imprimir el nombre y la nota de cada estudiante en el formato:
# "Alumno: <nombre> | Nota: <nota>"
import matplotlib
try:
    with open("notas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue  # Salta líneas vacías
            try:
                nombre, nota = linea.split(",")
                nombre = nombre.strip()
                nota = float(nota.strip())
                print(f"Alumna/o: {nombre} | Nota: {nota}")
            except Exception:
                print(f"Error en línea: {linea}. Formato incorrecto.")
except FileNotFoundError:
        print("Error: El archivo no existe.")

print("Fin del programa.")
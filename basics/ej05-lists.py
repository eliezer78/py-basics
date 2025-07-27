# #Crear una lista con números aleatorios y contar el número de repeticiones de cada número.
# Imprimir un menu con las opciones: 
# 1. Crear una nueva lista con número enteros aleatorios seleccionando la cantidad de numeros y entre 0 y cual hacerlo  
# 2. Imprimir la lista creada, sino está creada mandar un mensaje de aviso 
# 3. Mostrar las repeticiones de cada elemento 
# 4. Mostrar los porcentajes de repeticion  
# 5. Generar una lista nueva sin los elementos repetidos 
# 6 Salir

import random

# Funciones para las diferentes operaciones del menú
def crear_lista():
    """Permite crear una nueva lista con números aleatorios."""
    cantidad = int(input("¿Cuántos números aleatorios deseas generar? "))
    max_num = int(input("¿Cuál será el número máximo (de 0 a este número)? "))
    return [random.randint(0, max_num) for _ in range(cantidad)]

def imprimir_lista(lista):
    """Imprime la lista creada."""
    if lista is None:
        print("No se ha creado ninguna lista aún.")
    else:
        print("Lista actual:", lista)

def contar_repeticiones(lista):
    """Cuenta las repeticiones de cada número en la lista."""
    if lista is None:
        print("No se ha creado ninguna lista aún.")
    else:
        conteo = {}
        for num in lista:
            conteo[num] = conteo.get(num, 0) + 1
        print("Repeticiones por número:", conteo)
        return conteo

def mostrar_porcentajes(lista, conteo):
    """Muestra los porcentajes de repetición de cada número."""
    if lista is None:
        print("No se ha creado ninguna lista aún.")
    elif conteo is None:
        print("Primero debes contar las repeticiones.")
    else:
        total = len(lista)
        porcentajes = {num: (count / total) * 100 for num, count in conteo.items()}
        print("Porcentajes de repetición:")
        for num, porcentaje in porcentajes.items():
            print(f"El número {num} se repite un {porcentaje:.2f}%.")

def generar_lista_sin_repetidos(lista):
    """Genera una nueva lista sin elementos repetidos."""
    if lista is None:
        print("No se ha creado ninguna lista aún.")
    else:
        lista_sin_repetidos = list(set(lista))
        print("Nueva lista sin elementos repetidos:", lista_sin_repetidos)

# Programa principal
def menu():
    lista = None
    conteo = None

    while True:
        # Imprimir menú
        print("\n--- Menú de Operaciones ---")
        print("1. Crear una nueva lista con números aleatorios")
        print("2. Imprimir la lista creada")
        print("3. Mostrar las repeticiones de cada elemento")
        print("4. Mostrar los porcentajes de repetición")
        print("5. Generar una lista nueva sin los elementos repetidos")
        print("6. Salir")

        # Solicitar opción al usuario
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            lista = crear_lista()
            conteo = None  # Reiniciar el conteo al generar una nueva lista
        elif opcion == '2':
            imprimir_lista(lista)
        elif opcion == '3':
            conteo = contar_repeticiones(lista)
        elif opcion == '4':
            mostrar_porcentajes(lista, conteo)
        elif opcion == '5':
            generar_lista_sin_repetidos(lista)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
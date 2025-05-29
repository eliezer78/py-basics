import random

def generar_lista(cantidad):
    """Generar una lista de números aleatorios."""
    return [random.randint(1, 100) for _ in range(cantidad)]

def mostrar_lista(lista):
    """Mostrar la lista generada."""
    print("Lista generada:", lista)

def mostrar_mayor(lista):
    """Mostrar el valor máximo de la lista."""
    print("El mayor valor es:", max(lista))

def mostrar_menor(lista):
    """Mostrar el valor mínimo de la lista."""
    print("El menor valor es:", min(lista))

def calcular_suma(lista):
    """Calcular y mostrar la suma de los elementos de la lista."""
    print("La suma de los valores es:", sum(lista))

def calcular_promedio(lista):
    """Calcular y mostrar el promedio de los elementos de la lista."""
    promedio = sum(lista) / len(lista)
    print("El promedio de los valores es:", promedio)

def menu_operaciones(lista):
    """Menú interactivo para seleccionar operaciones con la lista."""
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Mostrar la lista")
        print("2. Mostrar el mayor de la lista")
        print("3. Mostrar el menor de la lista")
        print("4. Calcular la suma de los elementos")
        print("5. Calcular el promedio de los elementos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            mostrar_lista(lista)
        elif opcion == '2':
            mostrar_mayor(lista)
        elif opcion == '3':
            mostrar_menor(lista)
        elif opcion == '4':
            calcular_suma(lista)
        elif opcion == '5':
            calcular_promedio(lista)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Programa principal
if __name__ == "__main__": # Verifica si el archivo se está ejecutando como un programa principal
    cantidad = int(input("Ingresa la cantidad de valores aleatorios que deseas generar: "))
    lista = generar_lista(cantidad)
    menu_operaciones(lista)
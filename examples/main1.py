def saludar():
    print("Hola desde la función saludar.")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a,end=' ')
        a, b = b, a + b
    print()


# Este bloque se ejecuta solo si el archivo se ejecuta directamente
# y no si se importa como un módulo.
# Esto es útil para pruebas o para ejecutar código específico
# cuando el archivo es el programa principal.
# de Python.
if __name__ == "__main__":
    print("Este archivo se ejecuta directamente.")
    saludar()
    fibonacci(10)
    print(fibonacci2(10))
    
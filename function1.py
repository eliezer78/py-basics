def sumar(a, b):
    """Esta función suma dos números y devuelve el resultado.""" # Docstring
    # La cadena de documentación (docstring) describe la función y su propósito.
    return a + b

a =input("Ingresa el primer número: ")
b =input("Ingresa el segundo número: ")
resultado = sumar(a, b)
print(sumar.__doc__)  # Muestra: Esta función suma dos números y devuelve el resultado.
print("La suma es:", resultado)  # Muestra: La suma es: 3


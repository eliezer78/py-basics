# Algoritmo 1: Contar cuántas veces aparece el carácter "a" en una cadena de 10 caracteres
def contar_a(cadena):
    if len(cadena) != 10:
        return "La cadena debe tener exactamente 10 caracteres."
    return cadena.count("a")

# Algoritmo 2: Contar un carácter específico en una cadena de 10 caracteres
def contar_caracter(cadena, caracter):
    if len(cadena) != 10:
        return "La cadena debe tener exactamente 10 caracteres."
    return cadena.count(caracter)

# Ejemplo de uso:
cadena = input("Ingresa una cadena de 10 caracteres: ")

# Algoritmo 1: Contar "a"
resultado_a = contar_a(cadena)
print(f"El carácter 'a' aparece {resultado_a} veces en la cadena.")

# Algoritmo 2: Contar un carácter específico
caracter = input("Ingresa el carácter que deseas contar: ")
resultado_caracter = contar_caracter(cadena, caracter)
print(f"El carácter '{caracter}' aparece {resultado_caracter} veces en la cadena.")

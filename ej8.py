# Programa que permite al usuario jugar a adivinar un número 
# dentro de un rango definido por el usuario.
# El usuario tiene un número limitado de intentos para adivinar el número correcto.
# El programa termina cuando el usuario adivina el número o se queda sin intentos.

import random

def juego_adivina_el_numero():
    """
    Juego donde el usuario debe adivinar un número dentro de un rango con un número limitado de intentos.
    """
    print("¡Bienvenido al juego de adivinar el número!")
    
    # Pedir al usuario el rango de números
    rango_inferior = int(input("Ingrese el límite inferior del rango: "))
    rango_superior = int(input("Ingrese el límite superior del rango: "))
    
    # Validar que el rango sea válido
    if rango_inferior >= rango_superior:
        print("El límite inferior debe ser menor que el límite superior. Inténtelo de nuevo.")
        return
    
    # Generar un número aleatorio dentro del rango
    numero_secreto = random.randint(rango_inferior, rango_superior)
    
    # Pedir al usuario el número de intentos
    intentos = int(input("¿Cuántos intentos quieres tener? "))
    
    print(f"\nAdivina el número entre {rango_inferior} y {rango_superior}. ¡Tienes {intentos} intentos!")
    
    # Bucle para que el usuario adivine
    for intento in range(1, intentos + 1):
        try:
            # Pedir al usuario que adivine
            adivinanza = int(input(f"Intento {intento}/{intentos}: "))
            
            # Comparar la adivinanza con el número secreto
            if adivinanza == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intento} intentos.")
                break
            elif adivinanza < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        
        # Si se terminan los intentos
        if intento == intentos:
            print(f"Lo siento, te has quedado sin intentos. El número secreto era {numero_secreto}.")
            break

# Programa principal
if __name__ == "__main__":
    juego_adivina_el_numero()
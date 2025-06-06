# Programa que realiza un algoritmo al estilo de bola 8, 
# que genere 9 respuestas automaticas y aleatorias, usando una funcion.
# El usuario puede hacer preguntas y el programa responderá con una de las respuestas predefinidas.
# El programa termina cuando el usuario escribe "salir".
# Se utiliza la librería random para generar respuestas aleatorias.

import random

def bola_8():
    """
    Genera una respuesta aleatoria al estilo de la Bola 8 Mágica.
    """
    respuestas = [
        "Sí, definitivamente.",
        "Las señales apuntan a que sí.",
        "Sin duda alguna.",
        "No cuentes con ello.",
        "Mis fuentes dicen que no.",
        "Es muy dudoso.",
        "Pregunta más tarde.",
        "No puedo predecirlo ahora.",
        "Concéntrate y vuelve a intentarlo."
    ]
    return random.choice(respuestas)

# Programa principal
if __name__ == "__main__":
    print("¡Bienvenido a la Bola 8 Mágica!")
    while True:
        pregunta = input("\nHaz una pregunta (o escribe 'salir' para terminar): ")
        if pregunta.lower() == "salir":
            print("¡Gracias por jugar con la Bola 8 Mágica! ¡Hasta luego!")
            break
        respuesta = bola_8()
        print(f"Bola 8 dice: {respuesta}")
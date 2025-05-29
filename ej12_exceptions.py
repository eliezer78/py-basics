# Ejercicio Práctico: Calculadora de divisiones
#
# Crea un programa en Python que reciba una lista de pares de números 
# (dividendo y divisor) e intente realizar la división de cada par. 
# 
# El programa debe manejar los siguientes casos utilizando bloques try y except:
# Si el divisor es cero, debe mostrar un mensaje de error: "Error: No se puede 
# dividir por cero."
# Si alguno de los valores no es un número válido (por ejemplo, una letra), 
# debe mostrar: 
# "Error: Entrada inválida. Ambos valores deben ser números."
# Si la división es exitosa, debe imprimir el resultado en el formato: 
# "Resultado de dividir X entre Y es Z"

while True:
    try:
        n = int(input("¿Cuántos pares de números vas a ingresar? "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
    else:
        if n <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            break

for i in range(1, n + 1):
        while True:
            print(f"Par {i}:")
            try:
                a = float(input("  Introduce el dividendo: "))
                b = float(input("  Introduce el divisor: "))
                resultado = a / b
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.\n")
            except ValueError:
                print("Error: Entrada inválida. Ambos valores deben ser números.\n")
            except KeyboardInterrupt:
                print("\nError: Se interrumpió el programa.")
                break
            else:
                print(f"Resultado de dividir {a} entre {b} es {resultado}\n")
                break
            
print("Fin del programa.")

    
# Una empresa automotriz necesita un programa para manejar los montos de ventas de sus N sucursales, 
# a lo largo de los últimos M años.
# Los datos son dados de esta forma: M, N 
# MONTO 1 1 MONTO 1 2 ….. MONTO 1 N 
# MONTO 2 1 MONTO 2 2 ….. MONTO 2 N
# MONTO M 1 MONTO M 2 ….. MONTO M N 
# Donde: M es una variable entera que representa el número de años entre 1 y 30 inclusive. 
# N es una variable entera que representa el número de sucursales de la empresa entre 1 y 35 inclusive. 
# MONTO i j Variable real (matriz de 2 dimensiones) representa lo que se vendió en el año I en la sucursal J 
# La información que necesitan los directores de la empresa para tomar decisiones es la siguiente:
# a. Sucursal que más ha vendido en los M años.
# b. Promedio de ventas por año. 
# c. Año con mayor promedio de ventas.

# Programa para manejar los montos de ventas de sucursales en M años y N sucursales

def obtener_datos():
    """Solicita al usuario el número de años (M) y sucursales (N) y los datos de ventas."""
    while True:
        try:
            M = int(input("Ingrese el número de años (entre 1 y 30): "))
            N = int(input("Ingrese el número de sucursales (entre 1 y 35): "))
            if 1 <= M <= 30 and 1 <= N <= 35: 
                break
            else:
                print("Valores fuera de rango. Inténtelo nuevamente.")
        except ValueError:
            print("Entrada inválida. Inténtelo nuevamente.")
    
    ventas = []
    print(f"Ingrese los montos de ventas por año y sucursal (total {M} años y {N} sucursales):")
    for i in range(M):
        anio = []
        print(f"Año {i + 1}:")
        for j in range(N):
            while True:
                try:
                    monto = float(input(f"  Sucursal {j + 1}: "))
                    anio.append(monto)
                    break
                except ValueError:
                    print("Monto inválido. Inténtelo nuevamente.")
        ventas.append(anio)

    return M, N, ventas

def sucursal_mas_vendida(ventas):
    """Calcula la sucursal que más ha vendido en todos los años."""
    total_por_sucursal = [sum(sucursal) for sucursal in zip(*ventas)]
    sucursal_max = total_por_sucursal.index(max(total_por_sucursal)) + 1
    return sucursal_max

def promedio_ventas_anuales(ventas):
    """Calcula el promedio de ventas por año."""
    promedios = [sum(anio) / len(anio) for anio in ventas]
    return promedios

def anio_mayor_promedio(promedios):
    """Encuentra el año con el mayor promedio de ventas."""
    anio_max = promedios.index(max(promedios)) + 1
    return anio_max

def main():
    # Obtener los datos de ventas
    M, N, ventas = obtener_datos()

    # a. Sucursal que más ha vendido en los M años
    sucursal_max = sucursal_mas_vendida(ventas)
    print(f"\nSucursal que más ha vendido en todos los años: Sucursal {sucursal_max}")

    # b. Promedio de ventas por año
    promedios = promedio_ventas_anuales(ventas)
    print("\nPromedio de ventas por año:")
    for i, promedio in enumerate(promedios, start=1):
        print(f"  Año {i}: {promedio:.2f}")

    # c. Año con mayor promedio de ventas
    anio_max = anio_mayor_promedio(promedios)
    print(f"\nAño con mayor promedio de ventas: Año {anio_max}")

if __name__ == "__main__":
    main()
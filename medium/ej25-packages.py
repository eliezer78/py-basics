import random
import math
import numpy as np
import pandas as pd
import datetime as dt
from array import array

# --- EJERCICIO 1 ---
# Crea una función que genere una lista de 200 temperaturas (flotantes) aleatorias
# entre 10.0 y 40.0 grados Celsius.
# Luego, utilizando numpy y el módulo math, calcula y muestra:
# 1. El promedio de las temperaturas.
# 2. La desviación estándar.
# 3. El valor mínimo y máximo.

# Solución:

def analizar_temperaturas_aleatorias():
    """
    Genera y analiza una lista de temperaturas aleatorias.
    """
    print("--- Ejercicio 1: Analizador de Temperaturas ---")
    
    # Generar un array de temperaturas aleatorias usando numpy
    temperaturas = np.random.uniform(10.0, 40.0, 200)

    # Convertir a un array de Python para demostrar el uso de array.
    # Nota: np.array es más común en la práctica para este tipo de operaciones.
    temperaturas_array = array('f', temperaturas)

    # Convertir de nuevo a numpy para los cálculos eficientes
    np_temperaturas = np.array(temperaturas_array)

    # 1. Calcular el promedio usando numpy
    promedio = np.mean(np_temperaturas)

    # 2. Calcular la desviación estándar usando numpy
    desviacion_estandar = np.std(np_temperaturas)

    # 3. Calcular el mínimo y máximo
    minimo = np.min(np_temperaturas)
    maximo = np.max(np_temperaturas)

    print(f"Temperaturas generadas (primeros 5): {np_temperaturas[:5]}")
    print(f"Temperatura promedio: {promedio:.2f}°C")
    print(f"Desviación estándar: {desviacion_estandar:.2f}°C")
    print(f"Temperatura mínima: {minimo:.2f}°C")
    print(f"Temperatura máxima: {maximo:.2f}°C")

# Ejecutar el ejercicio 1
analizar_temperaturas_aleatorias()

print("\n" + "="*50 + "\n")


# --- EJERCICIO 2 ---
# Utilizando la Programación Orientada a Objetos (POO), crea una clase llamada
# 'Tarea' que tenga como atributos:
# - nombre (string)
# - fecha_limite (dt.date)
# - estado (string: 'pendiente', 'completada')
# La clase debe tener un método para verificar el estado y calcular los días
# restantes (o pasados) hasta la fecha límite.

# Luego, crea una lista de 5 instancias de la clase 'Tarea' con fechas límite
# aleatorias (usando random y datetime). Recorre la lista, llama al método
# de la clase y muestra la información de cada tarea.

# Solución:

class Tarea:
    """
    Representa una tarea con una fecha límite.
    """
    def __init__(self, nombre, fecha_limite, estado='pendiente'):
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.estado = estado

    def obtener_informacion(self):
        """
        Calcula los días restantes o pasados y retorna un resumen.
        """
        hoy = dt.date.today()
        diferencia = self.fecha_limite - hoy
        dias_restantes = diferencia.days

        if self.estado == 'completada':
            return f"Tarea: '{self.nombre}' | Estado: Completada."
        elif dias_restantes > 0:
            return f"Tarea: '{self.nombre}' | Estado: Pendiente. Faltan {dias_restantes} días."
        elif dias_restantes == 0:
            return f"Tarea: '{self.nombre}' | Estado: Pendiente. ¡Es la fecha límite hoy!"
        else:
            return f"Tarea: '{self.nombre}' | Estado: Pendiente. Vencida hace {-dias_restantes} días."

def gestor_de_tareas():
    """
    Crea y gestiona una lista de tareas.
    """
    print("--- Ejercicio 2: Gestor de Tareas ---")

    nombres = ["Proyecto A", "Informe", "Reunión", "Presentación", "Revisión"]
    tareas = []

    for nombre in nombres:
        # Generar fechas aleatorias en los próximos 30 días o pasadas
        dias_aleatorios = random.randint(-15, 30)
        fecha_limite = dt.date.today() + dt.timedelta(days=dias_aleatorios)
        
        # Simular una tarea completada al azar
        estado = 'completada' if random.random() < 0.2 else 'pendiente'
        
        tareas.append(Tarea(nombre, fecha_limite, estado))

    # Recorrer la lista y mostrar la información de cada tarea
    for tarea in tareas:
        print(tarea.obtener_informacion())

# Ejecutar el ejercicio 2
gestor_de_tareas()

print("\n" + "="*50 + "\n")


# --- EJERCICIO 3 ---
# Crea una clase llamada 'AnalizadorVentas' que, al ser inicializada,
# genere un DataFrame de pandas con datos de ventas.
# El DataFrame debe contener 100 filas y las columnas:
# - 'Fecha' (fechas aleatorias del último mes)
# - 'Producto' (elegido al azar de una lista de 5 productos)
# - 'Monto' (números aleatorios entre 50 y 500)
#
# La clase debe tener los siguientes métodos:
# - `calcular_ventas_por_producto()`: Agrupa los datos por 'Producto' y suma los 'Monto',
#   retornando un Series de pandas.
# - `obtener_promedio_diario()`: Calcula el promedio de ventas por día y lo retorna.
# - `filtrar_ventas_altas(monto_minimo)`: Retorna un nuevo DataFrame con las ventas
#   que superen un monto mínimo dado.

# Solución:

class AnalizadorVentas:
    """
    Clase para generar y analizar un DataFrame de ventas.
    """
    def __init__(self):
        self.df = self._generar_dataframe_ventas()

    def _generar_dataframe_ventas(self):
        """
        Método interno para generar el DataFrame de ventas.
        """
        print("--- Ejercicio 3: Analizador de Datos de Ventas ---")
        
        productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora']
        
        # Generar 100 fechas aleatorias en el último mes
        hoy = dt.date.today()
        fechas = [hoy - dt.timedelta(days=random.randint(0, 30)) for _ in range(100)]
        
        # Generar 100 productos aleatorios
        productos_aleatorios = random.choices(productos, k=100)
        
        # Generar 100 montos aleatorios
        montos = np.random.randint(50, 501, 100)

        # Crear el DataFrame
        df = pd.DataFrame({
            'Fecha': fechas,
            'Producto': productos_aleatorios,
            'Monto': montos
        })
        
        print("DataFrame de Ventas generado:")
        print(df.head())
        return df

    def calcular_ventas_por_producto(self):
        """
        Calcula y retorna las ventas totales por producto.
        """
        print("\nVentas totales por producto:")
        ventas_por_producto = self.df.groupby('Producto')['Monto'].sum()
        print(ventas_por_producto)
        return ventas_por_producto

    def obtener_promedio_diario(self):
        """
        Calcula y retorna el promedio de ventas por día.
        """
        print("\nPromedio de ventas diario:")
        promedio_diario = self.df.groupby('Fecha')['Monto'].sum().mean()
        print(f"El promedio diario de ventas es: {promedio_diario:.2f}")
        return promedio_diario

    def filtrar_ventas_altas(self, monto_minimo):
        """
        Retorna un DataFrame con ventas superiores a un monto mínimo.
        """
        print(f"\nFiltrando ventas mayores a ${monto_minimo}:")
        ventas_altas = self.df[self.df['Monto'] > monto_minimo]
        print(ventas_altas)
        return ventas_altas

# Ejecutar el ejercicio 3
analizador = AnalizadorVentas()
analizador.calcular_ventas_por_producto()
analizador.obtener_promedio_diario()
analizador.filtrar_ventas_altas(400)


print("\n" + "="*50 + "\n")


# --- EJERCICIO 4 ---
# Simula el valor de una inversión inicial de $10,000 durante un año (252 días hábiles).
# Para ello, genera rendimientos diarios aleatorios (cambios porcentuales diarios).
# Los rendimientos diarios siguen una distribución normal con una media de 0.03% y
# una desviación estándar de 0.8%.
#
# Utiliza numpy para generar los rendimientos y pandas para gestionar el valor de
# la inversión a lo largo del tiempo.
#
# Muestra:
# 1. El valor final de la inversión.
# 2. El rendimiento total anual.
# 3. Un resumen de las estadísticas de la serie de inversión (promedio, std, etc.).

# Solución:

def simular_inversion():
    """
    Simula el valor de una inversión en el tiempo.
    """
    print("--- Ejercicio 4: Simulación de Inversión ---")
    
    inversion_inicial = 10000
    dias_simulados = 252 # Un año de días hábiles

    # Generar rendimientos diarios aleatorios usando numpy
    media_rendimiento = 0.0003
    std_rendimiento = 0.008
    rendimientos = np.random.normal(media_rendimiento, std_rendimiento, dias_simulados)

    # Crear una serie de pandas para el valor de la inversión
    # El valor inicial es el primer elemento de la serie
    valores = pd.Series(np.zeros(dias_simulados))
    valores[0] = inversion_inicial * (1 + rendimientos[0])

    # Calcular el valor acumulado para cada día
    for i in range(1, dias_simulados):
        valores[i] = valores[i-1] * (1 + rendimientos[i])

    valor_final = valores.iloc[-1]
    rendimiento_total = (valor_final / inversion_inicial) - 1

    print(f"El valor de la inversión inicial fue: ${inversion_inicial}")
    print(f"El valor final de la inversión después de {dias_simulados} días es: ${valor_final:.2f}")
    print(f"El rendimiento total de la inversión fue del: {rendimiento_total:.2%}")

    # Mostrar un resumen estadístico de la serie de inversión
    print("\nResumen estadístico del valor de la inversión a lo largo del tiempo:")
    print(valores.describe().to_string())


# Ejecutar el ejercicio 4
simular_inversion()


# --- EJERCICIO 5 ---
# Crea una clase llamada `SimuladorPoblacion` que simule el crecimiento
# de una población a lo largo del tiempo.
# La clase debe tener los siguientes métodos:
# 1. `__init__(poblacion_inicial, tasa_crecimiento, anios)`: Inicializa
#    los atributos.
# 2. `simular_crecimiento()`: Utiliza la librería `numpy` para generar
#    una serie de pandas que represente la población a lo largo de los
#    años, aplicando la fórmula de crecimiento exponencial.
# 3. `obtener_datos_finales()`: Retorna un diccionario con la población
#    final y el total de años.

# La fórmula de crecimiento exponencial es: P(t) = P0 * (1 + r)^t
# Donde:
# P(t) = población en el tiempo t
# P0 = población inicial
# r = tasa de crecimiento
# t = años

# Solución:

class SimuladorPoblacion:
    """
    Simula el crecimiento exponencial de una población.
    """
    def __init__(self, poblacion_inicial, tasa_crecimiento, anios):
        self.poblacion_inicial = poblacion_inicial
        self.tasa_crecimiento = tasa_crecimiento
        self.anios = anios
    
    def simular_crecimiento(self):
        """
        Calcula el crecimiento de la población a lo largo de los años.
        Retorna un DataFrame de pandas.
        """
        print("--- Ejercicio 5: Simulador de Población ---")
        
        # Generar un rango de años usando numpy
        tiempos = np.arange(self.anios + 1)
        
        # Calcular la población para cada año usando la fórmula
        poblacion = self.poblacion_inicial * np.power(1 + self.tasa_crecimiento, tiempos)
        
        # Crear un DataFrame para una mejor visualización de los datos
        df_poblacion = pd.DataFrame({
            'Año': tiempos,
            'Poblacion': poblacion.astype(int)
        })
        
        print(f"Población inicial: {self.poblacion_inicial}")
        print(f"Tasa de crecimiento: {self.tasa_crecimiento:.2%}")
        print(f"Años simulados: {self.anios}")
        print("\nCrecimiento de la población:")
        print(df_poblacion.to_string())
        
        return df_poblacion
        
    def obtener_datos_finales(self):
        """
        Retorna la población final y el total de años.
        """
        poblacion_final = self.poblacion_inicial * math.pow(1 + self.tasa_crecimiento, self.anios)
        return {
            'poblacion_final': int(poblacion_final),
            'anios_simulados': self.anios
        }

# Ejecutar el ejercicio 5
simulador = SimuladorPoblacion(poblacion_inicial=1000, tasa_crecimiento=0.05, anios=10)
simulador.simular_crecimiento()
datos_finales = simulador.obtener_datos_finales()
print("\nDatos finales de la simulación:")
print(datos_finales)


print("\n" + "="*50 + "\n")

# --- EJERCICIO 6 ---
# Utiliza la librería `random` para crear una función que genere una contraseña
# aleatoria y segura. La contraseña debe tener:
# - Una longitud aleatoria entre 12 y 16 caracteres.
# - Al menos una letra mayúscula, una minúscula, un dígito y un símbolo.
# Utiliza la función `random.choice()` para seleccionar los caracteres.

# Solución:

def generar_contrasena_segura():
    """
    Genera una contraseña aleatoria que cumple con criterios de seguridad.
    """
    print("--- Ejercicio 6: Generador de Contraseñas Seguras ---")
    
    # Definir los conjuntos de caracteres
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~"
    
    # Asegurar que la contraseña contenga al menos un caracter de cada tipo
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Unir todos los conjuntos de caracteres para el resto de la contraseña
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    
    # Generar el resto de la contraseña
    longitud = random.randint(12, 16)
    resto_longitud = longitud - len(contrasena)
    
    resto_contrasena = random.choices(todos_los_caracteres, k=resto_longitud)
    
    # Unir las partes y mezclar la contraseña para que no siga un patrón
    contrasena_final = contrasena + resto_contrasena
    random.shuffle(contrasena_final)
    
    # Unir la lista de caracteres en un string y retornarlo
    contrasena_str = "".join(contrasena_final)
    
    print(f"Contraseña generada: {contrasena_str}")
    print(f"Longitud: {len(contrasena_str)}")
    return contrasena_str

# Ejecutar el ejercicio 6
generar_contrasena_segura()

print("\n" + "="*50 + "\n")


# --- EJERCICIO 7 ---
# Crea una clase `AnalizadorEncuesta` que, al ser inicializada, genere un
# DataFrame de pandas.
# - Las columnas deben ser: 'ID_Encuesta', 'Edad', 'Nivel_Satisfaccion' (1-5)
# - Genera 500 filas de datos aleatorios.
# - El ID de la encuesta debe ser un entero secuencial (usando numpy.arange).
#
# La clase debe tener los siguientes métodos:
# - `estadisticas_edad()`: Retorna un resumen estadístico de la columna 'Edad'.
# - `satisfaccion_por_rango_edad(rangos)`: Retorna un Series que muestre el
#   nivel de satisfacción promedio para cada rango de edad definido.
#   Ejemplo: `rangos = [18, 30, 50, 70]`

# Solución:

class AnalizadorEncuesta:
    """
    Clase para analizar un DataFrame de encuestas simuladas.
    """
    def __init__(self, num_encuestas=500):
        self.df = self._generar_datos(num_encuestas)
        
    def _generar_datos(self, num_encuestas):
        """
        Método interno para generar los datos aleatorios de la encuesta.
        """
        print("--- Ejercicio 7: Analizador de Encuestas ---")
        
        ids = np.arange(1, num_encuestas + 1)
        edades = np.random.randint(18, 80, num_encuestas)
        satisfaccion = np.random.randint(1, 6, num_encuestas)
        
        df = pd.DataFrame({
            'ID_Encuesta': ids,
            'Edad': edades,
            'Nivel_Satisfaccion': satisfaccion
        })
        
        print("DataFrame de Encuestas generado (primeros 5):")
        print(df.head())
        return df
        
    def estadisticas_edad(self):
        """
        Retorna un resumen estadístico de la edad.
        """
        print("\nEstadísticas de la columna 'Edad':")
        estadisticas = self.df['Edad'].describe()
        print(estadisticas)
        return estadisticas
        
    def satisfaccion_por_rango_edad(self, rangos):
        """
        Calcula el nivel de satisfacción promedio por rangos de edad.
        """
        print(f"\nNivel de Satisfacción promedio por rango de edad ({rangos}):")
        
        # Asignar cada edad a un rango usando pandas.cut
        self.df['Rango_Edad'] = pd.cut(self.df['Edad'], bins=rangos, right=False)
        
        # Agrupar por el nuevo rango y calcular el promedio de satisfacción
        satisfaccion_promedio = self.df.groupby('Rango_Edad')['Nivel_Satisfaccion'].mean()
        
        print(satisfaccion_promedio.to_string())
        return satisfaccion_promedio

# Ejecutar el ejercicio 7
analizador_encuesta = AnalizadorEncuesta()
analizador_encuesta.estadisticas_edad()
rangos_edad = [18, 30, 45, 60, 80]
analizador_encuesta.satisfaccion_por_rango_edad(rangos_edad)


print("\n" + "="*50 + "\n")


# --- EJERCICIO 8 ---
# Crea una clase llamada `Circulo` que tenga como atributo `radio` (número).
# El método constructor debe recibir el radio y un `array` de tipo flotante `(f)`
# para el radio (usando la librería `array`).
# La clase debe tener dos métodos:
# 1. `area()`: que calcule y retorne el área del círculo utilizando `math.pi`.
# 2. `circunferencia()`: que calcule y retorne la circunferencia.
# Luego, crea una instancia de la clase y llama a sus métodos.

# Solución:

class Circulo:
    """
    Clase para representar y calcular propiedades de un círculo.
    """
    def __init__(self, radio):
        # Usar un array de tipo 'f' para el radio
        self.radio = array('f', [radio])

    def area(self):
        """
        Calcula el área del círculo.
        """
        print("--- Ejercicio 8: Cálculo de Área de un Círculo ---")
        radio_float = self.radio[0]
        area_calc = math.pi * radio_float**2
        print(f"Radio del círculo: {radio_float:.2f}")
        print(f"Área del círculo: {area_calc:.2f}")
        return area_calc

    def circunferencia(self):
        """
        Calcula la circunferencia del círculo.
        """
        radio_float = self.radio[0]
        circunferencia_calc = 2 * math.pi * radio_float
        print(f"Circunferencia del círculo: {circunferencia_calc:.2f}")
        return circunferencia_calc

# Ejecutar el ejercicio 8
radio_circulo = 10.5
mi_circulo = Circulo(radio_circulo)
mi_circulo.area()
mi_circulo.circunferencia()


print("\n" + "="*50 + "\n")


# --- EJERCICIO 9 ---
# Genera una lista de 200 fechas aleatorias en un rango de 100 años.
# Para ello, utiliza la librería `datetime` y `random`.
# Luego, utilizando `pandas`, crea un DataFrame con las fechas.
# Analiza y muestra:
# 1. El año más antiguo y el más reciente.
# 2. El mes con más fechas.
# 3. El día de la semana con más ocurrencias (lunes, martes, etc.).

# Solución:

def analizador_de_fechas():
    """
    Genera y analiza una lista de fechas históricas.
    """
    print("--- Ejercicio 9: Analizador de Fechas Históricas ---")
    
    fechas = []
    hoy = dt.date.today()
    
    for _ in range(200):
        # Generar un número aleatorio de días en los últimos 100 años
        dias_aleatorios = random.randint(0, 365 * 100)
        fecha_aleatoria = hoy - dt.timedelta(days=dias_aleatorios)
        fechas.append(fecha_aleatoria)
        
    # Crear un DataFrame de pandas
    df_fechas = pd.DataFrame({'Fecha': fechas})
    
    # 1. Obtener el año más antiguo y el más reciente
    df_fechas['Año'] = df_fechas['Fecha'].dt.year
    anio_mas_antiguo = df_fechas['Año'].min()
    anio_mas_reciente = df_fechas['Año'].max()
    print(f"Año más antiguo: {anio_mas_antiguo}")
    print(f"Año más reciente: {anio_mas_reciente}")

    # 2. Obtener el mes con más fechas
    df_fechas['Mes'] = df_fechas['Fecha'].dt.month
    mes_mas_frecuente = df_fechas['Mes'].mode()[0]
    print(f"Mes con más fechas: {dt.date(1900, mes_mas_frecuente, 1).strftime('%B')}") # Convertir a nombre del mes

    # 3. Obtener el día de la semana con más ocurrencias
    df_fechas['Dia_Semana'] = df_fechas['Fecha'].dt.day_name()
    dia_mas_frecuente = df_fechas['Dia_Semana'].mode()[0]
    print(f"Día de la semana con más ocurrencias: {dia_mas_frecuente}")

# Ejecutar el ejercicio 9
analizador_de_fechas()


print("\n" + "="*50 + "\n")


# --- EJERCICIO 10 ---
# Crea una clase `ClasificadorNumeros` que genere un array de numpy
# con 100 números enteros aleatorios entre -100 y 100.
# La clase debe tener los siguientes métodos que utilicen la lógica
# de numpy para el filtrado:
# 1. `contar_positivos()`: Retorna el conteo de números positivos.
# 2. `contar_negativos()`: Retorna el conteo de números negativos.
# 3. `contar_ceros()`: Retorna el conteo de ceros.
# 4. `calcular_promedio_positivos()`: Retorna el promedio solo de los
#    números positivos. Utiliza `math.log` en el resultado.

# Solución:

class ClasificadorNumeros:
    """
    Clase para generar y clasificar números aleatorios.
    """
    def __init__(self, num_elementos=100):
        self.numeros = np.random.randint(-100, 101, num_elementos)
        
    def contar_positivos(self):
        """
        Cuenta los números positivos.
        """
        positivos = np.sum(self.numeros > 0)
        return positivos
        
    def contar_negativos(self):
        """
        Cuenta los números negativos.
        """
        negativos = np.sum(self.numeros < 0)
        return negativos

    def contar_ceros(self):
        """
        Cuenta los ceros.
        """
        ceros = np.sum(self.numeros == 0)
        return ceros
        
    def calcular_promedio_positivos(self):
        """
        Calcula el promedio de los números positivos y retorna su logaritmo.
        """
        # Filtrar solo los números positivos
        numeros_positivos = self.numeros[self.numeros > 0]
        
        if len(numeros_positivos) > 0:
            promedio = np.mean(numeros_positivos)
            log_promedio = math.log(promedio)
            return log_promedio
        else:
            return None # Retornar None si no hay números positivos

# Ejecutar el ejercicio 10
print("--- Ejercicio 10: Clasificador de Números Aleatorios ---")
clasificador = ClasificadorNumeros()

print(f"Números generados (primeros 10): {clasificador.numeros[:10]}")
print(f"Total de números positivos: {clasificador.contar_positivos()}")
print(f"Total de números negativos: {clasificador.contar_negativos()}")
print(f"Total de ceros: {clasificador.contar_ceros()}")

promedio_log = clasificador.calcular_promedio_positivos()
if promedio_log is not None:
    print(f"Logaritmo natural del promedio de los positivos: {promedio_log:.2f}")
else:
    print("No se encontraron números positivos para calcular el promedio.")


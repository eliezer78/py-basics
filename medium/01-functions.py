# Funciones Lambda, Orden Superior, Dunder y Closures en Python

## 1. Funciones Lambda

### Ejercicio 1: Suma rápida
# Escribe una función lambda que reciba dos números y devuelva su suma.

suma = lambda x, y: x + y
print(suma(6,7))

### Ejercicio 2: Filtrado de múltiplos
# Dada una lista de números, usa `filter` y una función lambda 
# para obtener una lista solo con los múltiplos de 4.

numeros = [1, 4, 6, 8, 9, 12, 15]
print(list(filter(lambda x: x % 4==0,numeros)))

### Ejercicio 3: Transformación de cadenas
# Usa `map` y una función lambda para convertir todas las palabras 
# de una lista de strings a mayúsculas.

lista = ["python","typescript","cobol"]
print(list(map(lambda palabra: palabra.upper(),lista)))


## 2. Funciones de Orden Superior

### Ejercicio 4: Aplica una función
# Escribe una función que reciba otra función y un número, 
# y retorne el resultado de aplicar esa función al número.

def aplicar_func(func, nro):
    return func(nro)

print(aplicar_func(lambda x: x ** 0.5, 36))


### Ejercicio 5: Función de composición
# Implementa una función que reciba dos funciones y devuelva 
# una nueva función que sea la composición de ambas.

def compuesta(f, g):
    return lambda x: f(g(x))

cuadrado = lambda x: x ** x
suma_uno = lambda x: x + 1
comp = compuesta(cuadrado,suma_uno)
print(comp(2))

### Ejercicio 6: Reducción personalizada
# Usa `reduce` para multiplicar todos los elementos de una lista de números.

from functools import reduce

numeros = [2,3,4,5]

print(reduce(lambda x, y: x * y,numeros))


## 3. Funciones Dunder

### Ejercicio 7: Clase con `__str__`
# Crea una clase `Libro` con atributos `titulo` y `autor`. 
# Redefine el método `__str__` para que al imprimir un objeto 
# muestre: `"Titulo - Autor"`.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
libro = Libro("1984","George Orwell")
print(libro)

### Ejercicio 8: Igualdad de objetos (`__eq__`)
# Crea una clase `Punto` (con `x` e `y`) y redefine 
# el método `__eq__` para que dos puntos sean iguales 
# si tienen las mismas coordenadas.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
punto1 = Punto(1,2)
punto2 = Punto(3,4)
print(punto1 == punto2)

punto3 = punto1 + punto2
print(punto3)

### Ejercicio 9: Suma con `__add__`
# Modifica la clase `Punto` para que puedas sumar dos puntos 
# usando el operador `+` (sobrecarga de `__add__`).


## 4. Closures

### Ejercicio 10: Multiplicador
# Escribe una función que reciba un número y retorne 
# una función que multiplica cualquier valor por ese número (closure).

def multiplica(x):
    def func(n):
        return x * n
    return func

doble = multiplica(2)
print(doble(10))

### Ejercicio 11: Contador
# Escribe una función que retorne una función que, 
# cada vez que se llame, devuelva un contador que 
# empieza en 1 y aumenta en uno.

def contador():
    cuenta = 0
    def siguiente():
        nonlocal cuenta 
        cuenta += 1
        return cuenta
    return siguiente

c = contador()
print(c())
print(c())
print(c())

### Ejercicio 12: Validador de rango
# Crea una función que reciba dos valores `min` y `max` y retorne una 
# función que verifica si un número está dentro de ese rango (inclusive).

def valida_rango(min_val, max_val):
    return lambda x: min_val <= x <= max_val

en_rango = valida_rango(10, 20)
print(en_rango(7))
print(en_rango(15))
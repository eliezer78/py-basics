### lambdas
# son funciones anonimas que se usan para   
# operaciones simples y de una sola linea
# se definen con la palabra lambda
# lambda argumentos: expresion

sum_two_values = lambda a,b:a+b
print(sum_two_values(7,8))

def sum_three(c):
    return lambda a,b: a+b+c

print(sum_three(4)(8,9))

is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("radar"))
print(is_palindrome("hello"))

es_par = lambda x: x % 2 == 0
print(es_par(4))
print(es_par(7))

raiz_cuadrada = lambda x: x ** 0.5
print(raiz_cuadrada(16))
print(raiz_cuadrada(25))

### High order functions
# son funciones que reciben otras funciones como argumentos
# o que retornan funciones como resultado

def suma_uno(x):
    return x + 1

def suma_dos(x):
    return x + 2

def suma_dos_valores_mas_otro(a,b,f_sum):
    return f_sum(a + b)
    
print(suma_dos_valores_mas_otro(2,3,suma_uno))
print(suma_dos_valores_mas_otro(2,3,suma_dos))

### clousures
# son funciones que retornan otras funciones
# estas funciones retornadas recuerdan el entorno
# en el que fueron creadas

def suma_diez(y):
    def suma(x):
        return x + 10 + y
    return suma

suma = suma_diez(1)
print(suma(2))

print(suma_diez(1)(5))

### Built-in high order functions
# son funciones que ya vienen integradas en python
# y que reciben otras funciones como argumentos
# algunas de las mas comunes son:
# map, filter, reduce, zip, enumerate, sorted, etc

lista =[2,51,9,7,1,26,15,4]

# map
print(list(map(lambda x: x ** 2, lista)))

# filter
print(list(filter(lambda x: x % 2 == 0, lista)))

# reduce
from functools import reduce
print(reduce(lambda a,b: a + b, lista))
print(reduce(lambda a,b: a if a > b else b, lista))


# Ejercicios

## Funciones Lambda

1. **Suma rápida:**
   Escribe una función lambda que reciba dos números y devuelva su suma.

2. **Filtrado de múltiplos:**  
   Dada una lista de números, usa `filter` y una función lambda para obtener una lista solo con los múltiplos de 4.

3. **Transformación de cadenas:**  
   Usa `map` y una función lambda para convertir todas las palabras de una lista de strings a mayúsculas.

---

## Funciones de Orden Superior

4. **Aplica una función:**  
   Escribe una función que reciba otra función y un número, y retorne el resultado de aplicar esa función al número.

5. **Función de composición:**  
   Implementa una función que reciba dos funciones y devuelva una nueva función que sea la composición de ambas.

6. **Reducción personalizada:**  
   Usa `reduce` para multiplicar todos los elementos de una lista de números.

---

## Funciones Dunder

7. **Clase con `__str__`:**  
   Crea una clase `Libro` con atributos `titulo` y `autor`. Redefine el método `__str__` para que al imprimir un objeto muestre: `"Titulo - Autor"`.

8. **Igualdad de objetos (`__eq__`):**  
   Crea una clase `Punto` (con `x` e `y`) y redefine el método `__eq__` para que dos puntos sean iguales si tienen las mismas coordenadas.

9. **Suma con `__add__`:**  
   Modifica la clase `Punto` para que puedas sumar dos puntos usando el operador `+` (sobrecarga de `__add__`).

---

## Closures

10. **Multiplicador:**  
    Escribe una función que reciba un número y retorne una función que multiplica cualquier valor por ese número (closure).

11. **Contador:**  
    Escribe una función que retorne una función que, cada vez que se llame, devuelva un contador que empieza en 1 y aumenta en uno.

12. **Validador de rango:**  
    Crea una función que reciba dos valores `min` y `max` y retorne una función que verifica si un número está dentro de ese rango (inclusive).
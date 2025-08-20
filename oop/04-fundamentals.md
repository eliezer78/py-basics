# Programación Orientada a Objetos (POO)

---

## ¿Qué es la Programación Orientada a Objetos?

La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el software en torno a “objetos”, que representan entidades del mundo real o conceptos abstractos, y que interactúan entre sí a través de métodos y atributos.

---

## Conceptos Fundamentales

### 1. **Clases**

- Una **clase** es un modelo o plantilla que define las características y comportamientos de un tipo de objeto.
- Es como un plano para construir objetos.

**Ejemplo (Python):**
```python
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")
```

---

### 2. **Objetos**

- Un **objeto** es una instancia concreta de una clase.
- Cada objeto tiene sus propios valores para los atributos definidos por la clase.

**Ejemplo (Python):**
```python
mi_perro = Perro("Firulais", "Labrador")
mi_perro.ladrar()
```

---

### 3. **Abstracción**

- La **abstracción** consiste en identificar las características esenciales de un objeto, ignorando los detalles irrelevantes.
- Permite modelar entidades complejas mostrando solo lo necesario.

**Ejemplo:**  
En una clase `Auto`, solo nos interesa la marca, el modelo y el método `acelerar()`, ignorando detalles internos del motor.

---

### 4. **Encapsulamiento**

- El **encapsulamiento** es el mecanismo que restringe el acceso directo a los datos internos de un objeto.
- Se logra usando métodos públicos para acceder/modificar atributos privados.
- Protege la integridad de los datos.

**Ejemplo (Python):**
```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo
```

---

### 5. **Herencia**

- La **herencia** permite crear nuevas clases a partir de una clase existente, heredando sus atributos y métodos.
- Facilita la reutilización y extensión de código.

**Ejemplo (Python):**
```python
class Animal:
    def comer(self):
        print("El animal come.")

class Gato(Animal):
    def maullar(self):
        print("Miau")
```

---

### 6. **Polimorfismo**

- El **polimorfismo** permite que diferentes clases respondan de manera distinta al mismo método.
- Facilita el uso de una interfaz común para diferentes tipos de objetos.

**Ejemplo (Python):**
```python
class Ave:
    def hablar(self):
        print("El ave canta.")

class Loro(Ave):
    def hablar(self):
        print("El loro imita sonidos.")

def presentar_ave(ave):
    ave.hablar()

presentar_ave(Ave())    # El ave canta.
presentar_ave(Loro())   # El loro imita sonidos.
```

---

## Temas Complementarios Esenciales

---

### 7. **Métodos y atributos estáticos**

- Un **método estático** pertenece a la clase, no a los objetos.
- Se usan para operaciones que no dependen de datos específicos de la instancia.
- **Atributo estático** es compartido por todas las instancias de la clase.

**Ejemplo (Python):**
```python
class Calculadora:
    contador = 0  # atributo estático

    @staticmethod
    def sumar(a, b):
        return a + b

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1
```

---

### 8. **Composición y agregación**

- La **composición** es una relación “tiene un” (has-a). Una clase contiene objetos de otra clase.
- Permite construir objetos complejos a partir de otros más simples.

**Ejemplo (Python):**
```python
class Motor:
    def arrancar(self):
        print("Motor encendido.")

class Auto:
    def __init__(self):
        self.motor = Motor()  # composición

    def arrancar(self):
        self.motor.arrancar()
```

---

### 9. **Constructores y destructores**

- **Constructor:** Método especial que se ejecuta al crear un objeto (en Python: `__init__`).
- **Destructor:** Método que se ejecuta cuando el objeto se elimina (en Python: `__del__`).

**Ejemplo (Python):**
```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Persona {nombre} creada.")

    def __del__(self):
        print(f"Persona {self.nombre} eliminada.")
```

---

### 10. **Sobrecarga de métodos y operadores**

- **Sobrecarga de métodos:** Definir múltiples métodos con el mismo nombre pero diferentes parámetros (limitado en Python).
- **Sobrecarga de operadores:** Definir cómo los operadores (+, -, etc.) funcionan para objetos personalizados.

**Ejemplo (Python):**
```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
```

---

### 11. **Visibilidad de atributos y métodos**

- **Público:** Accesible desde cualquier parte (sin guiones bajos).
- **Protegido:** Convención de un guion bajo `_atributo` (accesible en la clase y subclases).
- **Privado:** Doble guion bajo `__atributo` (accesible solo dentro de la clase).

**Ejemplo (Python):**
```python
class Ejemplo:
    def __init__(self):
        self.publico = 1
        self._protegido = 2
        self.__privado = 3
```

---

### 12. **Interfaces y clases abstractas**

- Una **interfaz** define un conjunto de métodos que una clase debe implementar.
- Una **clase abstracta** puede tener métodos implementados y métodos abstractos (sin implementación).
- En Python, se usa el módulo `abc`.

**Ejemplo (Python):**
```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
```

---

### 13. **Diagramas de clases UML**

- El **diagrama de clases UML** es una herramienta visual para mostrar la estructura de las clases y sus relaciones.
- Incluye clases, atributos, métodos y relaciones como herencia, composición y asociación.

**Ejemplo visual:**

```
+-----------------+
|     Animal      |
+-----------------+
| - nombre        |
+-----------------+
| + comer()       |
+-----------------+
        ^
        |
+---------------+
|     Perro     |
+---------------+
| + ladrar()    |
+---------------+
```
---

## Resumen Visual

| Concepto         | ¿Qué es?                                      | Ejemplo                |
|------------------|-----------------------------------------------|------------------------|
| Clase            | Plantilla o modelo                            | class Perro            |
| Objeto           | Instancia de una clase                        | mi_perro = Perro(...)  |
| Abstracción      | Ignorar detalles innecesarios                 | Solo mostrar acelerar()|
| Encapsulamiento  | Proteger datos internos                       | __saldo privado        |
| Herencia         | Reutilizar código de una clase base           | class Gato(Animal)     |
| Polimorfismo     | Comportamiento diferente según la clase       | hablar() en Ave/Loro   |
| Estáticos        | Compartidos por todas las instancias          | @staticmethod          |
| Composición      | "Tiene un" (has-a)                            | Auto tiene un Motor    |
| Constructores    | Inicializan objetos                           | __init__               |
| Sobrecarga       | Redefinir operadores                          | __add__                |
| Visibilidad      | Público, protegido, privado                   | _protegido, __privado  |
| Abstractas       | Métodos sin implementación                    | @abstractmethod        |
| UML              | Diagrama visual de clases                     | Clases y relaciones    |

---

## ¿Por qué usar POO?

- Organiza el código de forma más lógica y natural.
- Facilita el mantenimiento y la escalabilidad.
- Promueve la reutilización y la modularidad.

---

## Ejemplo Integrador

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print("Vehículo en marcha.")

class Moto(Vehiculo):
    def arrancar(self):
        print(f"{self.marca} Moto encendida.")

class Auto(Vehiculo):
    def arrancar(self):
        print(f"{self.marca} Auto encendido.")

def iniciar_vehiculo(vehiculo):
    vehiculo.arrancar()

iniciar_vehiculo(Moto("Yamaha"))
iniciar_vehiculo(Auto("Toyota"))
```

---
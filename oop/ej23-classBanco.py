# Ejercicio 23: Clases, Objetos y Funciones Avanzadas en Python

# Crear un sistema sencillo de gestión bancaria usando programación orientada a objetos 
# y funciones avanzadas en Python.

# 1. Define una clase llamada `Cuenta`: 
#   - Cada cuenta debe tener como atributos:  
#     - `titular` (nombre del cliente, tipo string)
#     - `saldo` (saldo de la cuenta, tipo numérico)
#     - `id` (identificador único que se asigne automáticamente a cada cuenta nueva)
#   - Implementa el método especial `__str__` para mostrar la información de la cuenta 
#     de forma legible, por ejemplo:  
#     `"ID: 1 | Titular: Ana | Saldo: 1500"`
#   - Implementa el método especial `__eq__` para poder comparar si dos cuentas tienen 
#     el mismo saldo (deben retornar `True` si los saldos son iguales).

# 2. Define una clase llamada `Banco`: 
#   - Debe tener un atributo que almacene una lista de cuentas (`self.cuentas`).
#   - Implementa un método `agregar_cuenta(titular, saldo_inicial)` que cree una nueva 
#     cuenta y la agregue a la lista.
#   - Implementa un método `mostrar_cuentas_ordenadas()` que muestre todas las cuentas 
#     ordenadas por saldo ascendente (usa la función `sorted` y una lambda como clave).
#   - Implementa un método `mostrar_cuentas_filtradas(monto)` que muestre solo las 
#     cuentas cuyo saldo sea mayor al monto recibido (usa `filter` y una lambda).
#   - Implementa un método `buscar_cuenta_por_titular(titular)` que devuelva la cuenta 
#     correspondiente al titular.
#   - Implementa un método `generar_aplicador_interes(titular, interes)` que devuelva 
#     una función (closure) que, al ejecutarse, aplique el interés (por ejemplo, 0.05 
#    para 5%) al saldo de la cuenta del titular indicado.  
#     - Si la cuenta no existe, la función devuelta debe informar que el titular no fue 
#       encontrado.

### Ayuda

# - Usa una variable de clase o contador estático para generar IDs únicos en `Cuenta`.
# - Para ordenar o filtrar listas, recuerda que puedes usar `sorted(lista, key=...)` 
#   y `filter(funcion, lista)`.
# - Las funciones lambda pueden ayudarte a definir funciones pequeñas y rápidas, 
#   por ejemplo, para filtrar o para la clave de ordenamiento.
# - Un closure es una función interna que recuerda el contexto donde fue creada 
#   (por ejemplo, la cuenta a la que debe aplicar el interés).

class Cuenta:
    _contador_id = 1

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.id = Cuenta._contador_id
        Cuenta._contador_id += 1

    def __str__(self):
        return f"ID: {self.id} | Titular: {self.titular} | Saldo: {self.saldo}"

    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.saldo == other.saldo
        return False

class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, titular, saldo_inicial):
        cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(cuenta)

    def mostrar_cuentas_ordenadas(self):
        print("Cuentas ordenadas por saldo:")
        for cuenta in sorted(self.cuentas, key=lambda x: x.saldo):
            print(cuenta)

    def mostrar_cuentas_filtradas(self, monto):
        print(f"Cuentas con saldo mayor a {monto}:")
        cuentas_filtradas = filter(lambda c: c.saldo > monto, self.cuentas)
        for cuenta in cuentas_filtradas:
            print(cuenta)

    def buscar_cuenta_por_titular(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    def generar_aplicador_interes(self, titular, interes):
        cuenta = self.buscar_cuenta_por_titular(titular)
        if cuenta is None:
            print(f"No se encontró la cuenta de {titular}.")
            return lambda: None
        # Closure que aplica interés a la cuenta seleccionada
        def aplicar_interes():
            cuenta.saldo += cuenta.saldo * interes
            print(f"Interés del {interes*100}% aplicado a la cuenta de {titular}. Nuevo saldo: {cuenta.saldo}")
        return aplicar_interes

# Ejemplo de uso
banco = Banco()

banco.agregar_cuenta("Ana", 1500)
banco.agregar_cuenta("Luis", 2400)
banco.agregar_cuenta("Marta", 800)

# Mostrar cuentas ordenadas por saldo
banco.mostrar_cuentas_ordenadas()

# Filtrar cuentas con saldo mayor a 1000
banco.mostrar_cuentas_filtradas(1000)

# Comparar si dos cuentas tienen el mismo saldo
print(banco.cuentas[0] == banco.cuentas[1])  # False

# Crear y aplicar un interés del 5% a la cuenta de Ana
interes_5 = banco.generar_aplicador_interes("Ana", 0.05)
interes_5()
print(banco.cuentas[0])  # Mostrar cuenta de Ana con el nuevo saldo
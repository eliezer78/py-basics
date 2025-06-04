### Ejercicio 17: Herencia - Clase Empleado
#
# Una empresa tiene diferentes tipos de empleados. Todos los empleados tienen un nombre, 
# un identificador (ID) y un salario base.
# Crea una clase base llamada Empleado que tenga:
# Atributos: nombre, id, salario_base
# Métodos: calcular_salario() que retorna el salario base.
#          informacion() que imprime el nombre, ID y salario base.
# 
# Crea una clase derivada llamada EmpleadoTiempoCompleto que herede de Empleado y tenga:
# Atributo adicional: bono_anual
# Sobrescribe el método calcular_salario() para que retorne el salario base 
# más el bono anual dividido entre 12 (bono mensual).
# Sobrescribe el método informacion() para mostrar también el bono anual.
# 
# Crea otra clase derivada llamada EmpleadoMedioTiempo que herede de Empleado y tenga:
# Atributo adicional: horas_trabajadas
# Sobrescribe el método calcular_salario() para que retorne el salario base 
# multiplicado por las horas trabajadas y dividido entre 80 
# (siendo 80 el total de horas de un mes de medio tiempo estándar).
# Sobrescribe el método informacion() para mostrar también las horas trabajadas.
# 
# Crea una lista de empleados (de ambos tipos) y muestra la información 
# y el salario calculado de cada uno.

class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Salario base: {self.salario_base}")

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id, salario_base, bono_anual):
        super().__init__(nombre, id, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario(self):
        # El bono anual se reparte mensualmente
        return self.salario_base + self.bono_anual / 12

    def informacion(self):
        super().informacion()
        print(f"Bono anual: {self.bono_anual}")

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, id, salario_base, horas_trabajadas):
        super().__init__(nombre, id, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        # El salario se ajusta según las horas trabajadas (de un máximo de 80 al mes)
        return self.salario_base * self.horas_trabajadas / 80

    def informacion(self):
        super().informacion()
        print(f"Horas trabajadas este mes: {self.horas_trabajadas}")

# Lista de empleados
empleados = [
    EmpleadoTiempoCompleto("Ana", 1, 2000, 4800),
    EmpleadoMedioTiempo("Luis", 2, 1500, 60),
    EmpleadoTiempoCompleto("Carlos", 3, 2200, 6000),
    EmpleadoMedioTiempo("Laura", 4, 1300, 40)
]

# Mostrar información y salario de cada empleado
for empleado in empleados:
    empleado.informacion()
    print(f"Salario calculado este mes: {empleado.calcular_salario():.2f}\n")
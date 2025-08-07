class Vector:
    # Constructor: inicializa los componentes x e y del vector
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representación legible por humanos, por ejemplo al usar print()
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Comparación de igualdad entre dos vectores
    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    # Suma de dos vectores usando el operador +
    def __add__(self, other):
        # if not isinstance(other, Vector):
        #    return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    # Resta de dos vectores usando el operador -
    def __sub__(self, other):
        # if not isinstance(other, Vector):
        #    return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplicación escalar usando el operador *
    def __mul__(self, scalar):
        # if not isinstance(scalar, (int, float)):
        #    return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    # Devuelve la magnitud del vector usando abs(v)
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Permite usar len(v): retorna 2 porque el vector tiene dos componentes
    def __len__(self):
        return 2

    # Permite usar 'in' para comprobar si un valor está en el vector
    def __contains__(self, value):
        return value == self.x or value == self.y

    # Permite llamar al objeto como una función (v())
    def __call__(self):
        print(f"Vector en ({self.x}, {self.y})")

    # Permite evaluar el vector en un contexto booleano (if v:)
    # def __bool__(self):
    #    return self.x != 0 or self.y != 0

    # Permite copiar el vector usando copy.copy(v)
    def __copy__(self):
        return Vector(self.x, self.y)

    # Método llamado cuando el objeto es destruido (al eliminarlo)
    # def __del__(self):
    #    print(f"Vector {self} eliminado")

# Ejemplo práctico de uso
v1 = Vector(2, 3)
v2 = Vector(1, 1)

print("Str:", v1)                              # __str__
print("Suma:", v1 + v2)                        # __add__
print("Resta:", v1 - v2)                       # __sub__
print("Multiplicación escalar:", v1 * 3)       # __mul__
print("Módulo:", abs(v1))                      # __abs__
print("Longitud:", len(v1))                    # __len__
v1()                                           # __call__
# print("¿Es verdadero?", bool(v1))              # __bool__

import copy
v3 = copy.copy(v1)                             # __copy__
print("Copia:", v3)
print("¿v1 == v3?:", v1 == v3)                 # __eq__
# El método __del__ se ejecuta automáticamente al eliminar el objeto o finalizar el programa

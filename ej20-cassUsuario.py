### Ejercicio 20: Encapsulamiento - Clase Usuario
# 
# Crea una clase llamada `Usuario` para gestionar usuarios en un sistema informático. 
# Debes aplicar encapsulamiento de la siguiente forma:
# 1. La clase debe tener los siguientes atributos privados:
#   - `__nombre_usuario` (string)
#   - `__clave` (string)
#   - `__email` (string)
#   - `__activo` (booleano, inicializa en `True`)
# 2. Implementa métodos públicos para:
#   - Obtener el nombre de usuario y el email.
#   - Cambiar la clave del usuario solo si la clave nueva tiene al menos 8 caracteres; si no, 
#     debe imprimirse un mensaje de error y no cambiar la clave.
#   - Cambiar el email. El nuevo email debe contener un `@` y un `.` (punto), 
#     en caso contrario debe imprimirse un mensaje de error y no modificar el email.
#   - Desactivar y reactivar la cuenta de usuario mediante los métodos `desactivar()` y `reactivar()`.  
#   - Consultar si el usuario está activo (`es_activo()`).
# 3. Implementa el método especial `__str__` para mostrar la información del usuario 
#    (nombre, email, estado activo/inactivo) de forma legible.
# 4. Escribe un pequeño programa de prueba que:
#   - Cree dos usuarios distintos.
#   - Cambie la clave y el email usando los métodos públicos, probando casos válidos e inválidos.
#   - Desactive y reactive una cuenta, mostrando el estado antes y después.

class Usuario:
    def __init__(self, nombre_usuario, clave, email):
        self.__nombre_usuario = nombre_usuario
        self.__clave = clave
        self.__email = email
        self.__activo = True

    # Métodos públicos para obtener información
    def obtener_nombre_usuario(self):
        return self.__nombre_usuario

    def obtener_email(self):
        return self.__email

    # Cambiar la clave si la nueva tiene al menos 8 caracteres
    def cambiar_clave(self, nueva_clave):
        if len(nueva_clave) < 8:
            print("Error: La clave debe tener al menos 8 caracteres.")
        else:
            self.__clave = nueva_clave

    # Cambiar el email si es válido
    def cambiar_email(self, nuevo_email):
        if "@" not in nuevo_email or "." not in nuevo_email:
            print("Error: El email no es válido.")
        else:
            self.__email = nuevo_email

    # Métodos para activar/desactivar cuenta
    def desactivar(self):
        self.__activo = False

    def reactivar(self):
        self.__activo = True

    def es_activo(self):
        return self.__activo

    def __str__(self):
        estado = "Activo" if self.__activo else "Inactivo"
        return f"Usuario: {self.__nombre_usuario} | Email: {self.__email} | Estado: {estado}"


usuario1 = Usuario("juanperez", "secreto123", "juan@correo.com")
usuario2 = Usuario("ana88", "clave4567", "ana@correo.com")

print(usuario1)
print(usuario2)

usuario1.cambiar_clave("corto")    # Debe mostrar mensaje de error
usuario1.cambiar_clave("nuevaclave123")
usuario2.cambiar_email("anacorreo.com")  # Debe mostrar mensaje de error
usuario2.cambiar_email("ana@gmail.com")

usuario1.desactivar()
print(usuario1.es_activo())  # False
usuario1.reactivar()
print(usuario1.es_activo())  # True

print(usuario1)
print(usuario2)
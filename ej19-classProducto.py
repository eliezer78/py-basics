### Ejercicio 19: Encapsulamiento - Clase Producto
# 
# Crea una clase llamada `Producto` para gestionar artículos 
# en un sistema de inventario. 
# Implementa los siguientes requisitos utilizando 
# encapsulamiento:
# 1. La clase debe tener los siguientes atributos privados:
#   - `__nombre`
#   - `__precio`
#   - `__stock`
#
# 2. Implementa métodos públicos para:
#   - Obtener el nombre, precio y stock del producto.
#   - Modificar el precio y el stock. El precio no puede ser 
#     negativo; si se intenta asignar un valor negativo, 
#     debe imprimirse un mensaje de error y no cambiar el valor. 
#     El stock solo puede ser modificado a través de métodos 
#     públicos `agregar_stock(cantidad)` y `vender(cantidad)`, 
#     que suman o restan la cantidad indicada. No se puede 
#     vender más de lo que hay en stock; en ese caso debe 
#     imprimirse un mensaje de error y no cambiar el stock.
# 
# 3. Implementa el método especial `__str__` para mostrar la información 
#    del producto de forma legible.
#
# 4. Escribe un pequeño programa de prueba que:
#   - Cree dos productos distintos.
#   - Modifique su precio y stock usando los métodos públicos.
#   - Intente asignar un precio negativo y vender más de lo disponible, 
#     mostrando cómo se controlan los errores.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        if precio < 0:
            print("El precio no puede ser negativo")
            precio = 0  
        if stock < 0:
            print("El stock no puede ser negativo")
            stock = 0  
        self.__precio = precio  
        self.__stock = stock

    def obtener_nombre(self):
        return self.__nombre
        
    def obtener_precio(self):
        return self.__precio
    
    def obtener_stock(self):
        return self.__stock

    def cambiar_precio(self,precio):
        if precio < 0:
            print("El precio no puede ser negativo")
        else:
            self.__precio = precio
            
    def agregar_stock(self,cantidad):
        if cantidad < 0:
            print("La cantidad no puede ser negativa")
        else:
            self.__stock += cantidad

    def vender(self,cantidad):
        if cantidad <= 0:
            print("La cantidad a vender no puede ser menor o igual a cero")
        elif cantidad > self.__stock:
            print("No hay stock suficiente.")
        else:
            self.__stock -= cantidad

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio:.2f}, Stock: {self.__stock}"
    
producto1 = Producto("Mate",5000,10)    
producto2 = Producto("Termo",50000,15)

print(producto1.__str__())
print(producto2.__str__())

producto1.agregar_stock(-5)
producto1.vender(11)
producto1.vender(0)

producto1.vender(4)
producto2.vender(2)
producto1.cambiar_precio(6000)
producto2.cambiar_precio(150000)

print(producto1)
print(producto2)
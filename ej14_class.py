# Definición de la clase Person
class Persona:
    def __init__(self, apellido, nombre, edad):
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
        self.nombre_completo = f"{nombre} {apellido}"
        
    def caminar(self): # Método para simular que la persona camina
        print(f"{self.nombre_completo} está caminando.")
        
    def hablar(self):
        print(f"{self.nombre_completo} está hablando.")

mi_persona = Persona("Messi", "Lionel", 37) # Instancia de la clase Person

print(mi_persona.nombre) # Imprime el tipo de la instancia
print(mi_persona.apellido) # Imprime el tipo de la instancia
print(mi_persona.edad) # Imprime el tipo de la instancia
print(mi_persona.nombre_completo) # Imprime el tipo de la instancia

mi_persona.caminar()
mi_persona.hablar()
    
    
    
    
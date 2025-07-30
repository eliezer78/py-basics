### Polimorfismo

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass
    
    @abstractmethod
    def caminar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    def caminar(self):
        return "Caminando..."
    def saltar(self):
        return "Saltando..."
    
class Gato(Animal):
    def hablar(self):
        return "Miau!"
    def caminar(self):
        return "Caminando..."

class Pajaro(Animal):
    def hablar(self):
        return "Pío!"
    def caminar(self):
        return "Caminando..."

mascotas = [Gato(), Perro(), Pajaro()]

for animal in mascotas:
    print(animal.hablar())
    print(animal.caminar())

# animal = Animal()  # Esto fallará porque Animal es abstracto y no se puede instanciar

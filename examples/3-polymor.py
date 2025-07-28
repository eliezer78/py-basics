### Polimorfismo
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

class Pajaro(Animal):
    def hablar(self):
        return "Pío!"

mascotas = [Gato(), Perro(), Pajaro()]
for animal in mascotas:
    print(animal.hablar())
    
# animal = Animal()  # Esto fallará porque Animal es abstracto y no se puede instanciar


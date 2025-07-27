### Polimorfismo

class Perro:
    def hablar(self):
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

mascotas = [Perro(), Gato()]

for mascota in mascotas:
    print(mascota.hablar())
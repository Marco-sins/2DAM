class Animal:
    def __init__(self, name):
        self.name = name
    def sonido(self):
        print(f"El {self.name} hace un sonido")

class Perro(Animal):
    def sonido(self):
        print(f"El {self.name} ladra")

class Gato(Animal):
    def sonido(self):
        print(f"El {self.name} maulla")

animal = Animal("caballo")
perro = Perro("perro")
gato = Gato("gato")

animal.sonido()
perro.sonido()
gato.sonido()
class Animal: 
    def __init__(self, nombre='Animal'):
        self.nombre = nombre
    def hablar(self):
        print(f'{self.nombre} hace un sonido')
    def mea(self):
        print(f'{self.nombre} esta meando')

class Perro(Animal):
    def __init__(self, nombre='Perro'):
        super().__init__(nombre)
    def hablar(self):
        print(f'{self.nombre} Guau Guau')

class Gato(Animal):
    def __init__(self, nombre='Gato'):
        super().__init__(nombre)
    def hablar(self):
        print(f'{self.nombre} Miau Miau')

a = Animal('Animal')
a.hablar()
p = Perro('Perro')
p.hablar()
a.mea()
p.mea()

for animal in [Gato(), Perro()]:
    animal.hablar()
    animal.mea()
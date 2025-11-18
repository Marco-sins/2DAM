class Mascota:
    """1"""
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    def hablar(self):
        """Esta funcion hace un sonido"""
        print("Algún sonido")


class Perro(Mascota):
    """1"""
    def hablar(self):
        print("Guau!")

    def __str__(self):
        return f"Perro: {self.nombre}, {self.edad} años"

class Gato(Mascota):
    """1"""
    def hablar(self):
        print("Miau!")
    
    def __str__(self):
        return f"Gato: {self.nombre}, {self.edad} años"

class Pajaro(Mascota):
    """1"""
    def hablar(self):
        print("Pio!")


perro = Perro("perro", 2, "perro")
print(perro.__str__())
gato = Gato("gato", 2, "gato")
print(gato.__str__())
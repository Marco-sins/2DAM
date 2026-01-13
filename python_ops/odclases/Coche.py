class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print(f"el {self.marca} ha arrancado")

mi_coche = Coche("Toyota", "Rojo")
mi_coche.arrancar()
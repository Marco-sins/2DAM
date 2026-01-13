class Jugador:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_info(self):
        print(f"Jugador: {self.nombre}, Vida: {self.vida}")

    def atacar(self, enemigo):
        enemigo.vida -= 10
        print(f"{self.nombre} ataca a {enemigo.nombre}")

jugador1 = Jugador("Heroe", 100)
jugador2 = Jugador("Villano", 100)
jugador1.mostrar_info()
jugador2.mostrar_info()
jugador1.atacar(jugador2)
jugador2.mostrar_info()
jugador1.mostrar_info()
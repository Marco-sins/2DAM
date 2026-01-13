class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.salud = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, enemigo):
        danio = self.ataque - enemigo.defensa
        if danio > 0:
            enemigo.recibir_daño(danio)
            print(f"{self.nombre} ataca a {enemigo.nombre} y causa {danio} de daño.")
        else:
            print(f"{self.nombre} ataca a {enemigo.nombre} pero no causa daño.")
    
    def esta_vivo(self):
        return self.salud > 0
    
    def recibir_daño(self, danio):
        self.salud -= danio
        print(f"{self.nombre} recibe {danio} de daño. Salud restante: {self.salud}")

    def __str__(self):
        return f"Personaje: {self.nombre}, Salud: {self.salud}, Ataque: {self.ataque}, Defensa: {self.defensa}"

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=30, defensa=10)

    def defender(self):
        self.defensa += 5
        print(f"{self.nombre} aumenta su defensa a {self.defensa}.")

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=40, defensa=5)

    def curar(self):
        self.salud += 20
        print(f"{self.nombre} se cura y su salud es ahora {self.salud}.")

g1 = Guerrero("Thor")
m1 = Mago("Merlín")

print("\t--- Comienza la batalla ---\n\tThor(Guerrero) vs Merlín(Mago)\n")
while True:
    print("Turno del Thor")
    op = input("Elige una acción: 1. Atacar 2. Defender\n")
    if op == '1':
        g1.atacar(m1)
    elif op == '2':
        g1.defender()
    else:
        print("Opción no válida.")
        continue
    if not m1.esta_vivo():
        print(f"{m1.nombre} ha sido derrotado. ¡{g1.nombre} gana!")
        break
    print("\nTurno del Merlín")
    op = input("Elige una acción: 1. Atacar 2. Curar\n")
    if op == '1':
        m1.atacar(g1)
    elif op == '2':
        m1.curar()
    else:
        print("Opción no válida.")
        continue
    if not g1.esta_vivo():
        print(f"{g1.nombre} ha sido derrotado. ¡{m1.nombre} gana!")
        break
    print("\n-----------------------------\n")  
print("\t--- Batalla Finalizada ---")
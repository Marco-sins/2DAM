import threading
import time

semaforo = threading.Condition()

class Persona(threading.Thread):
    def run(self):
        global semaforo

        with semaforo:
            print("Peatones cruzan")
            time.sleep(1)

class Vehiculo(threading.Thread):
    def run(self):
        global semaforo

        with semaforo:
            print("Vehiculos cruzan")
            time.sleep(1)


while True:
    vehiculo = Vehiculo()
    persona = Persona()
    persona1 = Persona()
    persona.start()
    persona1.start()
    vehiculo.start()

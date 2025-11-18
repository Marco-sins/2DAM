import threading
import time


evento = threading.Event()

class ladron(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while not evento.is_set():
            time.sleep(0.5)
            print("Estoy robando en un chino")
        
        print("Ya no robo. Me han pillado en un chino")
    
class polisia(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Soy la polisia y llego al chino.")
        evento.set()



elLadron = ladron()
elLadron.start()

time.sleep(2)

elPolisia = polisia()
elPolisia.start()

elLadron.join()
elPolisia.join()

print ("Programa terminado y ladrón en el chino atrapado.")

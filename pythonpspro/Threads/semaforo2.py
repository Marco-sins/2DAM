import threading
import time
import random

class Cruce:
    def __init__(self):
        self.condition = threading.Condition()
        self.peatonesCruzando = 0
        self.peatonesEnCruce = []
        self.cochesEnCruce = []
        self.cochesCruzando = 0

def coche(numCoche, cruce):
    print(f"LLega el coche {numCoche}")
    with cruce.condition:
        while cruce.cochesCruzando > 10 and cruce.cochesEnCruce.length <= 10:
            cruce.cochesEnCruce.append(numCoche)
            time.sleep(0.5)
            cruce.cochesCruzando -= 1

def peaton(numPeaton, cruce):
    print(f"Llega el peaton {numPeaton}")
    with cruce.condition:
        while cruce.peatonesCruzando > 10 and cruce.peatonesEnCruce.length <= 10:
            cruce.peatonesEnCruce.append(numPeaton)
            time.sleep(0.5)
            cruce.peatonesCruzando -= 1

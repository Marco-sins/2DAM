import threading #sin usar lock.
import time

g = 0
lock = threading.Lock()

def suma_uno():
    global g
    with lock:
        a=g
        time.sleep(0.001)
        g = a+1

def suma_tres():
    global g 
    with lock:
        a=g
        time.sleep(0.001)
        g =a+3

hilos = []
for func in [suma_uno,suma_tres]:
    hilos.append(threading.Thread(target=func))
    hilos[-1].start() # -1 señala al último elemento de la lista.

for hilo in hilos:
    hilo.join()

print(g)

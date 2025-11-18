import threading
import time
import random

colaImpresion = []
cond = threading.Condition()

class hiloImprime(threading.Thread):
    def run(self):
        global colaImpresion

        with cond:
            time.sleep(random.randint(1, 2))
            colaImpresion.append(f"Trabajo del proceso {threading.current_thread().name}")
            cond.notify()

class impresora(threading.Thread):
    def run(self):
        global colaImpresion
        global cond

        while True:
            with cond:
                cond.wait()
                print(colaImpresion[0])
                colaImpresion.pop(0)

laImpresora = impresora()
laImpresora.start()

while True:
    p = hiloImprime()
    p.start()
    print("")
    input("Pulsa para otro proceso")
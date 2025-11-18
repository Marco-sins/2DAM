import threading
import time

flag = threading.Event()
lentejas = []

class productor(threading.Thread):
    global flag
    global lentejas

    def run(self):
        while True:
            flag.wait()
            if lentejas:
                comanda = lentejas.pop(0)
                print(f"Estoy preparando las lentejas de la comanda {comanda}")
                time.sleep(1)
                print(f"Te mando las lentejitas calentitas de la comanda {comanda}")
            flag.clear()


class cliente(threading.Thread):
    global flag
    global lentejas

    def run(self):
        for i in range(1, 5):
            print(f"Quiero lentejas, comanda {i}")
            lentejas.append(i)
            flag.set()
            time.sleep(2)
        print("Que rica mis lentejitas con su chorizo portuano")

productor = productor()
productor.start()

cliente = cliente()
cliente.start()
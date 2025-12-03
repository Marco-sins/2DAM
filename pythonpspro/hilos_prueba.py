import threading
import time

pala = threading.Condition()
metros = 0

def cavar(tiempo, nombre, metros_cavados):
    global metros
    with pala:
        inicio = metros
        time.sleep(tiempo)
        print(f"{nombre} ha cogido la pala")
        metros = inicio + metros_cavados

jorge = threading.Thread(target=cavar, args=(4, "jorge", 3))
marco = threading.Thread(target=cavar, args=(1.5, "marco", 2))
jorge.start()
marco.start()
jorge.join()
marco.join()

print(f"Se termmino de cavar, se cavo {metros}")


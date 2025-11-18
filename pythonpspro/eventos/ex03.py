import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
stop_event = threading.Event()


def catInfinito():
    while not stop_event.is_set():
        logging.debug('Hilo en ejecucion...')
        time.sleep(1)
    logging.debug('Hilo detenido')

def catParador():
    time.sleep(random.randint(1, 5))
    print("El catParador entra en accion y te maulla fuerte")
    stop_event.set()

cat1 = threading.Thread(target=catInfinito, name="CatInfinito")
cat2 = threading.Thread(target=catParador, name="CatParador")

cat1.start()
cat2.start()

cat1.join()
cat2.join()

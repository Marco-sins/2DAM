'''
Crea un programa en Python que:

- Pida al usuario un número N (cantidad de procesos hijos a crear).

- Use os.fork() para crear N procesos hijos.

 -Cada hijo debe imprimir:

    Su número de proceso (PID).

    El número de orden en el que se cre (1<=numero<=N).

    Una pausa aleatoria entre impresiones (para simular trabajo), entre 1 y 2 minutos.
'''
import os
import time


n = int(input("Ingresa el numero de hijos que quieres crear (Piensa en la cpu)"))

def hijo(orden):
    print(f"Hijo {orden} creado con el número de proceso {os.getpid()}")
    os._exit(0)




i = 0
while i < n:
    newPid = os.fork()
    if (newPid == 0):
        hijo(i)
    i += 1
    time.sleep(1)


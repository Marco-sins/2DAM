'''
Escribe un programa en Python que:

Pida al usuario un número entero positivo N (por ejemplo, N = 100).
Se crean 2 procesos hijo.
El primer hijo buscará y contará los números primos en el rango [2, N//2].
El segundo hijo buscará y contará los números primos en el rango [N//2 + 1, N].
Cada hijo imprimirá cuántos primos encontró en su rango y la lista de los mismos.
'''

import os



def isPrime(n):
    i = 2
    while i < n:
        if (n % i == 0):
            return False
        i += 1
    return True

def contPrime(b, n):
    primero = []
    segundo = []
    if (b == 1):
        for i in range(2, n//2):
            if isPrime(i):
                primero.append(i)
        print(f"En el rango desde 2 hasta {n//2} el número de primos es {len(primero)}")
        print(f"Lista {primero}")
    else:
        for i in range(n//2 + 1, n):
            if isPrime(i):
                segundo.append(i)
        print(f"En el rango desde {n//2} hasta {n}, el número de primos es {len(segundo)}")
        print(f"Lista {segundo}")
    os._exit(0)
    

def main():
    n = int(input("Introduce un numero: "))

    i = 1
    while i < 3:
        newPid = os.fork()
        if (newPid == 0):
            contPrime(i, n)
        i += 1


main()

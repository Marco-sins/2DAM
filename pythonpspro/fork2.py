import os

def hijo(numHijo):
    sum = 0
    for i in range(1, (os.getpid() % 100)):
        sum = sum + i
    print(f"Soy el proceso hijo con PID: {os.getpid()} y la suma es: {sum}")
    os._exit(0)

def padre():
    for numHijo in range(1, 6):
        pid = os.fork()
        if (pid == 0):
            hijo(numHijo)
        else:
            print(f"Soy el proceso padre {numHijo} con PID: {os.getpid()}")

padre()

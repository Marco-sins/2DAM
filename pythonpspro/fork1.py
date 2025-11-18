import os

def hijo(numHijo):
    print(f"Soy el proceso hijo {numHijo} con PID {os.getpid()}")
    os._exit(0)

def padre():
    for numHijo in range(1, 4):
        newpid = os.fork()
        if (newpid == 0):
            hijo(numHijo)
        else:
            print(f"Soy el proceso padre con PID {os.getpid()}")

padre()
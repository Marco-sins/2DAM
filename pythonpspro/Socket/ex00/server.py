import socket
import random
import threading




def conexion():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 8082))
        server_socket.listen(5)
        print("Servidor conectado en 0.0.0.0:8082...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Conectado con {addr}")
            hilo = threading.Thread(target=game, args=(conn, addr))
            hilo.start()
    except socket.error as e:
        print(e)
    finally:
        server_socket.close()

def game(conn, addr):
    random_num = random.randint(1, 10)
    while True:
        print("Ingresa un numero del 1 al 10: ")
        data = conn.recv(1024)
        num = data.decode()
        if (int(num) == random_num):
            print(f"Has acertado, el numero era {random_num}")
            conn.sendall(b"0")
            break
        elif (int(num) < random_num):
            print("El numero es mayor")
            conn.sendall(b"1")
        else:
            print("El numero es menor")
            conn.sendall(b"-1")

conexion()
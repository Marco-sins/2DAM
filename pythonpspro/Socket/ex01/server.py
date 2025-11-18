import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("0.0.0.0", 8082))
    server_socket.listen(5)

    print("Servidor conectado en 0.0.0.0:8082...")
    conn, addr = server_socket.accept()
    print(f"Conectado con {addr}")

    while True:
        print("Di una palabra")
        data = conn.recv(1024)
        pala = data.decode()
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
except socket.error as e:
    print(f"Excepcion de socket: {e}")
finally:
    server_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(("127.0.0.1", 8081))

    data = client_socket.recv(1024)
    print("Servidor dice: ", data.decode())

    client_socket.sendall(b"Hola servidor, soy tu cliente")

except socket.error as e:
    print(f"Ha ocurrido el error {e}")
finally:
    client_socket.close()
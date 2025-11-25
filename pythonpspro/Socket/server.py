import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("127.0.0.1", 8081))
    server_socket.listen(5)

    print("Servidos esperando conexiones...")
    conn, addr = server_socket.accept() 
    print(f"Conectado con {addr}")
    conn.sendall(b"Hola, soy el servidor")
    data = conn.recv(1024)
    print("Cliente dice: ", data.decode())
    conn.close()
except socket.error as exc:
    print(f"Excepcion de socket: {exc}")
finally:
    server_socket.close()
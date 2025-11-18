import socket

# Crear socket de servidor. #AF_INET -> familia ip, transmision de stream mediante TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("127.0.0.1", 8081)) # si es 0.0.0.0 es desde cualquier interfaz
    # listen -> crea una cola de conexiones pendientes, conviene el socket en pasivo(servidor)
    server_socket.listen(5)

    print("Servidos esperando conexiones...")
    # Esperar un cliente. addr[0] es ip, addr[1] es el puerto
    conn, addr = server_socket.accept() # se queda bloqueado esperando a un cliente
    print(f"Conectado con {addr}")
    # Enviar y recibir datos
    conn.sendall(b"Hola, soy el servidor") # Mejor que usar conn.send, porque garantiza envio y si no excepcion
    data = conn.recv(1024) # se queda esperando hasta que se envia algo, 1024 bytes como maximo
    # Conviene los bytes recibidos a texto. Socket solo transmiten bytes
    # No todos los bytes representan textos. Por ejemplo una imagen, un emoticono
    print("Cliente dice: ", data.decode())
    # Cerrar conexion con ese cliente
    conn.close()
except socket.error as exc:
    print(f"Excepcion de socket: {exc}")
finally:
    # Quitamos el servidor de la escucha
    server_socket.close()
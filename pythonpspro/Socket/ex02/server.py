import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("127.0.0.1", 8081))

    
except socket.error as e:
    print(f"Exception de socket: {e}")
finally:
    server.close()
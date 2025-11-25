import socket
import threading

conexiones = []

def conexion():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 8081))
        server_socket.listen(20)
        print("Servidor conectado en 0.0.0.0:8081...")

        while True:
            conn, adrr = server_socket.accept()
            print(adrr)
            name = conn.recv(1024).decode()
            hilo = threading.Thread(name=name, target=chat, args=(conn, name), daemon=True)
            hilo.start()
            conexiones.append({'conexion':conn, 'name':name})
            print(f"{name} se ha conectado...")
    except socket.error as e:
        print(e)
    finally:
        server_socket.close()

def parserData(data, conn):
    try:
        if (data == "/conectados"):
            cone = ""
            b = False
            for conectados in conexiones:
                if b:
                    cone += ','
                cone += conectados['name']
                b = True
            conn.sendall(cone.encode())
            return True
        elif (data == "/help"):
            cone = "/conectados: Ver los conectados\n/help: Ver los comandos"
            conn.sendall(cone.encode())
            return True
        else:
            return False
    except socket.error as e:
        print(e)


def chat(conn, name):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                return
            if not parserData(data, conn):
                for conexion in conexiones:
                    if (conexion['conexion'] != conn):
                        msg = f"[{name}]: {data}"
                        conexion['conexion'].sendall(msg.encode())
    except socket.error as e:
        print(e)
    finally:
        print(f"{name} se ha desconectado...")
        for cone in conexiones:
            if (cone['conexion'] == conn):
                conexiones.remove(cone)

conexion()


"""
192.168.20.112: Miste
192.168.20.111: Ivan
192.168.20.105: Noah
192.168.20.164: Mario
192.168.20.112: Jorge
"""
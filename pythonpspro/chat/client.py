import socket
import threading
import time
import curses

running = True

def recibir(client_socket, win):
    try:
        global running
        while running:
            mensaje = client_socket.recv(1024).decode()
            win.addstr(f"{mensaje}\n")
            win.refresh()
    except socket.error as e:
        print(e)
    finally:
        client_socket.close()
        running = False

def mandar(client_socket, win_input, win_output):
    try:
        global running
        while running:
            put = win_input.getstr()
            client_socket.sendall(put)
            win_output.addstr(f"{put}\n")
            win_input.clear()
            win_input.refresh()
    except socket.error as e:
        print(e)
    except KeyboardInterrupt as e:
        print("Signal detected")
    finally:
        client_socket.close()
        running = False

def main(stdscr):
    curses.curs_set(1)
    curses.echo()
    height, width = stdscr.getmaxyx()
    win_msg = curses.newwin(height - 1, width, 0, 0)
    win_input = curses.newwin(1, width, height - 1, 0)
    

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Cambiar por la ip destino (192.168.20.110)
    client_socket.connect(("127.0.0.1", 8081))
    time.sleep(0.5)
    client_socket.sendall(win_input.getstr())

    recibir_hilo = threading.Thread(target=recibir, daemon=True, args=(client_socket, win_msg))
    mandar_hilo = threading.Thread(target=mandar, daemon=True, args=(client_socket, win_input, win_msg))
    recibir_hilo.start()
    mandar_hilo.start()
    recibir_hilo.join()
    mandar_hilo.join()

curses.wrapper(main)
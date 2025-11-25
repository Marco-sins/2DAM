import curses

def main(stdscr):
    curses.curs_set(1)

    alto, ancho = stdscr.getmaxyx()

    # Ventana para los mensajes (toda la pantalla menos la última línea)
    win_msgs = curses.newwin(alto - 1, ancho, 0, 0)

    # Ventana para escribir (la última línea)
    win_input = curses.newwin(1, ancho, alto - 1, 0)

    while True:
        win_input.clear()
        win_input.addstr(0, 0, "> ")
        win_input.refresh()

        texto = win_input.getstr().decode()

        win_msgs.addstr(f"{texto}\n")
        win_msgs.refresh()

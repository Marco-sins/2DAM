import subprocess

sale = True

while sale:
    mensaje = input("Escribe algo: ")
    if mensaje.lower() == "salir":
        sale = False
        break

    proceso = subprocess.Popen(
        ["tr", "[a-z]", "[A-Z]"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    proceso.stdin.write(mensaje)
    proceso.stdin.flush()
    proceso.stdin.close()

    salida = proceso.stdout.read()
    proceso.stdout.close()

    print(f"Mensaje usuario: {mensaje}")
    print(f"Mensaje usuario cambiado todo a mayusculas: {salida}")
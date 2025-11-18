import subprocess

process = subprocess.Popen(
    ["ping", "-c", "5", "google.com"],
    stdout=subprocess.PIPE,
    text=True
)


for linea in process.stdout:
    aux = linea.split("(")
    if len(aux) > 1:
        ip = aux[1].split(")")[0]
    else:
        ip = "Error, comprueba el codigo"
    
    aux = linea.split(":")
    if len(aux) > 1:
        datos = aux[1]
        print(f"El servidor {ip} manda los datos: {datos}")
    else:
        print("El servidor no ha enviado datos")

print("\nPing terminado.\n")
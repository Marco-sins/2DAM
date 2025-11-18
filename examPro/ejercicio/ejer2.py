'''
Crea un program en python que haga lo siguiente:
Pregunte por un directorio. Si se quiere listar el directorio actual no se introduce nada
El programa debe reportar cuando el directorio no es correcto por fallo del usuario.
No vale contar ni '.' ni '..' que son el directorio actual y el padre.
'''

import subprocess

entrada = input("Introduce el directorio(intro para actual): ")

if len(entrada) == 0:
    proceso = subprocess.Popen(
        ["ls", "-a"],
        stdout=subprocess.PIPE,
        text=True
    )
else:
    proceso = subprocess.Popen(
        ["ls", "-a", entrada],
        stdout=subprocess.PIPE,
        text=True
    )

i = 0
for linea in proceso.stdout:
    if (linea[0] == '.' and linea[1] != '.' and linea != "."):
        print(linea)
        i = i + 1

print(f"El numero de archivos ocultos es de {i}")
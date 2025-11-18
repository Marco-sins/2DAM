"""
Usando un programa que escribistes (ejemplos usados anteriormente en el capítulo),
almacena una función en un archivo separado. Importa la función en tu archivo de
programa principal, y llama a la función usando cada uno de los siguientes
procedimientos:
Mostrar un ejemplo de cada uno (usar distintos nombres para poder hacer uso de la
importación de dicha función al fichero principal de tu aplicación).
"""

from ex07 import hacer_sandwich
from ex08 import build_profile
from ex09 import almacenar_info_coche

# Llamada a la función hacer_sandwich desde ex07.py
hacer_sandwich("jamón", "queso", "lechuga")
hacer_sandwich("pavo", "tomate", "mayonesa", "mostaza")
hacer_sandwich("atún", "cebolla", "pepino", "aceitunas", "pimiento")
# Llamada a la función build_profile desde ex08.py
user_profile = build_profile('Marco', 'Membrilla',
                            location='Mijas',
                            field='DAM',
                            hobby='Videojuegos')
print(user_profile)
# Llamada a la función almacenar_info_coche desde ex09.py
info_coche = almacenar_info_coche('Toyota', 'Corolla',
                                    color='Rojo', transmision='Automática',
                                    año=2020)
print(info_coche)

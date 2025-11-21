"""
Enunciado:
Crea un diccionario donde las claves son nombres de usuario y los valores son
diccionarios con: nombre, apellido y ciudad.
Apartados:
a) Define al menos 3 usuarios con su información. (0,25 puntos)
b) Recorre el diccionario mostrando el nombre de usuario. (0,25 puntos)
c) Muestra nombre completo y ciudad de cada usuario usando el diccionario interno. (0,25 puntos)
d) Añade un nuevo usuario siguiendo la misma estructura. (0,25 puntos)
"""

usuarios = {
    "usuario1": {
        "nombre": "Ana",
        "apellido": "García",
        "ciudad": "Madrid"
    },
    "usuario2": {
        "nombre": "Luis",
        "apellido": "Martínez",
        "ciudad": "Barcelona"
    },
    "usuario3": {
        "nombre": "Sofía",
        "apellido": "López",
        "ciudad": "Valencia"
    }
}

for usuario in usuarios:
    print("Nombre de usuario:", usuario)
    info = usuarios[usuario]
    nombre_completo = f"{info['nombre']} {info['apellido']}"
    ciudad = info['ciudad']
    print(f"Nombre completo: {nombre_completo}, Ciudad: {ciudad}")
usuarios["usuario4"] = {
    "nombre": "Carlos",
    "apellido": "Sanchez",
    "ciudad": "Sevilla"
}
print(usuarios)
"""
Enunciado:
Crea un diccionario con varios usuarios y sus países.
Apartados:
a) Define el diccionario con al menos 4 usuarios. (0,25 puntos)
b) Recorre el diccionario mostrando los usuarios en orden alfabético (usa
sorted()). (0,25 puntos)
c) Comprueba si un usuario concreto existe en las claves. (0,25 puntos)
d) Si no existe, muestra un mensaje invitándolo a registrarse. (0,25 puntos)
"""

usuarios_paises = {
    "alice": "España",
    "bob": "México",
    "charlie": "Argentina",
    "diana": "Colombia"
}
for usuario in sorted(usuarios_paises.keys()):
    print(usuario)
usuario_buscar = "eva"
if usuario_buscar in usuarios_paises:
    print(f"El usuario {usuario_buscar} existe.")
else:
    print(f"El usuario {usuario_buscar} no existe. ¡Regístrate ahora!")
    
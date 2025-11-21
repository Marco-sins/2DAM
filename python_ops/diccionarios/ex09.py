"""
Enunciado:
Crea un diccionario donde cada clave es una persona y el valor una lista de
lugares favoritos.
Apartados:
a) Define al menos 3 personas con 2–3 lugares cada una. (0,25 puntos)
b) Recorre el diccionario e imprime el nombre de cada persona. (0,25 puntos)
c) Dentro del bucle, imprime cada lugar con sangría. (0,25 puntos)
d) Añade un nuevo lugar a una de las personas. (0,25 puntos)
"""

lugares_favoritos = {
    "Ana": ["Paris", "Nueva York", "Tokio"],
    "Luis": ["Londres", "Roma"],
    "Sofía": ["Barcelona", "Madrid", "Sevilla"]
}
for persona, lugares in lugares_favoritos.items():
    print("Persona:", persona)
    for lugar in lugares:
        print("\t-", lugar)
lugares_favoritos["Ana"].append("Berlin")
print(lugares_favoritos)

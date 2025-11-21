"""
Enunciado:
Crea un diccionario donde las claves sean nombres y los valores su comida
favorita.
Apartados:
a) Muestra solo los nombres usando keys(). (0,25 puntos)
b) Muestra solo las comidas usando values(). (0,25 puntos)
c) Recorre el diccionario con items() mostrando frases completas. (0,25 puntos)
d) Muestra las comidas sin repetición usando set(). (0,25 puntos)
"""

comidas_favoritas = {
    "Ana": "Pizza",
    "Luis": "Sushi",
    "Jose": "Tacos",
    "Carlos": "Pizza"
}

print(comidas_favoritas.keys())
print(comidas_favoritas.values())
for nombre, comida in comidas_favoritas.items():
    print(f"{nombre} tiene como comida favorita {comida}.")
print(set(comidas_favoritas.values()))
"""
Enunciado:
Crea un diccionario llamado ciudades, donde cada clave sea el nombre de una
ciudad y cada valor un diccionario con: país, población, dato interesante.
Apartados:
a) Crea 3 ciudades siguiendo la estructura. (0,25 puntos)
b) Recorre el diccionario e imprime el nombre de cada ciudad. (0,25 puntos)
c) Muestra su país, población y dato formateado. (0,25 puntos)
d) Añade una nueva ciudad con los mismos campos. (0,25 puntos)
"""

ciudades = {
    "París": {
        "país": "Francia",
        "población": "2.1 millones",
        "dato_interesante": "Conocida como la Ciudad de la Luz"
    },
    "Tokio": {
        "país": "Japón",
        "población": "14 millones",
        "dato_interesante": "La ciudad más poblada del mundo"
    },
    "Nueva York": {
        "país": "Estados Unidos",
        "población": "8.4 millones",
        "dato_interesante": "Famosa por la Estatua de la Libertad"
    }
}
for ciudad, info in ciudades.items():
    print("Ciudad:", ciudad)
    pais = info["país"]
    poblacion = info["población"]
    dato = info["dato_interesante"]
    print(f"\tPaís: {pais}")
    print(f"\tPoblación: {poblacion}")
    print(f"\tDato interesante: {dato}")
ciudades["Londres"] = {
    "país": "Reino Unido",
    "población": "9 millones",
    "dato_interesante": "Tiene el museo más grande del mundo"
}
print(ciudades)
"""
Enunciado:
Crea una lista de 5 aliens. Cada alien será un diccionario con: color, puntos,
velocidad.
Apartados:
a) Genera los 5 diccionarios en una lista. (0,25 puntos)
b) Cambia los 2 primeros aliens a color “amarillo” y velocidad “media”. (0,25
puntos)
c) Muestra solo los 3 primeros aliens. (0,25 puntos)
d) Indica cuántos aliens hay en total. (0,25 puntos)
"""

aliens = [
    {"color": "verde", "puntos": 5, "velocidad": "lenta"},
    {"color": "verde", "puntos": 5, "velocidad": "lenta"},
    {"color": "rojo", "puntos": 10, "velocidad": "rápida"},
    {"color": "azul", "puntos": 15, "velocidad": "media"},
    {"color": "amarillo", "puntos": 20, "velocidad": "rápida"}
]
for alien in aliens[:2]:
    alien["color"] = "amarillo"
    alien["velocidad"] = "media"
for alien in aliens[:3]:
    print(alien)
print("Número total de aliens:", len(aliens))
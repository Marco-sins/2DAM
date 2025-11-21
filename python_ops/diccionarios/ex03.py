"""
Enunciado:
Simula un inventario donde las claves son nombres de productos y sus valores
el stock.
Apartados:
a) Crea un diccionario con 4 productos. (0,25 puntos)
b) Reduce el stock de un producto (resta). (0,25 puntos)
c) Añade un nuevo producto al diccionario. (0,25 puntos)
d) Elimina un producto del inventario. (0,25 puntos)
"""

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
    "peras": 15
}
inventario["naranjas"] -= 5
inventario["uvas"] = 40
del inventario["platanos"]
print(inventario)
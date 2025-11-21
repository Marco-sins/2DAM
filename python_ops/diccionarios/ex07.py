"""
Enunciado:
Modela un pedido de pizza con un diccionario que incluya: tipo de masa y una
lista de toppings.
Apartados:
a) Define el diccionario con 1 masa y al menos 3 toppings. (0,25 puntos)
b) Recorre la lista de toppings e imprímelos con sangría. (0,25 puntos)
c) Añade un nuevo topping. (0,25 puntos)
d) Cambia la masa por otro tipo. (0,25 puntos)
"""

pedido_pizza = {
    "tipo_masa": "delgada",
    "toppings": ["pepperoni", "champiñones", "pimientos"]
}
print("Tipo de masa:", pedido_pizza["tipo_masa"])
print("Toppings:")
for topping in pedido_pizza["toppings"]:
    print("\t-", topping)
pedido_pizza["toppings"].append("aceitunas")
pedido_pizza["tipo_masa"] = "gruesa"
print("Pedido actualizado:", pedido_pizza)

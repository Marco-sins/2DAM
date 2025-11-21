"""
Apartados
1. Crea una función nuevo_producto(nombre, precio, stock) que construya un
diccionario.
2. Guarda cinco productos en una lista llamada inventario.
3. Crea una función mostrar_inventario(lista) que recorra e imprima cada
producto.
4. Añade una función actualizar_stock(producto, cantidad) que reste o sume
unidades.
Tip
• Los diccionarios pasan referencia, así que modificarás el original.
"""

def nuevo_producto(nombre, precio, stock):
    return {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

inventario = [
    nuevo_producto("Manzana", 0.5, 100),
    nuevo_producto("Banana", 0.3, 150),
    nuevo_producto("Naranja", 0.7, 80),
    nuevo_producto("Pera", 0.6, 120),
    nuevo_producto("Uva", 1.0, 60)
]

def mostrar_inventario(lista):
    for producto in lista:
        print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

def actualizar_stock(producto, cantidad):
    producto['stock'] += cantidad

mostrar_inventario(inventario)
print("\nActualizando stock...\n")
actualizar_stock(inventario[0], -10)
mostrar_inventario(inventario)
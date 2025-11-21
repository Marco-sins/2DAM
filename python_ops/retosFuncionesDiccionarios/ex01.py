"""
Crea un pequeño sistema para guardar contactos usando diccionarios y
funciones.
Apartados
1. Crea una función crear_contacto(nombre, telefono) que devuelva un
diccionario con esa información.
2. Crea una función mostrar_contacto(contacto) que imprima el nombre y el
teléfono de forma ordenada.
3. Crea tres contactos y guárdalos en una lista.
4. Recorre la lista y usa la función de mostrar para enseñar todos los
contactos.
Tip
• Recuerda que una función puede devolver un diccionario usando return.
"""

def crear_contacto(nombre, telefono):
    return {
        "nombre": nombre,
        "telefono": telefono
    }

def mostrar_contacto(contacto):
    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")

contactos = [
    crear_contacto("Ana", "123456789"),
    crear_contacto("Luis", "987654321"),
    crear_contacto("Sofía", "555666777")
]

for contacto in contactos:
    mostrar_contacto(contacto)
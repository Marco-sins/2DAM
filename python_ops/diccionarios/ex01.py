"""
Enunciado:
Crea un diccionario llamado contacto con información de una persona:
nombre, apellido, teléfono y ciudad.
Apartados:
a) Define el diccionario con 4 claves y sus valores. (0,25 puntos)
b) Muestra cada clave y valor mediante accesos con []. (0,25 puntos)
c) Añade un nuevo campo llamado email y muéstralo. (0,25 puntos)
d) Modifica la ciudad y elimina el teléfono usando del. (0,25 puntos)
"""

contacto = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "telefono": "123456789",
    "ciudad": "Madrid"
}

print("Nombre:", contacto["nombre"])
print("Apellido:", contacto["apellido"])
print("Teléfono:", contacto["telefono"])
print("Ciudad:", contacto["ciudad"])

contacto["email"] = "default@default.com"
print("Email:", contacto["email"])

contacto["ciudad"] = "Malaga"
del contacto["telefono"]

print(contacto)
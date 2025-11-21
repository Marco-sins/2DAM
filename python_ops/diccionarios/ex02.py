"""
Enunciado:
Crea un diccionario que almacene calificaciones de varios módulos para un
estudiante.
Apartados:
a) Define el diccionario con al menos 3 módulos y sus notas. (0,25 puntos)
b) Modifica la nota de uno de los módulos. (0,25 puntos)
c) Intenta acceder con get() a un módulo que no exista, mostrando un mensaje
por defecto. (0,25 puntos)
d) Añade un nuevo módulo con su nota. (0,25 puntos)
"""

calificaciones = {
    "matematicas": 8.5,
    "historia": 7.0,
    "ciencias": 9.0
}
calificaciones["historia"] = 8.0
nota_filosofia = calificaciones.get("filosofia", "Módulo no encontrado")
print("Nota de Filosofía:", nota_filosofia)
calificaciones["filosofia"] = 8.5
print(calificaciones)

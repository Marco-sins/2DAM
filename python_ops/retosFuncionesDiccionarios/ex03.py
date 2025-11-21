"""
Apartados
1. Crea una función crear_alumno(nombre, nota) que devuelva un diccionario.
2. Crea una lista con 4 alumnos.
3. Crea una función media(lista_alumnos) que devuelva la media de las notas.
4. Muestra la nota media con formato: "La media es X.X".
Tip
• Para acceder a datos dentro del diccionario usa diccionario['clave'].
"""

def crear_alumno(nombre, nota):
    return {
        "nombre": nombre,
        "nota": nota
    }

alumnos = [
    crear_alumno("Ana", 8.5),
    crear_alumno("Luis", 7.0),
    crear_alumno("Marco", 9.0),
    crear_alumno("Carlos", 6.5)
]

def media(lista_alumnos):
    total = 0
    for alumno in lista_alumnos:
        total += alumno['nota']
    return total / len(lista_alumnos)

print(f"La media es {media(alumnos):.1f}")
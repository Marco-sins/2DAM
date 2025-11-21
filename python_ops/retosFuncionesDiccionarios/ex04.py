"""
Apartados
1. Crea una función crear_perfil(nombre, edad=None, ciudad=None).
2. La función debe devolver un diccionario que solo incluya datos si fueron
proporcionados.
3. Crea tres perfiles distintos usando parámetros posicionales y keyword.
4. Muestra todos los perfiles generados.
Tip
• Usa if valor: para comprobar si un parámetro opcional fue enviado.
"""

def crear_perfil(nombre, edad=None, ciudad=None):
    perfil = {"nombre": nombre}
    if edad is not None:
        perfil["edad"] = edad
    if ciudad is not None:
        perfil["ciudad"] = ciudad
    return perfil

perfil1 = crear_perfil("Ana", 25, "Madrid")
perfil2 = crear_perfil("Luis", ciudad="Barcelona")
perfil3 = crear_perfil("Marco", 30)
perfiles = [perfil1, perfil2, perfil3]

for perfil in perfiles:
    print(perfil)

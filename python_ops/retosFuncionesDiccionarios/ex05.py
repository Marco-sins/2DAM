"""
Apartados
1. Solicita al usuario una frase (o crea una fija).
2. Crea una función que reciba la frase y devuelva un diccionario con el
conteo de palabras.
3. Muestra el diccionario resultante.
4. Indica cuál es la palabra más repetida.

Tip
• Usa .split() para separar palabras y suma en un diccionario.
"""

def contar_palabras(frase):
    palabras = frase.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower().strip('.,!?;"\'()[]{}')  # Normalizar palabras
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo
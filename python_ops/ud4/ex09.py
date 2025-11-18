"""
Escribe una función que almacene información de un coche en un diccionario. La
función debería siempre recibir el nombre del fabricante y modelo. Debería recibir un
número arbitrario de argumentos por palabra clave (keyword), tal como color y una
característica opcional. La función debería ser llamada de la siguiente forma:
"""

def almacenar_info_coche(fabricante, modelo, **caracteristicas):
    caracteristicas['fabricante'] = fabricante
    caracteristicas['modelo'] = modelo
    return caracteristicas

info_coche = almacenar_info_coche('Toyota', 'Corolla',
                                    color='Rojo', transmision='Automática',
                                    año=2020)
print(info_coche)
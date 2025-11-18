"""
Comienza con una copia de la función user_profile de la pagina 148.
Construye un perfil de tu persona llamando a build_profile(), usando tu nombre,
apellidos y tres pares de clave-valor que te describan.
"""

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Marco', 'Membrilla',
                            location='Mijas',
                            field='DAM',
                            hobby='Videojuegos')
print(user_profile)
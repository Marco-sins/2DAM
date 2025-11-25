
# listado general 30 libros
biblioteca_general = [
    {"titulo": "El Hobbit", "autor": "Tolkien", "paginas": 300, "genero": "Fantasía"},
    {"titulo": "1984", "autor": "Orwell", "paginas": 250, "genero": "Distopía"},
    {"titulo": "Dune", "autor": "Herbert", "paginas": 500, "genero": "Ciencia ficción"},
    {"titulo": "It", "autor": "Stephen King", "paginas": 600, "genero": "Terror"},
    {"titulo": "Fundación", "autor": "Asimov", "paginas": 230, "genero": "Ciencia ficción"},
    {"titulo": "Neuromante", "autor": "William Gibson", "paginas": 280, "genero": "Ciencia ficción"},
    {"titulo": "El Juego de Ender", "autor": "Orson Scott Card", "paginas": 320, "genero": "Ciencia ficción"},
    {"titulo": "La Llamada de Cthulhu", "autor": "H.P. Lovecraft", "paginas": 140, "genero": "Terror"},
    {"titulo": "Drácula", "autor": "Bram Stoker", "paginas": 400, "genero": "Terror"},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "paginas": 230, "genero": "Terror"},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "paginas": 100, "genero": "Fábula"},
    {"titulo": "Crimen y castigo", "autor": "Dostoievski", "paginas": 430, "genero": "Drama"},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "paginas": 600, "genero": "Novela"},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "paginas": 470, "genero": "Realismo mágico"},
    {"titulo": "Don Quijote", "autor": "Cervantes", "paginas": 1000, "genero": "Clásico"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "paginas": 520, "genero": "Misterio"},
    {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "paginas": 450, "genero": "Thriller"},
    {"titulo": "Los Juegos del Hambre", "autor": "Suzanne Collins", "paginas": 370, "genero": "Distopía"},
    {"titulo": "Harry Potter 1", "autor": "J.K. Rowling", "paginas": 350, "genero": "Fantasía"},
    {"titulo": "Harry Potter 2", "autor": "J.K. Rowling", "paginas": 370, "genero": "Fantasía"},
    {"titulo": "Harry Potter 3", "autor": "J.K. Rowling", "paginas": 430, "genero": "Fantasía"},
    {"titulo": "La Metamorfosis", "autor": "Kafka", "paginas": 120, "genero": "Absurdismo"},
    {"titulo": "El Nombre del Viento", "autor": "Patrick Rothfuss", "paginas": 700, "genero": "Fantasía"},
    {"titulo": "El Temor de un Hombre Sabio", "autor": "Patrick Rothfuss", "paginas": 1100, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 1", "autor": "Tolkien", "paginas": 500, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 2", "autor": "Tolkien", "paginas": 450, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 3", "autor": "Tolkien", "paginas": 550, "genero": "Fantasía"},
    {"titulo": "Solaris", "autor": "Stanislaw Lem", "paginas": 300, "genero": "Ciencia ficción"},
    {"titulo": "El Perfume", "autor": "Patrick Süskind", "paginas": 280, "genero": "Drama"},
    {"titulo": "El Alquimista", "autor": "Paulo Coelho", "paginas": 210, "genero": "Fábula"}
]


# ============================================
#   PLANTILLA DE PRUEBA OBSERVACIÓN DIRECTA – GESTIÓN BIBLIOTECA
# ============================================


# --- EJERCICIO 1 ---
def crear_libro(titulo, autor, paginas):
    """
    TODO: devolver un diccionario con los datos del libro.
    """
    #Devuelve un libro
    return {"titulo": titulo, "autor": autor, "paginas":paginas}


# --- EJERCICIO 2 ---
def buscar_por_autor(biblio, autor):
    """
    TODO: devolver todos los libros cuyo autor coincide.
    """
    #Mete en la lista los libros que se encuentren del autor
    libros = []
    #Mira si se ha encontrado para mostrar error o no
    b = False
    for libro in biblio:
        if libro.get("autor") == autor:
            libros.append(libro)
            b = True
    if not (b):
        print("Autor no encontrado")
    return libros


# --- EJERCICIO 3 ---
def info_libro(diccionario, titulo):
    """
    TODO: imprimir toda la información de un libro dentro de un diccionario de diccionarios.
    Si no existe, mostrar mensaje adecuado.
    """
    #Busca el la informacion del libro
    #Boleano para mirar si se encuentra o no existe
    b = False
    for libro in diccionario:
        if (libro.get(titulo)):
            print(libro)
            b = True
    if not b:
        print("El libro no esta en la biblioteca")

    pass



# --- EJERCICIO 4 ---
def crear_sistema_bibliotecas():
    """
    TODO:
    - Crear 3 bibliotecas.
    - Crear el diccionario sistema_bibliotecas con:
        "central", "universitaria", "infantil"
    - Añadir biblioteca "digital" vacía.
    - Devolver sistema_bibliotecas
    """
    #Crea bibliotecas con libros creado por defecto y los mete en el sistema que devuelve
    biblioteca1 = [crear_libro(titulo="titulo1", autor="Autor1", paginas=100), crear_libro(titulo="titulo2", autor="Autor2", paginas=200), crear_libro(titulo="titulo3", autor="Autor3", paginas=300)] 
    biblioteca2 = [crear_libro(titulo="titulo1", autor="Autor123", paginas=100), crear_libro(titulo="titulo2", autor="Autor2", paginas=200), crear_libro(titulo="titulo3", autor="Autor3", paginas=300)] 
    biblioteca3 = [crear_libro(titulo="titulo123", autor="Autor1", paginas=100), crear_libro(titulo="titulo2", autor="Autor2", paginas=200), crear_libro(titulo="titulo3", autor="Autor3", paginas=300)]
    sistema_biblioteca = {"Central": biblioteca1, "Universitaria": biblioteca2, "Infantil": biblioteca3, "Digital":""}
    return sistema_biblioteca
    pass



# --- EJERCICIO 5 ---
def buscar_libro_global(sistema, titulo):
    """
    TODO: buscar un libro en todas las bibliotecas del sistema.
    """
    #Busca el libro en las bibliotecas del sistema
    central = sistema.get("Central")
    universitaria = sistema.get("Universitaria")
    infantil = sistema.get("Infantil")
    digital = sistema.get("Digital")
    for libro in central:
        if (libro.get("titulo") == titulo):
            print(libro)
    for libro in universitaria:
        if (libro.get("titulo") == titulo):
            print(libro)
    for libro in infantil:
        if (libro.get("titulo") == titulo):
            print(libro)
    for libro in digital:
        if (libro.get("titulo") == titulo):
            print(libro)
    pass


def buscar_autor_global(sistema, autor):
    """
    TODO: devolver todos los libros de un autor en todas las bibliotecas.
    """
    #Busca libros de autores en las bibliotecas del sistema
    central = sistema.get("Central")
    universitaria = sistema.get("Universitaria")
    infantil = sistema.get("Infantil")
    digital = sistema.get("Digital")
    for libro in central:
        if (libro.get("autor") == autor):
            print(libro)
    for libro in universitaria:
        if (libro.get("autor") == autor):
            print(libro)
    for libro in infantil:
        if (libro.get("autor") == autor):
            print(libro)
    for libro in digital:
        if (libro.get("autor") == autor):
            print(libro)
    pass


# ============================================
#          MENÚ PRINCIPAL DEL EXAMEN
# ============================================

def menu_principal():
    biblioteca1 = []
    sistema_bibliotecas = []
    bilioteca_detallada = [
        {"titulo1": {"autor": "Yo", "paginas": 25, "genero": "fantasia"}, "prestamos": {"disponible": True, "dias_restantes": 0}},
        {"titulo2": {"autor": "Yo", "paginas": 25, "genero": "fantasia"}, "prestamos": {"disponible": True, "dias_restantes": 0}},
        {"titulo3": {"autor": "Yo", "paginas": 25, "genero": "fantasia"}, "prestamos": {"disponible": True, "dias_restantes": 0}},
        {"titulo4": {"autor": "Yo", "paginas": 25, "genero": "fantasia"}, "prestamos": {"disponible": True, "dias_restantes": 0}},
        {"titulo5": {"autor": "Yo", "paginas": 25, "genero": "fantasia"}, "prestamos": {"disponible": True, "dias_restantes": 0}}
        ]
    while True:
        print("\n===== GESTIÓN DE BIBLIOTECA =====")
        print("1. Crear libro")
        print("2. Buscar libros por autor")
        print("3. Mostrar información detallada de un libro")
        print("4. Crear sistema de bibliotecas")
        print("5. Buscar libro en todas las bibliotecas")
        print("6. Buscar autor en todas las bibliotecas")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            #Creacion del libro y de la biblioteca
            print("OPCIÓN 1: Crear libro")
            titulo = input("Ingrese el nombre del libro: ")
            autor = input("Ingrese el nombre del autor del libro: ")
            paginas = int(input("Ingrese las paginas del libro: "))
            biblioteca1 = [
                crear_libro(titulo=titulo, autor=autor, paginas=paginas),
                crear_libro(titulo="Titulo1", autor="Autor1", paginas=100),
                crear_libro(titulo="Titulo2", autor="Autor2", paginas=200),
                crear_libro(titulo="Titulo3", autor="Autor3", paginas=300),
                crear_libro(titulo="Titulo4", autor="Autor4", paginas=400)
            ]
            for libro in biblioteca1:
                libro["genero"] = "Fantasia"
                print(libro)
                
            # TODO: pedir datos al usuario y llamar a crear_libro()

        elif opcion == "2":
            #Se busca el libro por el autor
            print("OPCIÓN 2: Buscar libros por autor")
            autor = input("Ingrese el nombre del autor: ")
            lista = buscar_por_autor(biblio=biblioteca_general, autor=autor)
            for libro in lista:
                print(libro)
            lista = buscar_por_autor(biblio=biblioteca1, autor="Autor1")
            for libro in lista:
                print(libro)
            # TODO:

        elif opcion == "3":
            #Se devuelve la informacion del libro
            print("OPCIÓN 3: Información detallada de libro")
            info_libro(bilioteca_detallada, input("Ingresa el titulo del libro: "))
            # TODO: 

        elif opcion == "4":
            #Crea un sistema de bibliotecas
            print("OPCIÓN 4: Crear sistema de bibliotecas")
            sistema_bibliotecas = crear_sistema_bibliotecas()
            print(len(sistema_bibliotecas))
            for sistema, bibloteca in sistema_bibliotecas.items():
                print(f"{sistema}: {bibloteca}")
            # TODO: 

        elif opcion == "5":
            #Busca y muestra si existe el libro en todas las bibliotecas del sistema
            print("OPCIÓN 5: Búsqueda global de libro")
            buscar_libro_global(sistema_bibliotecas, "titulo123")
            # TODO

        elif opcion == "6":
            #Busca y muestra si existe el autor en todas las bibliotecas del sistema
            print("OPCIÓN 6: Búsqueda global de autor")
            buscar_autor_global(sistema_bibliotecas, "Autor123")
            # TODO

        elif opcion == "0":
            #Sale del programa
            print("Saliendo del programa...")
            break

        else:
            #Por si se falla en el input
            print("Opción no válida. Intente de nuevo.")


# EJECUTAR MENÚ
menu_principal()

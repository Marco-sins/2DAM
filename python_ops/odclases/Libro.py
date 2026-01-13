class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
l = Libro("Cien Años de Soledad", "Gabriel García Márquez")
print(l)
"""
Escribe una función llamada make_shirt() que acepta el tamaño “XS,S,M,L,XL,XXL”
y el texto de un mensaje que debería de ser impreso en la camiseta.
La función debería imprimir una frase que resuma el tamaño de la camiseta y el mensaje
impreso en ella.
Llama a la función una vez usando argumentos posicionales para crear una camiseta.
Llama a la función una segunda vez usando los argumentos por palabra clave
(keywork).
"""

def make_shirt(size, text):
    print(f"Size: {size}")
    print(f"Message: {text}")


make_shirt("S", "Macarrones con barbarcoa")
make_shirt(size="XL", text="Huevo sin sal")

"""
Escribe una función llamada make_shirt() que acepta el tamaño “XS,S,M,L,XL,XXL”
y el texto de un mensaje que debería de ser impreso en la camiseta.
La función debería imprimir una frase que resuma el tamaño de la camiseta y el mensaje
impreso en ella.
Llama a la función una vez usando argumentos posicionales para crear una camiseta.
Llama a la función una segunda vez usando los argumentos por palabra clave
(keywork).
"""

def make_shirt(size):
    if size == "XS":
        print("T-Shirt XS made")
    elif size == "S":
        print("T-Shirt S made")
    elif size == "M":
        print("T-Shirt M made")
    elif size == "L":
        print("T-Shirt L made")
    elif size == "XL":
        print("T-Shirt XL made")
    elif size == "XXL":
        print("T-Shirt XXL made")
    else:
        print("Bad size")

def main():
    while True:
        size = input("Enter a size T-Shirt (XS, S, M, L, XL, XXL) or exit for exit: ")
        if size == "exit":
            return
        make_shirt(size=size)

if __name__ == '__main__':
    main()
"""
Modifica la función make_tshirt (“del ejercicio anterior”) para que las camisetas con
tamaño L por defecto muestre el mensaje “I love Python” si no se especifica mensaje.
Haz la llamada a make_shirt() para las camisetas con tamaño L y M y muestre su
mensaje por defecto, y haz la llamada a make_shirt() de cualquier otro tamaño con un
mensaje diferente.
"""


def make_shirt(size):
    if size == "XS":
        print("T-Shirt XS made")
    elif size == "S":
        print("T-Shirt S made")
    elif size == "M":
        print("I love Python!")
    elif size == "L":
        print("I love Python!")
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
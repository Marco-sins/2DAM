"""
Modifica la función make_tshirt (“del ejercicio anterior”) para que las camisetas con
tamaño L por defecto muestre el mensaje “I love Python” si no se especifica mensaje.
Haz la llamada a make_shirt() para las camisetas con tamaño L y M y muestre su
mensaje por defecto, y haz la llamada a make_shirt() de cualquier otro tamaño con un
mensaje diferente.
"""


def make_shirt(size, text):
    print(f"Size: {size}")
    if (size == "L" or size == "M"):
        print("Message: I love Python!")
    else:
        print(f"Message: {text}")
    
make_shirt("S", "Macarrones con barbarcoa")
make_shirt(size="L", text="Huevo sin sal")

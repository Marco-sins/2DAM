"""
Comienza con una copia del ejercicio anterior (ejercicio 3).
Escribe una función llamada send_messages() que imprima cada mensaje recibido y
mueva cada mensaje a una lista llamada sent_messages a la vez que se imprime el
mensaje. Después de llamar la función send_messages(), imprime ambas listas de
mensajes (lista messages y lista sent_messages) para asegurarte que los mensajes fueron
movidos de lista correctamente.
"""

sent_messages = []

def send_messages(text):
    print(text)
    sent_messages.append(text)

def show_messages():
    lista = ["email John", "buy flowers", "complete tutorial", "buy food"]
    for text in lista:
        print(text)

show_messages()
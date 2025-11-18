"""
Comienza con una copia del ejercicio anterior (ejercicio 4).
Llama a la función send_messages() con una copia de la lista de mensajes.

Después de llamar la función send_messages(), imprime ambas listas de mensajes (lista
messages y lista sent_messages) para asegurarte que los mensajes fueron movidos de
lista correctamente.
"""

sent_messages = []
lista = ["email John", "buy flowers", "complete tutorial", "buy food"]

def send_messages():
    while len(lista) > 0:
        print(lista[0])
        sent_messages.append(lista[0])
        lista.remove(lista[0])
    print(lista)
    print(sent_messages)

send_messages()
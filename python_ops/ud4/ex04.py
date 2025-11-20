"""
Haz una lista que contenga una serie de mensajes breves. Pasa la lista a una función
llamada show_messages(), que imprima cada mensaje de texto en la lista.
La lista contendrá los mensajes: email John, buy flowers, complete tutorial y buy food.
"""

lista = ["email John", "buy flowers", "complete tutorial", "buy food"]

def show_messages():
    for text in lista:
        print(text)

show_messages()

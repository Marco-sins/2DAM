""" 
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""


personas = ["Rufian", "Ernesto", "Princesa Diana"]
print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[1]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[2]}, estas invitado a cenar el dia 3 de septiembre")

print("\n-------------------------\n")
print("Ernesto no puede venir a cenar")

personas.remove("Ernesto")
personas.append("Michael Jackson")
print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[1]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[2]}, estas invitado a cenar el dia 3 de septiembre")

personas.insert(1, "Armando Paredes")
personas.insert(int(len(personas) / 2), "Leo Messi")
personas.append("Julian")

print("\n-------------------------\n")
print("Se ha encontrado una mesa mas grande")

print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[1]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[2]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[3]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[4]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[5]}, estas invitado a cenar el dia 3 de septiembre")

print("\n-------------------------\n")
print("No va a llegar la mesa a tiempo")

print(f"Buenas tardes {personas[2]}, no estas invitado")
personas.pop(2)
print(f"Buenas tardes {personas[2]}, no estas invitado")
personas.pop(2)
print(f"Buenas tardes {personas[2]}, no estas invitado")
personas.pop(2)
print(f"Buenas tardes {personas[2]}, no estas invitado")
personas.pop(2)

print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
personas.pop(0)
print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
personas.pop(0)

print(personas)
""" 
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
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
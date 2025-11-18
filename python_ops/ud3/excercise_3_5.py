""" 
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
"""

personas = ["Rufian", "Ernesto", "Princesa Diana"]
print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[1]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[2]}, estas invitado a cenar el dia 3 de septiembre")

print("\n-------------------------\n")

personas.remove("Ernesto")
personas.append("Michael Jackson")
print(f"Buenas tardes {personas[0]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[1]}, estas invitado a cenar el dia 3 de septiembre")
print(f"Buenas tardes {personas[2]}, estas invitado a cenar el dia 3 de septiembre")

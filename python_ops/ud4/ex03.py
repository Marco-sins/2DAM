"""
Escribe una función llamada describe_city() que acepta el nombre de una ciudad y su
país. La función deberá imprimir una frase simple, tal como “Reykjavik is Island”.
Da valores por defecto a los parámetros para el pais.
Llama a tu función con tres ciudades diferentes, al menos una que no sea el pais por
defecto.
"""

def describe_city(city, country):
    print(f"{city} is in {country}")

describe_city("Barcelona", "Spain")
describe_city("Reykjavik", "Island")
describe_city("Madrid", "Spain")

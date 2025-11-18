# Funcion que convierte de kilometros a millas

def convertMillas():
    km = float(input("Introduce la cantidad de kilometros a convertir a millas: "))
    millas = (km * 7.38) / 11.88
    print(f"En millas, {km} kilometros son {millas} millas")

# Funcion que convierte de millas a kilometros

def convertKm():
    millas = float(input("Introduce la cantidad de millas a convertir a kilometros"))
    km = (millas * 11.88) / 7.38
    print(f"En kilometros, {millas} millas son {km} kilometros")

convertMillas()
convertKm()
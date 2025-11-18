# Funcion que calcula todo

def calc():
    n = float(input("Introduce la x: "))
    result = (3 * n ** 3) - (2 * n ** 2) + (3 * n) - 1
    print(f"El resultado es: {result}")

calc()
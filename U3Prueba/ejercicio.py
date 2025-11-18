''' 
Desarrolla un programa en Python que permita gestionar un control de tareas pendientes, aplicando el uso de listas, condicionales y bucles.
Cada tarea debe representarse como una lista con tres elementos:
tarea = [nombre, prioridad, estado]
donde:
•	nombre → Cadena de texto con el nombre de la tarea.
•	prioridad → Número entero del 1 al 10 (1 = baja, 10 = alta).
•	estado → Cadena con el valor "pendiente" o "finalizada".

Objetivos de aprendizaje
•	Practicar el uso de listas de listas.
•	Utilizar condicionales (if, elif, else).
•	Aplicar bucles (while, for) para recorrer listas.
•	Manipular listas y técnicas de ordenamiento.
•	Implementar un menú interactivo con opciones múltiples.

'''

# =====================================================
#   CONTROL DE TAREAS PENDIENTES
#   Plantilla base - Para completar por el alumno
# =====================================================



# Apartado 2
def agregar_tarea(tareas):
    # TODO: Solicitar nombre y prioridad (1-10)
    # TODO: Crear lista [nombre, prioridad, estado]
    # TODO: Agregar a la lista principal con append()

    while True:
        nombre = input("Ingrese el nombre de la tarea: ")
        if (nombre.isalpha()):
            prioridad = input("Ingresa la prioridad de la tarea (1-10): ")
            if (prioridad.isnumeric()):
                prioridad = int(prioridad)
                if (prioridad >= 1 and prioridad <= 10):
                    break
                else:
                    print ("Ingrese un valor valido")
            else: 
                print("Ingrese un numero")
        else:
            print("Ingresa un nombre valido")
    new_tarea = [nombre, prioridad, "pendiente"]
    tareas.append(new_tarea)
    pass


# Apartado 3
def cambiar_estado(tareas, nombre, estado):
    # TODO: Cambiar estado de "pendiente" a "finalizada" o viceversa

    for tarea in tareas:
        if (tarea[0] == nombre):
            tarea[2] = estado
    pass

def eliminar_tarea(tareas,nombre):
    # TODO: Eliminar una tarea según su nombre

    i = 0
    while i < len(tareas):
        if (tareas[i][0] == nombre):
            tareas.pop(i)
        else:
            i += 1
    pass


# Apartado 4
def ordenar_tareas_por_prioridad(tareas):
    # TODO: Ordenar tareas por prioridad de mayor a menor
    
    '''
    # Te dejo el algoritmo de la burbuja que te puede servir
    
    Cómo funciona ( Ejemplo )
    1 La lista [5, 2, 9, 1, 5, 6] se recorre de izquierda a derecha.

    2 Comparamos cada par de elementos:

        5 y 2 → se intercambian → [2, 5, 9, 1, 5, 6]

        5 y 9 → no se intercambian

        9 y 1 → se intercambian → [2, 5, 1, 9, 5, 6]

        … y así sucesivamente.

    3 Cada pasada “empuja” el número más grande hacia el final.
    4 Se repite hasta que la lista queda completamente ordenada.
    
    
    def burbuja(lista):
        n = len(lista)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp

    '''
    
    # Paso 1: Creamos una copia de la lista original para no modificarla directamente
    

    # Paso 2: Implementamos un ordenamiento sencillo (tipo burbuja)
    #         porque este tipo de ordenamiento se estudia en este tema.
    #         Recorremos la lista varias veces comparando elementos adyacentes.
    
    
    # Paso 3: Devolvemos la nueva lista ordenada
    

    l = len(tareas)

    i = 0
    while i < l - 1:
        if (tareas[i][1] > tareas[i + 1][1]):
            aux = tareas[i]
            tareas[i] = tareas[i + 1]
            tareas[i + 1] = aux
            i = 0
        else:
            i += 1
    return tareas


# Apartado 5
def buscar_tarea(tareas):
    # TODO: Buscar una tarea por nombre y mostrar su información
    # 1. Estudiar Python | Prioridad: 8 | Estado: pendiente
    
    nombre = input("Ingresa el nombre de la tarea: ")
    b = True
    for tarea in tareas:
        if (tarea[0] == nombre):
            print(tarea)
            b = False
    if b:
        print("No se ha encontrado la tarea")
    pass


# Apartado 6
def mostrar_tareas(tareas):
    # TODO: Mostrar todas las tareas con su nombre, prioridad y estado

    for tarea in tareas:
        print(f"Nombre: {tarea[0]}, Prioridad: {tarea[1]}, Estado: {tarea[2]}")
    pass


# Apartado 7
def listar_tareas_por_prioridad(tareas):
    # TODO: Pedir prioridad y mostrar solo las tareas con ese valor
    '''
    Tareas ordenadas por prioridad (de mayor a menor):
    Leer un libro | Prioridad: 9 | Estado: pendiente
    Estudiar Python | Prioridad: 8 | Estado: pendiente
    Hacer ejercicio | Prioridad: 5 | Estado: finalizada
    Lavar ropa | Prioridad: 3 | Estado: pendiente

    '''

    prio = int(input("Ingrese la prioridad: "))
    b = True
    for tarea in tareas:
        if (tarea[1] == prio):
            print(f"Nombre: {tarea[0]}, Prioridad: {tarea[1]}, Estado: {tarea[2]}")
            b = False
    if b:
        print("No se ha encontrado ninguna tarea con esa prioridad")
    pass


# Apartado 1 - Menú principal
def menu():
    tareas = []

    while True:
        print("\n===== CONTROL DE TAREAS PENDIENTES =====")
        print("1. Agregar tarea")
        print("2. Cambiar estado de tarea")
        print("3. Eliminar tarea")
        print("4. Ordenar tareas por prioridad")
        print("5. Buscar tarea")
        print("6. Mostrar todas las tareas")
        print("7. Listar tareas por prioridad")
        print("8. Salir")
        print("=========================================")
        option = input("Enter an option: ")

        if (option == "1"):
            agregar_tarea(tareas=tareas)
        elif (option == "2"):
            nombre = input("Ingrese el nombre: ")
            while True:
                estado = input("Ingrese el nuevo estado \"pendiente\" o \"finalizado\": ")
                if (estado == "pendiente" or estado == "finalizado"):
                    break
            cambiar_estado(tareas=tareas, nombre=nombre, estado=estado)
        elif (option == "3"):
            nombre = input("Ingrese el nombre: ")
            eliminar_tarea(tareas=tareas, nombre=nombre)
        elif (option == "4"):
            tareas = ordenar_tareas_por_prioridad(tareas=tareas)
        elif (option == "5"):
            buscar_tarea(tareas=tareas)
        elif (option == "6"):
            mostrar_tareas(tareas=tareas)
        elif (option == "7"):
            listar_tareas_por_prioridad(tareas=tareas)
        elif (option == "8"):
            return
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecución principal
if __name__ == "__main__":
    menu()
# Proyecto: "Lista de tareas".
"""Programa que permite agregar, eliminar o tachar tareas a una lista."""

# Bienvenida al programa.
print("Lista de tareas".center(50, "-"))
print("Agrege, elimine o tache una tarea en la lista.".center(50, "-"))

# Lista
lista_tareas = []

print("Mientras el programa se ejecuta, agregue la tarea que quiera.")
print("Si desea eliminar una tarea, escriba 'Eliminar'.")
print("Si desea tachar una tarea, escriba 'Tachar'.")
print("Si desea salir del programa, escriba 'Salir'.")


while True:
    # Funcion general del programa.
    control = input(": ").capitalize()

    # Funcion para salir del programa.
    if control.lower() == "salir":
        break

    # Funcion para eliminar tareas.
    if control.lower() == "eliminar":
        eliminar_tarea = int(input("Escriba el índice de la tarea que desea eliminar: "))

        if 1 <= eliminar_tarea <= len(lista_tareas):
            lista_tareas.pop(eliminar_tarea - 1)
        else:
            print("Índice inválido. No se ha eliminado ninguna tarea.")
        continue

    # Funcion para tachar tareas.
    if control.lower() == "tachar":
        tachar_tarea = int(input("Escriba el índice de la tarea que desea tachar: "))
        if 1 <= tachar_tarea <= len(lista_tareas):
            lista_tareas[tachar_tarea - 1] += " (Completada)"
        else:
            print("Índice inválido. No se ha tachado ninguna tarea.")
        continue

    # Funcion para agregar tareas.
    lista_tareas.append(control)

# Funcion para mostrar tareas.
def mostrar_lista():
    """Muestra la lista de tareas."""
    print("Lista de tareas".center(50, "-"))
    for indice, tarea in enumerate(lista_tareas):
        print(f"{indice + 1} - {tarea}")

# Despedida del programa.
mostrar_lista()
print("Gracias por usar el programa.".center(50, "-"))
print("Vuelva pronto.".center(50, "-"))

# Proyecto: "Simulador de dados".
"""Simulador de dados."""

import random

# Encabezado
print("\nSimulador de dados\n")
print("No tienes dados? No hay problema, este programa te ayudará a simularlos :).")
print("Elige la cantidad de uno a tres dados que deseas simular y tirar.")
print("Escriba 'Salir' para terminar el programa.\n")

def lanzar_dados(dados):
    """Esta función simula el lanzamiento de dados."""

    for i in range(dados):
        if dados == 1:
            print(f"Dado: {random.randint(1, 6)}")
        else:
            print(f"Dado {i + 1}: {random.randint(1, 6)}")

# Entradas
while True:
    try:
        cantidad_dados = input("Dados para simular: ")

        if cantidad_dados.lower() == "salir":
            break

        CANTIDAD_DADOS = int(cantidad_dados)

        if 1 <= CANTIDAD_DADOS <= 3:
            lanzar_dados(CANTIDAD_DADOS)
        else:
            print("Por favor ingrese un número entre 1 y 3.")

    except ValueError:
        print("Por favor ingrese un número válido.")

# Despedida
print("Gracias por usar el simulador de dados.")

"""Calculadora BMI (Índice de Masa Corporal):"""

# Inicio
print("Esta calculadora medira tu índice de masa corporal.")

# Función
def masa_corporal():
    try:
        altura = float(input("Ingrese su altura: "))
        peso = float(input("Ingrese su peso: "))
    except ValueError:
        print("Por favor, coloque los datos correctamente.")
        masa_corporal()

    BMI = peso / (altura ** 2)
    return f"Su masa corporal es {round(BMI, 1)}"

# Salida
res = masa_corporal()
print(res)

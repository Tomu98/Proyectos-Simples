# Proyecto: "Calculadora de propinas".
"""Calculadora que te ayuda a saber cuanto debes pagar de propina."""
import math

# Encabezado
print("""-----------------------------------------------------------------------------
Calculadora de propinas\n
Esta calculadora te ayudará a saber cuanto debes pagar de propina dependiendo del servicio recibido.
-----------------------------------------------------------------------------\n""")

# Entradas
MONTO_TOTAL = float(input("Ingrese el monto total de la cuenta: "))
PORCENTAJE_PROPINA = float(input("Ingrese el porcentaje de propina que desea pagar: "))
CANTIDAD_PERSONAS = int(input("Ingrese el número de personas que van a pagar la cuenta: "))

# Proceso
PROPINA = math.ceil(MONTO_TOTAL * (PORCENTAJE_PROPINA / 100))
CADA_UNO = MONTO_TOTAL / CANTIDAD_PERSONAS
P_CADA_UNO = PROPINA / CANTIDAD_PERSONAS
MONTO_TOTAL += PROPINA

# Resultados
print("\n-------------- Recibo de pago --------------")
print(f"La propina es de: {round(PROPINA, 2)}")
print(f"La propina por persona es de: {round(P_CADA_UNO, 2)}")
print(f"El monto total por persona es de: {round((CADA_UNO + P_CADA_UNO), 2)}")
print(f"El monto total a pagar es de: {round(MONTO_TOTAL, 2)}")
print("--------------------------------------------\n")

# Despedida
print("Gracias por usar la calculadora de propinas.")
print("Has sido atendido por: @Usuario")

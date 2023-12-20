"""Contador de Palabras"""

import re

# Inicio
print("Hola, bienvenido!")
print("Esta pequeña app te ayudará a contar cuantas palabras tiene el texto que ingreses.")

# Función
def contador():
    """Función que cuenta las palabras"""
    a = str(input("Coloque su texto aquí: ")).strip()

    # Manejo de texto vacío
    if not a:
        return "No ingresaste ningún texto."

    # Convertir a minúsculas para consistencia
    a = a.lower()

    # Eliminar puntuaciónes
    a = re.sub(r'[.,;:]', '', a)

    # Expresión regular para dividir el texto por espacios múltiples
    palabras = re.split(r'\s+', a)

    if len(palabras) == 1 and not palabras[0]:
        return "El texto solo contiene una palabra."

    return f"La cantidad de palabras que tiene el texto es: {len(palabras)} palabras."

print(contador())

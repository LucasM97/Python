"""
En tu directorio de trabajo de esta clase, escribí un programa
llamado esfera.py que le pida al usuario que ingrese por teclado el
radio r de una esfera y calcule e imprima el volumen de la misma.
Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para
responder ¿cuál es el volumen de una esfera de radio 6?
"""
import math

radio = float(input("Ingrese el radio de la esfera "))
volumen = (4 * math.pi * radio ** 3) / 3
print("Volmen de la esfera:",volumen)
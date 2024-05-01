"""
Una mañana ponés un billete en la vereda al lado del obelisco porteño.
A partir de ahí, cada día vas y duplicás la cantidad de billetes,
apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila
de billetes sea más alta que el obelisco?
"""

grosorBillete = 0.11 * 0.001 #grosor de un billete en metros
alturaObelisco = 67.5 #altura del Obelisco en metros
numeroBilletes = 1
dias = 1

while numeroBilletes * grosorBillete <= alturaObelisco:
    print(dias, numeroBilletes, numeroBilletes * grosorBillete)
    numeroBilletes = numeroBilletes * 2
    dias += 1;

print("Cantidad de dias ", dias)
print("Canridad de billetes", numeroBilletes)
print("Altura final ", numeroBilletes * grosorBillete)
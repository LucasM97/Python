"""
Frutas

Comencemos definiendo una cadena que contiene una lista de frutas

Extraer caracteres individuales y subcadenas
Los strings son vectores de caracteres. Tratá de extraer algunos
carateres

Testeo de pertenencia (test de subcadena)
Experimentá con el operador in para buscar subcadenas.

Modificá el código anterior de manera que dentro del ciclo el programa
cuente cuántas letras "o" hay en la cadena.
"""

#String con nombes de frutas
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

#Agregando Pera al final del String
frutas += ',Pera'

#Agregando Melon al inicio del String
frutas = 'Melon,' + frutas

#Test de pertenencia
print("¿Naranja esta en la lista? ",'Naranja' in frutas)
print("¿nana esta en la lista? ",'nana' in frutas)
print("¿Lima esta en la lista? ",'Lima' in frutas)

#Contando la cantidad de "o" en el String
contador = 0
letra = 'a'
for caracter in frutas:
    if letra in caracter:
        contador += 1

print('\nCantidad de',letra,":",contador)
print(frutas)

"""
Usá una iteración sobre el string cadena para agregar la sílaba 'pa',
'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
"""

vocales = 'AaEeIiOoUu'
textoGeringoso = ''
texto = input('Ingrese una palabra o frase\n')

for cararter in texto:
    textoGeringoso += cararter
    if cararter in vocales:
        textoGeringoso += 'p' + cararter

print('\nTexto frase en geringoso: \n')
print(textoGeringoso)



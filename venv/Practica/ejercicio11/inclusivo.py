"""
Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase
por su versión neutra. Como primera aproximación, completá el siguiente
código para reemplazar todas las letras 'o' que figuren en el último o
anteúltimo caracter de cada palabra por una 'e'. Por ejemplo 'todos somos
programadores' pasaría a ser 'todes somes programadores'.
"""

frase = 'Todos, tu también'
listaPalabras = frase.split()
fraseInclusiva = ''

for palabra in listaPalabras:
    if len(palabra) > 1 and 'o' in palabra:
        if palabra[-1] == 'o':
            palabraAux = list(palabra)
            palabraAux[-1] = 'e'
            palabra = ''.join(palabraAux)
        elif palabra[-2] == 'o':
            palabraAux = list(palabra)
            palabraAux[-2] = 'e'
            palabra = ''.join(palabraAux)

    fraseInclusiva += palabra + ' '

print(fraseInclusiva)
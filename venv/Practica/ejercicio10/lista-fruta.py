#String de frutas
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

#Lista de frutas
listaFrutas = frutas.split(',')

#Imprime la lista
print(listaFrutas)

#Imprime el primer elemento
print(listaFrutas[0])

#Imprime el segundo elemento
print(listaFrutas[1])

#Imprime el ultimo elemento
print(listaFrutas[-1])

#Imprime el penultimo elemento
print(listaFrutas[-2])

#Cambia el valor del tercer elemento
listaFrutas[2] = 'Granada'

#Imprime los tres primeros elementos
print(listaFrutas[0:3])

#Imprime los dos ultimos elementos
print(listaFrutas[-2:])

#Crea una lista vacia y agrega un elemento
compra = []
compra.append('Kiwi')

#Cambia los ultimos dos valores de la lista de frutas
listaFrutas[-2:] = compra

#Imprime la lista furtas con un bucle for
for fruta in listaFrutas:
    print('fruta =',fruta)

#Test de pertenencia
print('Esta Granada en la lista ','Granada' in listaFrutas)
print('Esta Lima en la lista ','Lima' in listaFrutas)
print('Esta Limon en la lista ','Limon' not in listaFrutas)

#Agregar en elemento con el valor Mango
listaFrutas.append('Mango')

#Insertar el valor Lima como segundo elemento
listaFrutas.insert(1,'Lima')

#Remueve el elemento Mandarina
listaFrutas.remove('Mandarina')

#Agrega el elemento Banana al final
listaFrutas+= ['Banana']

#Imprime la posicion de la primera aparicion de Banana
print(listaFrutas.index('Banana'))

#Cuenta las apariciones de Banana
print(listaFrutas.count('Banana'))

#Elimina la primera aparicion de Banana
del listaFrutas[listaFrutas.index('Banana')]

#Ordena la lista
listaFrutas.sort()
print(listaFrutas)

#Ordena la lista en sentido contrario
listaFrutas.sort(reverse=True)
print(listaFrutas)

#Une los elementos de la lista en un String separados por una coma
frutas = ','.join(listaFrutas)
print(frutas)
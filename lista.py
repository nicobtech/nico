#las listas se crean poniendo corchetes.

#creas variables de listas
demo_list = [1, 'hello', 1.34, 'true']
colores = ['red', 'yellow', 'brown']

#para crear listas tambien se puede poner asi: "list(1,2,3,4)". pero hay dos parentecis porqie no me deja
#agrupar de a 4, enonces lo cierro con parentesis y se agrupa como 1.
number_list = list((1, 2, 3, 4))
print(number_list)
#tipo de dato "lista"
print(type(number_list))

#crear lista basada en un rango: de donde a donde quiero crear una lista
# entonces pongo "crea una lista a partir de este rango:"
r = list(range(1, 10))
print(r)

#saber la informacion dela lista:
print(type(colores))
#saber que puedo hacer con la lista:
print(dir(colores))
#cual es la longitud o sus elementos de la lista
print(len(colores))
print(len(demo_list))
#imprime de colores la posicion 2
print(colores[2])
# imprimir si green esta en colores:
print('green' in colores)

#imprimir colores
print(colores)
#cambiar lo que esta en el "1" por rosa
colores[1] = 'rosa'
print(colores)

#le agrego violet a la lista.
#APPEND sol agrega a 1 solo elemento a la lista.
colores.append('violet')
print(colores)

#para agregar mas elemtos a la lista uso EXTEND. pero este sigue agregando de a 1 pero si le paso una dupla
#o una lista, va a agregar como un solo elemnto a cada uno.
colores.extend(['violet', 'green'])
print(colores)

#insertar en la posicion "1" un color. sin reemplazar a alguno.
colores.insert(1,'violeta')
print(colores)

#agregar un color en el ultimo de la lista: uso LEN pq me da la lungitud de esta.
colores.insert(len(colores),'rojo')
print(colores)

#sacar o eliminar el ultimo elemento de una lista:
colores.pop()
print(colores)
#si quiero sacar o eliminar uno especifico dandole especificamente el nombre:
colores.remove('violet')
print(colores)
#si quiero sacar o eliminar dandole un numero de la posicion:
colores.pop(1)
print(colores)
#eliminar la lista entera:
#colores.clear()   (pongo # pq se borra en serio)
print(colores)

#si quiero ordenar alfabeticamente una lista:
colores.sort()
print(colores)
#si quiero ordenar alfabeticamente al revez:
colores.sort(reverse=True)
print(colores)

#quiero obtener el indice de algo:
print(colores.index('brown'))

#quiero contar cuantas veces estuvo un elemento:
print(colores.count('red'))
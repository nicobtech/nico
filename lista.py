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
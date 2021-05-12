# los diccionario no se definen como una lista. se definen como: este es el nombre del producto, este es el precio,
#esta es la cantidad del producto.
producto = { 'nombre': "book", "cantidad": 3,"precio": 4.99}

persona = {'nombre': 'juan', 'apellido': 'perez'}
# los diccionario se usan para definir cosas de la vida real o poder agrupar distintos datos.

#se define como "dict"
print(type(producto))

#que puedo hacer con el diccionario:
print(dir(producto))

#para saber los nombres de las llaves: "nombre:" y que me de "apellido:"
print(persona.keys())
#si quiero tener los items: 'nombre': 'juan', 'apellido': 'perez'
print(persona.items())

#para eliminar los elementos internos:
#persona.clear()
print(persona)


#UNA LISTA PUEDE ESTAR CONFORMADA POR DISTINTOS DICCIONARIOS:
cosas = [{'nombre':'ivan', 'apellido':'alvarez'}, {'nombre':'coso'}]
print(cosas)
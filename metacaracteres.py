import re
lista_nombres = ['ana gomez', 'maria martin', 'sandra lopez', 'santiago martin', 'sandra fernandez']

#el: "^" es para marcar todos los strings que comienzan con esa palabra
for elemento in lista_nombres:
    if re.findall('^sandra', elemento):
        print(elemento)

# el elemento "$" es para todas las coincidencias que terminen con es palabra
for element in lista_nombres:
    if re.findall('martin$', element):
        print(element)


#[N]: busca cuanatas veces fue escrito el caractero o palabra que hayas buscado. te va a dar niños y niñas.
urls = ["hombres", "mujeres", "mascotas", "niños", "niñas"]

[print(url) for url in urls 
        if re.findall("niñ[oa]s", url)] 

[print(url) for url in urls 
        if re.findall("[e]", url)]
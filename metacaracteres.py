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


#[N]: busca cuantas veces fue escrito el caractero o palabra que hayas buscado. te va a dar niños y niñas.
urls = ["hombres", "mujeres", "mascotas", "niños", "niñas"]

[print(url) for url in urls 
        if re.findall("niñ[oa]s", url)] 

#aca te dan los que tienen la E. serian hombres y mujeres. tambien lo puedo hacer con las tildes.
[print(url) for url in urls 
        if re.findall("[e]", url)]


^	Inicio de línea
$	Fin de linea                EJ: patron$: coincide con cualquier cadena que termine con patron.
\A	Inicio de texto
\Z	Fin de texto
.	Coincide con cualquier caracter en una línea dada
*	Cero o más: todas las ocurrencias de un dado substring
+	Una o más ocurrencias del patrón
?	Cero o una             EJ: **?**: coincide con cero o una ocurrencia del patrón. Dicho de otra forma, hace que el patrón sea opcional
{n}	Exactamente n veces             EJ: [abc]: coincide con a, b, o c
{n,m}	Por lo menos n pero no más de m veces.      EJ: {4,}: al menos 4 dígitos
\w	Caracter alfanumércio
\W	Caracter NO alfanumércio
\d	Caracter numércio
\D	Caracter NO numércio
\s	Un espacio, de cualquier tipo (\t\n\r\f)
\S	Cualquier caracter que no sea un espacio
print('hola')
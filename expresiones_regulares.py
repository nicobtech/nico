#para las expresiones regulares se usa:
import re
cadena = 'vamos a aprender exp regulares vamos a aprender'

#para usar las cosas del RE, hay que poner RE.rearch (o lo que sea)

#metodo SEARCH: busca un string y lo localiza donde coincida.
#buscas el texto 'aprender' EN 'cadena'
print(re.search('aprender', cadena))


# si 'TEXTOBUSCAR' esta en cadena y no es NONE, imprimi algo y si no imprimi lo otro
textobuscar = 'vamos'
if re.search(textobuscar, cadena) is not None:
    print('lo encontre')
else:
    print(' no lo encontre')

#START nos da el numero de caracter de donde empieza la palabra que busco
textoencontrado = re.search(textobuscar, cadena)
print(textoencontrado.start())

#END nos da el numero de caracter de donde terminba la palabra que busco
print(textoencontrado.end())

#SPAN: nos devuelv el caracter donde empieza el texto y donde termina:
print(textoencontrado.span())

#FINDALL: te busca todos los strings que coinciden con lo que buscaste. te lo devuelve escrito, como numero no.
print(re.findall(textobuscar, cadena))
#LEN: si queres saber cuantas veces estan las palabras pero que te de numero pones len:
print(len(re.findall(textobuscar, cadena)))

# MATCH: devuelve la primer aparicion y solo al principio de la cadena. si encuentra alguna coincidencia en la 
#primera linea, devuelve el objeto de coincidencia.pero si se encuentra en otra linea devuelve el valor nulo.
print(re.match(textobuscar, cadena))

#GROUP: nos devyelve la coincidencia de forma mas limpia
print(re.search('aprender', cadena).group())

#ejemplo de como se usa el GROUP:
#>>> import re
#>>> texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
#>>> patron = "ipsum(.*)sit"
#>>> re.search(patron, texto).group()
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
#>>> re.search(patron, texto).group(0)
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
#>>> re.search(patron, texto).group(1)
#' dolor sit amet, consectetur ipsum elit. Amet '

#La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
print(re.sub(patron, "###", texto))

Texto = "hola estoy bien"
Patron = "bien"
print(re.sub(Patron, "mal", Texto))

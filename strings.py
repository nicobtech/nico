myStr = "hello world"

#print(dir(myStr))

#upper es para poner todo en MAYUS.
print(myStr.upper())
#lower todas minus
print(myStr.lower())
#swapcase es una si y una no (mayus minus)
print(myStr.swapcase())
#caputalize es solo la primer letra mayus
print(myStr.capitalize())

#relace: reeemplazar hello por bye
print(myStr.replace("hello","bye"))

#lo mismo que antes pero todo en mayus
print(myStr.replace("hello","bye").upper())

#count: contar cuantas "L" hay
print(myStr.count("l"))

#empieza con ququ? no.
print(myStr.startswith("ququ"))
#termina con d? si.
print(myStr.endswith("d"))

#separa a partir de una coma las palabras
print(myStr.split())
# separa a partir de la letra "o"
print(myStr.split("o"))

#find busca la posicion de la letra que buscas.
print(myStr.find("o"))

#len imprime la longitud del string
print(len(myStr))

#indice de la letra "E". es 1 pq empieza en 0. donde es la primera vez que aparece la letra.
print(myStr.index("e"))

#para saber si es numerico
print(myStr.isnumeric())
#para saber si es alfanumerico
print(myStr.isalpha())

# saber la posicion dandole el numero.
print(myStr[4])

#para saber el valor inverso
print(myStr[-1])


#en este valor "0" voy a colocar la variable "MYSTR"
print("mi nombre es {0}".format(myStr))


pepe = 'qwerty'

print(pepe[2])
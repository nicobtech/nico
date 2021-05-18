# Escribí un programa de python que imprima un diccionario cuyas claves sean los números de 1 a 15 y cuyos valores sean las potencias al cuadrado de estos números.
diccionario = {}
for numero in range(1, 16):
    diccionario[numero] = numero**2
for (clave, valor) in diccionario.items():
    print(clave, valor)

print('-----------------------------------')
#Realizá un programa que imprima la suma de todos los valores de un diccionario de números.
contador = 0
for valor in diccionario.keys():
    contador += valor
print(contador)

print(sum(diccionario.values()))

# Escribí un programa que obtenga, a partir de una lista de strings una lista con la longitud de esas strings e imprima la longitud de la lista de strings y los elementos de la lista de longitudes.

colores = ['red', 'yellow', 'brown']
print(len(colores))
for elementos in colores:
    print(len(elementos))


# Realizá un programa que a partir de una lista mixta (que contiene distintos tipos de datos) 
# imprima cuántos enteros tiene y además en el caso de los elementos que sean strings hay que crear una nueva 
# lista con estos strings pero reemplazando al A por la U (tanto mayúscula como minúscula) y luego imprimir estos elementos.
#FOR:

foods = ['manzanas', 'pan', 'queso', 'leche', 'banana', 'uvas']
#en vez de hacer esto:
#print(foods[0])
#print(foods[1])
#print(foods[2])
#print(foods[3])
#print(foods[4])

#hago esto

#FOR: en la lista de alimentos quiero cada uno de los alimentos.
#para comida en foods. (comida no esta definida desde antes, la defenis haciendo el for.OSEA QUE LA VARIABLE COMIDA SE DEFINE AHI)
for comida in foods:
    print(comida)

#si alimentos=queso que se imprima en la lista: 'tenes que comprar esto' arriba de queso
for alimentos in foods:
    if alimentos == 'queso':
        print('tenes que comprar esto')
    print(alimentos)


# si utilizas BREAK sigrnifica que si alimentos es igual a eso se deje de imprimir ahi. el queso no se llega a imprimir.
#solo se imprime MANZANA Y PAN
for alimentos in foods:
    if alimentos == 'queso':
        break
    print(alimentos)

#con CONTINUE significa que si alimentos es igual a queso, que siga imprimiendo. pero el queso no se imprime
for alimentos in foods:
    if alimentos == 'queso':
        continue
    print(alimentos)


#SEGUNDO EJ: en un rango que me los imprima todos.
for number in range(1, 8):
    print(number)

#tercer ej:
for letter in 'hello':
    print(letter)




#WHILE:
#en el while lo que pasa es que se va a hacer la validacion de si 'count' es menor o igual a 10 infinitamente, entonces por eso
#abajo se le pone que a count se le incrementa en 1. por ende va a seguir repitiendose hasta que en un momento 'count'
#sea 11. y ahi se termina se ejecutar el while.
count = 4
while count <= 10:
    print(count)
    count = count + 1
# el IF: si X es menor que 30, imprime...:
x = 10
if x < 30:
    print("x es menor a 30")

#si y es igul a 30 imprime "y es 30"
y = 30
if y ==30:
    print('y es 30')

#si esto es tal, imprimime esto, pero si no es asi imprimime tal otro:
q = 10
if q < 20:
    print('q es menor que 20')
else:
    print('q es mayor que 20')

#se puede no solo con numeros:
color = 'rojo'
if color == 'azul':
    print('el color es rojo')
else:
    print('otro color')

#HAY OTRA VARIABLE MAS: si es lisa imprimi esto. si es raspada imprimi esto, si no es ninguna de las dos imprimi esto
pared = 'lisa'
if pared == 'lisa':
    print('la pared es lisa')
elif pared == 'raspada':
    print('la pared esta raspada')
else:
    print('la pared esta colorida')


# si el nombre es john, quiero que valides el apellido tambien. si son correctos hay un print. si alguno
#no es correcto se imprime lo que puse en el ELSE.
name = 'john'
lastname = 'carter'
if name == 'john':
    if lastname == 'carter':
        print('you are john carter')
    else:
        print('you are not john carter')
else:
    print('vos no sos john')
#LO DE ARRIBA: si es john pero no es carter me de el "ELSE" de arriba. si el no se llama directamente jhon,
#me da directamente el "ELSE" de abajo.


#si x es mayor a 2 y x es mayor a 10 printiame:
z = 100
i = 100
if z > 2 and z <=10:
    print('z es myor que dos y menor o igual que 10')
if z > 2 or z <=20:
    print('z es mayor que dos o menor o igual a 20')   
if (not(z==i)):
    print('z no es igual a i')
else: 
    print('te dio cualquier numero')

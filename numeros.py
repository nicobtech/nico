10
14.4

#int=entero
print(type(9))
#float=flotante. cualquier numero que se "punto algo#
print(type(10.1))

#calculo
print(1+1)

#INPUT toma un caracter de lo que tipea el usuario en la consola
#input("inserte su edad")
#entonces el valor que me inserte yo lo voy a pasar a una variable
age = input("inserte su edad:")
print(age)

#creo una nueva variable en la que le sumo 5 a la "edad" y para que me agarre como numero la edad tengo que 
#escribir "INT". pq es un numero entero. si seria no entero pongo "FLOAT"
edad = input("pone su edad:")
new_age = int(edad)+5
print(new_age)

#
edad_del_chico = input("pon la edad:")
nueva_edad = float(edad_del_chico)*7
print(nueva_edad)
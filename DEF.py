#la palabra DEF hace referencia a la palabra que viene despues clasificandola como funcion.
#estamos creqndo una funcion y le doy el nombre que yo quiera. en este caso HELLO significa que se imprima HELLOWORLD.

def hello():
    print('helloworld')
hello()
#defino que en la variable cuando ponga "hola" y en el parentecis mi nombre aparezca "hola nico". se hace medianto poniendo
#la palabra "nombre" y despues que se imprima el "hola" +  el nombre. (tiene que haber un espacio entre la segunda comilla 
# y y el "hola" para  que haya un espacio). se pone el ='person' porque
def hola(nombre='person'):
    print('hola ' + nombre)
hola('nico')
hola('coso')


#otra funcion: aca pongo que para la funcion "add" pasa que se suman los dos numero que poingo en el parentesis.
def add(numbreone, numbertwo):
    return numbreone + numbertwo
print(add(10, 30))

#otra mas:
asa = lambda numberone, numbertwo: numberone + numbertwo
print(asa(10, 30))
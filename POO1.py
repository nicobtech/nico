#los objetos tienen un ESTADO, COMPORTAMIENTO Y PROPIEDADES
# CLASE: modelo donde se redactan las caracteristicas comunes de un grupo de objetos. por ej el chasis de un auto.
#el OBJETO: es el auto.
#creamos propiedades del coche. el FALSO significa que por defecto esta apagado.
#creamos los COMPORTAMIENTOS en forma de 'metodos'. lo creamos utilizando DEF. 
# para hacer que arranque mi objeto debo sacar la palabra PASS que lo unico que hace es que no me de error todo. 
# tengo que poner SELF.enmarcha=true para cambiar el comportamiento por defecto que este tiene.

class coche():
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False
    #el coche va a arrncar y despues decirnos su estado
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return 'el coche esta en marcha'
        else:
            return 'el coche esta parado'

micoche = coche()
print('el largo del coche es: ',micoche.largochasis)
print('el coche tiene ', micoche.ruedas, 'ruedas')
#ahora arranco el coche esribiendo esto y despues pongo el print para que me diga que arranque.
#si no pongo lo siguiente me va a decir que mi coche esta parado.
micoche.arrancar()
print(micoche.estado())

#EXPLICACION GENERAL: 
# propiedades: 4
# cuantos comportamientos tiene? 2. una pone el coche en marcha y el otro te dice el estado en el que esta
#depues creas la instancia o ejemplar de clase. y utilizando este pude acceder a las propiedades y estado del objeto.


print('-------------a continuacion creamos el segundo objeto------------------')
#creo la segunda instancia, le cambio el nombre y pertenece a la misma clase 'coche'
micoche2 = coche
print('el largo del coche 2 es: ',micoche2.largochasis)
print('el coche 2 tiene ', micoche2.ruedas, 'ruedas')
#le pregunto por mi estado
print(micoche2.estado())
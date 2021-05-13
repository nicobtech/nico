import re

nombres = ["Ana", "Pedro", "María", "Rosa", "Sandra", "Celia"]

# el RANGO es :"[o-t]" significa que te de todos los strings que contengan las letras entre la o y la t. DISTINGUE MAYUSCULAS
#Y MINUSCULAS.
for nombre in nombres:
    if re.findall("[o-t]", nombre):
        print(nombre)
#si queres poner todas los strings que terminen con letras entre la o y la t, pones el signo:$
for usuario in nombres:
    if re.findall("[o-t]$", nombre):
        print(usuario)

# si queremos todos los de 'MA' pero del 1 al 3 nada mas pones asi:
codigos = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4"]

for codigo in codigos:
    if re.findall("Ma[0-3]", codigo):
        print(codigo)
#para NEGCION pogo es adelante. para decirle cuales NO VAN, y me dan los otros.
for negacion in codigos:
    if re.findall("Ma[^0-3]", codigo):
        print(negacion)

# todos los que tienen el rango de 0 a 3 y los del rango A a B.
codigos_nuevos = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4",
           "MaA", "Ma5", "MaB", "MaC"]
for nuevos_codigos in codigos:
    if re.findall("Ma[0-3A-B]", codigo):
        print(nuevos_codigos)

# los elementos de MA que tienen "." o ":"
puntos = ["Ma.1", "Se1", "Ma2", "Ba1", "Ma:3", "Va1", "Va2", "Ma4",
           "MaA", "Ma.5", "MaB", "Ma:C"]
for puntitos in puntos:
    if re.findall("Ma[.:]", puntos):
        print(puntitos)

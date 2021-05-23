#Para abrir un archivo de texto, ya sea para usarlo o escribir en el, podemos usar la función nativa de Python open():
# ''' open(path_al_archivo, modo) ''' 
# - "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. 

# - "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.
archivo = open("mi_texto.txt")
print (archivo.read())


#algunos de los modos de lectura más frecuentes y sus difrerencias:

# r	abre un archivo solo para lectura
# r+	abre un archivo para lectura y escritura
# a	Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura
# w	Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura

# ¡Es muy importante cerrar los archivos una vez abiertos!
#cerrar un archivo luego de abrirlo? Existe un método close():
archivo = open(path_al_archivo, modo) 
archivo.close()

# otra forma de apertura de archivos que nos ahorra este paso y siempre nos asegura el cierre de adecuado:
with open(path_al_archivo, modo) as miarch: 
    #Aquí van las líneas de procesamiento del archivo


# EJEMPLO IMPORTNATE: crear archivo de texto:
archivo = open("Archivo_de_texto_pruebaa","w")  #el nombre de archivo que quiera crear, lueego pongo 'W' para "escribir"
archivo.write("hola\n")  #escribo lo que quiero poner. si qioero poner mas cosas pongo archivo write devuelta.
archivo.write("como estas")

archivo.close()         #despues hay que cerrarlo si o si.

import requests

#ahi me da todo
r = requests.get("https://ponyweb.ml/v1/character/all")
#si se usa GET, se devuelve el producto con id 45. Si se usa DELETE, se lo borra:
r = requests.get("https://ponyweb.ml/v1/character/45")
#si quiero saber las canciones: pongo song 
r = requests.get("https://ponyweb.ml/v1/song/all")
#quiero saber el status code:
r.status_code  #da: 200
#quiero saber el conent type:
r.headers  #da: 'Content-Type': 'application/json; charset=UTF-8'}
#quiero saber cuantos ponys o cual es la cantidad de lo que estoy buscando:
r.json()






# Dado el siguiente enlace "https://ponyweb.ml/v1/character/all", realizar las siguientes actividades adjuntando los archivos 
# resultantes y el código utilizado para la realización de cada paso:
#a) ¿Cuál es el dominio al que estamos consultando?
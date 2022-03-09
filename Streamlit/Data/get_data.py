#hacerle peticiones a la API

import requests


url='http://127.0.0.1:8000'

def map():
    return requests.get(url+"/geolocalizacion").json()

def poblacion_islas():
    return requests.get(url+'/poblacion/islas').json()

def media_peso():
    return requests.get(url+"/media_peso_especies/").json()

def media_peso():
    return requests.get(url+"/altura/sexo/{especie}/").json()

def specie_penguins():
    return requests.get(url+"/porcentaje/specie/penguins").json()

def esp_sex_penguins():
    return requests.get(url+'/specie/sex/penguins').json()   



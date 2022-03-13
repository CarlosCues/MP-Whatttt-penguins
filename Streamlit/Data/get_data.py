#hacerle peticiones a la API

import requests
from dotenv import load_dotenv
import os

load_dotenv()

url=os.getenv('url')


def map():
    return requests.get(url+"/geolocalizacion").json()#

def poblacion_islas():
    return requests.get(url+'/poblacion/islas').json()#

def media_peso():
    return requests.get(url+"/media/peso/especies/").json()#

def media_altura(especie):
    return requests.get(url+f"/altura/sexo/{especie}/").json()#

#Porcentaje de especie sobre total pinguinos
def specie_penguins():
    return requests.get(url+"/porcentaje/specie/penguins").json()

def esp_sex_penguins():
    return requests.get(url+'/specie/sex/penguins').json()#



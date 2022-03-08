import requests
import numpy as np

url='http://127.0.0.1:8000'

def get_saludo():
    return requests.get(url+'/hola').json()

def get_data():
    return ('Prueba', filter={}, project={'species':1,'body_mass_g':1,'_id':0}, limit=0, skip=0)
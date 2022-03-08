from fastapi import FastAPI
from Database.BBDD_MongoDB import get_data
from bson import json_util

app=FastAPI()

@app.get("/")
async def root():
    return {"Penguins"}

@app.get("/saludo/")
async def saludar():
    return {"hola"}

@app.get("/media_peso_especies/")
async def media_peso_especies():
    collection='Prueba'
    filter={}
    project={'species':1,'_id':0,'body_mass_g':1}
    return loads(json_util.dumps(get_data(collection,filter,project).json()))


@app.get("/altura/{especie}/")
async def altura_sexo_especies(especie):
    collection='Prueba'
    filter={'species':especie}
    project={'species':1,'_id':0,'sex':1,'culmen_length_mm':1}
    return loads(json_util.dumps(get_data(collection,filter,project).json()))


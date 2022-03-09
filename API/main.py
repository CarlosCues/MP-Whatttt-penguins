#pide datos a la base de datos

from fastapi import FastAPI
from Database.BBDD_MongoDB import get_data


app=FastAPI()

#### Geoquery
"""
@app.get("/geolocalizacion/islas")

async def geo():
    collection='geo_penguins'
    filter={}
    project={'location':1,'species':1,'sex':1,'_id':0}
    data_pinguinos=get_data(collection,filter, project)

    for pinguino in data_pinguinos:
            q={'location':{'$geometry':pinguino.location}}
"""

@app.get("/geolocalizacion")
async def geo():
    collection='penguins'
    filter={}
    project={'island':1,'location.coordinates':1,'_id':0}
    data_pinguinos=get_data(collection,filter, project)
    localizacion={}
    for pinguino in data_pinguinos:
        if not pinguino['island'] in localizacion.keys():
            localizacion[pinguino['island']]= pinguino['location']['coordinates']
        
    return localizacion


@app.get('/poblacion/islas')
async def poblacion_islas():
    collection='penguins'
    filter={}
    project={'island':1,'_id':0}
    data_pinguinos=get_data(collection, filter,project)
    pob_islas={}  
    for pinguino in data_pinguinos:
        if pinguino['island'] in list(pob_islas.keys()):
            pob_islas[pinguino['island']] += 1
        else:
            pob_islas[pinguino['island']]=1
    return pob_islas
        

@app.get("/media/peso/especies/")
async def media_peso_especies():
    collection='penguins'
    filter={}
    project={'species':1,'_id':0,'body_mass_g':1}
    data_pinguinos=get_data(collection,filter,project)
    media_peso_pinguino={} #diccionario que almacenara la suma de todos los pesos // despues del segundo for media de los pesos de los pinguinos
    num_especies={} # Contador de ejemplares de cada especie
    for pinguino in data_pinguinos:
        #si la especie del pinguino existe en el diccionario le sumo el peso del siguiente pinguino.
        if pinguino['species'] in list(media_peso_pinguino.keys()):
            media_peso_pinguino[pinguino['species']] +=pinguino['body_mass_g']
            num_especies[pinguino['species']]+=1 #Sumo uno al contador de pinguinos
        else:
            media_peso_pinguino[pinguino['species']]=pinguino['body_mass_g'] # si no existe el pinguino creo la key y el asigno como valor el peso
            num_especies[pinguino['species']]=1 #Incia la cuenta.

    for especies,peso in  media_peso_pinguino.items(): #recorro el diccionario
        media_peso_pinguino[especies]=peso/num_especies[especies] #saco la media

    return media_peso_pinguino

    #return loads(json_util.dumps(get_data(collection,filter,project).json())) el loads(json_util.dumps() solo se usa  cuando se devuelve un object id



@app.get("/altura/sexo/{especie}/")
async def altura_sexo_especies(especie):
    collection='penguins'
    filter={'species':especie}
    project={'species':1,'_id':0,'sex':1,'culmen_length_mm':1}
    data_pinguinos= get_data(collection,filter,project)

    specie_sex={}
    num_especies={}
    for pinguino in data_pinguinos:
        if pinguino['species']+ '_' + pinguino['sex'] in list(specie_sex.keys()):
            specie_sex[pinguino['species']+ '_' + pinguino['sex']]+=pinguino['culmen_length_mm']
            num_especies[pinguino['species']+ '_' + pinguino['sex']]+=1
        else:
            specie_sex[pinguino['species']+ '_' + pinguino['sex']]=pinguino['culmen_length_mm']
            num_especies[pinguino['species']+ '_' + pinguino['sex']]=1
  
    for especie_sexo,altura in specie_sex.items():
        specie_sex[especie_sexo]=altura/num_especies[especie_sexo]
      
    return (specie_sex)

@app.get('porcentaje/specie/penguins')
async def specie_penguins():
    collection='penguins'
    filter={}
    project={'species':1,'_id':0}
    data_pinguinos=get_data(collection,filter, project)
    penguin_specie={}
    for pinguino in data_pinguinos:
        if pinguino['species'] in list(penguin_specie.keys()):
            penguin_specie[pinguino['species']] += 1
        else:
            penguin_specie[pinguino['species']]=1

    for especie,porcentaje in penguin_specie.items():
        penguin_specie[especie]=round(porcentaje/len(data_pinguinos)*100,1)

    return penguin_specie

@app.get('/specie/sex/penguins')
async def specie_sex_penguins():
    collection='penguins'
    filter={}
    project={'species':1,'sex':1,'_id':0}
    data_pinguinos=get_data(collection,filter,project)
    specie_sex={}

    for pinguino in data_pinguinos:
        if pinguino['species']+ '_' + pinguino['sex'] in list(specie_sex.keys()):
            specie_sex[pinguino['species']+ '_' + pinguino['sex']]+=1
        else:
            specie_sex[pinguino['species']+ '_' + pinguino['sex']]=1

    for especie_sex,recuento in specie_sex.items():
        specie_sex[especie_sex]=round(recuento/len(data_pinguinos)*100,1)
      
    return (specie_sex)

# If Danny Devito would have known!

Projecto en proceso de desarrollo como mid project para un bootcamp, donde se analiza el dataset de palmerpenguins. 
Las distintas fases del proyecto han sido:
- **Limpieza** de datos.
- **Webscraping** para enriquecer los datos.
- **Creacion de BBDD** en MongoDB.
- **Creacion de una API** con FastAPI.
- **Creacion de un Dashboard** con Streamlit
- **Creacion de maquina virtual** con Docker.
- **Subida de la API a la nube** con Heorku.
Los datos fueron recogidos y puestos a disposición por la Dra. Kristen Gorman y la Estación Palmer, Antarctica LTER, miembro de la Red de Investigación Ecológica a Largo Plazo.


## Dependencies

Proyecto desarrollado integramente en Python, con las siguientes bibliotecas requeridas:
- Pandas
- Beautifull Soup
- Pymongo
- FastAPI
- Dotenv
- Folium
- Streamlit
## Contenido del dashboard 

El dashboard del proyecto se divide en 4 partes:
- **Home** --> Introduccion sobre la estrcutura del dashboard, qué información podrá encontrar el usuario en cada parte asi como las metricas del dashboard para entender las conclusiones que se exponen.
- **Meet the penguins**--> Contenido relacinado con las diferentes especies de pinguinos que se han estudiado. 
- **Insights**--> Visualización de los resultados del anaisis de los datos. 
- **Quiz**--> Un breve cuestionario para evaluar que has aprendido.
## To-Do

Proximos pasos:

- Enriquecer el contenido. 
- Incluir nuevos datos a la pestala Ingishts.
- Añadir una seccion donde el usuario pueda escribir y mandar su feedback.

## API Reference

#### Localizacion del habitat de los pingüinos.

```http
  GET /geolocalizacion
```
Marca la situacion de las islas donde habitan las tres especies de pingüinos.

***

#### Conocer la poblacion de los pingüinos en cada isla.

```http
  GET /poblacion/islas
```

Devuelve un diccionario con número de ejemplares por isla.

***
#### Conocer la media de  peso de cada especie.

```http
  GET /media/peso/especies/
```


Devuelve un diccionario con la media del peso,en gramos, de los ejemplares estudiados por especie.

***
#### Conocer la altura media de cada especie.
```http
  GET /altura/sexo/{especie}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `especie`      | `string` | **Required**. Especie del pungüino. |


Devuelve un diccionario con la media de la longitud del pico, en milimetros, de los ejemplares estudiados por especie.

***
#### Proporcion de cada especie entre los ejemplares estudiados

```http
  GET /porcentaje/specie/penguins
```



Devuelve un diccionario con los porcentajes que representan los ejemplares de cada especie sobre el total de pingüinos estudiado.

***

#### Proporcion por especie y sexo de los ejemplares estudiados

```http
  GET /specie/sex/penguins
```


Devuelve un diccionario con los porcentajes que representan los ejemplares de cada especie y sexo de  sobre el total de pingüinos estudiado.




## Contact
email: c.cuestac@yahoo.es

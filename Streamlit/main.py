#visualizar los datos

import streamlit as st
from Data.get_data import *
from streamlit_folium import folium_static
from folium import Map,Marker
import matplotlib.pyplot as plt

st.title("If Danny Devito would have known!")
st.image('https://www.denofgeek.com/wp-content/uploads/2021/12/batman-returns-penguin-danny-devito-warner.jpg?fit=1200,680',width=400)
st.header('Palmers Penguins')
st.image('https://miro.medium.com/max/1248/1*xJ6_zgmEEfI2BT0sRXP5cw.png')
st.header('Where do the Palmers Penguin live?')
m= Map()

for isla, coord in map().items():
    Marker(coord,tooltip=isla).add_to(m)
folium_static(m)


#mostrar poblacion de pinguinos en cada isla. 
fig, ax = plt.subplots()
ax.bar(poblacion_islas().keys(), poblacion_islas().values())
plt.xlabel('Islas')
plt.ylabel('Ejemplares')
st.pyplot(fig)
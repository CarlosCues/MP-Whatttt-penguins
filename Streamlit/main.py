from pkgutil import get_data
import streamlit as st
from Data.get_data import get_saludo

st.title('Penguins, Penguins, Penguins')
st.code(get_saludo())


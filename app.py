import streamlit as st
import pandas as pd
import numpy as np
import pickle
import altair as alt
from sklearn.preprocessing import LabelEncoder
from pandas import set_option
from st_aggrid import AgGrid
import plotly.express as px
import pygwalker as pyg 
import streamlit.components.v1 as stc 
import seaborn as sns
import matplotlib.pyplot as plt
import random
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Estudiante,Sede,Carrera,Pais,Ciudad,EstadoCivil, filtro_all_generico_combo
def main():
	"""Simple Login App"""
	imagen = "logo.png"
	st.set_page_config(page_title="Encuestas Bienestar",
					page_icon=imagen,
					layout="wide",
					initial_sidebar_state="auto"
					)
	st.subheader("📈 Encuestas a Estudiantes Titulados - Univalle 2024")
	# Mostrar la imagen en la barra lateral
	st.sidebar.image(imagen,  width=50, )	
	menu = ["Resultados","Analisis Dinamico","Analisis Exploratorio","Matriz de Correlacion"]
	
	##menu = ["Inicio","Tablas","Analisis Exploratorio","Matriz de Correlacion"]
	iconos=["house","book","book","cast"],
	with st.sidebar:
			choice=option_menu(
			menu_title="Menu",
			#menu_title=None,
			options=menu,
			icons=iconos,
			menu_icon="cast", #option
			default_index=0, #option
			orientation="vertical", )
	if choice == "Analisis Dinamico":
		st.subheader("📈 Principal")
		sedes= filtro_all_generico_combo(Sede,'nombre_sede')
		st.sidebar.multiselect("Selecciona una Sede:", sedes, default=sedes)
		carrera= filtro_all_generico_combo(Carrera,'nombre_carrera')
		st.sidebar.selectbox("Selecciona una Carrera:", carrera)
		gestion= filtro_all_generico_combo(Estudiante,'gestion')
		st.sidebar.selectbox("Selecciona la Gestion:", gestion)
		genero = st.sidebar.radio(
            "Geénero:",
            ('Masculino', 'Femenino')
        )
		estado_civil= filtro_all_generico_combo(EstadoCivil,'nombre_estado_civil')
		st.sidebar.multiselect("Selecciona Estado Civil:", estado_civil, default=estado_civil)
		pais= filtro_all_generico_combo(Pais,'nombre_pais')
		st.sidebar.selectbox("Selecciona el Pais:", pais)
		ciudad= filtro_all_generico_combo(Ciudad,'nombre_ciudad')
		st.sidebar.selectbox("Selecciona la Ciudad:", ciudad)
        # Mapeo de género a valor numérico
		if genero == 'Masculino':
			valor = 1
		else:
			valor = 2
		edad = st.sidebar.select_slider("Seleccionar Edad:", options=list(range(1, 101)),  value=25)
	elif choice == "Resultados":
		st.subheader('📃 Resultados')
	elif choice == "Matriz de Correlacion":	
		st.subheader('📃 Resultados')
	elif choice == "Analisis Exploratorio":	
		st.subheader('📃 Analisis Exploratorio')

if __name__ == '__main__':
    main()

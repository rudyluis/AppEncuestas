import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Estudiante, Sede, Carrera, Pais, Ciudad, EstadoCivil, filtro_all_generico_combo,filtro_busqueda_generico,filtro_all_generico,filtro_busqueda_generico_varios
from analisis_dinamico import AnalisisDinamico
from analisis_bivariados import AnalisisBivariado
import pandas as pd

# Configuración de la conexión a la base de datos
engine = create_engine('postgresql://bdencuestasunivalle_user:pWB2M9UReSOqeNYzI9qsztYaKIVUzk76@dpg-coe6k2i0si5c739bojmg-a.oregon-postgres.render.com:5432/bdencuestasunivalle')
Session = sessionmaker(bind=engine)
session = Session()

def main():
    """Simple Login App"""
    imagen = "logo.png"
    st.set_page_config(page_title="Encuestas Bienestar",
                       page_icon=imagen,
                       layout="wide",
                       initial_sidebar_state="auto")

    st.subheader("📈 Encuestas a Estudiantes Titulados - Univalle 2024")

    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Mostrar la imagen en la barra lateral
    st.sidebar.image(imagen, width=50)

    menu = [ "Analisis Dinamico", "Analisis Bivariado", "Matriz de Correlacion"]
    iconos = ["house", "book", "book", "cast"]

    with st.sidebar:
        choice = option_menu(
            menu_title="Menu",
            options=menu,
            icons=iconos,
            menu_icon="cast",
            default_index=0,
            orientation="vertical"
        )

    style_metric_cards("#f2f9aa", 3, "#CCC", 10, "#dc3545", True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="✏️ Varones", value=4, delta="Min: 4")
    with col2:
        st.metric(label="🖇️ Mujeres", value=4, delta="")
    with col3:
        st.metric(label="📋 Cantidad de Registros", value=4, delta="Max: 4")

    #### columnas de seleccion filtros
       # Sedes
    sedes = filtro_all_generico_combo(Sede, 'nombre_sede', session)
    selected_sedes = st.sidebar.multiselect("Selecciona una Sede:", sedes, default=sedes)

    # Carrera
    carreras = filtro_all_generico_combo(Carrera, 'nombre_carrera', session)
    selected_carrera = st.sidebar.selectbox("Selecciona una Carrera:", carreras)
    carrera = filtro_busqueda_generico(Carrera, 'nombre_carrera', selected_carrera, session)

    # Gestion
    gestiones = filtro_all_generico_combo(Estudiante, 'gestion', session)
    selected_gestion = st.sidebar.selectbox("Selecciona la Gestion:", gestiones)

    # Género
    genero = st.sidebar.radio("Género:", ('Masculino', 'Femenino'))
    genero_valor = 1 if genero == 'Masculino' else 0

    # Estado Civil
    estados_civiles = filtro_all_generico_combo(EstadoCivil, 'nombre_estado_civil', session)
    selected_estados_civiles = st.sidebar.multiselect("Selecciona Estado Civil:", estados_civiles, default=estados_civiles)

    # País
    paises = filtro_all_generico_combo(Pais, 'nombre_pais', session)
    selected_pais = st.sidebar.selectbox("Selecciona el Pais:", paises)
    pais = filtro_busqueda_generico(Pais, 'nombre_pais', selected_pais, session)

    # Ciudad
    ciudades = filtro_all_generico_combo(Ciudad, 'nombre_ciudad', session)
    selected_ciudad = st.sidebar.selectbox("Selecciona la Ciudad:", ciudades)

    # Edad
    edad = st.sidebar.select_slider("Seleccionar Edad:", options=list(range(1, 101)), value=25)

    # Filtrar estudiantes
    if carrera is None:
        estudiantes = filtro_all_generico(Estudiante, session)
    else:
        filtros = {
            "id_carrera": carrera[0]['id_carrera'],
            "sexo": genero_valor,
            "id_pais": pais[0]['id_pais']
        }
        estudiantes = filtro_busqueda_generico_varios(Estudiante, filtros, session)


    if choice == "Analisis Dinamico":
        AnalisisDinamico(st, session)
    elif choice == "Resultados":
        st.subheader('📃 Resultados')
    elif choice == "Matriz de Correlacion":
        st.subheader('📃 Resultados')
    elif choice == "Analisis Bivariado":
        st.subheader("📈 Reportes Bivariados")
        AnalisisBivariado(st, session)
        
        

if __name__ == '__main__':
    main()

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

    st.title("📈 Encuestas a Estudiantes Titulados - Univalle 2024")

    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Mostrar la imagen en la barra lateral
    st.sidebar.image(imagen, width=50)

    menu = [ "Analisis Dinamico", "Analisis Bivariado"]
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
    sedes = filtro_all_generico_combo(Sede, 'nombre_sede', session)
    selected_sedes = st.sidebar.multiselect("Selecciona una Sede:", sedes, default=sedes)

    # Carrera
    carreras = filtro_all_generico_combo(Carrera, 'nombre_carrera', session)
    ##carreras.insert(0, 'Todos')

    selected_carrera = st.sidebar.multiselect("Selecciona una Carrera:", carreras)

    ##carrera = filtro_busqueda_generico(Carrera, 'nombre_carrera', selected_carrera, session)

    # Gestion
    gestiones = filtro_all_generico_combo(Estudiante, 'gestion', session)
    gestiones = [year for year in gestiones if year is not None]

   ##selected_gestion = st.sidebar.selectbox("Selecciona la Gestion:", gestiones)
    selected_gestion = st.sidebar.slider("Seleccionar la Gestion:", 
                                          min_value=min(gestiones),
                                          max_value=max(gestiones),
                                          value=(min(gestiones),max(gestiones))
                                         
                                         )

    # Género
    genero = st.sidebar.radio("Género:", ('Todos','Masculino', 'Femenino'))
    genero_valor = 1 if genero == 'Masculino' else 0

    # Estado Civil
    estados_civiles = filtro_all_generico_combo(EstadoCivil, 'nombre_estado_civil', session)
    selected_estados_civiles = st.sidebar.multiselect("Selecciona Estado Civil:", estados_civiles, default=estados_civiles)

    # País
    paises = filtro_all_generico_combo(Pais, 'nombre_pais', session)
    selected_pais = st.sidebar.multiselect("Selecciona el Pais:", paises)
    ##pais = filtro_busqueda_generico(Pais, 'nombre_pais', selected_pais, session)

    # Ciudad
    ##ciudades = filtro_all_generico_combo(Ciudad, 'nombre_ciudad', session)
    ##ciudades.insert(0,'ciudades')
    ##selected_ciudad = st.sidebar.selectbox("Selecciona la Ciudad:", ciudades)

    # Edad
    rango_edad = filtro_all_generico_combo(Estudiante, 'edad', session)
    rango_edad = [edad for edad in rango_edad if edad is not None]
    ##edad = st.sidebar.select_slider("Seleccionar Edad:", options=list(range(rango_edad[0], rango_edad[-1])), value=25)
    selected_edad = st.sidebar.slider(
    "Seleccionar Rango de Edad:",
    min_value=min(rango_edad),
    max_value=max(rango_edad),
    value=(min(rango_edad),max(rango_edad))  # Valores por defecto del rango seleccionado
    )
    filtros={
        "sedes":selected_sedes,
        "genero":genero,
        "carrera":selected_carrera,
        "gestion":selected_gestion,
        "estado_civil":selected_estados_civiles,
        "pais":selected_pais,
        "edad":selected_edad
    }

    if choice == "Analisis Dinamico":
        AnalisisDinamico(st, session,filtros)
    elif choice == "Resultados":
        st.subheader('📃 Resultados')
    elif choice == "Matriz de Correlacion":
        st.subheader('📃 Resultados')
    elif choice == "Analisis Bivariado":
        st.subheader("📈 Reportes Bivariados")
        AnalisisBivariado(st, session)
        
        

if __name__ == '__main__':
    main()

import pandas as pd
from models import Estudiante, Sede, Carrera, Pais, Ciudad, EstadoCivil, filtro_busqueda_generico_varios, filtro_busqueda_generico, filtro_all_generico_combo, filtro_all_generico

def AnalisisDinamico(st, session):
    st.subheader("📈 Principal")
    
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
    
    df = pd.DataFrame(estudiantes)
    st.write(df)

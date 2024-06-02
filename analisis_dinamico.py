import pandas as pd
import plotly.express as px
from models import Estudiante, Sede, Carrera, Pais, Ciudad, EstadoCivil, Trabajo, SatisfaccionUnivalle, GradoSatisfaccion, ProgramasAcademicos, filtro_all_generico_combo, filtro_all_generico,filtro_busqueda_generico,filtro_busqueda_generico_varios,listadoGeneralEstudiantes

def AnalisisDinamico(st, session):
    st.subheader("📈 Principal")

 
    result= listadoGeneralEstudiantes(session)
    
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    df = df.loc[:, ~df.columns.duplicated()]
    if 'id_estudiante' in df.columns:
        df.drop(columns=['id_estudiante'], inplace=True)
    st.write(df)
    ##df = pd.DataFrame(estudiantes)

    # Gráficos
    c1,c2=st.columns(2)
    with c1: 
        st.subheader("Distribución de edades de los estudiantes")
        fig = px.histogram(df, x='edad', nbins=20, title='Distribución de Edades')
        st.plotly_chart(fig)
    with c2:
        st.write("### Proporción de estudiantes por sexo")
        fig = px.pie(df, names='sexo', title='Proporción de Estudiantes por Sexo', labels={'sexo': 'Sexo'}, hole=0.3)
        st.plotly_chart(fig)

    st.write("### Número de estudiantes por carrera")
    fig = px.bar(df, x='carrera', title='Número de Estudiantes por Carrera')
    st.plotly_chart(fig)

    c3,c4=st.columns(2)
    with c3:
        st.write("### Número de estudiantes que trabajan actualmente")
        trabajos = filtro_all_generico(Trabajo, session)
        df_trabajos = pd.DataFrame(trabajos)
        fig = px.pie(df_trabajos, names='trabaja_actualmente', title='Número de Estudiantes que Trabajan Actualmente', hole=0.3)
        st.plotly_chart(fig)
    with c4:
        st.write("### Distribución de satisfacción general con Univalle")
        satisfaccion = filtro_all_generico(SatisfaccionUnivalle, session)
        df_satisfaccion = pd.DataFrame(satisfaccion)
        fig = px.histogram(df_satisfaccion, x='satisfaccion_general_univalle', nbins=10, title='Distribución de Satisfacción General con Univalle')
        st.plotly_chart(fig)

    c5,c6=st.columns(2)
    with c5:
        st.write("### Número de estudiantes que planean realizar un curso de posgrado")
        programas = filtro_all_generico(ProgramasAcademicos, session)
        df_programas = pd.DataFrame(programas)
        fig = px.pie(df_programas, names='realizar_cursos_postgrado', title='Número de Estudiantes que Planean Realizar un Curso de Posgrado', hole=0.3)
        st.plotly_chart(fig)
    with c6:
        st.write("### Proporción de estudiantes por estado civil")
        fig = px.pie(df, names='id_estado_civil', title='Proporción de Estudiantes por Estado Civil', hole=0.3)
        st.plotly_chart(fig)
    c7,c8=st.columns(2)
    with c7:
        st.write("### Número de estudiantes por país de procedencia")
        fig = px.bar(df, x='pais', title='Número de Estudiantes por País de Procedencia')
        st.plotly_chart(fig)
    with c8:                  
        st.write("### Distribución de estudiantes por nivel de satisfacción con los docentes")
        fig = px.histogram(df, x='satisfaccion_docentes', nbins=10, title='Distribución de Satisfacción con los Docentes')
        st.plotly_chart(fig)

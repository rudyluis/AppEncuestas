import pandas as pd
import plotly.express as px
from models import Estudiante, Sede, Carrera, Pais, Ciudad, EstadoCivil, Trabajo, SatisfaccionUnivalle, GradoSatisfaccion, ProgramasAcademicos, filtro_all_generico_combo, filtro_all_generico,filtro_busqueda_generico,filtro_busqueda_generico_varios,listadoGeneralEstudiantes

def AnalisisBivariado(st, session):

    result= listadoGeneralEstudiantes(session)
    
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    df = df.loc[:, ~df.columns.duplicated()]
    if 'id_estudiante' in df.columns:
        df.drop(columns=['id_estudiante'], inplace=True)
    st.write(df)
    ##df = pd.DataFrame(estudiantes)

    # Gráficos
    c1,c2=st.columns(2)
    # Reportes Bivariados
    with c1:
        st.write("### Comparación de la satisfacción general con Univalle por sexo")
        fig = px.box(df, x='sexo', y='satisfaccion_general_univalle', title='Comparación de la Satisfacción General con Univalle por Sexo',color='sexo',color_discrete_sequence=px.colors.qualitative.Alphabet)
        st.plotly_chart(fig)
    with c2:
        st.write("### Relación entre la edad y la satisfacción con la formación académica")
        fig = px.scatter(df, x='edad', y='satisfaccion_formacion_academica', title='Relación entre Edad y Satisfacción con la Formación Académica', color='edad', color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig)
    c3,c4=st.columns(2)
    with c3:
        st.write("### Comparación de la satisfacción con los docentes por carrera")
        fig = px.box(df, x='carrera', y='satisfaccion_docentes', title='Comparación de la Satisfacción con los Docentes por Carrera',color='carrera',color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(fig)
    with c4:
        st.write("### Relación entre el trabajo actual y la satisfacción con la carrera")
        fig = px.box(df, x='trabaja_actualmente', y='satisfaccion_carrera', title='Relación entre el Trabajo Actual y la Satisfacción con la Carrera', color='trabaja_actualmente',color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig)
    c5,c6=st.columns(2)
    with c5:
        st.write("### Comparación de la satisfacción con la infraestructura por sede")
        fig = px.box(df, x='sede', y='satisfaccion_infraestructura', title='Comparación de la Satisfacción con la Infraestructura por Sede',color='sede',color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)
    with c6:
        st.write("### Relación entre el plan de posgrado y la carrera")
        fig = px.box(df, x='realizar_cursos_postgrado', y='carrera', title='Relación entre el Plan de Posgrado y la Carrera')
        st.plotly_chart(fig)
    c7,c8= st.columns(2)
    with c7:
        st.write("### Comparación de la satisfacción con los servicios de Univalle por carrera")
        fig = px.box(df, x='carrera', y='satisfaccion_servicios_univalle', title='Comparación de la Satisfacción con los Servicios de Univalle por Carrera')
        st.plotly_chart(fig)
    with c8:
        st.write("### Relación entre la ciudad de procedencia y la carrera")
        fig = px.box(df, x='ciudad', y='carrera', title='Relación entre la Ciudad de Procedencia y la Carrera',color='ciudad',color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig)
        
    st.write("### Comparación de la satisfacción con la atención administrativa por si trabaja actualmente o no")
    fig = px.box(df, x='trabaja_actualmente', y='satisfaccion_atencion_administrativa', title='Comparación de la Satisfacción con la Atención Administrativa por Si Trabaja Actualmente o No', color='trabaja_actualmente',color_discrete_sequence=px.colors.qualitative.Alphabet)
    st.plotly_chart(fig)

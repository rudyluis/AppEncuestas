import pandas as pd
import plotly.express as px
from models import Estudiante, Sede, Carrera, Pais, Ciudad, EstadoCivil, Trabajo, SatisfaccionUnivalle, GradoSatisfaccion, ProgramasAcademicos, filtro_all_generico_combo, filtro_all_generico,filtro_busqueda_generico,filtro_busqueda_generico_varios,listadoGeneralEstudiantes

def AnalisisDinamico(st, session,filtros):
    st.subheader("📈 Datos Principal")

    
    result= listadoGeneralEstudiantes(session)
    
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    df = df.loc[:, ~df.columns.duplicated()]
    if 'id_estudiante' in df.columns:
        df.drop(columns=['id_estudiante'], inplace=True)
    ### filtrar por SEDES    
    sedes=filtros['sedes']
    df = df[df['sede'].isin(sedes)]    
    ### filtrar GENEROS
    genero= filtros['genero']
    if(genero=='Todos'):
        genero=['M','F']
    if(genero=='Masculino'):
        genero=['M']
    if(genero=='Femenino'):
        genero=['F']        
    df = df[df['sexo'].isin(genero)]   

    ### CARRERA
    carrera=filtros['carrera'] 
    if not carrera:
        carrera = filtro_all_generico_combo(Carrera, 'nombre_carrera', session)

    df = df[df['carrera'].isin(carrera)]  
    ###Gestion
    gestion=filtros['gestion'] 

    min_gestion, max_gestion = gestion
    df = df[(df['gestion'] >= min_gestion) & (df['gestion'] <= max_gestion)]
    ## Estado Civil
    estado_civil= filtros['estado_civil']
    df = df[df['estado_civil'].isin(estado_civil)]   
    
    #3 Pais
    pais= filtros['pais']
    
    if not pais:
        pais = filtro_all_generico_combo(Pais, 'nombre_pais', session)
    ##print(pais)
    df = df[df['pais'].isin(pais)]  
    
    ### Rango EDAD
    edad= filtros['edad']
    min_edad, max_edad = edad
    df = df[(df['edad'] >= min_edad) & (df['edad'] <= max_edad)]
    st.write(df)
    ##df = pd.DataFrame(estudiantes)
    #GRAFICO 1
    # Calcular la distribución
    satisfaction_distribution = df['satisfaccion_general_univalle'].value_counts().sort_index()
    satisfaction_percentage = (satisfaction_distribution / df['satisfaccion_general_univalle'].count()) * 100

    # Crear la tabla de satisfacción
    satisfaction_table = pd.DataFrame({
        'Nivel de Satisfacción': satisfaction_distribution.index,
        'Número de Estudiantes': satisfaction_distribution.values,
        'Porcentaje (%)': satisfaction_percentage.values
    })

    # Streamlit app
    st.title('Distribución de Satisfacción General')

    st.subheader('Tabla 1: Distribución de Satisfacción General')
    st.write(satisfaction_table)
    st.subheader('Histograma de Satisfacción General')
    fig = px.histogram(df, x='satisfaccion_general_univalle', nbins=5, labels={'satisfaccion_general_univalle':'Nivel de Satisfacción'}, title='Distribución de Satisfacción General')
    fig.update_layout(xaxis_title='Nivel de Satisfacción', yaxis_title='Número de Estudiantes')
    fig.update_traces(texttemplate='%{y}', textposition='outside', marker_color='lightskyblue')

    st.plotly_chart(fig)

    #GRAFICO 2
    # Calcular la distribución de satisfacción por carrera
    satisfaction_by_career = df.groupby(['carrera', 'satisfaccion_general_univalle']).size().reset_index(name='Número de Estudiantes')
    #satisfaction_by_career['Porcentaje'] = satisfaction_by_career.groupby('carrera')['Número de Estudiantes'].apply(lambda x: (x / x.sum()) * 100)

    st.subheader('Tabla 2: Satisfacción por Carrera')
    st.write(satisfaction_by_career)
    # Gráfico de Barras de Satisfacción por Carrera
    st.subheader('Gráfico de Barras de Satisfacción por Carrera')
    fig2 = px.bar(satisfaction_by_career, x='carrera', y='Número de Estudiantes', color='satisfaccion_general_univalle', 
                labels={'Número de Estudiantes':'Número de Estudiantes', 'SatisfaccionGeneralDesc':'Nivel de Satisfacción'}, 
                title='Satisfacción por Carrera', barmode='group')
    fig2.update_layout(xaxis_title='carrera', yaxis_title='Número de Estudiantes')
    fig2.update_traces(texttemplate='%{y}', textposition='outside')
    st.plotly_chart(fig2)

  #GRAFICO 3
    # Calcular la distribución de satisfacción por sede
    satisfaction_by_sede = df.groupby(['sede', 'satisfaccion_general_univalle']).size().reset_index(name='Número de Estudiantes')

    #satisfaction_by_career['Porcentaje'] = satisfaction_by_career.groupby('carrera')['Número de Estudiantes'].apply(lambda x: (x / x.sum()) * 100)

    st.subheader('Tabla 3: Satisfacción por Sede')
    st.write(satisfaction_by_sede)
    # Gráfico de Barras de Satisfacción por Carrera
    st.subheader('Gráfico de Barras de Satisfacción por Sede')
    fig3 = px.bar(satisfaction_by_sede, x='sede', y='Número de Estudiantes', color='satisfaccion_general_univalle', 
                labels={'Número de Estudiantes':'Número de Estudiantes', 'satisfaccion_general_univalle':'Nivel de Satisfacción'}, 
                title='Satisfacción por Sede', barmode='group')
    fig3.update_layout(xaxis_title='sede', yaxis_title='Número de Estudiantes')
    fig3.update_traces(texttemplate='%{y}', textposition='outside')
    st.plotly_chart(fig3)

    ##GRAFICO 4
    satisfaction_by_sede = df.groupby(['sede', 'satisfaccion_general_univalle']).size().reset_index(name='Número de Estudiantes')
    # Calculate distribution of interest in postgraduate studies
    interest_counts = df['cursos_postgrado'].value_counts().reset_index()
    interest_counts.columns = ['Interes', 'Count']

    # Calculate percentages
    interest_counts['Percentage'] = (interest_counts['Count'] / interest_counts['Count'].sum()) * 100

    # Plot pie chart
    fig4 = px.pie(interest_counts, values='Count', names='Interes', title='Distribución General de Interés en Posgrado', labels={'Interes': 'Interés en Posgrado', 'Count': 'Número de Estudiantes'}, hole=0.3)

    # Streamlit app
    st.title('Análisis de Interés en Posgrado')
    st.write('Se analizó el interés general de los estudiantes en tomar un posgrado en la misma universidad.')

    # Display table
    st.write('### Tabla 4: Distribución General de Interés en Posgrado')
    st.write(interest_counts)

    # Display pie chart
    st.plotly_chart(fig4)

    #GRAFICO 5
     ##GRAFICO 4

    df_grouped = df.groupby(['cursos_postgrado', 'satisfaccion_general_univalle']).size().reset_index(name='Cantidad')

    # Calcular porcentajes
    df_grouped['Porcentaje'] = df_grouped['Cantidad'] / df_grouped['Cantidad'].sum() * 100

    # Crear gráfico de dispersión
    # Paso 3: Crear gráfico de dispersión
# Paso 3: Crear gráfico de barras con etiquetas
    fig5 = px.bar(df_grouped, x='satisfaccion_general_univalle', y='Cantidad', color='cursos_postgrado',
                labels={'satisfaccion_general_univalle': 'Nivel de Satisfacción', 'Cantidad': 'Número de Estudiantes'},
                title='Relación entre Satisfacción e Interés en Posgrado',
                barmode='group',
                text='Cantidad')

    # Ajustar el layout para mostrar las etiquetas
    fig5.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    # Configurar Streamlit
    st.title("Relación entre Satisfacción e Interés en Posgrado")
    st.write("Se analizó la relación entre el nivel de satisfacción de los estudiantes y su interés en tomar un posgrado en la universidad.")

    # Mostrar tabla
    st.write("### Tabla 7: Relación entre Satisfacción e Interés en Posgrado")
    st.dataframe(df_grouped)

    # Mostrar gráfico
    st.plotly_chart(fig5)
    # Gráficos
    c1,c2=st.columns(2)
    df['edad'] = df['edad'].fillna(df['edad'].mean())
    with c1: 
        st.subheader("Distribución de edades de los estudiantes")
        fig = px.histogram(df, x='edad', nbins=20, title='Distribución de Edades', color_discrete_sequence=px.colors.qualitative.Alphabet)
        st.plotly_chart(fig)
    with c2:
        st.write("### Proporción de estudiantes por sexo")
        fig = px.pie(df, names='sexo', title='Proporción de Estudiantes por Sexo', labels={'sexo': 'Sexo'}, hole=0.3)
        st.plotly_chart(fig)

    st.write("### Número de estudiantes por carrera")
    ##fig = px.bar(df, x='carrera', title='Número de Estudiantes por Carrera',color_discrete_sequence=['#EF553B'])
    fig = px.histogram(df, x='carrera', nbins=20, title='Número de Estudiantes por Carrera', color_discrete_sequence=px.colors.qualitative.Dark2)
       
    st.plotly_chart(fig)

    c3,c4=st.columns(2)
    with c3:
        st.write("### Número de estudiantes que trabajan actualmente")
        trabajos = filtro_all_generico(Trabajo, session)
        df_trabajos = pd.DataFrame(trabajos)
        fig = px.pie(df, names='estado_trabaja', title='Número de Estudiantes que Trabajan Actualmente', hole=0.3,color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig)
    with c4:
        st.write("### Distribución de satisfacción general con Univalle")
        satisfaccion = filtro_all_generico(SatisfaccionUnivalle, session)
        df_satisfaccion = pd.DataFrame(satisfaccion)
        fig = px.histogram(df, x='satisfaccion_general_univalle', nbins=10, title='Distribución de Satisfacción General con Univalle',color_discrete_sequence=['#AB63FA'])
        st.plotly_chart(fig)

    c5,c6=st.columns(2)
    with c5:
        st.write("### Número de estudiantes que planean realizar un curso de posgrado")
        programas = filtro_all_generico(ProgramasAcademicos, session)
        df_programas = pd.DataFrame(programas)
       ## fig = px.pie(df, names='cursos_postgrado', title='Número de Estudiantes que Planean Realizar un Curso de Posgrado', hole=0.3)
        fig = px.histogram(df, x='cursos_postgrado', nbins=10, title='Número de Estudiantes que Planean Realizar un Curso de Posgrado',color_discrete_sequence=['#19D3F3'])
       
        st.plotly_chart(fig)
    with c6:
        st.write("### Proporción de estudiantes por estado civil")
        fig = px.pie(df, names='estado_civil', title='Proporción de Estudiantes por Estado Civil', hole=0.3)
        st.plotly_chart(fig)
    c7,c8=st.columns(2)
    with c7:
        st.write("### Número de estudiantes por país de procedencia")
        fig = px.bar(df, x='pais', title='Número de Estudiantes por País de Procedencia',color_discrete_sequence=['#B6E880'])
        st.plotly_chart(fig)
    with c8:                  
        st.write("### Distribución de estudiantes por nivel de satisfacción con los docentes")
        fig = px.histogram(df, x='satisfaccion_docentes', nbins=10, title='Distribución de Satisfacción con los Docentes',color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig)

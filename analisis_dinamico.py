from models import Estudiante,Sede,Carrera,Pais,Ciudad,EstadoCivil,filtro_busqueda_generico_varios,filtro_busqueda_generico, filtro_all_generico_combo, filtro_all_generico
import pandas as pd

def AnalisisDinamico(st):
	st.subheader("📈 Principal")
	sedes= filtro_all_generico_combo(Sede,'nombre_sede')
	st.sidebar.multiselect("Selecciona una Sede:", sedes, default=sedes)
	## Carrera
	carrera= filtro_all_generico_combo(Carrera,'nombre_carrera')
	carrera= st.sidebar.selectbox("Selecciona una Carrera:", carrera)
	carrera= filtro_busqueda_generico(Carrera,'nombre_carrera',carrera)
	## fin Carrera
	gestion= filtro_all_generico_combo(Estudiante,'gestion')
	st.sidebar.selectbox("Selecciona la Gestion:", gestion)
	### Genero
	genero = st.sidebar.radio(
			"Género:",
			('Masculino', 'Femenino')
	)
	if genero == 'Masculino':
		genero = 1
	else:
		genero = 0
	## Fin Genero
	estado_civil= filtro_all_generico_combo(EstadoCivil,'nombre_estado_civil')
	st.sidebar.multiselect("Selecciona Estado Civil:", estado_civil, default=estado_civil)
 	## pais
	pais= filtro_all_generico_combo(Pais,'nombre_pais')
	pais=st.sidebar.selectbox("Selecciona el Pais:", pais)
	pais= filtro_busqueda_generico(Pais,'nombre_pais',pais)
 	## fiN Pais
	ciudad= filtro_all_generico_combo(Ciudad,'nombre_ciudad')
	st.sidebar.selectbox("Selecciona la Ciudad:", ciudad)
		# Mapeo de género a valor numérico
	
	edad = st.sidebar.select_slider("Seleccionar Edad:", options=list(range(1, 101)),  value=25)
	
	if carrera is None:
		estudiantes=filtro_all_generico(Estudiante)
	else:
		filtros = {
			"id_carrera": carrera[0]['id_carrera'],
			"sexo": genero,
			"id_pais":pais[0]['id_pais']
		}
		estudiantes=filtro_busqueda_generico_varios(Estudiante,filtros)
		
	df = pd.DataFrame(estudiantes)
	st.write(df)
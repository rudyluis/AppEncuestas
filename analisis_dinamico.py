from models import Estudiante,Sede,Carrera,Pais,Ciudad,EstadoCivil, filtro_all_generico_combo

def AnalisiDinamico(st):
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
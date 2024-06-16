from sqlalchemy import Column, Integer, String, ForeignKey, Date, Sequence, text
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import create_engine

# Conexión a la base de datos
engine = create_engine('postgresql://bdencuestasunivalle_user:pWB2M9UReSOqeNYzI9qsztYaKIVUzk76@dpg-coe6k2i0si5c739bojmg-a.oregon-postgres.render.com:5432/bdencuestasunivalle')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Definición de tablas
class Carrera(Base):
    __tablename__ = "carrera"
    id_carrera = Column(Integer, primary_key=True)
    nombre_carrera = Column(String(255), nullable=False)

class Ciudad(Base):
    __tablename__ = "ciudad"
    id_ciudad = Column(Integer, primary_key=True)
    nombre_ciudad = Column(String(255), nullable=False)

class EstadoCivil(Base):
    __tablename__ = "estado_civil"
    id_estado_civil = Column(Integer, primary_key=True)
    nombre_estado_civil = Column(String(255), nullable=False)

class Pais(Base):
    __tablename__ = "pais"
    id_pais = Column(Integer, primary_key=True)
    nombre_pais = Column(String(255), nullable=False)

class Sede(Base):
    __tablename__ = "sede"
    id_sede = Column(Integer, primary_key=True)
    nombre_sede = Column(String(255), nullable=False)

class Estudiante(Base):
    __tablename__ = 'estudiante'
    id_estudiante = Column(Integer, primary_key=True)
    nombre_completo = Column(String(255), nullable=False)
    gestion = Column(Integer)
    ci = Column(String(255), unique=True)
    sexo = Column(Integer)
    fecha_nacimiento = Column(Date)
    edad = Column(Integer)
    telefono = Column(String(20))
    celular = Column(String(20))
    direccion_actual = Column(String(255))
    correo_electronico = Column(String(255))
    nombre_facebook = Column(String(255))
    id_sede = Column(Integer, ForeignKey('sede.id_sede'))
    id_carrera = Column(Integer, ForeignKey('carrera.id_carrera'))
    id_pais = Column(Integer, ForeignKey('pais.id_pais'))
    id_ciudad = Column(Integer, ForeignKey('ciudad.id_ciudad'))
    id_estado_civil = Column(Integer, ForeignKey('estado_civil.id_estado_civil'))
    sede = relationship('Sede')
    carrera = relationship('Carrera')
    pais = relationship('Pais')
    ciudad = relationship('Ciudad')
    estadocivil = relationship('EstadoCivil')

class Trabajo(Base):
    __tablename__ = 'trabajo'
    id_trabajo = Column(Integer, primary_key=True)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id_estudiante'), nullable=False)
    trabaja_actualmente = Column(Integer, nullable=True)
    lugar_trabajo_actual = Column(String(255), nullable=True)
    fecha_ingreso_trabajo_actual = Column(Date)
    estudiante = relationship('Estudiante')

class AspectosPositivos(Base):
    __tablename__ = 'aspectos_positivos'
    id_aspecto_positivo = Column(Integer, primary_key=True)
    aspecto_positivo = Column(String(255))

class AspectosNegativos(Base):
    __tablename__ = 'aspectos_negativos'
    id_aspecto_negativo = Column(Integer, primary_key=True)
    aspecto_negativo = Column(String(255))

class RecomendacionCambio(Base):
    __tablename__ = 'recomendacion_cambio'
    id_recomendacion_cambio = Column(Integer, primary_key=True)
    recomendacion = Column(String(255))

class AspectosUnivalle(Base):
    __tablename__ = 'aspectos_univalle'
    id_aspectos_univalle = Column(Integer, primary_key=True)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id_estudiante'))
    aspectos_positivos_univalle1 = Column(Integer, ForeignKey('aspectos_positivos.id_aspecto_positivo'))
    aspectos_positivos_univalle2 = Column(Integer, ForeignKey('aspectos_positivos.id_aspecto_positivo'))
    aspectos_negativos_univalle1 = Column(Integer, ForeignKey('aspectos_negativos.id_aspecto_negativo'))
    aspectos_negativos_univalle2 = Column(Integer, ForeignKey('aspectos_negativos.id_aspecto_negativo'))
    recomendacion_de_cambio = Column(Integer, ForeignKey('recomendacion_cambio.id_recomendacion_cambio'))

    estudiante = relationship('Estudiante')
    aspectos_positivos1 = relationship('AspectosPositivos', foreign_keys=[aspectos_positivos_univalle1])
    aspectos_positivos2 = relationship('AspectosPositivos', foreign_keys=[aspectos_positivos_univalle2])
    aspectos_negativos1 = relationship('AspectosNegativos', foreign_keys=[aspectos_negativos_univalle1])
    aspectos_negativos2 = relationship('AspectosNegativos', foreign_keys=[aspectos_negativos_univalle2])
    recomendacion = relationship('RecomendacionCambio')

class GradoSatisfaccion(Base):
    __tablename__ = 'grado_satisfaccion'
    id_grado_satisfaccion = Column(Integer, primary_key=True)
    satisfaccion = Column(String(255))

class SatisfaccionUnivalle(Base):
    __tablename__ = 'satisfaccion_univalle'
    id_satisfaccion_univalle = Column(Integer, primary_key=True)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id_estudiante'))
    satisfaccion_carrera = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_docentes = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_formacion_academica = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_servicios_univalle = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_atencion_administrativa = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_infraestructura = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))
    satisfaccion_general_univalle = Column(Integer, ForeignKey('grado_satisfaccion.id_grado_satisfaccion'))

    estudiante = relationship("Estudiante")
    grado_satisfaccion_carrera = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_carrera])
    grado_satisfaccion_docentes = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_docentes])
    grado_satisfaccion_formacion_academica = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_formacion_academica])
    grado_satisfaccion_servicios_univalle = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_servicios_univalle])
    grado_satisfaccion_atencion_administrativa = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_atencion_administrativa])
    grado_satisfaccion_infraestructura = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_infraestructura])
    grado_satisfaccion_general_univalle = relationship("GradoSatisfaccion", foreign_keys=[satisfaccion_general_univalle])

class ProgramasAcademicos(Base):
    __tablename__ = 'programas_academicos'
    id_programa_academico = Column(Integer, primary_key=True)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id_estudiante'), nullable=False)
    realizar_cursos_postgrado = Column(Integer)
    conseguir_trabajo = Column(Integer)
    otro_plan = Column(String(40))
    diplomado = Column(Integer)
    especialidad = Column(Integer)
    maestria = Column(Integer)
    id_diplomado = Column(Integer, ForeignKey('diplomado.id_diplomado'), nullable=False)
    id_especialidad = Column(Integer, ForeignKey('especialidad.id_especialidad'), nullable=False)
    id_maestria = Column(Integer, ForeignKey('maestria.id_maestria'), nullable=False)
    estudiante = relationship("Estudiante")

class Postgrado(Base):
    __tablename__ = 'postgrado'
    id_postgrado = Column(Integer, primary_key=True)
    nombre_postgrado = Column(String(50), nullable=False)

# Funciones de filtrado
def filtro_busqueda_generico(nombre_tabla, nombre_id, valor_buscar, session):
    registros = session.query(nombre_tabla).filter_by(**{nombre_id: valor_buscar}).all()
    if registros:
        registros_dict = [{columna: getattr(registro, columna) for columna in registro.__table__.columns.keys()} for registro in registros]
        return registros_dict
    else:
        print("No se encontraron registros.")
        return None

def filtro_all_generico_combo(nombre_tabla, campo, session):
    valores = session.query(getattr(nombre_tabla, campo)).distinct().order_by(campo).all()
    valores = [valor[0] for valor in valores]
    return valores

def filtro_all_generico(nombre_tabla, session):
    registros = session.query(nombre_tabla).all()
    registros_dict = [{columna: getattr(registro, columna) for columna in registro.__table__.columns.keys()} for registro in registros]
    return registros_dict

def filtro_busqueda_generico_varios(nombre_tabla, filtros, session):
    query = session.query(nombre_tabla)
    for campo, valor in filtros.items():
        query = query.filter(getattr(nombre_tabla, campo) == valor)
    registros = query.all()
    if registros:
        registros_dict = [{columna: getattr(registro, columna) for columna in registro.__table__.columns.keys()} for registro in registros]
        return registros_dict
    else:
        print("No se encontraron registros.")
        return None


def listadoGeneralEstudiantes(session):
    session
    sql = """select * 
        from estudiante_datos da
        inner join estudiante_postgrado por on por.id_estudiante=da.id_estudiante
        inner join estudiante_aspectos asp on asp.id_estudiante=da.id_estudiante
        inner join estudiante_satisfaccion sat on sat.id_estudiante= da.id_estudiante
        inner join estudiante_trabajo tra on tra.id_estudiante=da.id_estudiante
        order by da.id_estudiante ;"""
    
    
    result = session.execute(text(sql))
    return result
    
    
    
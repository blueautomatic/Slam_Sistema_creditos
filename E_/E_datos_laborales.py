import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Numeric
from sqlalchemy import create_engine
from N_cliente import N_datos_datos_laborales
from sqlalchemy.orm import sessionmaker


 base = declarative_base()
class E_datos_laborales(base):
	tablename__= "datos_laborales"	
	id = Column(Integer, primary_key=True, autoincrement=True)
	id_party = Column(Integer, ForeignKey('party_party.id_party'))
	sueldo = Column(Numeric(100))
	anti_laboral = Column(String(10))
	tel_laboral = Column(String(30))
	dom_laboral = Column(String(100))
	posee_recibo_sueldo = Column(String(6))
	organismo = Column(String(50))
	ocupacion = Column(String(50))
	categoria = Column(String(50))
	

	def __init__(self,id):
		a = id


	def guardar(self,obj_N_datos_laborales):
	    engine=create_engine('postgresql://postgres:postgres@localhost:5432/credired')
	    Session= sessionmaker(bind=engine) 
	    session=Session()
	    new_record = E_datos_laborales(1)
	    new_record.sueldo = obj_N_datos_laborales.sueldo	
	    new_record.anti_laboral = obj_N_datos_laborales.anti_laboral
	    new_record.tel_laboral = obj_N_datos_laborales.tel_laboral
	    new_record.dom_laboral = obj_N_datos_laborales.dom_laboral
	    new_record.posee_recibo_sueldo = obj_N_datos_laborales.posee_recibo_sueldo
	    new_record.organismo = obj_N_datos_laborales.organismo
	    new_record.ocupacion = obj_N_datos_laborales.ocupacion
	    new_record.categoria = obj_N_datos_laborales.categoria
	    session.add(new_record)
	    session.commit()

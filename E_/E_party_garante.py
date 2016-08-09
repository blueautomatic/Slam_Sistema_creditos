import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from N_cliente import N_party_garante
from sqlalchemy.orm import sessionmaker


base = declarative_base()
class E_party_garante(base):
	__tablename__="party_garante"
	id_garante=Column(Integer, primary_key=True, autoincrement=True)
	id_party=Column(Integer, ForeignKey('party.id_party'))
	nombre=Column(String(30))
	ciudad=Column(String(30))
	apellido=Column(String(30))
	domicilio=Column(String(30))
	num_cliente=Column(String(200))
	activo=Column(String(50))
	inactivo=Column(String(10))
	fec_nac=Column(DateTime)
	tipo_documento=Column(Integer(30))
	num_documento=Column(Integer(30))
	limite_credito=Column(Integer(30))
	comment=Column(Integer(30))

	def __init__(self, id_party):
		a = id_party

	def guardar(self, obj_N_party_garante):
		engine=create_engine('postgresql://postgres:postgres@localhost:5432/credired')
		Session= sessionmaker(bind=engine) 
		session=Session()
		new_record = E_party_garante(1)
		new_record.nombre = obj_N_party_garante.nombre
		new_record.ciudad = obj_N_party_garante.ciudad
		new_record.apellido = obj_N_party_garante.apellido
		new_record.domicilio = obj_N_party_garante.domicilio
		new_record.num_cliente = obj_N_party_garante.num_cliente
		new_record.activo = obj_N_party_garante.activo
		new_record.inactivo = obj_N_party_garante.inactivo
		new_record.fec_nac = obj_N_party_garante.fec_nac
		new_record.tipo_documento = obj_N_party_garante.tipo_documento
		new_record.num_documento = obj_N_party_garante.num_documento
		new_record.limite_credito = obj_N_party_garante.limite_credito
		new_record.comment = obj_N_party_garante.comment
		new_record.estado_civil = obj_N_party_garante.estado_civil
		new_record.email = obj_N_party_garante.email
		new_record.barrio = obj_N_party_garante.barrio
		session.add(new_record)
		session.commit()
	














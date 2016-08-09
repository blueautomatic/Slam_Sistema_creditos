import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class E_party_address(Base):
	__tablename__="party_address"
	id = Column(Integer, primary_key=True, autoincrement=True)
	id_party = Column(Integer)
	ciudad = Column(String)
	domicilio = Column(String)
	barrio = Column(String)

	def __init__(self, id):
		a = id
			
	def guardar(self,obj_N_party_address,id_party):

		engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
		Session= sessionmaker(bind=engine) 
		session=Session()
		new_record = E_party_address(1)
		new_record.ciudad = obj_N_party_address.ciudad
		new_record.barrio = obj_N_party_address.barrio
		new_record.domicilio = obj_N_party_address.domicilio
		new_record.id_party = id_party
		session.add(new_record)
		session.commit()




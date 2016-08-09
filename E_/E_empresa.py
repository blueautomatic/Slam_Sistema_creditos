import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



base = declarative_base()
	class E_empresa(base):
		    __tablename__="empresa"
			id_empresa = Column(Integer, primary_key=True, autoincrement=True)
			nombre =  Column(String(30))
			ciudad =  Column(String(100))
			direccion =  Column(String(100))
			telefono =  Column(Integer(50))
			email = Column(String(100))
			website = Column(String(100))
			tipo_iva = Column(String(50))
			ingresos_brutos = Column(String(50))
			cuit = Column(String(50))
			nombre_fantasia = Column(String(50))



   		 def __init__  (self,id_empresa,nombre,ciudad,direccion,telefono,email,website,tipo_iva,ingresos_brutos,cuit,nombre_fantasia):
	        id_empresa = id_empresa
			self.nombre = nombre
			self.ciudad = ciudad
			self.direccion = direccion
			self.telefono = telefono
			self.email = email
			self.website = website
			self.tipo_iva = tipo_iva
			self.ingresos_brutos = ingresos_brutos
			self.cuit = cuit
			self.nombre_fantasia = nombre_fantasia
		


    	 def guardar(self):

	        engine=create_engine('postgresql://postgres:121212@localhost:5432/credired')
	        Session= sessionmaker(bind=engine) 
	        session=Session()
	        new_record = E_empresa
	        new_record.nombre = write_uid
			new_record.ciudad = write_date		
	        new_record.direccion = nombre
	        new_record.telefono = apellido
	        new_record.email = tipo
	        new_record.website = num_doc
	        new_record.tipo_iva = estado_civil
			new_record.ingresos_brutos = num_cliente
			new_record.cuit = cuit
	        new_record.nombre_fantasia = nombre_fantasia
	        session.add(new_record)
	        session.commit()

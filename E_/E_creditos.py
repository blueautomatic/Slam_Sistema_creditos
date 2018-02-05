import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

base = declarative_base()
	class E_creditos(base):
			tablename__= "credito"	
		    id_party = Column(Integer, primary_key=True, autoincrement=True)
		    id_credito = Column(Integer, ForeignKey('cliente.id_cliente'))
		    id_usuario = Column(Integer, ForeignKey('cliente.id_usuario'))
			num_credito =  Column(String(50))
			fecha_credito =  Column(DateTime)
			tasa =  Column(String(50))
			formula =  Column(String(50))
			importe_prestamo =  Column(String(50))
			cantidad_cuotas =  Column(String(50))
			tipo_vencimiento =  Column(String(50))
			vto_primer_cuota =  Column(String(50))
			interes =  Column(Integer(50))
			gastos =  Column(Integer(50))
			seguros =  Column(Integer(50))
			impuestos =  Column(Integer(50))
			cred_total =  Column(Integer(50))
			en_letras =  Column(String(100))
			observaciones =  Column(String(50))
		




	   def __init__(self,id_party,id_credito,id_usuario,num_credito,fecha_credito,tasa,formula,importe_prestamo,cantidad_cuotas,tipo_vencimiento,vto_primer_cuota,interes,gastos,seguros,impuestos,cred_total,en_letras,observaciones):
	        id_party = id_party
			self.id_credito = id_credito
			self.id_usuario = id_usuario
			self.num_credito = num_credito
			self.fecha_credito = fecha_credito
			self.tasa = tasa
			self.formula = formula
			self.importe_prestamo = importe_prestamo
			self.cantidad_cuotas = cantidad_cuotas
			self.tipo_vencimiento = tipo_vencimiento
			self.vto_primer_cuota = vto_primer_cuota
			self.interes = interes
			self.gastos = gastos
			self.seguros = seguros
			self.impuestos = impuestos
			self.cred_total = cred_total
			self.en_letras = en_letras
			self.observaciones = observaciones



	   def guardar(self):

	    	engine=create_engine('postgresql://postgres:121212@localhost:5432/credired')
	        Session= sessionmaker(bind=engine) 
	        session=Session()
	        new_record = E_creditos
	        new_record.num_credito = num_credito
			new_record.fecha_credito = fecha_credito		
	        new_record.tasa = tasa
	        new_record.formula = formula
	        new_record.importe_prestamo = importe_prestamo
	        new_record.cantidad_cuotas = cantidad_cuotas
	        new_record.tipo_vencimiento = tipo_vencimiento
			new_record.vto_primer_cuota = vto_primer_cuota
			new_record.interes = interes
	        new_record.gastos = gastos
	        new_record.seguros = seguros
			new_record.impuestos = impuestos
			new_record.cred_total = cred_total
	        new_record.en_letras = en_letras
			new_record.observaciones = observaciones
	        session.add(new_record)
	        session.commit()






















import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from N_cliente import N_datos_personales_cliente
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_party_party(base):
      __tablename__="party_party"
      id_party = Column(Integer, primary_key=True, autoincrement=True)
      create_date = Column(DateTime, default=func.now())
      write_uid = Column(Integer)
      write_date = Column(DateTime, default=func.now())
      fec_nac = Column(DateTime, default=func.now())
      nombre =  Column(String)
      apellido =  Column(String)
      tipo_doc =  Column(String)
      num_doc =  Column(String)
      estado_civil = Column(String)
      limite_credito = Column(Numeric)
      estado= Column(String)


      # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
      def __init__(self,rt):
            a = rt
            self.create_date =func.now()
            self.write_date = func.now()
            self.write_uid = 1

      def guardar(self, obj_N_datos_personales_cliente,id_usu):
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_party_party(1)
            new_record.write_uid = id_usu
            new_record.nombre = obj_N_datos_personales_cliente.nombre
            new_record.apellido = obj_N_datos_personales_cliente.apellido
            new_record.tipo_doc = obj_N_datos_personales_cliente.tipo_doc
            new_record.fec_nac = obj_N_datos_personales_cliente.fec_nac
            new_record.num_doc = obj_N_datos_personales_cliente.nro_doc
            new_record.estado_civil = obj_N_datos_personales_cliente.estado_civil
            new_record.limite_credito = obj_N_datos_personales_cliente.limite_credito
            new_record.estado= obj_N_datos_personales_cliente.estado
            session.add(new_record)
            try :
                  session.commit()
                  num_doc=obj_N_datos_personales_cliente.nro_doc
                  obj_party_party = session.query(E_party_party).filter_by(num_doc=str(num_doc)).first()
                  return obj_party_party.id_party

            except IntegrityError : 
                  session.rollback()
                  return "False" 

      def get_party_party(self, nro_doc):
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine)
            session=Session()
            obj_party_party = session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            return obj_party_party

            

      def get_id_party(self, nro_doc):
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine)
            session=Session()

            obj_party_party = session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            return obj_party_party.id_party

      def buscar_id_party_por_nro_doc(self, nro_doc):
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine)
            session=Session()

            obj_party_party = session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            return obj_party_party



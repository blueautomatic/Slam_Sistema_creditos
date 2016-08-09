import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from N_cliente import N_datos_personales_cliente
from sqlalchemy.exc import IntegrityError

base = declarative_base()
class E_party_party(base):
      __tablename__="party_party"
      id_party = Column(Integer, primary_key=True, autoincrement=True)
      create_date = Column(DateTime, default=func.now())
      write_uid = Column(Integer, ForeignKey('usuario.id_usuario'))
      write_date = Column(DateTime, default=func.now())
      fec_nac = Column(DateTime)
      nombre =  Column(String(30))
      apellido =  Column(String(50))
      tipo =  Column(String(50))
      num_doc =  Column(String(10))
      estado_civil = Column(String(20))
      num_cliente = Column(Integer(30), autoincrement=True,unique = True)


        # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
            def __init__(self,id_party):
            a = id_party
            self.create_date =func.now()
            self.write_date = func.now()
            self.write_uid = 1
            #self.nombre = nombre
            #self.apellido = apellido
            #self.tipo = tipo
            #self.num_doc = num_doc
            #self.estado_civil = estado_civil
            #self.num_cliente = num_cliente

        def guardar(self, obj_N_datos_personales_cliente,id_usu):

            engine=create_engine('postgresql://postgres:postgres@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_party_party(1)
            new_record.write_uid = id_usu
            new_record.nombre = obj_N_datos_personales_cliente.nombre
            new_record.apellido = obj_N_datos_personales_cliente.apellido
            new_record.tipo = obj_N_datos_personales_cliente.tipo_doc
            new_record.tipo = obj_N_datos_personales_cliente.fec_nac
            new_record.num_doc = obj_N_datos_personales_cliente.nro_doc
            new_record.estado_civil = obj_N_datos_personales_cliente.estado_civil
            session.add(new_record)
            session.commit()
            obj_party_party = session.query(E_party_party).filter_by(nro_doc=obj_N_datos_personales_cliente.nro_doc).first()
            return obj_party_party.id


        def get_id_party(self, nro_doc):
            engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
            Session= sessionmaker(bind=engine)
            session=Session()
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_party_party = session.query(E_party_party).filter_by(nro_doc=nro_doc).first()
            return obj_party_party.id


             
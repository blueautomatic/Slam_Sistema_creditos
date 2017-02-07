import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
      write_uid = Column(Integer)
      session=""

      # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
      def __init__(self):
            self.create_date =func.now()
            self.write_date = func.now()
            self.write_uid = 1
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_N_datos_personales_cliente ):

            obj_party = cls()
            obj_party.write_uid = obj_N_datos_personales_cliente.id_party
            obj_party.nombre = obj_N_datos_personales_cliente.nombre
            obj_party.apellido = obj_N_datos_personales_cliente.apellido
            obj_party.tipo_doc = obj_N_datos_personales_cliente.tipo_doc
            obj_party.fec_nac = obj_N_datos_personales_cliente.fec_nac
            obj_party.num_doc = obj_N_datos_personales_cliente.nro_doc
            obj_party.estado_civil = obj_N_datos_personales_cliente.estado_civil
            obj_party.limite_credito = obj_N_datos_personales_cliente.limite_credito
            obj_party.estado= obj_N_datos_personales_cliente.estado
            obj_party.session.add(obj_party)

            try :
                  obj_party.session.commit()
                  num_doc=obj_N_datos_personales_cliente.nro_doc
                  obj_party_party = obj_party.session.query(E_party_party).filter_by(num_doc=str(num_doc)).first()
                  obj_party.session.close()
                  return obj_party_party.id_party

            except IntegrityError :
                  obj_party.session.rollback()
                  obj_party.session.close()
                  return "False"

      def get_party_party(self, nro_doc):
            obj_party_party = self.session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            self.session.close()
            return obj_party_party

      def get_id_party(self, nro_doc):
            obj_party_party = self.session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            self.session.close()
            return obj_party_party.id_party

      def buscar_id_party_por_nro_doc(self, nro_doc):
            obj_party_party = self.session.query(E_party_party).filter_by(num_doc=str(nro_doc)).first()
            self.session.close()
            return obj_party_party

      def buscar_party_party_id(self,id_party):
            obj_party_party = self.session.query(E_party_party).filter_by(id_party=str(id_party)).first()
            self.session.close()
            return obj_party_party


      def actualizar(self,obj_N_datos_personales_cliente,id_party):

            u = update(E_party_party).where(E_party_party.id_party == id_party).values(nombre=obj_N_datos_personales_cliente.nombre, apellido = obj_N_datos_personales_cliente.apellido,tipo_doc = obj_N_datos_personales_cliente.tipo_doc, num_doc = obj_N_datos_personales_cliente.nro_doc, estado_civil = obj_N_datos_personales_cliente.estado_civil, limite_credito = obj_N_datos_personales_cliente.limite_credito, estado = obj_N_datos_personales_cliente.estado)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def buscar(self, apellido):
            list_party_party = self.session.query(E_party_party).filter_by(apellido = str(apellido)).all()
            self.session.close()
            return list_party_party

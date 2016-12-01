import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from N_cliente import N_datos_personales_cliente
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_party_cliente(base):
    __tablename__="party_cliente"
    nro_cliente = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    comment= Column(String)
    session=""


    def __init__(self):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        self.session=Session()

    def buscar_E_party_cliente_por_nro_cliente(self,nro_cliente):

        obj_party_cliente = session.query(E_party_cliente).filter_by(nro_cliente=nro_cliente).first()
        self.session.close()
        return obj_party_cliente

    def get_party_cliente(self,id_party):

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_party_cliente = self.session.query(E_party_cliente).filter_by(id_party=id_party).first()
        self.session.close()          
        return obj_party_cliente

    def get_nro_cliente(self,id_party):

        obj_party_cliente = self.session.query(E_party_cliente).filter_by(id_party=id_party).first()
        self.session.close()
        return obj_party_cliente.nro_cliente

    @classmethod
    def guardar(cls,comment, id_party):

        new_record = cls()
        new_record.id_party = id_party
        new_record.comment= comment
        new_record.session.add(new_record)
        new_record.session.commit()
        new_record.session.close()

    def buscar_id_party_por_nro_cliente(self, nro_cliente):

        obj_party_cliente = self.session.query(E_party_cliente).filter_by(nro_cliente=nro_cliente).first()
        if obj_party_cliente != None:
            self.session.session.close()
            return obj_party_cliente.id_party
        else:
            self.session.session.close()
            return False
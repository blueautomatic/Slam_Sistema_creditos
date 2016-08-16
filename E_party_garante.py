import sys 
#from N_party_garante import N_party_garante
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey,DateTime, Numeric, func,Boolean
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook


Base = declarative_base()
class E_party_garante(Base):
    __tablename__="party_garante"
    id_garante=Column(Integer, primary_key=True, autoincrement=True)
    id_party_garante=Column(Integer)
    comment=Column(String)
    tipo_garante= Column(String)
    nro_cliente=Column(String)

    def __init__(self, id_party):
        a = id_party


    def guardar(self, obj_N_party_garante,nro_cliente):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        new_record = E_party_garante(1)
        new_record.nro_cliente= nro_cliente
        new_record.comment = obj_N_party_garante.comment
        new_record.id_party_garante = obj_N_party_garante.id_party_garante
        new_record.tipo_garante = obj_N_party_garante.tipo_garante 
        session.add(new_record)
        session.commit()

    def es_garante_de_otro_cliente(self, id_party_garante):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        obj_party_garante = session.query(E_party_garante).filter_by(id_party_garante=id_party_garante).first()
        if obj_party_garante != None :
            return True
        else: 
            return False


    
    














import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric
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

    def __init__(self, id_party):
        a= id_party

    def get_nro_cliente(self,id_party):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        obj_party_cliente = session.query(E_party_cliente).filter_by(id_party=id_party).first()
          
        return obj_party_cliente.nro_cliente

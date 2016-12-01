import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from PyQt5.QtCore import pyqtRemoveInputHook

Base = declarative_base()
class E_party_address(Base):
    __tablename__="party_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    ciudad = Column(String)
    domicilio = Column(String)
    barrio = Column(String)
    session = ""

    def __init__(self):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        self.session=Session()
         
    

    @classmethod   
    def guardar(cls,obj_N_party_address,id_party):
        new_record = cls()
        new_record.ciudad = obj_N_party_address.ciudad
        new_record.barrio = obj_N_party_address.barrio
        new_record.domicilio = obj_N_party_address.domicilio
        new_record.id_party = id_party
        new_record.session.add(new_record)
        new_record.session.commit()
        new_record.session.close()

    def get_party_address(self,id_party):

        obj_party_address = self.session.query(E_party_address).filter_by(id_party=id_party).first()
        self.session.close()
        return obj_party_address


    def actualizar(self,obj_N_party_address,id_party):

        u = update(E_party_address).where(E_party_address.id_party == id_party).values(ciudad=obj_N_party_address.ciudad,domicilio = obj_N_party_address.domicilio, barrio = obj_N_party_address.barrio) 
        self.session.execute(u)
        self.session.commit()
        self.session.close()
import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
    class E_party_address(Base):
        __tablename__="party_address"
        id = Column(Integer, primary_key=True, autoincrement=True)
        id_party = Column(Integer, ForeignKey('party_party.id_party'))
        ciudad = Column(String(30))
        domicilio = Column(String(50))
        barrio = Column(String(50))

        def __init__(self, id):
            a = id
            
        def guardar(self,obj_N_party_address):

            engine=create_engine('postgresql://postgres:postgres@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_party_address(1)
            new_record.ciudad = obj_N_party_address.ciudad
            new_record.barrio = obj_N_party_address.barrio
            new_record.domicilio = obj_N_party_address.domicilio
            session.add(new_record)
          # try:
            session.commit()
            return true
            #exception 



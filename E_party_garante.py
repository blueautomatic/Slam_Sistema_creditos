import sys 
#from N_party_garante import N_party_garante
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey,DateTime, Numeric, func,Boolean
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class E_party_garante(Base):
    __tablename__="party_garante"
    id_garante=Column(Integer, primary_key=True, autoincrement=True)
    id_party=Column(Integer)
    comment=Column(String)
    activo=Column(Boolean)
    inactivo=Column(Boolean)
    num_cliente=Column(Integer)
    id_address=Column(Integer)
    id_contact=Column(Integer)

    


    def __init__(self, id_party):
        a = id_party

    


    def guardar(self, obj_N_party_garante,id_party):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_party_garante(1)
        new_record.comment = obj_N_party_garante.comment
        new_record.activo = obj_N_party_garante.activo
        new_record.inactivo = obj_N_party_garante.inactivo
        new_record.num_cliente = obj_N_party_garante.num_cliente
        new_record.id_address = obj_N_party_garante.id_address
        new_record.id_contact = obj_N_party_garante.id_contact  
        new_record.id_party = id_party

        
        
        
        session.add(new_record)
        session.commit()
    














import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from N_cliente import N_party_otros
from sqlalchemy.orm import sessionmaker

base = declarative_base()
    class E_party_otros(base):
            tablename__= "party_otros"  
            id = Column(Integer, primary_key=True, autoincrement=True)
        	id_party = Column(Integer, ForeignKey('party_party.id_party'))
            tipo_iva = Column(String(50))
            cuit = Column(String(15))
        	cbu = Column(String(30))
        	num_beneficio = Column(String(100))
    

        def __init__(self,id):
            a = id
        	

	    def guardar(self,obj_N_party_otros):

            engine=create_engine('postgresql://postgres:postgres@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_party_otros(1)	
            new_record.tipo_iva = obj_N_party_otros.tipo_iva
            new_record.cuit = obj_N_party_otros.cuit
            new_record.cbu = obj_N_party_otros.cbu
            new_record.num_beneficio = obj_N_party_otros.num_beneficio
            session.add(new_record)
            session.commit()

    

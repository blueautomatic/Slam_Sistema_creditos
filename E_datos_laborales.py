import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Numeric, func, Boolean
from sqlalchemy import create_engine
#from N_cliente import N_datos_datos_laborales
from sqlalchemy.orm import sessionmaker

base = declarative_base()
class E_datos_laborales(base):

        __tablename__= "datos_laborales"  
        id = Column(Integer, primary_key=True, autoincrement=True)
        id_party = Column(Integer)
        sueldo = Column(Numeric)
        anti_laboral = Column(String)
        tel_laboral = Column(String)
        dom_laboral = Column(String)
        organismo = Column(String)
        ocupacion = Column(String)
        categoria = Column(String)
        posee_recibo_sueldo = Column(Boolean)
    

        def __init__(self,id):
            a = id

        def guardar(self,obj_N_datos_laborales,id_party):

            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine) 
            session=Session()
            new_record = E_datos_laborales(1)
            new_record.sueldo = obj_N_datos_laborales.sueldo    
            new_record.anti_laboral = obj_N_datos_laborales.anti_laboral
            new_record.tel_laboral = obj_N_datos_laborales.tel_laboral
            new_record.dom_laboral = obj_N_datos_laborales.dom_laboral
            new_record.organismo = obj_N_datos_laborales.organismo
            new_record.ocupacion = obj_N_datos_laborales.ocupacion
            new_record.categoria = obj_N_datos_laborales.categoria
            new_record.id_party = id_party
            new_record.posee_recibo_sueldo = obj_N_datos_laborales.posee_recibo_sueldo
            session.add(new_record)
            session.commit()

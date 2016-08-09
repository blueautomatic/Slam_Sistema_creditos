import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


base = declarative_base()
class E_usuario(base):
    __tablename__= "usuarios"   
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=func.now())  
    write_date = Column(DateTime, default=func.now())
    nombre = Column(String)
    tipo_usuario = Column(String)
    password = Column(String)
    password2 = Column(String)

    def __init__(self,id_usuario,nombre,tipo_usuario,password,passwor2,create_date,write_date):
        id_usuario = id_usuario
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        self.password = password
        self.password = password2
        self.create_date = create_date
        self.write_date = write_date

    def guardar(self):

        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session = Session()
        new_record = E_usuario
        new_record.write_date = write_date      
        new_record.nombre = nombre
        new_record.tipo_usuario = tipo_usuario
        new_record.password = password
        new_record.password2 = password2
        session.add(new_record)
        session.commit()

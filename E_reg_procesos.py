import sys, datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer,func,update
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook


base = declarative_base()

class E_reg_procesos(base):
    __tablename__= "reg_procesos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, default=func.now())
    descripcion = Column(String)
    tipo = Column(String)
    write_uid = Column(Integer)
    session =""

    def __init__(self):
        engine = create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session = sessionmaker(bind=engine)
        self.session = Session()


    @classmethod
    def guardar(cls, obj_reg):
        new_record = cls()
        new_record.descripcion = obj_reg.descripcion
        new_record.tipo = obj_reg.tipo


        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except:
            new_record.session.rollback()
            new_record.session.close()
            return False

    def buscar_reg_procesos_punitorios(self):

        obj_creditos = self.session.query(E_reg_procesos).filter_by(tipo="Punitorios").all()
        try:
            self.session.close()
            return obj_creditos
        except :
            self.session.close()
            return False

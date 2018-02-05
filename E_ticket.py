import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer,func,Numeric,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cuotas import E_cuotas
from E_configuracion import configuracion
base = declarative_base()

class E_ticket(base):

    __tablename__= "ticket"
    nro_ticket = Column(Integer, primary_key=True, autoincrement=True)
    monto = Column(Numeric)
    fecha = Column(DateTime, default=func.now())
    nro_credito = Column(Integer)
    write_uid = Column(Integer)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()


    @classmethod
    def guardar_ticket(cls,obj_ticket):

            new_record = cls()
            new_record.monto = obj_ticket.monto
            new_record.fecha = obj_ticket.fecha
            new_record.nro_credito = obj_ticket.nro_credito
            new_record.write_uid = obj_ticket.write_uid
            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def buscar_ticket(self,nro_credito):

            queryresult = self.session.query(func.max(E_ticket.nro_ticket).label('nro_ticket')).filter_by(nro_credito=nro_credito).first() 
            #cuotas_ingreso = self.session.query(E_ticket).filter_by(nro_credito = nro_credito ).first()
            try:
                self.session.close()
                for x in queryresult:
                    return x
            except :
                self.session.close()
                return False
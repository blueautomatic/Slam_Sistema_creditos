import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer,func,Numeric,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cuotas import E_cuotas
from E_configuracion import configuracion
base = declarative_base()

class E_ingresos(base):

    __tablename__= "caja_ingreso"
    id = Column(Integer, primary_key=True, autoincrement=True)
    monto_cobrado = Column(Numeric)
    fecha_cobro = Column(DateTime, default=func.now())
    id_cuota = Column(Integer)
    nombre = Column(String)
    write_uid = Column(Integer)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    def ingresos_buscar(self ,fecha):
        #sql = text("select cta.nro_cuota, cta.importe_cobrado, pp.nombre, pp.apellido,cta.punitorios, cta.descuento, cta.estado_cuota from cuotas as cta inner join credito as cd  on cta.nro_credito = cd.nro_credito inner join party_party as pp on cd.id_party= pp.id_party  where cta.fecha_cobro = '"+ str(fecha) +"'")
        sql = text ("select cta.nro_cuota, ci.monto_cobrado,pp.nombre,pp.apellido,cta.punitorios,cta.descuento,cta.estado_cuota from cuotas as cta inner join credito as cd on cta.nro_credito = cd.nro_credito inner join party_party as pp on cd.id_party= pp.id_party inner join caja_ingreso as ci on cta.id = ci.id_cuota where ci.fecha_cobro = '"+ str(fecha) +"'")
        result = self.session.execute(sql)
        self.session.close()
        return result


    @classmethod
    def guardar_ingresos(cls,obj_ingreso):

            new_record = cls()
            new_record.monto_cobrado = obj_ingreso.monto
            new_record.nombre = obj_ingreso.nombre
            new_record.id_cuota = obj_ingreso.id_cuota

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook



base = declarative_base()
class E_empresa(base):
    __tablename__="empresa"
    id_empresa = Column(Integer, primary_key=True,autoincrement=True)
    nombre =  Column(String)
    ciudad =  Column(String)
    direccion =  Column(String)
    telefono =  Column(String)
    email = Column(String)
    website = Column(String)
    tipo_iva = Column(String)
    ingresos_brutos = Column(String)
    cuit = Column(String)
    nombre_fantasia = Column(String)
    desc_interna=Column(String)
    write_uid = Column(Integer)
    session=""

    def __init__  (self, id_empresa):
        a = id_empresa
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        self.session=Session()


    @classmethod
    def guardar(cls, obj_N_datos_empresa):
        new_record = cls(1)
        new_record.nombre =obj_N_datos_empresa.nombre
        new_record.ciudad =obj_N_datos_empresa.ciudad
        new_record.direccion = obj_N_datos_empresa.direccion
        new_record.telefono = obj_N_datos_empresa.telefono
        new_record.email = obj_N_datos_empresa.email
        new_record.website = obj_N_datos_empresa.website
        new_record.tipo_iva = obj_N_datos_empresa.tipo_iva
        new_record.ingresos_brutos = obj_N_datos_empresa.ingresos_brutos
        new_record.cuit = obj_N_datos_empresa.cuit
        new_record.nombre_fantasia = obj_N_datos_empresa.nombre_fantasia
        new_record.desc_interna= "credired"

        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except:
            new_record.session.close()
            new_record.session.rollback()
            return False



    def actualizar(self, obj_N_datos_empresa):
        u = update(E_empresa).values(nombre=obj_N_datos_empresa.nombre,ciudad = obj_N_datos_empresa.ciudad,direccion =obj_N_datos_empresa.direccion,telefono= obj_N_datos_empresa.telefono,email = obj_N_datos_empresa.email,website =obj_N_datos_empresa.website,tipo_iva = obj_N_datos_empresa.tipo_iva,ingresos_brutos = obj_N_datos_empresa.ingresos_brutos, cuit = obj_N_datos_empresa.cuit, nombre_fantasia = obj_N_datos_empresa.nombre_fantasia)
        self.session.execute(u)
        self.session.commit()
        self.session.close()

    def get_empresa(self, nombre_empresa):

        obj_datos_empresa = self.session.query(E_empresa).filter_by(desc_interna="credired").first()
        self.session.close()
        return obj_datos_empresa

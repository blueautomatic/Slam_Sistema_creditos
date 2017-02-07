import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_cobradores(base):

    __tablename__="cobradores"
    id_cobrador = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    documento = Column(String)
    telefono =  Column(String)
    cbdor_predeterminado = Column(String)
    cbdor_activo = Column(String)
    domicilio = Column(String)
    email=Column(String)
    domicilio=Column(String)
    aplicar_importe_peso=Column(String)
    aplicar_importe_porcentaje=Column(String)
    write_uid = Column(Integer)
    session =""


    def __init__  (self, a):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        self.session=Session()
        a=1


    @classmethod
    def guardar(cls, obj_N_cobradores):

        new_record = cls(1)
        new_record.nombre =obj_N_cobradores.nombre
        new_record.apellido =obj_N_cobradores.apellido
        new_record.documento = obj_N_cobradores.documento
        new_record.telefono = obj_N_cobradores.telefono
        new_record.cbdor_activo = obj_N_cobradores.cbdor_activo
        new_record.cbdor_predeterminado = obj_N_cobradores.cbdor_predeterminado
        new_record.domicilio = obj_N_cobradores.domicilio
        new_record.email = obj_N_cobradores.email
        new_record.aplicar_importe_peso = obj_N_cobradores.aplicar_importe_peso
        new_record.aplicar_importe_porcentaje = obj_N_cobradores.aplicar_importe_porcentaje
        new_record.write_uid=0
        new_record.session.add(new_record)
        new_record.session.commit()
        new_record.session.close()




import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, Integer, ForeignKey,Boolean,update
from sqlalchemy import create_engine
#from N_cliente import N_datos_datos_laborales
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_party_otros(base):
    __tablename__= "party_otros"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    cuit = Column(String)
    tipo_iva=Column(String)
    cbu = Column(String)
    num_beneficio = Column(String)
    presento_factura= Column(Boolean)
    figura_veraz=Column(Boolean)
    es_jubilado_pensionado=Column(Boolean)
    write_uid = Column(Integer)


    def __init__(self,id):
        a = id

    def get_party_otros(self, id_party):

        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        session=Session()
        obj_party_otros = session.query(E_party_otros).filter_by(id_party=id_party).first()
        session.close()
        return obj_party_otros


    def guardar(self,obj_N_party_otros,id_party):

        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        session=Session()

        new_record = E_party_otros(1)
        new_record.id_party= id_party
        new_record.cuit = obj_N_party_otros.cuit
        new_record.tipo_iva = obj_N_party_otros.tipo_iva
        new_record.cbu = obj_N_party_otros.cbu
        new_record.num_beneficio = obj_N_party_otros.num_beneficio
        new_record.presento_factura = obj_N_party_otros.presento_factura
        new_record.figura_veraz = obj_N_party_otros.figura_veraz
        new_record.es_jubilado_pensionado = obj_N_party_otros.es_jubilado_pensionado
        session.add(new_record)
        session.commit()
        session.close()

    def actualizar(self,obj_N_party_otros,id_party):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        session=Session()
        u = update(E_party_otros).where(E_party_otros.id_party == id_party).        values(cuit=obj_N_party_otros.cuit,            tipo_iva = obj_N_party_otros.tipo_iva,            cbu = obj_N_party_otros.cbu,            num_beneficio = obj_N_party_otros.num_beneficio,            presento_factura = obj_N_party_otros.presento_factura,        figura_veraz= obj_N_party_otros.figura_veraz,        es_jubilado_pensionado = obj_N_party_otros.es_jubilado_pensionado)
        session.execute(u)
        session.commit()
        session.close()

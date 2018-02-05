import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

Base = declarative_base()
class E_party_contacto(Base):
    __tablename__="party_contact"
    id_contact = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    create_date = Column(DateTime, default=func.now())
    write_date = Column(DateTime, default=func.now())
    comment = Column(String)
    value = Column(String)
    type_contacto = Column(String)
    write_uid = Column(Integer)


    def __init__(self,id_party):
        a=id_party


    def guardar(self,obj_N_party_contacto,id_party):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        session=Session()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = E_party_contacto(1)
        new_record.comment= ""
        new_record.value = obj_N_party_contacto.value
        new_record.type_contacto = obj_N_party_contacto.type_contacto
        new_record.id_party = id_party
        session.add(new_record)
        session.commit()
        session.close()

    def get_list_party_contacto(self, id_party):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        session=Session()
        list_party_contacto = session.query(E_party_contacto).filter_by(id_party=id_party).all()
        session.close()
        return list_party_contacto

    def actualizar(self,obj_N_party_contacto,id_party):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        session=Session()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        u = update(E_party_contacto).where((E_party_contacto.id_party == id_party) & (E_party_contacto.type_contacto == obj_N_party_contacto.type_contacto)).values(value=obj_N_party_contacto.value)
        session.execute(u)
        session.commit()
        session.close()








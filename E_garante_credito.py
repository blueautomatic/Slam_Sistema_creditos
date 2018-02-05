import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from sqlalchemy import text
from E_configuracion import configuracion


base = declarative_base()
class E_garante_credito(base):
    __tablename__="garante_credito"
    id = Column(Integer, primary_key=True,autoincrement=True)
    id_party_garante = Column(Integer)
    nro_credito = Column(Integer)
    tipo_garante = Column(String)
    write_uid = Column(Integer)
    session = ""


    def __init__  (self, id_garante):
        a = id_garante
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls,lista_garantes_credito ,nro_credito):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in lista_garantes_credito:
            new_record = cls(1)
            new_record.id_party_garante = item.id_party_garante
            new_record.nro_credito = int(nro_credito)
            new_record.tipo_garante = item.tipo_garante
            try:
                new_record.session.add(new_record)
                new_record.session.commit()

            except:
                new_record.session.rollback()
                new_record.session.close()
                return False

        return True

    def get_garante_credito(self, id_party):

        obj_garante_prestamo = self.session.query(E_garante_credito).filter_by(id_party=id_party).all()
        self.session.close()
        return obj_garante_prestamo

    def buscar_id_party_por_id_party(self, id_party):
        obj_party_party = self.session.query(E_garante_credito).filter_by(id_party_garante=str(id_party)).first()
        self.session.close()
        return obj_party_party



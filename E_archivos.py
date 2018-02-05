import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey,update,DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion


base = declarative_base()
class E_archivo(base):
    __tablename__="archivos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    id_party = Column(Integer)
    tipo_doc = Column(String)
    fec_create = Column(DateTime)


    def __init__  (self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_archivo):

        new_record = E_archivo()
        new_record.descripcion =obj_archivo.descripcion
        new_record.id_party = obj_archivo.id_party
        new_record.tipo_doc =obj_archivo.tipo_doc
        new_record.fec_create = obj_archivo.fec_create


        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except:
            new_record.session.rollback()
            new_record.session.close()
            return False

    def actualizar(self, obj_archivo):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_arch = self.get_nombre_archivo(obj_archivo.id_party)
            if obj_arch.descripcion =="":
                self.guardar(obj_archivo)
                self.session.close()
                return True
            else:
                query = update(E_archivo).where(E_archivo.id_party == obj_archivo.id_party ).values(descripcion = obj_archivo.descripcion)
                try:
                    self.session.execute(query)
                    self.session.commit()
                    self.session.close()
                    return True
                except:
                    return False


    def get_nombre_archivo(self, id_party):
        obj_archivo= self.session.query(E_archivo).filter_by(id_party = id_party).first()
        try :
            a=obj_archivo.descripcion
            self.session.close()
            return obj_archivo
        except:
            obj_archivo = E_archivo()
            obj_archivo.descripcion = ""
            self.session.close()
            return obj_archivo

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion


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
    descarga = Column(String)
    session=""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def guardar(cls,obj_usu):
        new_record = cls()
        new_record.nombre = obj_usu.nombre
        new_record.tipo_usuario = obj_usu.tipo_usuario
        new_record.password = obj_usu.password
        new_record.password2 = obj_usu.password2
        new_record.descarga = obj_usu.descarga
        new_record.session.add(new_record)
        new_record.session.commit()
        new_record.session.close()

    def buscar_usuario(self,nombre,clave):

        obj_usuario = self.session.query(E_usuario).filter_by(nombre=nombre, password= clave).first()
        if obj_usuario !=None :
            self.session.close()
            return obj_usuario
        else:
            self.session.close()
            return False


    def buscar_usuario_id(self,idusu):

        obj_usuario = self.session.query(E_usuario).filter_by(id_usuario=idusu).first()
        if obj_usuario !=None :
            self.session.close()
            return obj_usuario
        else:
            self.session.close()
            return False


    def buscar_todos_los_usuarios(self):
        obj_party_party = self.session.query(E_usuario).all()
        self.session.close()
        return obj_party_party

    @classmethod
    def actualizar(cls, obj_usuario):
        try:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj = cls()
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({"nombre" :obj_usuario.nombre})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({"tipo_usuario" : obj_usuario.tipo_usuario})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({ "password" : obj_usuario.password})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({ "password2" : obj_usuario.password2})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({ "descarga" : obj_usuario.descarga})

            #self.session.execute(u)
            obj.session.commit()
            obj.session.close()
            return True
        except :

            return False


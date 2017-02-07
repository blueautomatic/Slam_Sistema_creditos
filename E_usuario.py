import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func,update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook


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
    session=""

    def __init__(self):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def guardar(cls,obj_usu):
        new_record = cls()
        new_record.nombre = obj_usu.nombre
        new_record.tipo_usuario = obj_usu.tipo_usuario
        new_record.password = obj_usu.password
        new_record.password2 = obj_usu.password2
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
            #sess.query(User).filter(User.age == 25).update({User.age: User.age - 10}
            #"age": User.age
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({"nombre" :obj_usuario.nombre})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({"tipo_usuario" : obj_usuario.tipo_usuario})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({ "password" : obj_usuario.password})
            obj.session.query(E_usuario).filter(E_usuario.id_usuario == obj_usuario.id_usuario).update({ "password2" : obj_usuario.password2})
            #self.session.execute(u)
            obj.session.commit()
            obj.session.close()
            return True
        except :
            return False


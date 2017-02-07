import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Numeric, func, Boolean, update
from sqlalchemy import create_engine
#from N_cliente import N_datos_datos_laborales
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_datos_laborales(base):

        __tablename__= "datos_laborales"
        id = Column(Integer, primary_key=True, autoincrement=True)
        id_party = Column(Integer)
        sueldo = Column(Numeric)
        anti_laboral = Column(DateTime)
        tel_laboral = Column(String)
        dom_laboral = Column(String)
        organismo = Column(String)
        ocupacion = Column(String)
        categoria = Column(String)
        posee_recibo_sueldo = Column(Boolean)
        write_uid = Column(Integer)
        session=""


        def __init__(self):
            engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
            Session= sessionmaker(bind=engine)
            self.session=Session()

        def get_datos_laborales(self, id_party):

            obj_party_laborales = self.session.query(E_datos_laborales).filter_by(id_party=id_party).first()
            self.session.close()
            return obj_party_laborales

        @classmethod
        def guardar(cls,obj_N_datos_laborales,id_party):
            obj_E_datos_laborales = cls()
            obj_E_datos_laborales.sueldo = obj_N_datos_laborales.sueldo
            obj_E_datos_laborales.anti_laboral = obj_N_datos_laborales.anti_laboral
            obj_E_datos_laborales.tel_laboral = obj_N_datos_laborales.tel_laboral
            obj_E_datos_laborales.dom_laboral = obj_N_datos_laborales.dom_laboral
            obj_E_datos_laborales.organismo = obj_N_datos_laborales.organismo
            obj_E_datos_laborales.ocupacion = obj_N_datos_laborales.ocupacion
            obj_E_datos_laborales.categoria = obj_N_datos_laborales.categoria
            obj_E_datos_laborales.id_party = id_party
            obj_E_datos_laborales.posee_recibo_sueldo = obj_N_datos_laborales.posee_recibo_sueldo
            obj_E_datos_laborales.session.add(obj_E_datos_laborales)
            obj_E_datos_laborales.session.commit()
            obj_E_datos_laborales.session.close()



        def actualizar(self,obj_N_datos_laborales,id_party):

            u = update(E_datos_laborales).where(E_datos_laborales.id_party == id_party).values(ocupacion=obj_N_datos_laborales.ocupacion,organismo=obj_N_datos_laborales.organismo, categoria= obj_N_datos_laborales.categoria,posee_recibo_sueldo=obj_N_datos_laborales.posee_recibo_sueldo,sueldo=obj_N_datos_laborales.sueldo,anti_laboral=obj_N_datos_laborales.anti_laboral,tel_laboral=obj_N_datos_laborales.tel_laboral,dom_laboral=obj_N_datos_laborales.dom_laboral)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

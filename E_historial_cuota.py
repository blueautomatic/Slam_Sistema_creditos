import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion
from E_cuotas import E_cuotas


base = declarative_base()
class E_historial_cuota(base):
    __tablename__="cuotas_historial"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_credito =Column(Integer)
    nro_cuota= Column(Integer)
    estado_cuota=Column(String)
    fecha_cobro=Column(DateTime, default=func.now())
    importe_cobrado=Column(Numeric)
    descripcion= Column(String)
    importe_cuota=Column(Numeric)
    write_uid= Column(Integer)
    primer_vencimiento=Column(DateTime)
    id_cuota = Column(Integer)
    session=""

    def __init__(self):
            self.create_date =func.now()
            self.write_date = func.now()
            self.write_uid = 1
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

    @classmethod
    def guardar(cls, obj_hist_cta ):
            obj_hist = cls()
            obj_hist.nro_credito =obj_hist_cta.nro_credito
            obj_hist.nro_cuota = obj_hist_cta.nro_cuota
            obj_hist.estado_cuota = obj_hist_cta.estado_cuota
            obj_hist.fecha_cobro = obj_hist_cta.fecha_cobro
            obj_hist.importe_cobrado = obj_hist_cta.importe_cobrado
            obj_hist.descripcion = obj_hist_cta.descripcion
            obj_hist.importe_cuota = obj_hist_cta.importe_cuota
            obj_hist.write_uid = obj_hist_cta.write_uid
            obj_hist.primer_vencimiento = obj_hist_cta.primer_vencimiento
            obj_hist.id_cuota= obj_hist_cta.id_cuota
            try :
                obj_hist.session.add(obj_hist)
                obj_hist.session.commit()
                obj_hist.session.close()
                return True

            except:
                obj_hist.session.rollback()
                obj_hist.session.close()
                return "False"

    def get_historial_cuota(self, id_cuota):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            lista_historial_cuota = self.session.query(E_historial_cuota).filter_by(id_cuota=id_cuota).all()
            self.session.close()
            return lista_historial_cuota

    def guardar_historial(self,nro_credito):
        obj_ctas= E_cuotas(1)
        list_cta = obj_ctas.get_cuotas_por_nro_credito(nro_credito)
        obj_hist = E_historial_cuota()


        for item in list_cta:
            obj_hist.nro_credito =item.nro_credito
            obj_hist.nro_cuota = item.nro_cuota
            obj_hist.estado_cuota = item.estado_cuota
            #obj_hist.fecha_cobro = item.fecha_cobro
            obj_hist.importe_cobrado = 0
            obj_hist.descripcion = ""
            obj_hist.importe_cuota = item.importe_cuota
            obj_hist.write_uid = item.write_uid
            obj_hist.primer_vencimiento = item.primer_vencimiento
            obj_hist.id_cuota= item.id
            self.guardar(obj_hist)



import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer,func,Numeric,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook


base = declarative_base()

class E_egresos(base):
    __tablename__= "caja_egreso"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_credito = Column(Integer)
    id_party = Column(Integer)
    nombre = Column(String)
    costo = Column(Numeric)
    fecha = Column(DateTime, default=func.now())
    write_uid = Column(Integer)
    orden = 0
    apellido = ""
    nombre_cliente = ""
    cantidad_cuotas = 0
    importe_primer_venc = 0
    session = ""
    def __init__(self,id_party):
        a = id_party
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar_egresos_creditos(cls , obj_N_creditos,nro_credito):

        new_record = cls(1)
        new_record.nro_credito = nro_credito
        new_record.id_party = obj_N_creditos.id_party
        new_record.nombre = "Creditos Personales"
        new_record.costo = obj_N_creditos.importe_prestamo

        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except:
            new_record.session.rollback()
            new_record.session.close()
            return False

    def buscar_egresos(self,fecha):


        sql = text(" select cje.id as orden, pp.nombre, pp.apellido, cje.nro_credito, cje.nombre, c.cantidad_cuotas, cta.importe_primer_venc, cje.costo from caja_egreso as cje INNER JOIN party_party as pp ON cje.id_party = pp.id_party INNER JOIN credito as c ON cje.nro_credito = c.nro_credito INNER JOIN cuotas as cta ON c.nro_credito = cta.nro_credito where cje.fecha = '" + str(fecha) + "' group by cje.id, pp.nombre, pp.apellido,cje.nro_credito, cje.nombre, c.cantidad_cuotas,cta.importe_primer_venc,cje.costo")
        result = self.session.execute(sql)
        lista_egresos = list()
        for row in result:
            obj_E_egresos = E_egresos(1)
            obj_E_egresos.id = row[0]
            obj_E_egresos.nombre_cliente = row[1]
            obj_E_egresos.apellido = row[2]
            obj_E_egresos.nro_credito = row[3]
            obj_E_egresos.cantidad_cuotas = row[5]
            obj_E_egresos.importe_primer_venc = row[6]
            obj_E_egresos.costo = row[7]
            lista_egresos.append(obj_E_egresos)
        self.session.close()
        return lista_egresos

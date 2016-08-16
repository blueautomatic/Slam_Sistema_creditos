import sys 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook

base = declarative_base()
class E_creditos(base):
    __tablename__= "credito"  
    nro_credito = Column(Integer, primary_key=True, autoincrement=True)
    nro_cliente = Column(Integer)
    id_usuario = Column(Integer)
    fecha_credito =  Column(DateTime)
    tasa =  Column(String)
    formula =  Column(String)
    importe_prestamo =  Column(String)
    cantidad_cuotas =  Column(String)
    tipo_vencimiento =  Column(String)
    vto_primer_cuota =  Column(String)
    interes =  Column(Integer)
    gastos =  Column(Integer)
    seguros =  Column(Integer)
    impuestos =  Column(Integer)
    cred_total =  Column(Integer)
    en_letras =  Column(String)
    observaciones =  Column(String)


    def __init__(self,id_party):
        a = id_party

    def buscar_creditos_por_cliente(self,nro_cliente):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        obj_creditos_cliente = session.query(E_creditos).filter_by(nro_cliente=str(nro_cliente)).all()
        return obj_creditos_cliente


    def guardar(self, N_credito):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_creditos
        new_record.nro_cliente= N_credito.nro_cliente
        new_record.fecha_credito = N_credito.fecha_credito        
        new_record.tasa = N_credito.tasa
        new_record.formula = N_credito.formula
        new_record.importe_prestamo = N_credito.importe_prestamo
        new_record.cantidad_cuotas = N_credito.cantidad_cuotas
        new_record.tipo_vencimiento = N_credito.tipo_vencimiento
        new_record.vto_primer_cuota = N_credito.vto_primer_cuota
        new_record.interes = N_credito.interes
        new_record.gastos = N_credito.gastos
        new_record.seguros = N_credito.seguros
        new_record.impuestos = N_credito.impuestos
        new_record.cred_total = N_credito.cred_total
        new_record.en_letras = N_credito.en_letras
        new_record.observaciones = N_credito.observaciones

        session.add(new_record)
        session.commit()

    def get_tiene_prestamos_activo(self, nro_cliente):
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        session=Session()

        obj_E_creditos = session.query(E_creditos).filter_by(nro_cliente= nro_cliente).first()

        if obj_E_creditos != None :
            return obj_E_creditos.nro_credito

        return 0

























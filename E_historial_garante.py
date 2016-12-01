import sys 
#import datetime
#from N_profesionales import N_datos_academicos
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean,update
from PyQt5.QtCore import pyqtRemoveInputHook
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError 
from sqlalchemy import text

class E_historial_garante(object):
    tipo_garante="" 
    estado_credito = ""  
    nro_credito=""
    importe_prestamo = ""
    nro_cliente = ""
    num_doc = ""
    apellido = ""
    nombre = ""
    session=""

    def __init__(self, slam):
        slam1 = slam
        engine=create_engine('postgresql://postgres:slam2016@localhost:5432/credired')
        Session= sessionmaker(bind=engine) 
        self.session=Session()
    

    def buscar_historial_garante(self,id_party):

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        sql = text("select  gc.tipo_garante, gc.nro_credito, c.importe_prestamo, pc.nro_cliente, pp.num_doc, pp.apellido, pp.nombre, c.estado from garante_credito as gc INNER JOIN credito as c ON gc.nro_credito  = c.nro_credito INNER JOIN party_party as pp ON c.id_party = pp.id_party INNER JOIN party_cliente as pc ON c.id_party = pc.id_party INNER JOIN party_garante as pg ON gc.id_party_garante = pg.id_party_garante where pg.id_party_garante =" + str(id_party) + "group by gc.tipo_garante, gc.nro_credito, c.importe_prestamo, pc.nro_cliente, pp.num_doc, pp.apellido, pp.nombre, c.estado")
        result = self.session.execute(sql)
        lista_historial_garante = list()
        for row in result:
            obj_E_historial_garante = E_historial_garante(1)
            obj_E_historial_garante.tipo_garante = row[0]
            obj_E_historial_garante.nro_credito = row[1]
            obj_E_historial_garante.importe_prestamo = row[2]
            obj_E_historial_garante.nro_cliente = row[3]
            obj_E_historial_garante.num_doc = row[4]
            obj_E_historial_garante.apellido = row[5]
            obj_E_historial_garante.nombre = row[6]
            obj_E_historial_garante.estado_credito = row[7]
            lista_historial_garante.append(obj_E_historial_garante)
        self.session.close()
        return lista_historial_garante

import sys
import datetime
from E_egresos import E_egresos
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook

class  N_egresos(object):
    id = 0
    nro_credito = 0
    id_party = 0
    nombre = ""
    costo = 0
    fecha = datetime
    orden = 0
    apellido = ""
    nombre_cliente = ""
    cantidad_cuotas = 0
    importe_primer_venc = 0


    """docstring for  N_egres"""
    def __init__(self, a):
        slam=a

    def guardar_egresos_creditos(self,obj_N_creditos,nro_credito):
        obj_e_egresos = E_egresos(1)
        result = obj_e_egresos.guardar_egresos_creditos(obj_N_creditos,nro_credito)
        return result

    def buscar_egresos(self, fecha):
        obj_e_egresos = E_egresos(1)
        return obj_e_egresos.buscar_egresos(fecha)
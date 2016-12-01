import sys
import datetime
from E_ingresos import E_ingresos
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook


class N_ingresos(object):

    id=0
    monto=0
    fecha=datetime
    id_cuota=0
    nombre=""
    nro_cta =0

    def __init__(self, a):
        slam=a

    def ingresos_buscar(self, fecha):
        obj_e_ingresos = E_ingresos()
        return obj_e_ingresos.ingresos_buscar(fecha)
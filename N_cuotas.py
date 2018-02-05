import sys
import datetime
from E_cuotas import E_cuotas
from E_ingresos import E_ingresos
from PyQt5.QtCore import pyqtRemoveInputHook

class N_cuotas(object):
    id = ""
    nro_credito= 0
    nro_cuota= 0
    primer_vencimiento= datetime
    importe_primer_venc= 0
    estado_cuota = ""
    fecha_cobro = ""
    importe_cobrado= 0
    capital = 0
    interes = 0
    gastos = 0
    punitorios = 0
    importe_cuota=0
    descripcion = ""
    descuento = 0

    def __init__(self,a):

        slam = a

    def guardar(self, lista_cuotas, nro_credito):
        obj_E_cuotas = E_cuotas(1)
        for item in lista_cuotas:
            obj_E_cuotas.guardar(item,nro_credito)

    def get_cuotas_por_nro_credito(self, nro_credito):
        obj_e_cuotas = E_cuotas(1)

        return obj_e_cuotas.get_cuotas_por_nro_credito(nro_credito)

    def pagar_cuota(self, obj_cuotas):
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.pagar_cuota(obj_cuotas)

    def lista_cuotas_venc_30_dias(self):
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.lista_cuotas_venc_30_dias()

    def lista_cuotas_venc_60_dias(self,slam):
        ejezeta = slam
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.lista_cuotas_venc_60_dias(ejezeta)

    def lista_cuotas_venc_90_dias(self,slam):
        ejezeta = slam
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.lista_cuotas_venc_90_dias(ejezeta)

    def buscar_cuota_por_id_cuota(self, id_cuota):
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.buscar_cuota_por_id_cuota(id_cuota)

    def generar_punitorios(self,id):
        slam = id
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.generar_punitorios(slam)

    def guardar_ingresos(self, N_cuota):
        #obj_E_ingresos = E_ingresos(1)
        obj_ingreso  = E_ingresos()
        obj_ingreso.monto = N_cuota.importe_cobrado
        obj_ingreso.nombre = "Cuotas"
        obj_ingreso.id_cuota = N_cuota.id

        obj_ingreso.guardar_ingresos(obj_ingreso)
        #obj_E_ingresos.guardar_ingresos(obj_ingreso)
        return True

    def buscar_cta_por_nro_cred_y_nro_cta(self, nro_credito, nro_cuota):
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.buscar_cta_por_nro_cred_y_nro_cta(nro_credito, nro_cuota)

    def actualizar(self):
        obj_e_cuotas = E_cuotas(1)
        return obj_e_cuotas.actualizar(self)

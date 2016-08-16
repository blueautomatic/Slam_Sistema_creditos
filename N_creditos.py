import sys
import datetime
from E_creditos import E_creditos


class N_creditos(object):

    nro_credito = ""
    nro_cliente = ""
    id_usuario = ""
    fecha_credito =""
    tasa =  ""
    formula = ""
    importe_prestamo = ""
    cantidad_cuotas = ""
    tipo_vencimiento =""
    vto_primer_cuota =""
    interes = ""
    gastos =  ""
    seguros =  ""
    impuestos = ""
    cred_total =  ""
    en_letras =  ""
    observaciones = ""


    def __init__(self,nro_credito):

        a= nro_credito    

    def get_tiene_prestamos_activo(self, nro_documento):
        obj_E_credito = E_creditos(1)
        tiene_prestamo=0
        tiene_prestamo = obj_E_credito.get_tiene_prestamos_activo(nro_documento)
        if tiene_prestamo !=0:
            return True
        else:
            return False


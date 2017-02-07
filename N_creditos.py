import sys
import datetime
from E_creditos import E_creditos
from E_party_cliente import E_party_cliente
from E_party_party import E_party_party
from E_historial_garante import E_historial_garante


class N_creditos(object):

    nro_credito = ""
    nro_cliente = ""
    id_party=""
    fecha_credito =""
    tasa =  ""
    formula = ""
    importe_prestamo = 0
    cantidad_cuotas = 0
    vto_primer_cuota = ""
    interes = 0
    gastos =  0
    seguros =  ""
    impuestos = 0
    cred_total =  ""
    observaciones = ""
    estado = "Activo"

    def __init__(self,nro_credito):
        a= nro_credito

    def guardar_credito(self,obj_N_creditos):
   
        result = E_creditos.guardar(obj_N_creditos)
        return result

    def get_id_partycliente(self,nro_cliente):
        obj_E_party_cliente = E_party_cliente(1)
        id_party = obj_E_party_cliente.get_id_party(nro_doc_cliente)
        return id_party

    def get_tiene_prestamos_activo(self, nro_documento):
        obj_E_credito = E_creditos()
        tiene_prestamo=0
        tiene_prestamo = obj_E_credito.get_tiene_prestamos_activo(nro_documento)
        if tiene_prestamo !=0:
            return True
        else:
            return False

    def buscar_nro_credito_por_party(self, id_party):
        obj_E_credito = E_creditos()
        return obj_E_credito.buscar_nro_credito_por_party(id_party)

    def get_list_credito(self,id_party):

        obj_E_creditos = E_creditos()
        list_creditos = list()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        list_creditos = obj_E_creditos.get_creditos(id_party)

        list_N_creditos = list()

        for item in list_creditos:
            obj_creditos = N_creditos(1)
            obj_creditos.nro_cliente = item.nro_cliente
            obj_creditos.fecha_credito = item.fecha_credito
            obj_creditos.nro_credito = item.nro_credito
            obj_creditos.cantidad_cuotas= item.cantidad_cuotas
            obj_creditos.cred_total = item.cred_total
            obj_creditos.observaciones = item.observaciones
            obj_creditos.gastos = item.gastos
            obj_creditos.estado = item.estado
            list_N_creditos.append(obj_creditos)
        
        return list_N_creditos  

    def buscar_credito_por_nro_credito(self, nro_credito):
        obj_E_credito = E_creditos()
        return obj_E_credito.buscar_credito_por_nro_credito(nro_credito)

    def cancelar_credito(self,nro_credito):
        obj_E_credito = E_creditos()
        return obj_E_credito.cancelar_credito(nro_credito)




class N_historial_garante(object):
    tipo_garante = ""
    estado_credito = ""
    nro_credito = ""
    importe_prestamo = ""
    nro_cliente = ""
    num_doc = ""
    apellido = ""
    nombre = ""

    def __init__(self, a ):
        slam=a

    def buscar_historial_garante(self, id_party):
        obj_E_historial_garante = E_historial_garante(1)
        return obj_E_historial_garante.buscar_historial_garante(id_party)



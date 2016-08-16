import sys
import datetime
from E_party_garante import E_party_garante
from E_party_contacto import E_party_contacto
from E_party_party import E_party_party
from E_datos_laborales import E_datos_laborales
from E_party_address import E_party_address
from E_party_otros import E_party_otros
from E_usuario import E_usuario
from E_party_cliente import E_party_cliente
from E_party_address import E_party_address

from PyQt5.QtCore import pyqtRemoveInputHook


class N_datos_personales_cliente(object):
    apellido = ""
    nombre = ""
    tipo_doc = ""
    nro_doc = ""
    estado_civil = ""
    fec_nac = ""
    limite_credito = ""
    id_party = ""
    estado = ""

    def __init__(self, apellido):
        a = apellido

    def guardar(self, obj_datos_personales_cliente, id_party):
        obj_E_party_party = E_party_party(1)
        result = obj_E_party_party.guardar(obj_datos_personales_cliente, id_party)
        return result

    def get_garante_habilitado_buscar(self, numero_documento_garante):
        obj_E_party_cliente = E_party_party("q")
        obj_party_cliente = obj_E_party_cliente.get_party_party(numero_documento_garante)
        return obj_party_cliente

    def get_garante_habilitado_buscar_nrocliente(self,nro_cliente):
        obj_E_party_cliente = E_party_party("q")
        obj_party_cliente = obj_E_party_cliente.get_party_party(nro_cliente)
        return obj_party_cliente

    def get_id_party_party_garante(self,nro_doc_garante):
        obj_E_party_cliente = E_party_party("q")
        id_party_party_garante = obj_E_party_cliente.get_id_party(nro_doc_garante)
        return id_party_party_garante
    
    def buscar_party_party_por_nro_doc(self, dni_cliente):
        obj_E_party_party_nro_cliente = E_party_party("a")
        party_party_por_nro_doc = obj_E_party_party_nro_cliente.get_party_party(dni_cliente)

        obj_N_datos_personales_cliente=N_datos_personales_cliente("a")

        obj_N_datos_personales_cliente.apellido = party_party_por_nro_doc.apellido
        obj_N_datos_personales_cliente.nombre = party_party_por_nro_doc.nombre
        obj_N_datos_personales_cliente.tipo_doc = party_party_por_nro_doc.tipo_doc
        obj_N_datos_personales_cliente.nro_doc = party_party_por_nro_doc.num_doc
        obj_N_datos_personales_cliente.estado_civil = party_party_por_nro_doc.estado_civil
        obj_N_datos_personales_cliente.fec_nac = party_party_por_nro_doc.fec_nac
        obj_N_datos_personales_cliente.limite_credito = party_party_por_nro_doc.limite_credito
        obj_N_datos_personales_cliente.id_party = party_party_por_nro_doc.id_party
        obj_N_datos_personales_cliente.estado = party_party_por_nro_doc.estado
        return obj_N_datos_personales_cliente      


class N_party_cliente(object):
    nro_cliente = ""
    comment=""

    def __init__(self,id_party):
        a= id_party

    def get_party_cliente(self, id_party):
        obj_E_party_cliente = E_party_cliente(id_party)
        party_cliente = obj_E_party_cliente.get_party_cliente(id_party)
        return party_cliente

    def guardar_N_party_cliente(self, comment, id_party):
        obj_E_party_cliente= E_party_cliente(id_party)
        obj_E_party_cliente.guardar(comment, id_party)



class N_party_address(object):
    ciudad = ""
    barrio = ""
    domicilio = ""
    id_party = ""

    def __init__(self, ciudad):
        a = ciudad
    def get_party_address(self,id_party):
        obj_E_party_address3= E_party_address(id_party)
        obj_E_party_address2 =obj_E_party_address3.get_party_address(id_party)
       # pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        obj_N_party_address= N_party_address(1)
        if obj_N_party_address != "":                
            try :
                obj_N_party_address.ciudad = obj_E_party_address2.ciudad
            except:
                obj_N_party_address.ciudad=""
            
            try :
                obj_N_party_address.domicilio = obj_E_party_address2.domicilio
            except:
                obj_N_party_address.domicilio =""

            try:
                obj_N_party_address.barrio= obj_E_party_address2.barrio  
            except:
                obj_N_party_address.barrio=""


        return obj_N_party_address

    def guardar(self, obj_N_party_address, id_party):
        obj_E_party_address = E_party_address(1)
        result = obj_E_party_address.guardar(obj_N_party_address, id_party)
        return result


class N_datos_laborales(object):
    id_party = ""
    sueldo = ""
    anti_laboral = ""
    tel_laboral = ""
    dom_laboral = ""
    organismo = ""
    ocupacion = ""
    categoria = ""
    posee_recibo_sueldo = ""

    def __init__(self, organismo):
        a = organismo

    def get_datos_laborales(self, id_party):
        obj_E_datos_laborales=E_datos_laborales(1)
        obj_datos_laborales=obj_E_datos_laborales.get_datos_laborales(id_party)

        obj_N_datos_laborales = N_datos_laborales(1)
        obj_N_datos_laborales.sueldo = obj_datos_laborales.sueldo
        obj_N_datos_laborales.anti_laboral = obj_datos_laborales.anti_laboral
        obj_N_datos_laborales.tel_laboral = obj_datos_laborales.tel_laboral
        obj_N_datos_laborales.dom_laboral = obj_datos_laborales.dom_laboral
        obj_N_datos_laborales.organismo = obj_datos_laborales.organismo
        obj_N_datos_laborales.ocupacion = obj_datos_laborales.ocupacion
        obj_N_datos_laborales.categoria = obj_datos_laborales.categoria
        obj_N_datos_laborales.posee_recibo_sueldo = obj_datos_laborales.posee_recibo_sueldo

        return obj_N_datos_laborales



    def guardar(self, obj_N_datos_laborales, id_party):
        obj_E_datos_laborales = E_datos_laborales(1)
        result = obj_E_datos_laborales.guardar(obj_N_datos_laborales, id_party)
        return result


class N_party_garante(object):
    id_party = ""
    id_garante = ""
    comment = ""
    nro_doc= ""
    tipo_garante= ""
    nro_cliente=""

    def __init__(self, apellido):
        a = apellido

    def guardar(self, list_party_cliente, nro_cliente):
        obj_E_party_garante = E_party_garante(1)

        for item in list_party_cliente:
            obj_E_party_garante.guardar(item, nro_cliente)
        

    def validar_garante(self, obj_N_party_garante):
        a=obj_N_party_garante
    
    def guardar_garante(self, obj_party_garante):
        obj_E_party_party = E_party_party(1)
        id_party_garante = obj_E_party_party.get_id_party(obj_party_garante.nro_doc)
        obj_E_party_garante = E_party_garante(id_party_garante)
        obj_E_party_garante.guardar(obj_party_garante,id_party_garante)

    def es_garante_de_otro_cliente(self,nro_doc_garante):
        obj_E_party_garante= E_party_garante(nro_doc_garante)
        obj_party_cliente=E_party_party(1)
        id_party_garante=obj_party_cliente.get_id_party(nro_doc_garante)

        result =obj_E_party_garante.es_garante_de_otro_cliente(id_party_garante)
        return result

    def get_tiene_prestamos_activo(self, nro_doc_garante):
        obj_party_cliente=obj_E_party_party(1)
        id_party_garante=obj_party_cliente.get_id_party(nro_doc_garante)
        obj_E_prestamo=E_prestamo(1)
        obj_E_prestamo.validar_cliente_prestamo_activo(id_party_garante)


class N_party_otros(object):
    id_party = ""
    tipo_iva = ""
    cuit = ""
    cbu = ""
    num_beneficio = ""

    def __init__(self, cuit):
        a = cuit

    def guardar(self, obj_N_party_otros, id_party):
        obj_E_party_otros = E_party_otros(1)
        result = obj_E_party_otros.guardar(obj_N_party_otros, id_party)
        return result



class N_party_contacto(object):
    id_party=""
    type_contacto=""
    comment=""
    value=""
    id_contact=""

    def __init__(self, id_party):
        a=id_party

    def guardar(self, obj_N_party_contact, id_party):
        obj_E_party_contact = E_party_contacto(1)
        obj_E_party_contact.guardar(obj_N_party_contact, id_party)

    def get_list_party_contacto(self, id_party):
        list_E_party_contact = E_party_contacto(1)
        return list_E_party_contact.get_list_party_contacto(id_party)
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
        result = obj_E_party_party.guardar(
            obj_datos_personales_cliente, id_party)
        return result

    def get_garante_habilitado(self, numero_documento_garante):
        obj_E_party_cliente = E_party_party("q")
        obj_party_cliente = obj_E_party_cliente.get_party_party(numero_documento_garante)
        return obj_party_cliente

    def get_garante_habilitado_buscar_nrocliente(self,nro_cliente):
        obj_E_party_cliente = E_party_party("q")
        obj_party_cliente = obj_E_party_cliente.get_party_party(nro_cliente)
        return obj_party_cliente


class N_party_cliente(object):
    nro_cleinte = ""

    def __init__(self,id_party):
        a= id_party

    def get_nro_cliente(self, id_party):
        obj_E_party_cliente = E_party_cliente(id_party)
        nro_cliente = obj_E_party_cliente.get_nro_cliente(id_party)
        return nro_cliente


class N_party_address(object):
    ciudad = ""
    barrio = ""
    domicilio = ""
    id_party = ""

    def __init__(self, ciudad):
        a = ciudad

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

    def guardar(self, obj_N_datos_laborales, id_party):
        obj_E_datos_laborales = E_datos_laborales(1)
        result = obj_E_datos_laborales.guardar(obj_N_datos_laborales, id_party)
        return result


class N_party_garante(object):
    id_party = ""
    id_garante = ""
    comment = ""
    nro_doc= ""

    def __init__(self, apellido):
        a = apellido

    def guardar(self, list_N_party_garante, id_party):
        obj_E_party_garante = E_party_garante(1)
        #result = obj_E_party_garante.guardar(obj_N_party_garante, id_party)
        # return result

    def validar_garante(self, obj_N_party_garante):
        a=obj_N_party_garante


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

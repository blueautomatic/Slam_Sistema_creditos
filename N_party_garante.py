import sys
from E_party_garante import E_party_garante
from E_garante_credito import E_garante_credito
from PyQt5.QtCore import pyqtRemoveInputHook

class N_party_garante(object):
    id_party=""
    nombre = ""
    apellido=""
    domicilio=""
    fec_nac=""
    tipo_documento=""
    num_cliente=""
    num_documento=""
    comment=""
    ciudad=""
    barrio=""
    email=""
    estado_civil=""
    limite_credito=""
    activo=""
    inactivo=""
    num_cliente=""
    
    
    def __init__(self, apellido):
        a = apellido
        
    def guardar(self, obj_N_party_garante, id_party):
        obj_N_party_garante = E_party_garante(id_party)
        result = obj_E_party_garante.guardar(obj_N_party_garante, id_party)
        return result


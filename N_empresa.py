import sys
from E_empresa import E_empresa


class N_datos_empresa(object):
    id_empresa=""
    nombre = ""
    ciudad = ""
    direccion = ""
    telefono = ""
    email = ""
    website = ""
    tipo_iva = ""
    ingresos_brutos=""
    cuit=""
    nombre_fantasia="" 
    desc_interna=""  



    def __init__(self, nombre):
       a = nombre


    def guardar(self, obj_N_datos_empresa):
       obj_E_empresa = E_empresa(1)
       result=obj_E_empresa.guardar(obj_N_datos_empresa)
       return result


    def actualizar(self, obj_N_datos_empresa):
        obj_N_empresa = E_empresa(1)
        obj_datos_empresa=obj_N_empresa.actualizar(obj_N_datos_empresa)
        return obj_datos_empresa

    def get_empresa_actualizar(self, nombre_empresa):
        obj_E_empresa = E_empresa(1)
        obj_datos_empresa = obj_E_empresa.get_empresa(nombre_empresa)
        return obj_datos_empresa













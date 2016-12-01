import sys
from E_cobradores import E_cobradores

class N_datos_cobrador(object):

  nombre=""
  apellido=""
  documento=""
  telefono=""
  cbdor_predeterminado=""
  cbdor_activo=""
  domicilio=""
  email=""
  domicilio=""
  aplicar_importe_peso=""
  aplicar_importe_porcentaje=""


  def __init__(self, nombre):
    a = nombre

  def guardar(self, N_datos_cobrador):
    obj_E_cobradores = E_cobradores(1)
    result=obj_E_cobradores.guardar(N_datos_cobrador)
    return result











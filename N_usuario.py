import sys
from E_usuario import E_usuario
from PyQt5.QtCore import pyqtRemoveInputHook


class N_usuario(object):
    id_usuario = 0
    nombre = ""
    tipo_usuario = ""
    password = ""
    password2 = ""
    descarga = ""



    def buscar_usuario(self,nombre,clave):
        obj_E_usuario = E_usuario()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        return obj_E_usuario.buscar_usuario(nombre,clave)

    def guardar(self, obj_usu):
        return E_usuario().guardar(obj_usu)

    def buscar_todos_los_usuarios(self):
        obj_E_usuario = E_usuario()
        return obj_E_usuario.buscar_todos_los_usuarios()

    def actualizar(self,obj_n_usuario):
        return E_usuario().actualizar(obj_n_usuario)

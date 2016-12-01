import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from form_login import Ui_Form_login
from w_mainwindow import Mainwindow
from N_usuario import N_usuario

#tipo_usuario =""
class Singleton(object):
     _instance = None
     tipo_usuario =""

     def __new__(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
            self.tipo_usuario = ""
        return self._instance


class login(QDialog):
    obj_form = Ui_Form_login()
   
    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_Form_login()
        self.obj_form.setupUi(self)
        self.obj_form.boton_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        usuario = self.obj_form.lne_nombre.text()
        clave = self.obj_form.lne_pass.text()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_N_usuario = N_usuario()
        obj_usuario = obj_N_usuario.buscar_usuario(usuario,clave)
        singleton = Singleton()
        singleton.tipo_usuario= obj_usuario.tipo_usuario
        self.form_mainwindow = Mainwindow(singleton)
        self.form_mainwindow.show()
        self.close()





app = QApplication(sys.argv)
dialogo= login()
dialogo.show()

app.exec_()  








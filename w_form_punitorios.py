import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import QDate
from N_cuotas import N_cuotas
from form_punitorios import Ui_form_punitorios

class punitorios(QDialog):
    obj_form = Ui_form_punitorios()
   
    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_punitorios()
        self.obj_form.setupUi(self)
        self.obj_form.boton_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        obj_N_cuotas = N_cuotas(1)
        slam = obj_N_cuotas.generar_punitorios(1)



#app = QApplication(sys.argv)
#punitorio= punitorios()
#punitorio.show()
#app.exec_()
    
    